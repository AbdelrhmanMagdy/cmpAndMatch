from PIL import Image
import imagehash
import cv2
import argparse
from os import listdir
from os.path import isfile, join
import imutils

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--path", required=True)
    ap.add_argument("-c", "--cutOff", required=False)
    path = vars(ap.parse_args())['path']
    # cutOff = vars(ap.parse_args())['cutOff']
    start_cmp(path) # get the path of the folder that contains the images to be compared

def start_cmp(path, cutoff = 15):
    imgs = [f for f in listdir(path) if isfile(join(path, f))]
    # array of images hashes to be compared
    hashedImgs = [(img,imagehash.average_hash(Image.open(path+'/'+img))) for img in imgs] 
    compared_pairs = []
    for h1 in range(len(hashedImgs)):
        for h2 in range(h1, len(hashedImgs)):
            if hashedImgs[h1] == hashedImgs[h2]:
                continue
            if hashedImgs[h1][1]-hashedImgs[h2][1] < cutoff:
                compared_pairs.append([hashedImgs[h1][0],hashedImgs[h2][0]])
    imgsToCompare = get_common_imgs(compared_pairs)
    viewAndGetDelList = viewAndDel(imgsToCompare =  ['input/12.jpg','input/13.jpg','input/11.jpg'])
    print(res)
def get_common_imgs(compared_pairs):
    # for pair in compared_pairs:
    pass
def viewAndDel(imgsToCompare):
    if len(imgsToCompare)>10:
        imgsToCompare = imgsToCompare[:9]
    delImgs = []
    while(1):
        for i in range(len(imgsToCompare)):
            img =  cv2.imread(imgsToCompare[i])
            cv2.imshow(str(i+1), imutils.resize(img, width=600))
        k = cv2.waitKey(0)
        if k==27:    # Esc key to stop
            cv2.destroyAllWindows()
            break
        elif chr(k).isdigit():  
            if int(chr(k)) <= len(imgsToCompare):
                delImgs.append(imgsToCompare[int(chr(k))-1])
            else:
                print('please enter valid img index to be deleted or ESC to finish')
        else:
            print('please enter valid img index to be deleted or ESC to finish')
    print(set(delImgs))
    # for img in del imgs -> delete
if __name__ == "__main__":
    main()
    # viewAndDel(imgsToCompare =  ['input/12.jpg','input/13.jpg','input/11.jpg'])
    
