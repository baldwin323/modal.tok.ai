```python
from flask import Flask, session, redirect, url_for, escape, request
from werkzeug.security import generate_password_hash, check_password_hash
from user_model import User

app = Flask(__name__)

@app.route('/account', methods=['GET', 'POST'])
def account_management():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        old_password = request.form['old_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        user = User.query.filter_by(username=session['username']).first()

        if not check_password_hash(user.password, old_password):
            return 'Invalid old password'

        if new_password != confirm_password:
            return 'New password and confirm password do not match'

        user.password = generate_password_hash(new_password)

        return 'Password updated successfully'

    return '''
        <form method="post">
            <p><input type=text name=old_password>
            <p><input type=text name=new_password>
            <p><input type=text name=confirm_password>
            <p><input type=submit value=Update>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
```