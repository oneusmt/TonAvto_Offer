import { useState } from 'react';

const OfferForm = ({ offer, onSubmit, onCancel }) => {
  const formatDateForInput = (dateStr) => {
    if (!dateStr) return '';
    const d = new Date(dateStr);
    return d.toISOString().slice(0, 10);
  };

  const [formData, setFormData] = useState({
    name: offer?.name || '',
    description: offer?.description || '',
    number: offer?.number || '',
    price: offer?.price || '',
    image_url: offer?.image_url || '',
    status: offer?.status || 'active',
    callback_date: formatDateForInput(offer?.callback_date) || '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: name === 'number' || name === 'price' ? (value === '' ? '' : Number(value)) : value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const data = { ...formData };
    if (!data.callback_date) data.callback_date = null;
    else data.callback_date = new Date(data.callback_date + 'T12:00:00').toISOString();
    onSubmit(data);
  };

  return (
    <form onSubmit={handleSubmit} className="offer-form">
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
        <label>Описание:</label>
        <textarea
          name="description"
          value={formData.description}
          onChange={handleChange}
          rows="3"
        />
      </div>
      <div className="form-group">
        <label>Номер:</label>
        <input
          type="number"
          name="number"
          value={formData.number}
          onChange={handleChange}
          required
        />
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
        <label>URL изображения:</label>
        <input
          type="text"
          name="image_url"
          value={formData.image_url}
          onChange={handleChange}
        />
      </div>
      <div className="form-group">
        <label>Статус:</label>
        <select
          name="status"
          value={formData.status}
          onChange={handleChange}
          required
        >
          <option value="active">Активные</option>
          <option value="thinking">Надо подумать</option>
          <option value="bought">Выкупленные</option>
        </select>
      </div>
      <div className="form-group">
        <label>Дата повторного звонка:</label>
        <input
          type="date"
          name="callback_date"
          value={formData.callback_date}
          onChange={handleChange}
        />
      </div>
      <div className="form-actions">
        <button type="submit" className="btn btn-primary">
          {offer ? 'Обновить' : 'Создать'}
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

export default OfferForm;
