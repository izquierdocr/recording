import cv2

print(cv2.version)

image = cv2.imread("../test.jpg");
dimensions = image.shape
print("Dimensions:",dimensions)

image = cv2.resize(image,(100,100))
cv2.imshow('Preview',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
