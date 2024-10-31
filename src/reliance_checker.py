import bpy
import os


ATMOSPHERE_PATH = './addons/PSA-1.81-addon-EN.zip'
ICITY_PATH = './addons/iCity_1.03_iBlender.zip'
PROCEDURAL_CROWD_PATH = './addons/procedural_crowds/Procedural Crowds 2.1.2_addon_EN.zip'
PROCEDURAL_CROWD_ASSET_PATH = './addons/procedural_crowds/Procedural_Crowds_Assets_v2.0.0/'

def check_reliances(file_name=''):
    check_modules()
    check_assets(file_name)
    
    return


def check_assets(file_name=''):
    a_icity = bpy.context.preferences.addons.get('icity')
    base_path = a_icity.preferences.sna_assets_path
    texture_paths = [
        base_path + '/textures',
        base_path + '/Assets/Default/textures'
    ]
    for path in texture_paths:
        bpy.ops.file.find_missing_files(directory=path)
    print('In fetching the missing textures of addon ICITY.')
    if '.blend' in file_name:
        bpy.ops.wm.save_as_mainfile(filepath=file_name)
    return


def check_modules():
    addons = bpy.context.preferences.addons.keys()
    print(bpy.app.version)
    print(addons)
    # PSA
    t_addon = bpy.context.preferences.addons.get('physical-starlight-atmosphere')
    if t_addon is None:
        bpy.ops.preferences.addon_install(filepath=ATMOSPHERE_PATH)
        bpy.ops.preferences.addon_enable(module='physical-starlight-atmosphere')
        bpy.ops.wm.save_userpref()
        t_addon = bpy.context.preferences.addons.get('physical-starlight-atmosphere')
        if t_addon is None:
            raise Exception('PSA does not exist and fails to install!')
    else:
        print('PSA is satisfied.')
    # ICity
    t_addon = bpy.context.preferences.addons.get('icity')
    if t_addon is None:
        bpy.ops.preferences.addon_install(filepath=ICITY_PATH)
        bpy.ops.preferences.addon_enable(module='icity')
        bpy.ops.wm.save_userpref()
        t_addon = bpy.context.preferences.addons.get('icity')
        if t_addon is None:
            raise Exception('ICITY does not exist and fails to install!')
    else:
        print('ICITY is satisfied.')
    # Procedural Crowd.
    t_addon = bpy.context.preferences.addons.get('Procedural Crowds')
    if t_addon is None:
        bpy.ops.preferences.addon_install(filepath=PROCEDURAL_CROWD_PATH)
        bpy.ops.preferences.addon_enable(module='Procedural Crowds')
        bpy.ops.wm.save_userpref()
        t_addon = bpy.context.preferences.addons.get('Procedural Crowds')
        if t_addon is None:
            raise Exception('PROCEDURAL CROWDS does not exist and fails to install!')
        t_addon.preferences.filepath = PROCEDURAL_CROWD_ASSET_PATH
    else:
        print('PROCEDURAL CROWD is satisfied.')
    addons = bpy.context.preferences.addons.keys()
    print(bpy.app.version)
    print(addons)

if __name__ == '__main__':
    # bpy.ops.wm.open_mainfile(filepath=filepath)
    check_assets(bpy.data.filepath)