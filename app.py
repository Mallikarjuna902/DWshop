from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Azure! This is my Flask app running on Azure Web App.'

if __name__ == '__main__':
    app.run(debug=True)
