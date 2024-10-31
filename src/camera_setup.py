import bpy
from mathutils import Vector

import math
import random


class CameraController():
    instance = None
    @staticmethod
    def get_instance():
        if CameraController.instance == None:
            CameraController.instance = CameraController()
        return CameraController.instance

    def __init__(self):
        self.camera = bpy.data.cameras.get('Camera')
        self.camera_object = bpy.data.objects.get('Camera')
    
    def randomize(self):
        out_band_ratio = 0.4
        road_width = 9
        road_length = 110
        pitch_range = 30
        basic_height = 1.2
        height_range = 1.8
        # Set left and right.
        rot_x = (90 + (random.random() - 1) * pitch_range) * 2 * math.pi / 360
        rot_z = random.random() * 2 * math.pi
        rot_over = random.choice(range(4)) * math.pi / 2
        x = random.random() * (1 + out_band_ratio) * road_width
        x -= out_band_ratio * road_width if rot_z < math.pi else road_width
        y = random.random() * road_length
        z = random.random() * height_range + basic_height
        x_prime = x * math.cos(rot_over) - y * math.sin(rot_over)
        y_prime = x * math.sin(rot_over) + y * math.cos(rot_over)
        self.camera_object.location = Vector((x_prime, y_prime, z))
        self.camera_object.rotation_euler = Vector((rot_x, 0, rot_z + rot_over))
        # Set rotation angle.
        return


if __name__ == '__main__':
    cc = CameraController.get_instance()
    cc.randomize()