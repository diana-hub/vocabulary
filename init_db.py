from .main import get_db
from .main import app

def init_db():
    """
    Создание пустой бД. Перезатирает существующую!!!
    """
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()