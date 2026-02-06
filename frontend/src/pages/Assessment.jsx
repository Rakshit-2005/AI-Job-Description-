import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { getAssessmentQuestions, submitAnswer, completeAssessment } from '../api';

export default function Assessment() {
  const { assessmentId } = useParams();
  const navigate = useNavigate();
  const [questions, setQuestions] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [answers, setAnswers] = useState({});
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);

  useEffect(() => {
    fetchQuestions();
  }, []);

  const fetchQuestions = async () => {
    try {
      const response = await getAssessmentQuestions(assessmentId);
      setQuestions(response.data);
    } catch (err) {
      alert('Failed to load questions');
    } finally {
      setLoading(false);
    }
  };

  const handleAnswer = (questionId, value) => {
    setAnswers({
      ...answers,
      [questionId]: value
    });
  };

  const handleSubmitQuestion = async () => {
    const question = questions[currentIndex];
    const answer = answers[question.id];

    if (!answer) {
      alert('Please provide an answer');
      return;
    }

    const submitData = {
      question_id: question.id
    };

    if (question.question_type === 'mcq') {
      submitData.selected_option = answer;
    } else if (question.question_type === 'coding') {
      submitData.code_submission = answer;
    } else {
      submitData.answer = answer;
    }

    try {
      await submitAnswer(assessmentId, submitData);
      
      if (currentIndex < questions.length - 1) {
        setCurrentIndex(currentIndex + 1);
      } else {
        // Last question - complete assessment
        await handleCompleteAssessment();
      }
    } catch (err) {
      alert('Failed to submit answer');
    }
  };

  const handleCompleteAssessment = async () => {
    setSubmitting(true);
    try {
      await completeAssessment(assessmentId);
      navigate(`/results/${assessmentId}`);
    } catch (err) {
      alert('Failed to complete assessment');
      setSubmitting(false);
    }
  };

  if (loading) {
    return <div className="loading">Loading assessment...</div>;
  }

  if (questions.length === 0) {
    return <div className="loading">No questions available</div>;
  }

  const currentQuestion = questions[currentIndex];
  const progress = ((currentIndex + 1) / questions.length) * 100;

  return (
    <div className="container" style={{ maxWidth: '900px' }}>
      {/* Progress Bar */}
      <div style={{ marginBottom: '24px' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '8px', color: 'white' }}>
          <span>Question {currentIndex + 1} of {questions.length}</span>
          <span>{Math.round(progress)}% Complete</span>
        </div>
        <div className="progress-bar">
          <div className="progress-fill" style={{ width: `${progress}%` }}></div>
        </div>
      </div>

      {/* Question Navigation */}
      <div className="question-nav">
        {questions.map((q, idx) => (
          <button
            key={q.id}
            className={`question-nav-btn ${idx === currentIndex ? 'active' : ''} ${answers[q.id] ? 'answered' : ''}`}
            onClick={() => setCurrentIndex(idx)}
          >
            {idx + 1}
          </button>
        ))}
      </div>

      {/* Question Card */}
      <div className="card">
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '16px' }}>
          <span className={`badge badge-${currentQuestion.difficulty}`}>
            {currentQuestion.difficulty.toUpperCase()}
          </span>
          <span className="badge badge-primary">
            {currentQuestion.question_type.toUpperCase()}
          </span>
        </div>

        <h3 style={{ marginBottom: '16px', lineHeight: '1.6' }}>
          {currentQuestion.question_text}
        </h3>

        {currentQuestion.question_type === 'mcq' && (
          <div>
            {currentQuestion.options?.map((option, idx) => (
              <label
                key={idx}
                style={{
                  display: 'block',
                  padding: '12px',
                  marginBottom: '8px',
                  border: '2px solid',
                  borderColor: answers[currentQuestion.id] === option ? '#667eea' : '#e5e7eb',
                  borderRadius: '8px',
                  cursor: 'pointer',
                  background: answers[currentQuestion.id] === option ? '#f0f4ff' : 'white',
                  transition: 'all 0.3s'
                }}
              >
                <input
                  type="radio"
                  name="mcq"
                  value={option}
                  checked={answers[currentQuestion.id] === option}
                  onChange={(e) => handleAnswer(currentQuestion.id, e.target.value)}
                  style={{ marginRight: '8px' }}
                />
                {option}
              </label>
            ))}
          </div>
        )}

        {currentQuestion.question_type === 'subjective' && (
          <textarea
            className="textarea"
            placeholder="Type your answer here..."
            value={answers[currentQuestion.id] || ''}
            onChange={(e) => handleAnswer(currentQuestion.id, e.target.value)}
            style={{ minHeight: '200px' }}
          />
        )}

        {currentQuestion.question_type === 'coding' && (
          <div>
            <textarea
              className="code-editor"
              placeholder={currentQuestion.starter_code || "# Write your code here\n\ndef solution():\n    pass"}
              value={answers[currentQuestion.id] || currentQuestion.starter_code || ''}
              onChange={(e) => handleAnswer(currentQuestion.id, e.target.value)}
              style={{ fontFamily: 'monospace' }}
            />
          </div>
        )}

        <div style={{ display: 'flex', gap: '12px', marginTop: '24px' }}>
          {currentIndex > 0 && (
            <button
              className="btn btn-secondary"
              onClick={() => setCurrentIndex(currentIndex - 1)}
            >
              ← Previous
            </button>
          )}
          
          <button
            className="btn btn-primary"
            onClick={handleSubmitQuestion}
            disabled={submitting}
            style={{ flex: 1 }}
          >
            {submitting ? 'Submitting...' : 
             currentIndex === questions.length - 1 ? 'Submit & Complete' : 'Next →'}
          </button>
        </div>
      </div>
    </div>
  );
}
