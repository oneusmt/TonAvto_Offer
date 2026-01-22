import { useState, useEffect } from 'react';
import { offersAPI } from '../api/client';

const BuyForm = ({ buy, onSubmit, onCancel }) => {
  const [offers, setOffers] = useState([]);
  const [formData, setFormData] = useState({
    name: buy?.name || '',
    offer_id: buy?.offer_id || '',
    price: buy?.price || '',
    vlozheno: buy?.vlozheno || 0,
  });

  useEffect(() => {
    loadOffers();
  }, []);

  const loadOffers = async () => {
    try {
      const response = await offersAPI.getAll();
      setOffers(response.data);
    } catch (err) {
      console.error('Ошибка загрузки предложений:', err);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: name === 'offer_id' || name === 'price' || name === 'vlozheno' 
        ? (value === '' ? '' : Number(value)) 
        : value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <form onSubmit={handleSubmit} className="buy-form">
      <div className="form-group">
        <label>Название:</label>
        <input
          type="text"
          name="name"
          value={formData.name}
          onChange={handleChange}
          required
        />
      </div>
      <div className="form-group">
        <label>Предложение (Offer):</label>
        <select
          name="offer_id"
          value={formData.offer_id}
          onChange={handleChange}
          required
        >
          <option value="">Выберите предложение</option>
          {offers.map((offer) => (
            <option key={offer.id} value={offer.id}>
              {offer.name} (ID: {offer.id})
            </option>
          ))}
        </select>
      </div>
      <div className="form-group">
        <label>Цена:</label>
        <input
          type="number"
          name="price"
          value={formData.price}
          onChange={handleChange}
          step="0.01"
          required
        />
      </div>
      <div className="form-group">
        <label>Вложено:</label>
        <input
          type="number"
          name="vlozheno"
          value={formData.vlozheno}
          onChange={handleChange}
          min="0"
          step="1"
          required
        />
      </div>
      <div className="form-actions">
        <button type="submit" className="btn btn-primary">
          {buy ? 'Обновить' : 'Создать'}
        </button>
        {onCancel && (
          <button type="button" onClick={onCancel} className="btn btn-secondary">
            Отмена
          </button>
        )}
      </div>
    </form>
  );
};

export default BuyForm;
