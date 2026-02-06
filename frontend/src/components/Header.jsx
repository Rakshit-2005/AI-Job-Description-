import { Link } from 'react-router-dom';

export default function Header({ user, onLogout }) {
  return (
    <header className="header">
      <div className="header-content">
        <Link to="/" className="logo">
          🎯 AI Assessment Platform
        </Link>
        {user && (
          <div style={{ display: 'flex', gap: '16px', alignItems: 'center' }}>
            <span style={{ color: '#667eea', fontWeight: 600 }}>
              {user.full_name} ({user.role})
            </span>
            <button onClick={onLogout} className="btn btn-secondary">
              Logout
            </button>
          </div>
        )}
      </div>
    </header>
  );
}
