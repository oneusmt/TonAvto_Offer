import { useState, useEffect } from 'react';
import { offersAPI } from '../api/client';
import OfferForm from './OfferForm';

const OfferList = () => {
  const [offers, setOffers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [editingOffer, setEditingOffer] = useState(null);

  useEffect(() => {
    loadOffers();
  }, []);

  const loadOffers = async () => {
    try {
      setLoading(true);
      const response = await offersAPI.getAll();
      setOffers(response.data);
      setError(null);
    } catch (err) {
      setError('Ошибка загрузки предложений');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleCreate = async (data) => {
    try {
      await offersAPI.create(data);
      await loadOffers();
      setShowForm(false);
    } catch (err) {
      alert('Ошибка создания предложения');
      console.error(err);
    }
  };

  const handleUpdate = async (data) => {
    try {
      await offersAPI.update(editingOffer.id, data);
      await loadOffers();
      setEditingOffer(null);
    } catch (err) {
      alert('Ошибка обновления предложения');
      console.error(err);
    }
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Вы уверены, что хотите удалить это предложение?')) {
      return;
    }
    try {
      await offersAPI.delete(id);
      await loadOffers();
    } catch (err) {
      alert('Ошибка удаления предложения');
      console.error(err);
    }
  };

  if (loading) {
    return <div className="loading">Загрузка...</div>;
  }

  return (
    <div className="offer-list-container">
      <div className="section-header">
        <h2>Предложения (Offers)</h2>
        <button
          onClick={() => {
            setShowForm(!showForm);
            setEditingOffer(null);
          }}
          className="btn btn-primary"
        >
          {showForm ? 'Скрыть форму' : '+ Добавить предложение'}
        </button>
      </div>

      {showForm && !editingOffer && (
        <div className="form-container">
          <h3>Создать новое предложение</h3>
          <OfferForm
            onSubmit={handleCreate}
            onCancel={() => setShowForm(false)}
          />
        </div>
      )}

      {editingOffer && (
        <div className="form-container">
          <h3>Редактировать предложение</h3>
          <OfferForm
            offer={editingOffer}
            onSubmit={handleUpdate}
            onCancel={() => setEditingOffer(null)}
          />
        </div>
      )}

      {error && <div className="error">{error}</div>}

      <div className="cards-grid">
        {offers.map((offer) => (
          <div key={offer.id} className="card">
            {offer.image_url && (
              <img src={offer.image_url} alt={offer.name} className="card-image" />
            )}
            <div className="card-content">
              <h3>{offer.name}</h3>
              {offer.description && <p>{offer.description}</p>}
              <div className="card-info">
                <span>Номер: {offer.number}</span>
                <span className="price">Цена: {offer.price} ₽</span>
              </div>
              <div className="card-actions">
                <button
                  onClick={() => setEditingOffer(offer)}
                  className="btn btn-small btn-secondary"
                >
                  Редактировать
                </button>
                <button
                  onClick={() => handleDelete(offer.id)}
                  className="btn btn-small btn-danger"
                >
                  Удалить
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>

      {offers.length === 0 && !loading && (
        <div className="empty-state">Нет предложений</div>
      )}
    </div>
  );
};

export default OfferList;
