import os
import cv2
from google.cloud import vision
import io
import io
from PIL import Image

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\User\Desktop\Warehouse_search_vision\token.json'


def detect_text(path):
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                     for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


def detect_text_my(path):
    client = vision.ImageAnnotatorClient()
    img = Image.open(path)
    print(img.size)
    width, height = img.size
    new_width = 1050
    new_height = height * (new_width / width)
    img.thumbnail((new_width, new_height))
    print(img.size)
    buffer = io.BytesIO()
    img.save(buffer, "JPEG")
    content = buffer.getvalue()
    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    print(response.text_annotations[13].description)
    # texts = response.text_annotations
    #
    # for text in texts:
    #     vertices = (['({},{})'.format(vertex.x, vertex.y)
    #                  for vertex in text.bounding_poly.vertices])
    #
    # if response.error.message:
    #     raise Exception(
    #         '{}\nFor more info on error messages, check: '
    #         'https://cloud.google.com/apis/design/errors'.format(
    #             response.error.message))


detect_text_my('media/IMG_3663.JPG')
