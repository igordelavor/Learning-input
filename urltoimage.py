import numpy as np
import urllib.request
import cv2

def url_to_image_2(url):
	resp = urllib.request.urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	return image
image = url_to_image_2("https://p.bigstockphoto.com/GeFvQkBbSLaMdpKXF1Zv_bigstock-Aerial-View-Of-Blue-Lakes-And--227291596.jpg")
cv2.imwrite('random.png',image)
cv2.imshow("Image", image)
cv2.waitKey(0)
