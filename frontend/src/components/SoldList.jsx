import { useState, useEffect } from 'react';
import { soldsAPI } from '../api/client';
import SoldForm from './SoldForm';

const SoldList = () => {
  const [solds, setSolds] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [editingSold, setEditingSold] = useState(null);

  useEffect(() => {
    loadSolds();
  }, []);

  const loadSolds = async () => {
    try {
      setLoading(true);
      const response = await soldsAPI.getAll();
      setSolds(response.data);
      setError(null);
    } catch (err) {
      setError('Ошибка загрузки продаж');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleCreate = async (data) => {
    try {
      await soldsAPI.create(data);
      await loadSolds();
      setShowForm(false);
    } catch (err) {
      alert('Ошибка создания продажи');
      console.error(err);
    }
  };

  const handleUpdate = async (data) => {
    try {
      await soldsAPI.update(editingSold.id, data);
      await loadSolds();
      setEditingSold(null);
    } catch (err) {
      alert('Ошибка обновления продажи');
      console.error(err);
    }
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Вы уверены, что хотите удалить эту продажу?')) {
      return;
    }
    try {
      await soldsAPI.delete(id);
      await loadSolds();
    } catch (err) {
      alert('Ошибка удаления продажи');
      console.error(err);
    }
  };

  if (loading) {
    return <div className="loading">Загрузка...</div>;
  }

  return (
    <div className="sold-list-container">
      <div className="section-header">
        <h2>Продажи (Sold)</h2>
        <button
          onClick={() => {
            setShowForm(!showForm);
            setEditingSold(null);
          }}
          className="btn btn-primary"
        >
          {showForm ? 'Скрыть форму' : '+ Добавить продажу'}
        </button>
      </div>

      {showForm && !editingSold && (
        <div className="form-container">
          <h3>Создать новую продажу</h3>
          <SoldForm
            onSubmit={handleCreate}
            onCancel={() => setShowForm(false)}
          />
        </div>
      )}

      {editingSold && (
        <div className="form-container">
          <h3>Редактировать продажу</h3>
          <SoldForm
            sold={editingSold}
            onSubmit={handleUpdate}
            onCancel={() => setEditingSold(null)}
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
              <th>ID Покупки</th>
              <th>Цена</th>
              <th>Прибыль</th>
              <th>Действия</th>
            </tr>
          </thead>
          <tbody>
            {solds.map((sold) => (
              <tr key={sold.id}>
                <td>{sold.id}</td>
                <td>{sold.name}</td>
                <td>{sold.buy_id}</td>
                <td>{sold.price} ₽</td>
                <td className={sold.profit >= 0 ? 'profit-positive' : 'profit-negative'}>
                  {sold.profit !== undefined ? `${sold.profit.toFixed(2)} ₽` : '0.00 ₽'}
                </td>
                <td>
                  <button
                    onClick={() => setEditingSold(sold)}
                    className="btn btn-small btn-secondary"
                  >
                    Редактировать
                  </button>
                  <button
                    onClick={() => handleDelete(sold.id)}
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

      {solds.length === 0 && !loading && (
        <div className="empty-state">Нет продаж</div>
      )}
    </div>
  );
};

export default SoldList;
