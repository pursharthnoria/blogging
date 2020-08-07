from flask import Flask,render_template, request,redirect, session
import backend
import os
from datetime import date
import shutil

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
        session['user_pk'] = rows[0][0]
        session['user_email'] = rows[0][1]
        return redirect('/dashboard.html')
    else:
        return redirect('/')

@app.route('/dashboard.html')
def dashboard():
    if 'user_id' in session:
        data = backend.display_all_posts()
        return render_template('dashboard.html',pk=session['user_pk'],name=session['user_id'],data=data)
    else:
        return redirect('/index.html')

@app.route('/logout',methods=['POST'])
def logout():
    session.pop('user_id')
    session.pop('user_pk')
    session.pop('user_email')
    return redirect('/index.html')



@app.route('/newpost.html')
def opennewpost():
    if 'user_id' in session:
        return render_template('newpost.html',name=session['user_id'])
    else:
        return redirect('/index.html')


@app.route('/addapost',methods=['POST'])
def addpost():
    data = request.form.to_dict()
    backend.insert_in_post(session['user_pk'],session['user_id'],session['user_email'],date.today(),data['text'],0,0)
    return redirect('/viewall.html')

@app.route('/viewall.html')
def viewall():
    data = backend.display_user_posts(session['user_pk'])
    if 'user_id' in session:
        return render_template('viewall.html',data=data,name=session['user_id'])
    else:
        return redirect('/index.html')

@app.route('/increaselike/<int:post_id>',methods=['POST'])
def increaselike(post_id):
    backend.updatedislikes(post_id)
    return redirect('dashboard.html')

app.run(debug=True)