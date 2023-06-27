import os

project_root = os.path.dirname(os.path.abspath(__file__))


class Configuration:
    # classification
    image_folder_path = os.path.join(project_root, 'app/static/imagenet_subset')
    models = ('resnet18', 'alexnet', 'vgg16', 'inception_v3',)
    UPLOADED_IMAGE_FOLDER=os.path.join(project_root,'app/static/images_uploaded')
    allowed_extension = ('jpeg', 'jpg', 'png')
    # web server
    SECRET_KEY = os.environ.get('SECRET_KEY') or '9cj328s61hsd8'

    # queue
    REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
    REDIS_PORT = os.environ.get('REDIS_PORT', '6379')
    REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
    QUEUE = "classification"
    
    # configuration information for histogram
    QUEUE_HIST = "histogram"
