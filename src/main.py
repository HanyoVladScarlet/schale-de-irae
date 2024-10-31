import numpy as np
import matplotlib.pyplot as plt
import cv2
from autograd import elementwise_grad as egrad

import time
import bpy
import datetime


from blend_loader import load_blend_file
from generator import Generator
from reliance_checker import check_modules

def main():
    ''''''
    # print(bpy.app.binary_path)
    check_modules()
    load_blend_file('asset00.blend')
    # grr = Generator.get_instance()
    # grr.render_one('output.png')
    # grr.generate_one_pair('test')
    iterate()

def iterate():
    grr = Generator.get_instance()
    t_start = datetime.datetime.now()
    for i in range(2):
        grr.generate_one_pair(f'dateset_{t_start.strftime("%Y-%m-%d-%H-%M-%S")}/test_{i}')
    print(f'\nTotal time consumed: {datetime.datetime.now() - t_start}')


def c_res(x):
    return 50 * x**3

def draw_curve():
    t1_image = cv2.imread('./output1.png')
    t2_image = cv2.imread('./output2.png')
    print(t1_image.shape)
    Y1 = t1_image[int(t1_image.shape[0]/2)][:, 0].astype(float)
    Y2 = t2_image[int(t2_image.shape[0]/2)][:, 0].astype(float)
    X = np.linspace(0, 1, t1_image.shape[1])
    # degrees = 12
    # poly_params = np.polyfit(X, Y1, deg=degrees,)
    # print(np.linspace(degrees, 0, degrees + 1) )
    # poly_params_prime = np.linspace(degrees, 0, degrees + 1) * poly_params
    # p = np.poly1d(poly_params)
    # p_prime = np.poly1d(poly_params_prime)
    # roots = np.roots(poly_params_prime)
    # print([float(root) for root in roots])
    # print([float(root) for root in roots if root > 0.2])
    # Z = p(X)
    # Z_prime = p_prime(X)
    Y1_prime = np.hstack((np.zeros((1,)), np.diff(Y1)))
    print(Y1)
    print(Y1_prime)
    Y2_prime = np.hstack((np.zeros((1,)), np.diff(Y2)))
    plt.figure()
    plt.scatter(X, Y1, color='red', s=1.5)
    plt.scatter(X, Y2, color='blue', s=1.5)
    plt.scatter(X, Y1_prime, color='#f09090', s=1.5)
    plt.scatter(X, Y2_prime+5, color='#9090f0', s=1.5)
    plt.show()

if __name__ == '__main__':
    main()

