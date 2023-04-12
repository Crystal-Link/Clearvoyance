import os
import socket

from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)
app.config['UPLOADED_PHOTOS_DEST'] = '../../../Photos_Slides'
app.config["SECRET_KEY"] = os.urandom(24)
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

class UploadForm(FlaskForm):
    photo = FileField('Upload an image', validators=[
        FileRequired(),
        FileAllowed(photos, 'Images only!')
    ])


@app.route('/', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
    return render_template('home.html', form=form)


if __name__ == '__main__':
    app.run(host=ip_address)
