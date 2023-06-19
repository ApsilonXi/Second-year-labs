import numpy as np
import cv2

img = cv2.imread("C:\EmilyVolkova\Codirovanie\lab3/encrypted.bmp", cv2.IMREAD_GRAYSCALE)
row = 177
col = 284

def intToBitArray(img) :
    list = []
    for i in range(row):
        for j in range(col):
             list.append (np.binary_repr( img[i][j] ,width=8  ) )

    return list 

imgIn1D = intToBitArray(img)
imgIn2D = np.reshape(imgIn1D , (row, col) )
def bitplane(bitImgVal , img1D ):
    bitList = [int(i[bitImgVal]) for i in img1D]
    return bitList

bit7 = np.array( bitplane(0, imgIn1D ) ) * 128
bit6 = np.array( bitplane(1,imgIn1D) ) * 64
bit5 = np.array( bitplane(2,imgIn1D) ) * 32
bit4 = np.array( bitplane(3,imgIn1D) ) * 16
bit3 = np.array( bitplane(4,imgIn1D) ) * 8
bit2 = np.array( bitplane(5,imgIn1D) ) * 4
bit1 = np.array( bitplane(6,imgIn1D) ) * 2
bit0 = np.array( bitplane(7,imgIn1D) ) * 1

sevenbitimg = np.reshape(bit7,(row,col))
cv2.imwrite("c:\EmilyVolkova\Codirovanie\lab2/bit7.bmp" , sevenbitimg )

sixbitimg = np.reshape(bit6,(row,col))
cv2.imwrite("c:\EmilyVolkova\Codirovanie\lab2/bit6.bmp" , sixbitimg )

fivebitimg = np.reshape(bit5,(row,col))
cv2.imwrite("c:\EmilyVolkova\Codirovanie\lab2/bit5.bmp" , fivebitimg )

fourbitimg = np.reshape(bit4,(row,col))
cv2.imwrite("c:\EmilyVolkova\Codirovanie\lab2/bit4.bmp" , fourbitimg )

threebitimg = np.reshape(bit3,(row,col))
cv2.imwrite("c:\EmilyVolkova\Codirovanie\lab2/bit3.bmp" , threebitimg )

twobitimg = np.reshape(bit2,(row,col))
cv2.imwrite("c:\EmilyVolkova\Codirovanie\lab2/bit2.bmp" , twobitimg )

onebitimg = np.reshape(bit1,(row,col))
cv2.imwrite("c:\EmilyVolkova\Codirovanie\lab2/bit1.bmp" , onebitimg )

zerobitimg = np.reshape(bit0,(row,col))
cv2.imwrite("c:\EmilyVolkova\Codirovanie\lab2/bit0.bmp" , zerobitimg )