# import bpy
import random


from camera_setup import CameraController
from dustification import DustController


class Randomizor():
    instance = None
    @staticmethod
    def get_instance():
        if Randomizor.instance == None:
            Randomizor.instance = Randomizor()
        return Randomizor.instance

    def __init__(self):
        dc = DustController.get_instance()
        dc.set_density(0.05)
        dc.set_emission_strength(0.05)
        dc.set_emission_blue(1)
        dc.set_emission_green(1)
        dc.set_emission_red(1)

    def randomize_all(self):
        self.randomize_camera()

    def randomize_camera(self):
        cc = CameraController.get_instance()
        cc.randomize()

    def randomize_dust(self):
        dc = DustController.get_instance()
        dc.set_density(random.random() * 0.1)
        dc.set_emission_strength(random.random() * 0.1)