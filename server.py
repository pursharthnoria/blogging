from flask import Flask,render_template, request,redirect, session
import backend
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

backend.connect()

def get_fname(s):

    n = ''
    for char in s:
        if char!=' ':
            n+=char
        elif char==' ':
            break
    return n

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/register',methods=['POST'])
def register():
    data = request.form.to_dict()
    rows = backend.search(data['email'],data['password'])
    if len(rows)>=1:
        return redirect('/')
    else:
        backend.insert(data['email'],data['password'],data['name'],data['address'],data['city'],data['state'],data['zip'])
        return redirect('/index.html')

@app.route('/login',methods=['POST'])
def login():
    data = request.form.to_dict()
    rows = backend.search(data['email'],data['password'])
    if len(rows)==1:
        session['user_id'] = get_fname(rows[0][3])
        return redirect('/dashboard.html/' + session['user_id'])
    else:
        return redirect('/')

@app.route('/dashboard.html/<string:name>')
def dashboard(name):
    if 'user_id' in session:
        return render_template('dashboard.html',name=session['user_id'])
    else:
        return redirect('/index.html')

@app.route('/dashboard.html/logout',methods=['POST'])
def logout():
    session.pop('user_id')
    return redirect('/index.html')


@app.route('/gotohome',methods=['GET'])
def gotohome():
    return redirect('/dashboard.html/'+session['user_id'])

@app.route('/dashboard.html/gotonewpost',methods=['GET'])
def gotonewpost():
    return redirect('/newpost.html/'+session['user_id'])

@app.route('/newpost.html/<string:name>')
def opennewpost(name):
    return render_template('newpost.html',name=session['user_id'])


app.run(debug=True)