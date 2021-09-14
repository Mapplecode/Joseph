import os
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import glob
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)

db = SQLAlchemy()
app.config['SECRET_KEY'] = 'mysecretkey@123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Get current path
path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'uploads')

# Make directory if uploads is not exists
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed extension you can set your own
ALLOWED_EXTENSIONS = set(['txt', 'xlsx', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if request.form.get("rememberme") == "on":
            print("True")       
    return render_template("login.html")

@app.route('/signup',methods=["GET","POST"])
def signup():
    if request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        email = request.form["email"]
        password = request.form["password"]
        cpassword = request.form["cpassword"]
        if password == cpassword:
            print(fname,lname,email,cpassword,password)
        # return redirect(url_for('login'))
    return render_template("signup.html")


@app.route('/',methods=["GET","POST"])
def dashboard():
    tab = "dashboard"
    if request.method == 'POST':
        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                print("*********************")
                print(filename,request.form.get("type"),request.form.get("collectiontype"))
                print("*********************")
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('File(s) successfully uploaded')
        return redirect('/')
    files = os.listdir('uploads')
    return render_template("dashboard.html",data=tab,files_data=files)

@app.route('/departments',methods=["GET","POST"])
def departments():
    tab = "Departments"
    if request.method == 'POST':
        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('File(s) successfully uploaded')
        return redirect('/departments')
    return render_template("dashboard.html",data=tab)


@app.route('/usermanual',methods=["GET","POST"])
def usermanual():
    tab = "User Manual"
    if request.method == 'POST':
        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('File(s) successfully uploaded')
        return redirect('/usermanual')
    return render_template("dashboard.html",data=tab)

@app.route('/tribeknowledge',methods=["GET","POST"])
def tribeknowledge():
    tab = "Tribe Knowledge"
    if request.method == 'POST':
        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('File(s) successfully uploaded')
        return redirect('/tribeknowledge')
    return render_template("dashboard.html",data=tab)

@app.route('/qrcodes',methods=["GET","POST"])
def qrcodes():
    tab = "QR Codes"
    if request.method == 'POST':
        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('File(s) successfully uploaded')
        return redirect('/qrcodes')
    return render_template("dashboard.html",data=tab)


if __name__ == '__main__':
    db.create_all()
    app.run(host='127.0.0.1',port=5000,debug=False,threaded=True)
    
