import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { useState, useEffect } from 'react';
import Header from './components/Header';
import Login from './pages/Login';
import Register from './pages/Register';
import RecruiterDashboard from './pages/RecruiterDashboard';
import CandidateDashboard from './pages/CandidateDashboard';
import Assessment from './pages/Assessment';
import Results from './pages/Results';
import Leaderboard from './pages/Leaderboard';

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem('token');
    const userData = localStorage.getItem('user');
    if (token && userData) {
      setUser(JSON.parse(userData));
    }
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    setUser(null);
  };

  return (
    <BrowserRouter>
      <Header user={user} onLogout={handleLogout} />
      <Routes>
        <Route path="/login" element={
          user ? <Navigate to={user.role === 'recruiter' ? '/recruiter' : '/dashboard'} /> 
               : <Login setUser={setUser} />
        } />
        <Route path="/register" element={
          user ? <Navigate to={user.role === 'recruiter' ? '/recruiter' : '/dashboard'} /> 
               : <Register setUser={setUser} />
        } />
        <Route path="/recruiter" element={
          user?.role === 'recruiter' ? <RecruiterDashboard /> : <Navigate to="/login" />
        } />
        <Route path="/dashboard" element={
          user ? <CandidateDashboard /> : <Navigate to="/login" />
        } />
        <Route path="/assessment/:assessmentId" element={
          user ? <Assessment /> : <Navigate to="/login" />
        } />
        <Route path="/results/:assessmentId" element={
          user ? <Results /> : <Navigate to="/login" />
        } />
        <Route path="/leaderboard/:jobId" element={<Leaderboard />} />
        <Route path="/" element={<Navigate to="/login" />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
