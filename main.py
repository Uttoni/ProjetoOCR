import easyocr
import cv2
from matplotlib import pyplot as plt

if __name__ == '__main__':
    IMAGE_PATH = 'black friday.jpg'


    reader = easyocr.Reader(['en'])
    result = reader.readtext(IMAGE_PATH)
    result




    certeza = []
    top_left = []
    bottom_right = []
    palavras = []

    for r in result:
        print(r)
        top_left.append(tuple(r[0][0]))
        bottom_right.append(tuple(r[0][2]))
        palavras.append(r[1])
        certeza.append(r[2])

    print(top_left)
    print(bottom_right)
    print(palavras)
    print(certeza)
    font = cv2.FONT_HERSHEY_SIMPLEX





    img = cv2.imread(IMAGE_PATH)

    for i in range(len(palavras)):
        if certeza[i] > 0.5:
            img = cv2.rectangle(img, top_left[i], bottom_right[i], (0, 255, 0), 3)
            img = cv2.putText(img, palavras[i], top_left[i], font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

    plt.imshow(img)
    plt.show()