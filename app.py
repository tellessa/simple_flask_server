from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello_world')
def hello_world():
    return 'Hello, World'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'do_the_login()'
    else:
        return 'show_the_login_form()'


# @app.get('/login')
# def login_get():
#     return 'show_the_login_form()'
#     # return show_the_login_form()

# @app.post('/login')
# def login_post():
#     return 'do_the_login()'
#     # return do_the_login()


# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)