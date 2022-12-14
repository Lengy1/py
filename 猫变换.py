import numpy as np
import cv2


def arnold_encode(image, a, b,shuffle_times):
    # 1:创建新图像
    arnold_image = np.zeros(shape=image.shape)  # 返回给定形状和类型的新数组，用0填充。img.shape返回img的长宽信息

    # 2：计算N
    h, w = image.shape[0], image.shape[1]  # image.shape[0],image.shape[1],image.shape[2]表示图像长，宽，通道数
    N = w  # 或N=w

    # 3：遍历像素坐标变换
    for i in range(0, shuffle_times):  # 遍历次数
        for x in range(h):
            for y in range(w):
                # 按照公式坐标变换
                new_x = (1 * x + b * y) % N  # 解密：上下对换，a变b,x变y,+变-
                new_y = (a * x + (a * b + 1) * y) % N
                arnold_image[new_x, new_y, :] = image[x, y, :]

                #new_x = (1 * x + a * y) % N  # 解密：上下对换，a变b,x变y,+变-
                #new_y = (b * x + (a * b + 1) * y) % N
                #arnold_image[new_x, new_y, :] = image[x, y, :]

    arnold_image = np.uint8(arnold_image)

    return arnold_image


def dearnold_encode(image, a, b,shuffle_times):
    # 1:创建新图像
    arnold_image = np.zeros(shape=image.shape)  # 返回给定形状和类型的新数组，用0填充。img.shape返回img的长宽信息

    # 2：计算N
    h, w = image.shape[0], image.shape[1]  # image.shape[0],image.shape[1],image.shape[2]表示图像长，宽，通道数
    # N = w  # 或N=w
    N = w

    # 3：遍历像素坐标变换
    for i in range(0, shuffle_times):  # 遍历次数
        for x in range(h):
            for y in range(w):
                # 按照公式坐标变换
                new_x = ((a * b + 1) * x - b * y) % N
                new_y = (-a * x + y) % N
                arnold_image[new_x, new_y, :] = image[x, y, :]

    arnold_image = np.uint8(arnold_image)

    return arnold_image

r = cv2.imread('1.png')
shuffle_times=0x61
a=0x726e
b=0x6f6c64

r = dearnold_encode(r, a, b,shuffle_times)

cv2.imshow("arnold", r)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('flag.png', r)