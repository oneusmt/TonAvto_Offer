import { useState, useEffect } from 'react';
import { buysAPI } from '../api/client';

const SoldForm = ({ sold, onSubmit, onCancel }) => {
  const [buys, setBuys] = useState([]);
  const [formData, setFormData] = useState({
    name: sold?.name || '',
    buy_id: sold?.buy_id || '',
    price: sold?.price || '',
  });

  useEffect(() => {
    loadBuys();
  }, []);

  const loadBuys = async () => {
    try {
      const response = await buysAPI.getAll();
      setBuys(response.data);
    } catch (err) {
      console.error('Ошибка загрузки покупок:', err);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: name === 'buy_id' || name === 'price' ? (value === '' ? '' : Number(value)) : value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <form onSubmit={handleSubmit} className="sold-form">
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
        <label>Покупка (Buy):</label>
        <select
          name="buy_id"
          value={formData.buy_id}
          onChange={handleChange}
          required
        >
          <option value="">Выберите покупку</option>
          {buys.map((buy) => (
            <option key={buy.id} value={buy.id}>
              {buy.name} (ID: {buy.id})
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
      <div className="form-actions">
        <button type="submit" className="btn btn-primary">
          {sold ? 'Обновить' : 'Создать'}
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

export default SoldForm;
