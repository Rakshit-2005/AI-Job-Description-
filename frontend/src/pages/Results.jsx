import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { getResults } from '../api';

export default function Results() {
  const { assessmentId } = useParams();
  const [evaluation, setEvaluation] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchResults();
  }, []);

  const fetchResults = async () => {
    try {
      const response = await getResults(assessmentId);
      setEvaluation(response.data);
    } catch (err) {
      console.error('Error fetching results:', err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="loading">Loading results...</div>;
  }

  if (!evaluation) {
    return <div className="loading">No results available</div>;
  }

  const totalScore = evaluation.mcq_score + evaluation.subjective_score + evaluation.coding_score;

  return (
    <div className="container" style={{ maxWidth: '900px' }}>
      <h1 style={{ color: 'white', fontSize: '32px', marginBottom: '24px' }}>
        Assessment Results
      </h1>

      {/* Overall Score */}
      <div className="card" style={{ textAlign: 'center', background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)', color: 'white' }}>
        <h2 style={{ fontSize: '48px', marginBottom: '8px' }}>{totalScore.toFixed(1)}</h2>
        <p style={{ fontSize: '20px', opacity: 0.9 }}>
          {evaluation.qualified ? '✅ Qualified' : '❌ Not Qualified'}
        </p>
        <p style={{ fontSize: '16px', opacity: 0.8, marginTop: '8px' }}>
          Percentile: {evaluation.percentile}th
        </p>
      </div>

      {/* Section-wise Scores */}
      <div className="card">
        <h3 style={{ marginBottom: '16px' }}>Section-wise Performance</h3>
        <div className="grid grid-3">
          <div style={{ textAlign: 'center', padding: '16px', background: '#f0f4ff', borderRadius: '8px' }}>
            <div style={{ fontSize: '24px', fontWeight: 700, color: '#667eea' }}>
              {evaluation.mcq_score.toFixed(1)}
            </div>
            <div style={{ fontSize: '14px', color: '#6b7280', marginTop: '4px' }}>MCQ Score</div>
          </div>
          
          <div style={{ textAlign: 'center', padding: '16px', background: '#f0fdf4', borderRadius: '8px' }}>
            <div style={{ fontSize: '24px', fontWeight: 700, color: '#10b981' }}>
              {evaluation.subjective_score.toFixed(1)}
            </div>
            <div style={{ fontSize: '14px', color: '#6b7280', marginTop: '4px' }}>Subjective Score</div>
          </div>
          
          <div style={{ textAlign: 'center', padding: '16px', background: '#fef3c7', borderRadius: '8px' }}>
            <div style={{ fontSize: '24px', fontWeight: 700, color: '#f59e0b' }}>
              {evaluation.coding_score.toFixed(1)}
            </div>
            <div style={{ fontSize: '14px', color: '#6b7280', marginTop: '4px' }}>Coding Score</div>
          </div>
        </div>
      </div>

      {/* Skill-wise Scores */}
      <div className="card">
        <h3 style={{ marginBottom: '16px' }}>Skill-wise Performance</h3>
        <div className="grid grid-2">
          {Object.entries(evaluation.skill_scores).map(([skill, score]) => (
            <div key={skill} style={{ marginBottom: '12px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '4px' }}>
                <span style={{ fontWeight: 500 }}>{skill}</span>
                <span style={{ color: '#667eea', fontWeight: 600 }}>{score.toFixed(1)}</span>
              </div>
              <div className="progress-bar">
                <div 
                  className="progress-fill" 
                  style={{ width: `${(score / 30) * 100}%` }}
                ></div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Strengths & Weaknesses */}
      <div className="grid grid-2">
        <div className="card">
          <h3 style={{ marginBottom: '16px', color: '#10b981' }}>✅ Strengths</h3>
          <ul style={{ paddingLeft: '20px', lineHeight: '2' }}>
            {evaluation.strengths.map((strength, idx) => (
              <li key={idx} style={{ color: '#374151' }}>{strength}</li>
            ))}
          </ul>
        </div>

        <div className="card">
          <h3 style={{ marginBottom: '16px', color: '#ef4444' }}>⚠️ Areas for Improvement</h3>
          <ul style={{ paddingLeft: '20px', lineHeight: '2' }}>
            {evaluation.weaknesses.map((weakness, idx) => (
              <li key={idx} style={{ color: '#374151' }}>{weakness}</li>
            ))}
          </ul>
        </div>
      </div>

      {/* Skill Gaps */}
      {evaluation.skill_gaps.length > 0 && (
        <div className="card">
          <h3 style={{ marginBottom: '16px' }}>📚 Skills to Develop</h3>
          <div>
            {evaluation.skill_gaps.map((skill, idx) => (
              <span key={idx} className="badge badge-medium">{skill}</span>
            ))}
          </div>
        </div>
      )}

      {/* AI Summary */}
      <div className="card">
        <h3 style={{ marginBottom: '16px' }}>🤖 AI Analysis</h3>
        <p style={{ color: '#374151', lineHeight: '1.8', marginBottom: '16px' }}>
          {evaluation.ai_summary}
        </p>
        <div style={{ 
          background: evaluation.qualified ? '#d1fae5' : '#fee2e2', 
          padding: '16px', 
          borderRadius: '8px',
          color: evaluation.qualified ? '#065f46' : '#991b1b'
        }}>
          <strong>Recommendation:</strong> {evaluation.recommendation}
        </div>
      </div>
    </div>
  );
}
