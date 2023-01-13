from flask import Flask, render_template, url_for, send_from_directory, request, flash, redirect, send_file
import os
from werkzeug.utils import secure_filename
from db import Meme

UPLOAD_FOLDER = '/app/memes'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__, static_folder='public', static_url_path="")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/vite.svg')
def fav():
    return send_from_directory('/app/build/', 'vite.svg', mimetype="image/svg+xml")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return app.send_static_file("index.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            # flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            new_meme = Meme.create(filename=filename, tags="{'tags': []}")
            new_meme.save()
            return redirect(request.url)
    return redirect(url_for('download_file', name=filename))

@app.route('/images')
def get_images():
    return {'memes': os.listdir(UPLOAD_FOLDER)}

@app.route('/image/<file>')
def get_image(file):
    return send_file(UPLOAD_FOLDER + '/' + file)

@app.errorhandler(404)
def not_found(e):
    return { 'error': 'Not found', 'code': 404 }