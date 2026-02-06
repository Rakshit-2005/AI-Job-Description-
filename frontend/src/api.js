import axios from 'axios';

const API_URL = 'http://localhost:8000';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add auth token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Auth
export const register = (data) => api.post('/register', data);
export const login = (email, password) => {
  const formData = new FormData();
  formData.append('username', email);
  formData.append('password', password);
  return api.post('/token', formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
  });
};

// Jobs
export const createJob = (data) => api.post('/jobs', data);
export const getJobs = () => api.get('/jobs');
export const getJob = (id) => api.get(`/jobs/${id}`);

// Assessments
export const createAssessment = (data) => api.post('/assessments', data);
export const getAssessmentQuestions = (assessmentId) => 
  api.get(`/assessments/${assessmentId}/questions`);
export const submitAnswer = (assessmentId, data) => 
  api.post(`/assessments/${assessmentId}/submit`, data);
export const completeAssessment = (assessmentId) => 
  api.post(`/assessments/${assessmentId}/complete`);

// Results
export const getResults = (assessmentId) => 
  api.get(`/assessments/${assessmentId}/results`);
export const getLeaderboard = (jobId) => 
  api.get(`/jobs/${jobId}/leaderboard`);

export default api;
