from flask import Flask, render_template, url_for, send_from_directory, request, flash, redirect, send_file
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
from db import Meme
from playhouse.shortcuts import model_to_dict
import json

UPLOAD_FOLDER = '/app/memes'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__, static_folder='public', static_url_path="")
CORS(app)
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
    print(request.method)
    if request.method == 'POST':
        # check if the post request has the file part
        files = request.files.getlist("file")

        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        for file in files:
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                print(file)
                meme_query = Meme.select().where(Meme.filename == file.filename)
                if meme_query.exists():
                    print('it does exist')
                else:
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    # new_meme = Meme.create(filename=filename, tags="{'tags")
                    new_meme = Meme.create(filename=filename, tags=request.form['tags'])
                    new_meme.save()
        return redirect(request.url)
            # return redirect(url_for('download_file', name=filename))

@app.route('/images')
def get_images():
    memes = Meme.select()
    memes = [model_to_dict(u) for u in memes]
    memes = json.dumps(memes)
    return memes

@app.route('/image/<file>')
def get_image(file):
    return send_file(UPLOAD_FOLDER + '/' + file)

@app.route('/image/delete/<id>', methods=['GET'])
def delete_image(id):
    # print(id)
    
    meme = Meme.get_by_id(pk=id)
    print(meme.filename)
    if os.path.isfile(UPLOAD_FOLDER + '/' + meme.filename):
        os.remove(path=UPLOAD_FOLDER + '/' + meme.filename)
    Meme.delete_by_id(pk=id)
    response = {'message': 'image deletion: success'}
    return response

@app.route('/image/edit/<id>', methods=['POST'])
def edit_meme(id):
    json_data = json.loads(request.data)
    var = Meme.set_by_id(id, {"tags": json_data["tags"]})
    meme = Meme.get_by_id(id)
    print(var)
    return { 'tags': meme.tags }


@app.errorhandler(404)
def not_found(e):
    return { 'error': 'Not found', 'code': 404 }