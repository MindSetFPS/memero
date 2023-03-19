from flask import Flask, render_template, url_for, send_from_directory, request, flash, redirect, send_file
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
from db import Meme,  MEME_FOLDER
from playhouse.shortcuts import model_to_dict
import json

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__, static_folder='public', static_url_path="")
app.config['MEME_FOLDER'] = MEME_FOLDER
CORS(app=app) #only for development

def tag_length(meme):
    return len(meme['tags'])

@app.route('/vite.svg')
def fav():
    return send_from_directory('/app/build/', 'vite.svg', mimetype="image/svg+xml")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return app.send_static_file("index.html")

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
                    file.save(os.path.join(app.config['MEME_FOLDER'], filename))
                    # new_meme = Meme.create(filename=filename, tags="{'tags")
                    new_meme = Meme.create(filename=filename, tags=request.form['tags'])
                    new_meme.save()
        return redirect(request.url)
            # return redirect(url_for('download_file', name=filename))

# fetch every 25 images
@app.route('/images/<int:page>')
def get_images(page):
    # sort by name, tags or date
    print(request.args.get('sort'))

    if request.args.get('sort') == 'name':
        memes = Meme.select().paginate(page, 25).order_by(Meme.filename)

    if request.args.get('sort') == 'tags':
        memes = Meme.select().paginate(page, 25).order_by(Meme.tags)
    
    # if request.args.get == 'date':
    #     memes = Meme.select()

    memes = [model_to_dict(u) for u in memes]
    # memes.sort(key=tag_length, reverse=True)
    memes = json.dumps(memes)
    return memes

# fetch image by filename
@app.route('/image/file/<file>')
def get_image(file):
    return send_file(MEME_FOLDER + '/' + file)

# fetch image by id
@app.route('/image/data/<int:img_id>')
def get_image_by_id(img_id):
    img_filename = Meme.get_by_id(pk=img_id)
    print(vars(img_filename))
    # return img_filename
    img_json = json.dumps(model_to_dict(img_filename))
    return img_json

# delete image by id
@app.route('/image/delete/<id>', methods=['GET'])
def delete_image(id):
    # print(id)
    meme = Meme.get_by_id(pk=id)
    print(meme.filename)
    if os.path.isfile(MEME_FOLDER + '/' + meme.filename):
        os.remove(path=MEME_FOLDER + '/' + meme.filename)
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