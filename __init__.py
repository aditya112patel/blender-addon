

bl_info = {
    "name": "Task1",
    "author": "Aditya",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "category": "Object",
}

import bpy
from . task_op import Place_cubes,Delete_cubes,Merge_cubes
from .task_pnl import main_PL_panel

def register(): 
    bpy.utils.register_class(Place_cubes)
    bpy.utils.register_class(Delete_cubes)
    bpy.utils.register_class(Merge_cubes)
    bpy.utils.register_class(main_PL_panel)
    bpy.types.Scene.input_number = bpy.props.IntProperty(
        name="Number of Cubes",
        default=1,
        min=1,
        max=100,
        description="Number of cubes to place"
    )
    
def unregister():
    bpy.utils.unregister_class(Place_cubes)
    bpy.utils.unregister_class(Delete_cubes)
    bpy.utils.unregister_class(Merge_cubes)
    bpy.utils.unregister_class(main_PL_panel)
    del bpy.types.Scene.input_number


if __name__ == "__main__":
    register()