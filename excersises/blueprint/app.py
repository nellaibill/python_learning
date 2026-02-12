from flask import Flask
from models import db
from users import users_bp

app =  Flask("__name_")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()
 
app.register_blueprint(users_bp,url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
    
