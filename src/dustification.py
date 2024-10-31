import bpy


class DustController():
    instance = None
    @staticmethod
    def get_instance():
        if DustController.instance == None:
            DustController.instance = DustController()
        return DustController.instance
    
    def __init__(self):
        self.dust_driver = bpy.data.objects.get('dust_driver')
        print([o_name for o_name in bpy.data.objects.keys() if 'dust' in o_name])
        if self.dust_driver is None:
            raise Exception(f'DUST_DRIVER does not exist, check the project file {bpy.context.blend_data.filepath}.')
        self.dust_volume = bpy.data.objects.get('dust_volume')
        if self.dust_volume is None:
            raise Exception(f'DUST_VOLUME does not exist, check the project file {bpy.context.blend_data.filepath}.')
        return

    def set_density(self, val):
        self.dust_driver.location.x = val
        return

    def set_emission_green(self, val):
        self.dust_driver.rotation_euler.y = val
        return

    def set_emission_blue(self, val):
        self.dust_driver.rotation_euler.z = val
        return

    def set_emission_strength(self, val):
        self.dust_driver.rotation_euler.y = val
        return

    def set_emission_red(self, val):
        self.dust_driver.rotation_euler.x = val
        return

    def set_active_dust(self, active=True):
        self.dust_volume.hide_render = not active
        bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[1].default_value = 0 if active else 1
        return