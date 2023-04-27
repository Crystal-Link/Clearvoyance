import os
import socket
from pathlib import Path
# import threading
# import queue

from flask import Flask, render_template, send_from_directory, url_for, request, redirect
from flask_uploads import UploadSet, IMAGES, configure_uploads
    # FLASK_REUPLOADED
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

this_path = Path(__file__).parent
relative = '../../../Photos_Slides'
dir_path = (this_path / relative).resolve()

relativeSaved = '../../../WebServerPhotos'
saved_dir_path = (this_path / relativeSaved).resolve()

app = Flask(__name__)
## THIS LINK WORKS RELATIVE TO COMMAND-LINE
app.config['SAVED_PHOTOS_DEST'] = str(saved_dir_path)
app.config['UPLOADED_PHOTOS_DEST'] = str(dir_path)
app.config["SECRET_KEY"] = os.urandom(24)

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

class UploadForm(FlaskForm):
    photo = FileField(
        validators=[
            FileAllowed(photos, 'Only images are allowed'),
            FileRequired('File field cannot be empty.')
        ]
    )
    submit = SubmitField('Upload')

def get_saved_images():
    saved_images = []
    for filename in os.listdir(app.config['UPLOADED_PHOTOS_DEST']):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            saved_images.append(url_for('get_file', filename=filename))
    return saved_images

@app.route('/uploads/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)

@app.route('/saved/<filename>')
def get_saved_files(filename):
    return send_from_directory(app.config['SAVED_PHOTOS_DEST'], filename)

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    logo_url = url_for('get_saved_files', filename="Clearvoyance_Logo.png")
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        upload_queue.put(filename)
        file_url = url_for('get_file', filename=filename)
    else:
        file_url = None
    saved_images = get_saved_images()
    return render_template('index.html', logo_url=logo_url, form=form, file_url=file_url, saved_images=saved_images)

@app.route('/delete_image', methods=['POST'])
def delete_image():
    filename = request.form['filename'].replace("/uploads/", "")
    delete_queue.put(filename)
    file_path = os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    return redirect('/')

def store_server(new_img_queue, delete_img_queue):
    global upload_queue, delete_queue
    upload_queue = new_img_queue
    delete_queue = delete_img_queue
    print('Detected IP ' + ip_address)
    app.run(host='0.0.0.0')