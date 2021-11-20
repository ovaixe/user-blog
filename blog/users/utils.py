import os
import secrets
from PIL import Image
from flask import url_for
from flask_mail import Message, current_app
from blog import mail




def save_file(form_picture) :
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_name = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/imgs', picture_name)
    size = (125, 125)
    img = Image.open(form_picture)
    img.thumbnail(size)
    img.save(picture_path)

    return picture_name


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    msg.body = f"""To reset your password, click on following link:
    {url_for('users.reset_token', token=token, external=True)}
    If you did not make this request then simply ignore this email and no changes will be made.
    """
    mail.send(msg)