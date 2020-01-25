from bottle import error, route, request, run, static_file, template, get

@route('/')
def index():
    return template('tables')

@route('/boletos')
def index():
    return template('boletos')

@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return  static_file(filename, root="static")

@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return  static_file(filename, root="static")

@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def javascripts(filename):
    return  static_file(filename, root="static")

@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return  static_file(filename, root="static")

@route('/login')
def login():
    return template('login')

def check_login(usename, password):
    return True

@route('/login', method='POST')
def logar():
    username = request.forms.get('login')
    password = request.forms.get('password')
    if check_login(username, password):
        return '<center><h1>Login realizado com sucesso</h1></center>'
    else:
        return template('login', login=username)

@error(404)
def erro_404(error):
    return template('404')

if __name__ == '__main__':
    run(host='localhost', port=8888, debug=True, reloader=True)