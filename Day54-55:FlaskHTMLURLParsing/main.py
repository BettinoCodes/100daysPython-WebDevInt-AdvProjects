from flask import Flask
from functools import wraps
import random 
app = Flask(__name__)

chosen = random.randint(1,10)

#write a decorator function
def make_bold(function):
    @wraps(function)
    def wrapped_bold_function(**kwargs):
        return f'<b>{function(**kwargs)}</b>'
    return wrapped_bold_function

def make_underline(function):
    @wraps(function)
    def wrapped_underline_function(**kwargs):
        return f'<u>{function(**kwargs)}</u>'
    return wrapped_underline_function

def make_emp(function):
    @wraps(function)
    def wrapped_emp_function(**kwargs):
        return f'<em>{function(**kwargs)}</em>'
    return wrapped_emp_function

@app.route('/')
@make_bold
def start_screen():
    return '<h1>GUESS A NUMBER FROM 1 THROUGH 9!</h1>'\
            '<div><img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWp1dGZrZzAzZzEzZDNyMWNjZXJ6Z2EyYTZ5bHI3amdlcTc3amprZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/abHQ4aDqRqlyBTdAP0/giphy.webp"></div>'


@app.route('/<int:number>')
@make_bold
@make_emp
def hello_name(number):
    if number < chosen:
        return f'<h1> Your Guess is too low </h1>' \
                '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExc20zem5jemswNGZpNG01ZjRnbGN3emJtdDJqNTJia2ozZTg4NHh6bSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oz8xLd9DJq2l2VFtu/giphy.webp">'
    elif number > chosen:
        return f'<h1> Your Guess is too high </h1>' \
                '<img src= "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdXJ6ejZtdXBwaGNoYXc1anRoOTh2ajBlZWRwZXA3cnBraXRqeDJ0dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/sTikSg4ca35M4NAH07/giphy.webp">'
    else:
        return f'<h1>Your Guess is Correct! </h1>' \
                '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExa244Y2djZ251azJhdTlycTRiZmo0cWZqc2YzbDVqNDUwZHk0dDYzbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oEdv3Ul8g6BCngQ36/giphy.webp">'


if __name__ == "__main__":
    app.run(debug=True)

