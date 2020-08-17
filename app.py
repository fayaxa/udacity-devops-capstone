import socket
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    html = '''
        <title>Casptone Project</title>
        <h1 style="color: grey; text-align: center;">Hello World!</h1>
        <h2 style="color: grey; text-align: center;">This is Udacity's Devops Nanodegree Capstone Project 🚀</h2>
    '''
    return html.format(format)
    
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
