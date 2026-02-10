from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database config (single file)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ======================
# MODEL (TABLE)
# ======================
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }

# ======================
# CREATE TABLES
# ======================
with app.app_context():
    if User.query.count() == 0:
        user = User(name="Saleem", email="saleem@test.com")
        db.session.add(user)
        db.session.commit()

# ======================
# ROUTE
# ======================
@app.route("/users")
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])

# ======================
# RUN APP
# ======================
if __name__ == "__main__":
    app.run(debug=True)
