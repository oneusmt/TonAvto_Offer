import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';
const AUTH_EVENT = 'auth:unauthorized';

const emitUnauthorized = () => {
  if (typeof window !== 'undefined') {
    window.dispatchEvent(new Event(AUTH_EVENT));
  }
};

const getToken = () => {
  if (typeof window === 'undefined') {
    return null;
  }
  return localStorage.getItem('authToken');
};

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

apiClient.interceptors.request.use((config) => {
  const token = getToken();
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      if (typeof window !== 'undefined') {
        localStorage.removeItem('authToken');
      }
      emitUnauthorized();
    }
    return Promise.reject(error);
  }
);

// Offers API
export const offersAPI = {
  getAll: () => apiClient.get('/offer'),
  getById: (id) => apiClient.get(`/offer/${id}`),
  create: (data) => apiClient.post('/offer', data),
  update: (id, data) => apiClient.put(`/offer/${id}`, data),
  delete: (id) => apiClient.delete(`/offer/${id}`),
};

// Buys API
export const buysAPI = {
  getAll: () => apiClient.get('/buy'),
  getById: (id) => apiClient.get(`/buy/${id}`),
  create: (data) => apiClient.post('/buy', data),
  update: (id, data) => apiClient.put(`/buy/${id}`, data),
  delete: (id) => apiClient.delete(`/buy/${id}`),
};

// Sold API
export const soldsAPI = {
  getAll: () => apiClient.get('/sold'),
  getById: (id) => apiClient.get(`/sold/${id}`),
  create: (data) => apiClient.post('/sold', data),
  update: (id, data) => apiClient.put(`/sold/${id}`, data),
  delete: (id) => apiClient.delete(`/sold/${id}`),
};

export const authAPI = {
  login: (credentials) => apiClient.post('/auth/login', credentials),
  logout: () => apiClient.post('/auth/logout'),
};

export const AUTH_UNAUTHORIZED_EVENT = AUTH_EVENT;

export default apiClient;
