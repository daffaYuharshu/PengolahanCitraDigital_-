import numpy as np
import cv2 as cv

img_gray = cv.imread('PangeranDiponogoro.jpg', cv.IMREAD_GRAYSCALE)
cv.imwrite("PangeranDiponogoroGrayscale.jpg", img_gray)
cv.namedWindow('Pangeran Diponegoro - 11 November 1785 - Yogyakarta', cv.WINDOW_NORMAL)
cv.imshow('Pangeran Diponegoro - 11 November 1785 - Yogyakarta', img_gray)
cv.waitKey(0)
cv.destroyAllWindows()
