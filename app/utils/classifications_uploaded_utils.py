from config import Configuration
from werkzeug.utils import secure_filename
import os


def check_extensions(filename):
    '''
    this function checks if the extension of the file uploaded is included
    among those specified in the tuple allowed_extension
    if it is return True
    else return False
    '''
    if len(filename.split('.')) == 2:
        return filename.split('.')[1] in Configuration.allowed_extension
    return False


def is_valid_filename(filename):
    '''
    Check if the filename is not blank
    and call the function check_extension
    return True if both those checks are successfully
    else return False
    '''
    if filename == '':
        return False
    return check_extensions(filename)


def return_path():
    '''
    this function returns the path of the image specified in UPLOADED_IMAGE_FOLDER (in config.py)
    if this path doesn't exist, it creates it
    '''
    image_path = Configuration.UPLOADED_IMAGE_FOLDER
    if not os.path.exists(image_path):
        os.mkdir(image_path)
    return image_path


def save_image(upload_image):
    '''
    this function stores the image uploaded by the user
    '''
    image_path = return_path()
    filename = secure_filename(upload_image.filename)
    upload_image.save(os.path.join(image_path, filename))
