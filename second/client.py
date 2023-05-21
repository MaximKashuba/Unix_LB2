import requests

while True:
    message = input('Enter a message (or "exit" to quit): ')
    if message == 'exit':
        break
    response = requests.post('http://server:5000/messages', data={'message': message})
    print(response.text)
