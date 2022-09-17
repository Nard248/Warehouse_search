import cv2
import easyocr
from matplotlib import pyplot as plt
from pyzbar.pyzbar import decode

IMAGE_PATH = 'Media/IMG_3088.JPG'


def resize_image(path):
    image = cv2.imread(path)
    height = image.shape[0]
    width = image.shape[1]
    size = (1500, int((1500 / width) * height))
    image_resized = cv2.resize(image, dsize=size)
    return image_resized


def reader_ocr(image):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image)
    font = cv2.FONT_HERSHEY_COMPLEX
    return_dict = {}
    tracking_dict = {}
    for detection in result:
        text = detection[1]
        top_left = tuple(detection[0][0])
        bot_right = tuple(detection[0][2])
        top_left = (int(top_left[0]), int(top_left[1]))
        bot_right = (int(bot_right[0]), int(bot_right[1]))
        if 'ARM' in text:
            text = text.split()
            for l in text:
                if 'ARM' in l:
                    return_dict['arm_code'] = l
                    image = cv2.rectangle(image, top_left, bot_right, (255, 0, 0), 2)
                    image = cv2.putText(image, l, (int(top_left[0]) + 25, int(top_left[1])), font, 2, (255, 0, 0), 2,
                                        cv2.LINE_AA)
        if 'AYRE' in text:
            return_dict['address'] = text
            image = cv2.rectangle(image, top_left, bot_right, (0, 255, 0), 2)
            image = cv2.putText(image, text, (int(top_left[0]) + 25, int(top_left[1])), font, 2, (0, 255, 0), 2,
                                cv2.LINE_AA)
        decoded = decode(image)
        for i in range(len(decoded)):
            tracking_dict[i] = str(decoded[i].data.decode('utf-8'))
            # image = cv2.rectangle(image, top_left, bot_right, (255, 0, 0), 2) image = cv2.putText(image, text,
            # (int(top_left[0]) + 25, int(top_left[1])), font, 2, (255, 0, 0), 2, cv2.LINE_AA) f.write(text + "\n")
        return_dict['tracking'] = tracking_dict
    plt.rcParams['figure.figsize'] = (15, 15)
    plt.imshow(image)
    plt.show()
    return return_dict


def test():
    import math
    from PIL import Image, ImageDraw

    w, h = 220, 190
    shape = [(40, 40), (w - 10, h - 10)]

    # creating new Image object
    img = Image.new("RGB", (w, h))

    # create rectangle image
    img1 = ImageDraw.Draw(img)
    img1.rectangle(shape, fill="#ffff33", outline="red")
    img.show()


test()
