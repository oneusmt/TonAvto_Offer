import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

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

export default apiClient;
