import numpy as np

from keras.models import load_model
from keras.preprocessing import image
test_image = image.load_img('tests/20181020_032657.jpg', target_size= (64,64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)

test_image1 = image.load_img('tests/20181020_031512.jpg', target_size= (64,64))
test_image1 = image.img_to_array(test_image1)
test_image1 = np.expand_dims(test_image1, axis = 0)

test_image2 = image.load_img('tests/20181020_031514.jpg', target_size= (64,64))
test_image2 = image.img_to_array(test_image2)
test_image2 = np.expand_dims(test_image2, axis = 0)

test_image3 = image.load_img('tests/20181020_031516.jpg', target_size= (64,64))
test_image3 = image.img_to_array(test_image3)
test_image3 = np.expand_dims(test_image3, axis = 0)

test_image4 = image.load_img('tests/20181020_031517.jpg', target_size= (64,64))
test_image4 = image.img_to_array(test_image4)
test_image4 = np.expand_dims(test_image4, axis = 0)

model = load_model("cansort.h5")

result = model.predict(test_image)
result1 = model.predict(test_image1)
result2 = model.predict(test_image2)
result3 = model.predict(test_image3)
result4 = model.predict(test_image4)

#training_set.class_indices

if result[0][0] <= 0.5:
    print("can")
else:
    print("garbage")

print(' ', result[0][0], '\n')

if result1[0][0] <= 0.5:
    print("can")
else:
    print("garbage")

print(' ', result1[0][0],'\n')

if result2[0][0] <= 0.5:
    print("can")
else:
    print("garbage")

print(" ",result2[0][0],"\n")

if result3[0][0] <= 0.5:
    print("can")
else:
    print("garbage")

print(" ",result3[0][0],"\n")

if result4[0][0] <= 0.5:
    print("can")
else:
    print("garbage")

print(" ",result4[0][0],"\n")



