import google.generativeai as genai
from config import get_settings
import json
from typing import List, Dict, Any

settings = get_settings()
genai.configure(api_key=settings.GEMINI_API_KEY)

class GeminiService:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-pro')
    
    def parse_job_description(self, jd_text: str) -> Dict[str, Any]:
        """Parse job description and extract key information"""
        prompt = f"""
Analyze this job description and extract the following information in JSON format:
- required_skills: List of technical and soft skills (array)
- experience_level: Fresher, Junior, Mid-level, Senior, or Expert
- role_type: Job role category (e.g., Full Stack Developer, Data Analyst)
- domain_knowledge: Required domain/industry knowledge (array)
- key_responsibilities: Main responsibilities (array)
- tools_technologies: Specific tools and technologies (array)

Job Description:
{jd_text}

Return ONLY valid JSON without any markdown formatting or extra text.
"""
        
        response = self.model.generate_content(prompt)
        try:
            # Clean response and parse JSON
            text = response.text.strip()
            if text.startswith('```json'):
                text = text[7:]
            if text.startswith('```'):
                text = text[3:]
            if text.endswith('```'):
                text = text[:-3]
            return json.loads(text.strip())
        except:
            return {
                "required_skills": [],
                "experience_level": "Mid-level",
                "role_type": "General",
                "domain_knowledge": [],
                "key_responsibilities": [],
                "tools_technologies": []
            }
    
    def generate_questions(self, job_data: Dict[str, Any], num_mcq: int = 10, 
                          num_subjective: int = 5, num_coding: int = 3) -> List[Dict[str, Any]]:
        """Generate assessment questions based on job requirements"""
        
        questions = []
        
        # Generate MCQ questions
        mcq_prompt = f"""
Generate {num_mcq} multiple choice questions for assessing candidates for this role:
Skills: {', '.join(job_data.get('required_skills', []))}
Experience: {job_data.get('experience_level', 'Mid-level')}
Role: {job_data.get('role_type', 'General')}

For each question, provide:
- question_text: The question
- options: Array of 4 options (A, B, C, D)
- correct_answer: The correct option letter
- difficulty: easy, medium, or hard
- skill_tested: Which skill this tests

Return as JSON array without markdown formatting.
"""
        
        try:
            response = self.model.generate_content(mcq_prompt)
            text = response.text.strip()
            if text.startswith('```json'):
                text = text[7:]
            if text.startswith('```'):
                text = text[3:]
            if text.endswith('```'):
                text = text[:-3]
            mcq_questions = json.loads(text.strip())
            
            for q in mcq_questions[:num_mcq]:
                questions.append({
                    "question_type": "mcq",
                    "question_text": q.get("question_text", ""),
                    "options": q.get("options", []),
                    "correct_answer": q.get("correct_answer", "A"),
                    "difficulty": q.get("difficulty", "medium"),
                    "skill_tested": q.get("skill_tested", "general"),
                    "max_score": 10 if q.get("difficulty") == "hard" else 5 if q.get("difficulty") == "medium" else 3
                })
        except Exception as e:
            print(f"Error generating MCQ: {e}")
        
        # Generate subjective questions
        subj_prompt = f"""
Generate {num_subjective} subjective/scenario-based questions for this role:
Skills: {', '.join(job_data.get('required_skills', []))}
Responsibilities: {', '.join(job_data.get('key_responsibilities', [])[:3])}

For each question:
- question_text: Detailed scenario or problem
- difficulty: easy, medium, or hard
- skill_tested: Which skill/competency

Return as JSON array without markdown formatting.
"""
        
        try:
            response = self.model.generate_content(subj_prompt)
            text = response.text.strip()
            if text.startswith('```json'):
                text = text[7:]
            if text.startswith('```'):
                text = text[3:]
            if text.endswith('```'):
                text = text[:-3]
            subj_questions = json.loads(text.strip())
            
            for q in subj_questions[:num_subjective]:
                questions.append({
                    "question_type": "subjective",
                    "question_text": q.get("question_text", ""),
                    "difficulty": q.get("difficulty", "medium"),
                    "skill_tested": q.get("skill_tested", "analytical"),
                    "max_score": 20 if q.get("difficulty") == "hard" else 15 if q.get("difficulty") == "medium" else 10
                })
        except Exception as e:
            print(f"Error generating subjective: {e}")
        
        # Generate coding questions
        if num_coding > 0 and any(tech in str(job_data.get('required_skills', [])).lower() 
                                  for tech in ['python', 'java', 'javascript', 'programming', 'code']):
            coding_prompt = f"""
Generate {num_coding} coding problems for this role:
Skills: {', '.join(job_data.get('required_skills', []))}
Technologies: {', '.join(job_data.get('tools_technologies', []))}

For each problem:
- question_text: Problem description with constraints
- difficulty: easy, medium, or hard
- skill_tested: Which programming skill
- starter_code: Basic function template
- test_cases: Array of {"input": "...", "expected_output": "..."}

Return as JSON array without markdown formatting.
"""
            
            try:
                response = self.model.generate_content(coding_prompt)
                text = response.text.strip()
                if text.startswith('```json'):
                    text = text[7:]
                if text.startswith('```'):
                    text = text[3:]
                if text.endswith('```'):
                    text = text[:-3]
                coding_questions = json.loads(text.strip())
                
                for q in coding_questions[:num_coding]:
                    questions.append({
                        "question_type": "coding",
                        "question_text": q.get("question_text", ""),
                        "difficulty": q.get("difficulty", "medium"),
                        "skill_tested": q.get("skill_tested", "programming"),
                        "starter_code": q.get("starter_code", ""),
                        "test_cases": q.get("test_cases", []),
                        "max_score": 30 if q.get("difficulty") == "hard" else 20 if q.get("difficulty") == "medium" else 15
                    })
            except Exception as e:
                print(f"Error generating coding: {e}")
        
        return questions
    
    def evaluate_subjective_answer(self, question: str, answer: str, 
                                   max_score: float) -> Dict[str, Any]:
        """Evaluate subjective answer using AI"""
        prompt = f"""
Evaluate this answer to a subjective question:

Question: {question}
Answer: {answer}
Maximum Score: {max_score}

Provide evaluation in JSON format:
- score: Number between 0 and {max_score}
- feedback: Detailed feedback (2-3 sentences)
- strengths: What was good (array)
- weaknesses: What could be improved (array)

Return ONLY valid JSON without markdown formatting.
"""
        
        response = self.model.generate_content(prompt)
        try:
            text = response.text.strip()
            if text.startswith('```json'):
                text = text[7:]
            if text.startswith('```'):
                text = text[3:]
            if text.endswith('```'):
                text = text[:-3]
            return json.loads(text.strip())
        except:
            return {
                "score": max_score * 0.5,
                "feedback": "Unable to evaluate automatically.",
                "strengths": [],
                "weaknesses": []
            }
    
    def generate_evaluation_report(self, assessment_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate comprehensive evaluation report"""
        prompt = f"""
Generate a comprehensive evaluation report for this candidate:

Assessment Data:
{json.dumps(assessment_data, indent=2)}

Provide analysis in JSON format:
- strengths: Top 3-5 strengths (array)
- weaknesses: Top 3-5 areas for improvement (array)
- skill_gaps: Missing or weak skills (array)
- ai_summary: Overall performance summary (2-3 sentences)
- recommendation: Hire/Maybe/Reject with reasoning

Return ONLY valid JSON without markdown formatting.
"""
        
        response = self.model.generate_content(prompt)
        try:
            text = response.text.strip()
            if text.startswith('```json'):
                text = text[7:]
            if text.startswith('```'):
                text = text[3:]
            if text.endswith('```'):
                text = text[:-3]
            return json.loads(text.strip())
        except:
            return {
                "strengths": ["Completed assessment"],
                "weaknesses": ["Needs more practice"],
                "skill_gaps": [],
                "ai_summary": "Average performance.",
                "recommendation": "Maybe - requires further evaluation"
            }
    
    def detect_resume_mismatch(self, resume_skills: List[str], 
                               performance_data: Dict[str, float]) -> Dict[str, Any]:
        """Detect mismatch between resume claims and actual performance"""
        prompt = f"""
Analyze if there's a mismatch between claimed skills and performance:

Resume Skills: {', '.join(resume_skills)}
Performance Scores: {json.dumps(performance_data)}

Return JSON with:
- is_suspicious: true/false
- mismatch_details: Array of specific mismatches
- confidence_score: 0-100 how confident about mismatch

Return ONLY valid JSON without markdown formatting.
"""
        
        response = self.model.generate_content(prompt)
        try:
            text = response.text.strip()
            if text.startswith('```json'):
                text = text[7:]
            if text.startswith('```'):
                text = text[3:]
            if text.endswith('```'):
                text = text[:-3]
            return json.loads(text.strip())
        except:
            return {
                "is_suspicious": False,
                "mismatch_details": [],
                "confidence_score": 0
            }

# Create singleton instance
gemini_service = GeminiService()
