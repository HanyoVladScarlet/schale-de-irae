import bpy


from randomizor import Randomizor
from dustification import DustController


OUTPUT_PATH = './outputs/'

class Generator():
    instance = None
    @staticmethod
    def get_instance():
        if Generator.instance == None:
            Generator.instance = Generator()
        return Generator.instance

    def __init__(self):
        output_settings = {
            'width': 512,
            'height': 512,
            'format': 'PNG',
            'samples': 256,
        }
        # print(bpy.context.preferences.addons["cycles"].preferences.compute_device_type + 'hao!')
        # for d in bpy.context.preferences.addons["cycles"].preferences.devices:
        #     d["use"] = 1 # Using all devices, include GPU and CPU
        # print(d["name"], d["use"])
        bpy.context.preferences.addons["cycles"].preferences.get_devices()
        bpy.context.preferences.addons['cycles'].preferences.compute_device_type = 'CUDA'
        # TODO: Make this adaptive.
        bpy.context.preferences.addons['cycles'].preferences.devices['NVIDIA GeForce RTX 4090'].use = True
        print(bpy.context.preferences.addons['cycles'].preferences.compute_device_type)
        self.renderer = bpy.context.scene.render
        self.renderer.engine = 'CYCLES'
        self.renderer.resolution_x = (output_settings['width'])
        self.renderer.resolution_y = int(output_settings['height'])
        self.renderer.image_settings.file_format = str.upper(output_settings['format']) 
        bpy.context.scene.cycles.samples = int(output_settings['samples'])
        bpy.context.scene.cycles.device = 'GPU'
        return


    def render_one(self, path):
        bpy.context.scene.frame_set(83)
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render(path)
        return

    def generate_one_pair(self, name):
        rdr = Randomizor.get_instance()
        rdr.randomize_all()
        dc = DustController.get_instance()
        dc.set_active_dust(False)
        self.render_one(OUTPUT_PATH + name + '.png')
        dc.set_active_dust(True)
        self.render_one(OUTPUT_PATH + name + '_hazed.png')
        
        return