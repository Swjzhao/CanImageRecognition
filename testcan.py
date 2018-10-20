import numpy as np
import serial
from keras.models import load_model
from keras.preprocessing import image
#test_image = image.load_img('tests/20181020_032657.jpg', target_size= (64,64))
#test_image = image.img_to_array(test_image)
#test_image = np.expand_dims(test_image, axis = 0)

#test_image1 = image.load_img('tests/20181020_031512.jpg', target_size= (64,64))
#test_image1 = image.img_to_array(test_image1)
#test_image1 = np.expand_dims(test_image1, axis = 0)

#test_image2 = image.load_img('tests/20181020_031514.jpg', target_size= (64,64))
#test_image2 = image.img_to_array(test_image2)
#test_image2 = np.expand_dims(test_image2, axis = 0)

#test_image3 = image.load_img('tests/20181020_031516.jpg', target_size= (64,64))
#test_image3 = image.img_to_array(test_image3)
#test_image3 = np.expand_dims(test_image3, axis = 0)

#test_image4 = image.load_img('tests/20181020_032409.jpg', target_size= (64,64))
#test_image4 = image.img_to_array(test_image4)
#test_image4 = np.expand_dims(test_image4, axis = 0)

def prediction():
    model = load_model("cansort1.h5")

    bool = 0;

    while(bool == 0):
        try:
            test_image5 = image.load_img("images\screenshot.jpg", target_size= (64,64))
            bool = 1
        except:
            bool = 0

    test_image5 = image.img_to_array(test_image5)
    test_image5 = np.expand_dims(test_image5, axis = 0)
    result5 = model.predict(test_image5)

    msg = 1
    if result5[0][0] <= 0.5:
        print("pepsi \n")
        msg = 0
        return 0
    else:
        print("garbage \n")
        msg = 1
        return 1

    print (result5[0][0])

#result = model.predict(test_image)
#result1 = model.predict(test_image1)
#result2 = model.predict(test_image2)
#result3 = model.predict(test_image3)
#result4 = model.predict(test_image4)



#training_set.class_indices


# if result[0][0] <= 0.5:
#     print("can")
# else:
#     print("garbage")
#
# print(' ', result[0][0], '\n')
#
# if result1[0][0] <= 0.5:
#     print("can")
# else:
#     print("garbage")
#
# print(' ', result1[0][0],'\n')
#
# if result2[0][0] <= 0.5:
#     print("can")
# else:
#     print("garbage")
#
# print(" ",result2[0][0],"\n")
#
# if result3[0][0] <= 0.5:
#     print("can")
# else:
#     print("garbage")
#
# print(" ",result3[0][0],"\n")
#
# if result4[0][0] <= 0.5:
#     print("can")
# else:
#     print("garbage")
#
# print(" ",result4[0][0],"\n")
#


