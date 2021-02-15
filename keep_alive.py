from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Thank you Skaryey#5622 for making this and allow me to use this!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
