```python
from flask import Flask, render_template, request, redirect, url_for, session
from user_auth_system.account_management import User
from messaging_system.message_management import Message

app = Flask(__name__)

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        message_content = request.form['message_input']
        sender_id = session['user_id']
        receiver_id = request.form['receiver_id']

        message = Message(sender_id, receiver_id, message_content)
        message.sendMessage()

    user = User(session['username'])
    messages = user.getMessages()

    return render_template('chat.html', messages=messages)

if __name__ == "__main__":
    app.run(debug=True)
```
This code creates a Flask web application with a chat route. It checks if the user is logged in, and if not, redirects them to the login page. If the user is logged in and a POST request is made (i.e., a message is sent), it creates a new Message object and sends the message. It then retrieves all messages for the logged-in user and passes them to the chat template.