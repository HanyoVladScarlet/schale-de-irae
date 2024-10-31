import bpy 

DEFAULT_PATH = r'C:\Users\hanyo\Documents\Lyapunov\Blender\paramization\main.blend'


def load_blend_file(filepath):
    bpy.ops.wm.open_mainfile(filepath=filepath)


if __name__ == '__main__':
    load_blend_file(DEFAULT_PATH)