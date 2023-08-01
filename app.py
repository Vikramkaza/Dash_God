# app.py
from flask import Flask, render_template, request, redirect, url_for, json
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# For this example, we create a simple dummy user
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

# In a real application, you would validate users from a database
users = {'user1': {'password': 'password1'}, 'user2': {'password': 'password2'}}
user_objects = {user_id: User(user_id) for user_id in users}

@login_manager.user_loader
def load_user(user_id):
    return user_objects.get(user_id)

# Routes
@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and user['password'] == password:
            login_user(user_objects[username])
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid login credentials. Please try again.'

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if username in users:
            return 'Username already exists. Please choose a different username.'

        if password != confirm_password:
            return 'Passwords do not match. Please try again.'

        # For this example, we're storing the user details in a dictionary
        users[username] = {'password': password}
        user_objects[username] = User(username)

        login_user(user_objects[username])
        return redirect(url_for('dashboard'))

    return render_template('signup.html')
# Assuming you have a data structure to store the webcam information
webcams = [
]

@app.route('/update_webcam_info', methods=['GET'])
def update_webcam_info():
    # Get the query parameters from the request
    name = request.args.get('name')
    date = request.args.get('date')
    time = request.args.get('time')
    location = request.args.get('location')

    # Update the webcam information or create a new entry if it doesn't exist
    # for webcam in webcams:
    #     if webcam['name'] == name:
    #         webcam['date'] = date
    #         webcam['time'] = time
    #         webcam['location'] = location
    #         break
    # else:
    webcams.append({"name": name, "date": date, "time": time, "location": location})

    return 'Webcam information updated successfully.'

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
@app.route('/get_data')
@login_required
def get_data():
    return json.dumps(webcams)

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(host='0.0.0.0', port=5000, debug=True)
=======
    app.run(host='0.0.0.0', port=5001, debug=True)
>>>>>>> b5fd9f6 (form)
