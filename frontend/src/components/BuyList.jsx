import { useState, useEffect } from 'react';
import { buysAPI } from '../api/client';
import BuyForm from './BuyForm';

const BuyList = () => {
  const [buys, setBuys] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [editingBuy, setEditingBuy] = useState(null);

  useEffect(() => {
    loadBuys();
  }, []);

  const loadBuys = async () => {
    try {
      setLoading(true);
      const response = await buysAPI.getAll();
      setBuys(response.data);
      setError(null);
    } catch (err) {
      setError('Ошибка загрузки покупок');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleCreate = async (data) => {
    try {
      await buysAPI.create(data);
      await loadBuys();
      setShowForm(false);
    } catch (err) {
      alert('Ошибка создания покупки');
      console.error(err);
    }
  };

  const handleUpdate = async (data) => {
    try {
      await buysAPI.update(editingBuy.id, data);
      await loadBuys();
      setEditingBuy(null);
    } catch (err) {
      alert('Ошибка обновления покупки');
      console.error(err);
    }
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Вы уверены, что хотите удалить эту покупку?')) {
      return;
    }
    try {
      await buysAPI.delete(id);
      await loadBuys();
    } catch (err) {
      alert('Ошибка удаления покупки');
      console.error(err);
    }
  };

  if (loading) {
    return <div className="loading">Загрузка...</div>;
  }

  return (
    <div className="buy-list-container">
      <div className="section-header">
        <h2>Покупки (Buys)</h2>
        <button
          onClick={() => {
            setShowForm(!showForm);
            setEditingBuy(null);
          }}
          className="btn btn-primary"
        >
          {showForm ? 'Скрыть форму' : '+ Добавить покупку'}
        </button>
      </div>

      {showForm && !editingBuy && (
        <div className="form-container">
          <h3>Создать новую покупку</h3>
          <BuyForm
            onSubmit={handleCreate}
            onCancel={() => setShowForm(false)}
          />
        </div>
      )}

      {editingBuy && (
        <div className="form-container">
          <h3>Редактировать покупку</h3>
          <BuyForm
            buy={editingBuy}
            onSubmit={handleUpdate}
            onCancel={() => setEditingBuy(null)}
          />
        </div>
      )}

      {error && <div className="error">{error}</div>}

      <div className="table-container">
        <table className="data-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Название</th>
              <th>ID Предложения</th>
              <th>Цена</th>
              <th>Действия</th>
            </tr>
          </thead>
          <tbody>
            {buys.map((buy) => (
              <tr key={buy.id}>
                <td>{buy.id}</td>
                <td>{buy.name}</td>
                <td>{buy.offer_id}</td>
                <td>{buy.price} ₽</td>
                <td>
                  <button
                    onClick={() => setEditingBuy(buy)}
                    className="btn btn-small btn-secondary"
                  >
                    Редактировать
                  </button>
                  <button
                    onClick={() => handleDelete(buy.id)}
                    className="btn btn-small btn-danger"
                  >
                    Удалить
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {buys.length === 0 && !loading && (
        <div className="empty-state">Нет покупок</div>
      )}
    </div>
  );
};

export default BuyList;
