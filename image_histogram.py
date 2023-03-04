from ml.classification_utils import fetch_image

@staticmethod
def generate(img_id):
    """! Generate histogram information-set
    @param img_id ID of the image to retrieve and analyze
    @return List of histogram dataset for RGB
    """
    img = fetch_image(img_id)
    r, g, b = img.split()
    img.close()

    n_channels = 3
    results = [0] * n_channels

    results[0] = r.histogram()
    results[1] = g.histogram()
    results[2] = b.histogram()

    return results
