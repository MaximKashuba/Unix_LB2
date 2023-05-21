from flask import Flask, request

app = Flask(__name__)

messages = []

def save_message(message):
    with open('messages.txt', 'a') as file:
        file.write(message + '\n')

@app.route('/messages', methods=['GET', 'POST'])
def handle_messages():
    if request.method == 'POST':
        message = request.form['message']
        messages.append(message)
        save_message(message)
        return 'Message received: {}'.format(message)
    elif request.method == 'GET':
        return '\n'.join(messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
