import os
import uuid
import json

from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename 
from google_fr import detect_faces

UPLOAD_FOLDER = 'uploads/' #where we store uploaded files
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'} #set of allowed file extensions 

app = Flask(__name__, static_folder='static/', template_folder='templates/')
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000 #limits max allowed payload to 16 mg, if it's bigger Flask raises RequestEntityTooLarge exception
app.secret_key = uuid.uuid4().hex



#export FLASK_APP=webserver
#export GOOGLE_APPLICATION_CREDENTIALS="/home/natem135/Downloads/rosehack2022-f178de763729.json"

def allowed_file(filename): 
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/submitImage', methods=['POST'])
def upload_file():
    if request.method == 'POST': #check if the post request has the file part 
        if 'file' not in request.files: 
            flash('No file part')
            for k in request.files:
                print(k)
            print(len(request.files))
            return redirect(request.url)
        file = request.files['file']
        if file.filename == ' ': #if user doesn't select file, browser submits an empty file w/o filename 
            flash('No selected file')
            #print("it aint reaching endk;sgjldskjm")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            #print("this *is* working dabdab")
            filename = secure_filename(file.filename) #returns secure version of filename, so it can be stored safely on file system
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            n = detect_faces(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            with open(f'descriptions/{n[:-4]}.json') as f:
                d=json.load(f)
            return redirect(url_for('results', data=json.dumps(d)))
            #return f'''
            #    <!doctype HTML>
            #    <title>suck ess</title>
            #    <h1>Your Match Is: {d['name']}</h1>
            #    <p>{d['description']}</p>
            #'''
        #else:
            #print("ayo ayo ayo ayo ayo this no work :(")
    return '''
    <!doctype HTML>
    <title>Upload new File</title>
    <h1>Upload new Fileuwu</h1>
    <form method=post enctype=multipart/form-data>
        <input type=file name=file>
        <input type=submit value=Upload>
    </form>
    '''

@app.route("/results")
def results():
    d = json.loads(request.args['data'])
    return render_template('results.html', name=d['name'], desc=d['description'])