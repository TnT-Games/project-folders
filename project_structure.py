bl_info = {
    "name": "Project Folders",
    "blender": (2, 80, 0),
    "category": "System",
}

import bpy
from bpy.app.handlers import persistent

import json

import os

from colorama import Fore, init

line_beginning = Fore.GREEN + "[" + bl_info["name"] + "]" + Fore.WHITE + " "
config_directory = bpy.utils.resource_path("USER") + os.sep + "config" + os.sep
config_file_name = project_folders_config.json

def create_structure(self):
    print("In handler")
    if not bpy.data.is_saved:
        print("File saving for first time...")
        project_path = bpy.context.blend_data.filepath
        print(project_path)
        

def create_default_config():
    print(line_beginning + "Creating default configuration at " + config_directory + config_file_name)
    data = {}
    data["folders"] = []
    data["folders"].append({
        "name": "Blend"
    })
    data["folders"].append({
        "name": "Unwraps"
    })
    data["folders"].append({
        "name": "Maps"
    })
    data["folders"].append({
        "name": "Refs"
    })
    data["folders"].append({
        "name": "Export"
    })
    
    with open(config_directory + config_file_name, "w") as outfile:
        json.dump(data, outfile)

def read_config():
    with open(config_directory + config_file_name, "r") as config:
        return json.load(config)

def register():
    init()
    print(line_beginning + "Registering " + bl_info["name"])
    create_default_config()
    bpy.app.handlers.save_post.append(create_structure)

def unregister():
    print("Unregistering: " + bl_info["name"])

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()