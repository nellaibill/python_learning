#Write some simple code for flask app
from flask import Flask, render_template,request,jsonify,session,redirect,url_for
import logging

from extensions import db
from routes.employees import employees_bp
from routes.login import login_bp

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#Set a secret key for session management
app.secret_key = 'your_secret_key'  # Set a secret key for session management

# 🔥 THIS LINE FIXES YOUR ERROR
db.init_app(app)

#Set logging level to DEBUG for detailed logs
app.logger.setLevel(logging.DEBUG)

#Register blueprints for employees and login routes
app.register_blueprint(employees_bp)
app.register_blueprint(login_bp)

@app.route('/')
def home():
    userid = session.get('user_id')
    if userid:
        logger.info(f"User ID {userid} found in session. Rendering home page.")
        return render_template('index.html')
    else:
        logger.info("No user ID found in session. Rendering home page without user-specific data.")
        return redirect(url_for('login.login'))
    
@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove user ID from session to log out
    return redirect(url_for('home'))  # Redirect to home page after logout
if __name__ == '__main__':
    app.run(debug=True)
 
    