from pydantic import BaseModel, EmailStr
from typing import List, Optional, Dict, Any
from datetime import datetime

# User schemas
class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    role: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# Job schemas
class JobCreate(BaseModel):
    title: str
    description: str
    duration_minutes: Optional[int] = 60
    cutoff_percentage: Optional[float] = 60.0

class JobResponse(BaseModel):
    id: int
    title: str
    description: str
    required_skills: Optional[List[str]]
    experience_level: Optional[str]
    role_type: Optional[str]
    domain_knowledge: Optional[List[str]]
    duration_minutes: int
    cutoff_percentage: float
    created_at: datetime
    is_active: bool
    
    class Config:
        from_attributes = True

# Question schemas
class QuestionResponse(BaseModel):
    id: int
    question_type: str
    question_text: str
    difficulty: str
    skill_tested: str
    options: Optional[List[str]]
    max_score: float
    starter_code: Optional[str]
    
    class Config:
        from_attributes = True

# Assessment schemas
class AssessmentCreate(BaseModel):
    job_id: int
    resume_url: Optional[str]

class AssessmentResponse(BaseModel):
    id: int
    job_id: int
    candidate_id: int
    status: str
    started_at: Optional[datetime]
    completed_at: Optional[datetime]
    total_score: Optional[float]
    percentage: Optional[float]
    rank: Optional[int]
    
    class Config:
        from_attributes = True

# Submission schemas
class SubmissionCreate(BaseModel):
    question_id: int
    answer: Optional[str]
    selected_option: Optional[str]
    code_submission: Optional[str]

class SubmissionResponse(BaseModel):
    id: int
    question_id: int
    score: Optional[float]
    is_correct: Optional[bool]
    ai_feedback: Optional[str]
    submitted_at: datetime
    
    class Config:
        from_attributes = True

# Evaluation schemas
class EvaluationResponse(BaseModel):
    id: int
    assessment_id: int
    strengths: List[str]
    weaknesses: List[str]
    skill_gaps: List[str]
    skill_scores: Dict[str, float]
    mcq_score: float
    subjective_score: float
    coding_score: float
    percentile: float
    qualified: bool
    ai_summary: str
    recommendation: str
    
    class Config:
        from_attributes = True

# Leaderboard schema
class LeaderboardEntry(BaseModel):
    rank: int
    candidate_name: str
    total_score: float
    percentage: float
    skill_scores: Dict[str, float]
    completed_at: datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
