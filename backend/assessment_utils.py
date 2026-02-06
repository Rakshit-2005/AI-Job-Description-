import subprocess
import json
from typing import Dict, Any, List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class CodeExecutor:
    """Execute code safely in subprocess"""
    
    def execute_python_code(self, code: str, test_cases: List[Dict[str, Any]], 
                           timeout: int = 5) -> Dict[str, Any]:
        """Execute Python code with test cases"""
        results = []
        
        for test_case in test_cases:
            try:
                # Create test code
                test_code = f"""
{code}

# Test case
test_input = {test_case.get('input')}
result = main(test_input) if 'main' in dir() else eval(test_input)
print(result)
"""
                
                # Execute with timeout
                process = subprocess.run(
                    ['python', '-c', test_code],
                    capture_output=True,
                    text=True,
                    timeout=timeout
                )
                
                output = process.stdout.strip()
                expected = str(test_case.get('expected_output', '')).strip()
                
                results.append({
                    "passed": output == expected,
                    "expected": expected,
                    "actual": output,
                    "error": process.stderr if process.stderr else None
                })
                
            except subprocess.TimeoutExpired:
                results.append({
                    "passed": False,
                    "error": "Code execution timed out"
                })
            except Exception as e:
                results.append({
                    "passed": False,
                    "error": str(e)
                })
        
        passed_count = sum(1 for r in results if r.get("passed", False))
        total_count = len(results)
        
        return {
            "test_results": results,
            "passed": passed_count,
            "total": total_count,
            "score_percentage": (passed_count / total_count * 100) if total_count > 0 else 0
        }

class PlagiarismDetector:
    """Detect code/text similarity"""
    
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
    
    def check_similarity(self, text1: str, text2: str) -> float:
        """Calculate cosine similarity between two texts"""
        try:
            tfidf = self.vectorizer.fit_transform([text1, text2])
            similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
            return float(similarity * 100)  # Return as percentage
        except:
            return 0.0
    
    def check_against_database(self, submission: str, 
                               previous_submissions: List[str]) -> Dict[str, Any]:
        """Check submission against all previous submissions"""
        if not previous_submissions:
            return {"is_plagiarized": False, "max_similarity": 0.0, "similar_to": []}
        
        similarities = []
        for idx, prev_sub in enumerate(previous_submissions):
            similarity = self.check_similarity(submission, prev_sub)
            if similarity > 70:  # Threshold for suspicion
                similarities.append({
                    "submission_id": idx,
                    "similarity": similarity
                })
        
        max_sim = max([s["similarity"] for s in similarities]) if similarities else 0.0
        
        return {
            "is_plagiarized": max_sim > 80,
            "max_similarity": max_sim,
            "similar_submissions": similarities,
            "flagged": max_sim > 70
        }

class AnomalyDetector:
    """Detect suspicious assessment behavior"""
    
    def detect_anomalies(self, assessment_data: Dict[str, Any]) -> List[str]:
        """Detect various types of suspicious behavior"""
        flags = []
        
        submissions = assessment_data.get("submissions", [])
        if not submissions:
            return flags
        
        # Check for too-fast submissions
        avg_time = sum(s.get("time_taken_seconds", 0) for s in submissions) / len(submissions)
        if avg_time < 10:  # Less than 10 seconds per question
            flags.append("Suspiciously fast submission times")
        
        # Check for all same answers pattern (random guessing)
        mcq_answers = [s.get("selected_option") for s in submissions 
                      if s.get("selected_option")]
        if len(mcq_answers) > 5 and len(set(mcq_answers)) == 1:
            flags.append("All same option selected - possible random guessing")
        
        # Check for perfect score with low time
        total_score = assessment_data.get("total_score", 0)
        max_score = assessment_data.get("max_possible_score", 100)
        if total_score / max_score > 0.95 and avg_time < 30:
            flags.append("Unrealistically high score with low time investment")
        
        # Check for high plagiarism
        high_plagiarism = [s for s in submissions 
                          if s.get("plagiarism_score", 0) > 70]
        if len(high_plagiarism) > len(submissions) * 0.3:
            flags.append("High plagiarism detected in multiple answers")
        
        return flags

# Create singleton instances
code_executor = CodeExecutor()
plagiarism_detector = PlagiarismDetector()
anomaly_detector = AnomalyDetector()
