import cv2

image = cv2.imread("Image_Video/image.png")
while True:
    cv2.rectangle(image, (49,145),(154,194),(255,100,100),2)
    cv2.imshow("Input image",image)
    if cv2.waitKey(1) & 0xFF==ord("1"):
        break;
