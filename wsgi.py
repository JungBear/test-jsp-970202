from app.main import app
from start import db_create

if __name__ == "__main__":
    app.run(threaded=True, port=5000)