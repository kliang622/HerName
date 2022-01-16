import os
import uuid

from flask import Flask, flash, request, redirect, url_for 
from werkzeug.utils import secure_filename 
from google_fr import detect_faces

UPLOAD_FOLDER = 'uploads/' #where we store uploaded files
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'} #set of allowed file extensions 

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000 #limits max allowed payload to 16 mg, if it's bigger Flask raises RequestEntityTooLarge exception
app.secret_key = uuid.uuid4().hex


def allowed_file(filename): 
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def hello_world():
    return "<p>yooooo</p>"

@app.route('/submitImage', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST': #check if the post request has the file part 
        if 'file' not in request.files: 
            flash('No file part')
            #for k in request.files:
                #print(k)
            #print(len(request.files))
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

            #return redirect(url_for('download_file', name=filename))
            return f'''
                <!doctype HTML>
                <title>suck ess</title>
                <h1>This person is: {n}</h1>
            '''
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