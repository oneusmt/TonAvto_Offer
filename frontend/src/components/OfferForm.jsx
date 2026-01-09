import { useState } from 'react';

const OfferForm = ({ offer, onSubmit, onCancel }) => {
  const [formData, setFormData] = useState({
    name: offer?.name || '',
    description: offer?.description || '',
    number: offer?.number || '',
    price: offer?.price || '',
    image_url: offer?.image_url || '',
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
    onSubmit(formData);
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
