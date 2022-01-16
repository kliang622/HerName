import cv2
import numpy as np


def main():
    img = cv2.imread("test_image.jpeg")
    
    # assume coord is a list with 8 float values, the points of the rectangle area should
    # have be clockwise
    #x1, y1, x2, y2, x3, y3, x4, y4 = coord
    ##(133,89),(171,89),(171,133),(133,133)
    cnt = np.array([[[133, 89]],
                [[171, 89]],
                [[171, 133]],
                [[133, 133]]
                ])
    # cv2.drawContours(img, [cnt], 0, (128, 255, 0), 3)
    # find the rotated rectangle enclosing the contour
    # rect has 3 elments, the first is rectangle center, the second is
    # width and height of the rectangle and the third is the rotation angle
    rect = cv2.minAreaRect(cnt)
    print("rect: {}".format(rect))
    # convert rect to 4 points format
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    print("bounding box: {}".format(box))

    # draw the roated rectangle box in the image
    cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
    
    # crop the rotated rectangle from the image
    im_crop = crop_rect(img, rect)
    # print("size of original img: {}".format(img.shape))
    # print("size of rotated img: {}".format(img_rot.shape))
    # print("size of cropped img: {}".format(im_crop.shape))
    
    cv2.imshow("cropped_box", im_crop)
    cv2.imshow("original contour", img)
    
    cv2.waitKey(0)

# this function is base on post at https://goo.gl/Q92hdp
def crop_rect(img, rect):
    # get the parameter of the small rectangle
    center = rect[0]
    size = rect[1]
    angle = rect[2]
    center, size = tuple(map(int, center)), tuple(map(int, size))

    # get row and col num in img
    rows, cols = img.shape[0], img.shape[1]

    M = cv2.getRotationMatrix2D(center, angle, 1)
    img_rot = cv2.warpAffine(img, M, (cols, rows))
    out = cv2.getRectSubPix(img, size, center)

    return out


if __name__ == "__main__":
    main()
