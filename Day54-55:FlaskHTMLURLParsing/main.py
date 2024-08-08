from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/username/<name>/<int:number>')
def hello_name(name, number):
    return f'<h1>Hello {name}, your are {number} years old!</h1>'\
            '<p>This is a paragraph</p>'\
            '<img src="https://www.wsupercars.com/wallpapers-regular/BMW/2024-BMW-XM-Label-Red-001-1080.jpg">'


if __name__ == "__main__":
    app.run(debug=True)
