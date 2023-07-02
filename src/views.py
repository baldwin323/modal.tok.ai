```python
from flask import Flask, render_template, request, redirect, url_for
from src.controllers import UserController, PaymentController, SocialMediaController
from src.authentication import Authentication
from src.authorization import Authorization

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if Authentication.loginUser(username, password):
            return redirect(url_for('userProfile', username=username))
        else:
            return 'Invalid credentials'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if UserController.registerUser(username, password):
            return redirect(url_for('login'))
        else:
            return 'Registration failed'
    return render_template('register.html')

@app.route('/user/<username>')
@Authorization.requires_login
def userProfile(username):
    user = UserController.getUser(username)
    return render_template('profile.html', user=user)

@app.route('/payment', methods=['GET', 'POST'])
@Authorization.requires_login
def payment():
    if request.method == 'POST':
        card_number = request.form['card_number']
        expiry_date = request.form['expiry_date']
        cvv = request.form['cvv']
        if PaymentController.processPayment(card_number, expiry_date, cvv):
            return 'Payment successful'
        else:
            return 'Payment failed'
    return render_template('payment.html')

@app.route('/social_login/<platform>', methods=['GET', 'POST'])
def social_login(platform):
    if request.method == 'POST':
        token = request.form['token']
        if SocialMediaController.socialMediaLogin(platform, token):
            return redirect(url_for('userProfile', username=token))
        else:
            return 'Social login failed'
    return render_template('social_login.html', platform=platform)

if __name__ == '__main__':
    app.run(debug=True)
```