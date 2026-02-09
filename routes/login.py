from flask import Blueprint, redirect, render_template, request, session, url_for
login_bp = Blueprint('login', __name__)
@login_bp.route('/login')
def login():
    return render_template('login.html')

@login_bp.route('/login/submit', methods=['POST'])
def submit_login():
    username = request.form.get('username')
    password = request.form.get('password')
    # Here you would typically validate the username and password against your user database
    if username == 'admin' and password == 'admin':  # Example validation    
        session['user_id'] = 1  # Set a user ID in the session to indicate the user is logged in
        return redirect(url_for('home'))  # Redirect to the home page after successful login


