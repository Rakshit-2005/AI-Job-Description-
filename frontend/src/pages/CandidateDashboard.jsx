import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { getJobs, createAssessment } from '../api';

export default function CandidateDashboard() {
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    fetchJobs();
  }, []);

  const fetchJobs = async () => {
    try {
      const response = await getJobs();
      setJobs(response.data);
    } catch (err) {
      console.error('Error fetching jobs:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleStartAssessment = async (jobId) => {
    try {
      const response = await createAssessment({ job_id: jobId });
      navigate(`/assessment/${response.data.id}`);
    } catch (err) {
      alert(err.response?.data?.detail || 'Failed to start assessment');
    }
  };

  if (loading) {
    return <div className="loading">Loading available assessments...</div>;
  }

  return (
    <div className="container">
      <h1 style={{ color: 'white', fontSize: '32px', marginBottom: '24px' }}>
        Available Assessments
      </h1>

      <div className="grid grid-2">
        {jobs.map((job) => (
          <div key={job.id} className="card">
            <h3 style={{ marginBottom: '12px', color: '#667eea' }}>{job.title}</h3>
            <p style={{ color: '#6b7280', marginBottom: '16px', fontSize: '14px', lineHeight: '1.6' }}>
              {job.description.substring(0, 200)}...
            </p>

            <div style={{ marginBottom: '16px' }}>
              <h4 style={{ fontSize: '14px', fontWeight: 600, marginBottom: '8px' }}>
                Required Skills:
              </h4>
              {job.required_skills?.slice(0, 6).map((skill, idx) => (
                <span key={idx} className="badge badge-primary">{skill}</span>
              ))}
            </div>

            <div style={{ 
              background: '#f9fafb', 
              padding: '12px', 
              borderRadius: '8px',
              marginBottom: '16px',
              fontSize: '14px'
            }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '4px' }}>
                <span>⏱️ Duration:</span>
                <strong>{job.duration_minutes} minutes</strong>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '4px' }}>
                <span>📊 Passing Score:</span>
                <strong>{job.cutoff_percentage}%</strong>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                <span>📈 Level:</span>
                <strong>{job.experience_level}</strong>
              </div>
            </div>

            <button 
              className="btn btn-primary" 
              style={{ width: '100%' }}
              onClick={() => handleStartAssessment(job.id)}
            >
              Start Assessment
            </button>
          </div>
        ))}
      </div>

      {jobs.length === 0 && (
        <div className="card" style={{ textAlign: 'center', padding: '60px' }}>
          <h3 style={{ color: '#6b7280' }}>No assessments available</h3>
          <p style={{ color: '#9ca3af', marginTop: '12px' }}>
            Check back later for new opportunities
          </p>
        </div>
      )}
    </div>
  );
}
