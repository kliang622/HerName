import cv2
import numpy as np


class Crop:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4, inpFileName, outFileName):
        self.x1=x1
        self.x2=x2
        self.x3=x3
        self.x4=x4
        self.y1=y1
        self.y2=y2
        self.y3=y3
        self.y4=y4
        self.inpFileName=inpFileName
        self.outFilename=outFileName
    def generate_crop(self):
        img = cv2.imread(self.inpFileName)
        cnt = np.array([[[self.x1, self.y1]],
                    [[self.x2, self.y2]],
                    [[self.x3, self.y3]],
                    [[self.x4, self.y4]]
                    ])
        rect = cv2.minAreaRect(cnt)
        print("rect: {}".format(rect))
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        print("bounding box: {}".format(box))
        cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
        im_crop = self.crop_rect(img, rect)
        print(self.outFilename + "outfileoutfile")
        cv2.imwrite(f'./../tmp/{self.outFilename[7:]}', im_crop)

    def crop_rect(self, img, rect):
        center = rect[0]
        size = rect[1]
        angle = rect[2]
        center, size = tuple(map(int, center)), tuple(map(int, size))

        # get row and col num in img
        rows, cols = img.shape[0], img.shape[1]

        M = cv2.getRotationMatrix2D(center, angle, 1)
        out = cv2.getRectSubPix(img, size, center)

        return out