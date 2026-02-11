import { useEffect, useState } from 'react';
import OfferList from './components/OfferList';
import BuyList from './components/BuyList';
import SoldList from './components/SoldList';
import LoginForm from './components/LoginForm';
import { authAPI, AUTH_UNAUTHORIZED_EVENT } from './api/client';
import './App.css';

const AUTH_USERNAME = 'oneusmt';

function App() {
  const [activeTab, setActiveTab] = useState('offers');
  const [token, setToken] = useState(() => {
    if (typeof window === 'undefined') {
      return null;
    }
    return localStorage.getItem('authToken');
  });
  const [authError, setAuthError] = useState('');

  useEffect(() => {
    const handleUnauthorized = () => {
      setToken(null);
    };
    window.addEventListener(AUTH_UNAUTHORIZED_EVENT, handleUnauthorized);
    return () => window.removeEventListener(AUTH_UNAUTHORIZED_EVENT, handleUnauthorized);
  }, []);

  const handleLogin = async (credentials) => {
    setAuthError('');
    try {
      const { data } = await authAPI.login(credentials);
      localStorage.setItem('authToken', data.token);
      setToken(data.token);
    } catch (error) {
      setAuthError('Неверный логин или пароль');
      throw error;
    }
  };

  const handleLogout = async () => {
    try {
      await authAPI.logout();
    } catch (error) {
      // ignore logout errors (e.g., expired token)
    } finally {
      localStorage.removeItem('authToken');
      setToken(null);
    }
  };

  if (!token) {
    return (
      <div className="app">
        <header className="app-header">
          <div className="header-top">
            <h1>TonAvto Offer Management</h1>
          </div>
        </header>
        <main className="app-main auth-main">
          <LoginForm onSubmit={handleLogin} error={authError} />
        </main>
      </div>
    );
  }

  return (
    <div className="app">
      <header className="app-header">
        <div className="header-top">
          <h1>TonAvto Offer Management</h1>
          <div className="auth-info">
            <span>Вы вошли как {AUTH_USERNAME}</span>
            <button className="btn btn-secondary btn-small" onClick={handleLogout}>
              Выйти
            </button>
          </div>
        </div>
        <nav className="tabs">
          <button
            className={activeTab === 'offers' ? 'tab active' : 'tab'}
            onClick={() => setActiveTab('offers')}
          >
            Предложения
          </button>
          <button
            className={activeTab === 'buys' ? 'tab active' : 'tab'}
            onClick={() => setActiveTab('buys')}
          >
            Покупки
          </button>
          <button
            className={activeTab === 'solds' ? 'tab active' : 'tab'}
            onClick={() => setActiveTab('solds')}
          >
            Продажи
          </button>
        </nav>
      </header>

      <main className="app-main">
        {activeTab === 'offers' && <OfferList />}
        {activeTab === 'buys' && <BuyList />}
        {activeTab === 'solds' && <SoldList />}
      </main>
    </div>
  );
}

export default App;
