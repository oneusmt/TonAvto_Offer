import { useState } from 'react';
import OfferList from './components/OfferList';
import BuyList from './components/BuyList';
import './App.css';

function App() {
  const [activeTab, setActiveTab] = useState('offers');

  return (
    <div className="app">
      <header className="app-header">
        <h1>TonAvto Offer Management</h1>
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
        </nav>
      </header>

      <main className="app-main">
        {activeTab === 'offers' && <OfferList />}
        {activeTab === 'buys' && <BuyList />}
      </main>
    </div>
  );
}

export default App;
