import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

forFileName = "kritika.jpg"
def findTags(forFileName = forFileName):
    # Authenticate environment
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="VideoAnalyticsEngine-c194ee79cbef.json"
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),
        forFileName)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    parsedLabels = {}
    # print('Labels:')
    for label in labels:
        parsedLabels[label.description] = label.score
        # print(label.description)
    return parsedLabels
# print(findTags())
