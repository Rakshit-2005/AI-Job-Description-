import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { createJob, getJobs } from '../api';

export default function RecruiterDashboard() {
  const [jobs, setJobs] = useState([]);
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    duration_minutes: 60,
    cutoff_percentage: 60
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchJobs();
  }, []);

  const fetchJobs = async () => {
    try {
      const response = await getJobs();
      setJobs(response.data);
    } catch (err) {
      console.error('Error fetching jobs:', err);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      await createJob(formData);
      setShowForm(false);
      setFormData({ title: '', description: '', duration_minutes: 60, cutoff_percentage: 60 });
      fetchJobs();
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to create job');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '24px' }}>
        <h1 style={{ color: 'white', fontSize: '32px' }}>Recruiter Dashboard</h1>
        <button className="btn btn-primary" onClick={() => setShowForm(!showForm)}>
          {showForm ? 'Cancel' : '+ Create New Job'}
        </button>
      </div>

      {error && <div className="error">{error}</div>}

      {showForm && (
        <div className="card">
          <h2 style={{ marginBottom: '20px' }}>Create Job & Generate Assessment</h2>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label className="label">Job Title</label>
              <input
                type="text"
                className="input"
                value={formData.title}
                onChange={(e) => setFormData({...formData, title: e.target.value})}
                required
                placeholder="e.g., Full Stack Developer"
              />
            </div>

            <div className="form-group">
              <label className="label">Job Description</label>
              <textarea
                className="textarea"
                value={formData.description}
                onChange={(e) => setFormData({...formData, description: e.target.value})}
                required
                placeholder="Paste complete job description here. AI will parse skills, experience level, and generate relevant questions."
                style={{ minHeight: '200px' }}
              />
            </div>

            <div className="grid grid-2">
              <div className="form-group">
                <label className="label">Duration (minutes)</label>
                <input
                  type="number"
                  className="input"
                  value={formData.duration_minutes}
                  onChange={(e) => setFormData({...formData, duration_minutes: parseInt(e.target.value)})}
                  min="15"
                  max="180"
                />
              </div>

              <div className="form-group">
                <label className="label">Cutoff Percentage</label>
                <input
                  type="number"
                  className="input"
                  value={formData.cutoff_percentage}
                  onChange={(e) => setFormData({...formData, cutoff_percentage: parseFloat(e.target.value)})}
                  min="0"
                  max="100"
                  step="0.1"
                />
              </div>
            </div>

            <button type="submit" className="btn btn-primary" disabled={loading}>
              {loading ? 'Creating & Generating Questions...' : 'Create Job'}
            </button>
          </form>
        </div>
      )}

      <div className="grid grid-2">
        {jobs.map((job) => (
          <div key={job.id} className="card">
            <h3 style={{ marginBottom: '12px', color: '#667eea' }}>{job.title}</h3>
            <p style={{ color: '#6b7280', marginBottom: '12px', fontSize: '14px' }}>
              {job.description.substring(0, 150)}...
            </p>
            
            <div style={{ marginBottom: '12px' }}>
              {job.required_skills?.slice(0, 5).map((skill, idx) => (
                <span key={idx} className="badge badge-primary">{skill}</span>
              ))}
            </div>

            <div style={{ fontSize: '14px', color: '#6b7280', marginBottom: '12px' }}>
              <div>⏱️ Duration: {job.duration_minutes} min</div>
              <div>📊 Cutoff: {job.cutoff_percentage}%</div>
              <div>📅 Created: {new Date(job.created_at).toLocaleDateString()}</div>
            </div>

            <Link to={`/leaderboard/${job.id}`}>
              <button className="btn btn-secondary" style={{ width: '100%' }}>
                View Leaderboard
              </button>
            </Link>
          </div>
        ))}
      </div>

      {jobs.length === 0 && !showForm && (
        <div className="card" style={{ textAlign: 'center', padding: '60px' }}>
          <h3 style={{ color: '#6b7280' }}>No jobs created yet</h3>
          <p style={{ color: '#9ca3af', marginTop: '12px' }}>
            Create your first job to get started
          </p>
        </div>
      )}
    </div>
  );
}
