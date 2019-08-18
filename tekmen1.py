#tek kullanımlık yazılmış (bu kötü bir şey) kod. Kötü örnek olarak atıyorum. 
#kötü kod örneği

import os
import sys
from PIL import Image



source = "/home/incognito/Downloads/YOLO-Annotation-Tool/Images/001/"
image_names = os.listdir(source)

#burada os modülü kullanılarak daha dinamik pathler yazılabilirdi. O zaman bunu bilmiyormuşum vay be.
def renameImages():
    flag = 0

    for img in image_names:
        dst = "/home/incognito/Downloads/YOLO-Annotation-Tool/Images/001/uav_" + str(flag) +".jpg"
        src =  source + img
        os.rename(src,dst)

        flag += 1

#conversion is okey

#def png2jpg():
 #   for name in image_names:
  #      if name[-4:] == ".png":
   #         name = source + name
    #        im = Image.open(name)
     #       bg = Image.new("RGB", im.size, (255, 255, 255))
      #      bg.paste(im, im)
       #     bg.save(name[:-4] + ".jpg")


def makeTxtFiles():
    for name in image_names:
        #resimlerin hepsini jpg e çevirene kadar eksik
        name = "/home/incognito/Downloads/YOLO-Annotation-Tool/Images/001/" + name[:-4] + ".txt"
        #burada ileride dosya içine yazma yapılabilir
        file = open(name,"w")
        file.write("0 ")
        file.close()


def makeDataset():
    renameImages()
    makeTxtFiles()


if __name__ == "__main__":
    pass
