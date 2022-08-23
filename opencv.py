import cv2

def resize():
    path =["C:\\Users\\Naresh01\\Desktop\\HANDS ON\\OOPS\\lord-shiva-digitalart-wallpaper-vedicfeed.jpg","C:\\Users\\Naresh01\\Desktop\\HANDS ON\\OOPS\\Naresh Photo.JPG"]
    for i in path:
        im = i.split('\\')[-1]
        print(im)
        name = f'image{im}.jpg'
        image = cv2.imread(i)
        #print(image)
        resized = cv2.resize(image, (240,350))
        cv2.imwrite(name, resized)
        print('saved')
    return
resize()     