import cv2 
import matplotlib.pyplot as plt

image = cv2.imread('14cf27cc08b0be5f8d45475e4559be8b.jpeg')
image = cv2.cvtColor(image, cv2.COLOR_BRG2RGB)
plt.imshow(image)
plt.show()
