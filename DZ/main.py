# import flask
# print(flask.__version__)

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

def Fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b=b, a+b

@app.route('/')
def view_from():
    return render_template('input.html')

@app.route('/handle_get', methods = ['GET'])
def handle_get():
    if request.method == 'GET':
        n = int(request.args['N'])
        f_g = Fibonacci_generator()
        ans = ""
        for i in range(n):
            ans += str(next(f_g)) + ' '
        return ans[:-1]
    else:
        render_template('input.html')

if __name__== "__main__":
    app.run()
