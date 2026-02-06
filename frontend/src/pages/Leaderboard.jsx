import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { getLeaderboard } from '../api';

export default function Leaderboard() {
  const { jobId } = useParams();
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchLeaderboard();
  }, []);

  const fetchLeaderboard = async () => {
    try {
      const response = await getLeaderboard(jobId);
      setLeaderboard(response.data);
    } catch (err) {
      console.error('Error fetching leaderboard:', err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="loading">Loading leaderboard...</div>;
  }

  return (
    <div className="container">
      <h1 style={{ color: 'white', fontSize: '32px', marginBottom: '24px' }}>
        🏆 Leaderboard
      </h1>

      <div className="card">
        {leaderboard.length === 0 ? (
          <div style={{ textAlign: 'center', padding: '40px', color: '#6b7280' }}>
            <h3>No candidates have completed the assessment yet</h3>
          </div>
        ) : (
          <table className="leaderboard-table">
            <thead>
              <tr>
                <th>Rank</th>
                <th>Candidate</th>
                <th>Score</th>
                <th>Percentage</th>
                <th>Completed At</th>
              </tr>
            </thead>
            <tbody>
              {leaderboard.map((entry) => (
                <tr key={entry.rank}>
                  <td>
                    <span 
                      className={`rank-badge ${entry.rank <= 3 ? `rank-${entry.rank}` : ''}`}
                      style={entry.rank > 3 ? { background: '#e5e7eb', color: '#6b7280' } : {}}
                    >
                      {entry.rank}
                    </span>
                  </td>
                  <td>
                    <strong>{entry.candidate_name}</strong>
                  </td>
                  <td>
                    <span style={{ fontSize: '18px', fontWeight: 600, color: '#667eea' }}>
                      {entry.total_score.toFixed(1)}
                    </span>
                  </td>
                  <td>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <div className="progress-bar" style={{ width: '100px' }}>
                        <div 
                          className="progress-fill" 
                          style={{ width: `${entry.percentage}%` }}
                        ></div>
                      </div>
                      <span style={{ fontWeight: 500 }}>
                        {entry.percentage.toFixed(1)}%
                      </span>
                    </div>
                  </td>
                  <td style={{ color: '#6b7280' }}>
                    {new Date(entry.completed_at).toLocaleString()}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>

      {/* Top 3 Highlight */}
      {leaderboard.length >= 3 && (
        <div style={{ marginTop: '32px' }}>
          <h2 style={{ color: 'white', marginBottom: '16px' }}>Top Performers</h2>
          <div className="grid grid-3">
            {leaderboard.slice(0, 3).map((entry, idx) => (
              <div 
                key={entry.rank} 
                className="card"
                style={{
                  background: idx === 0 ? 'linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%)' :
                             idx === 1 ? 'linear-gradient(135deg, #d1d5db 0%, #9ca3af 100%)' :
                             'linear-gradient(135deg, #fca5a5 0%, #ef4444 100%)',
                  color: 'white'
                }}
              >
                <div style={{ fontSize: '48px', textAlign: 'center' }}>
                  {idx === 0 ? '🥇' : idx === 1 ? '🥈' : '🥉'}
                </div>
                <h3 style={{ textAlign: 'center', marginTop: '12px' }}>
                  {entry.candidate_name}
                </h3>
                <div style={{ textAlign: 'center', fontSize: '24px', fontWeight: 700, marginTop: '8px' }}>
                  {entry.total_score.toFixed(1)} ({entry.percentage.toFixed(1)}%)
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
