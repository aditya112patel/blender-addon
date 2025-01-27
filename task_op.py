import bpy
import bmesh
from math import ceil, sqrt

class Place_cubes(bpy.types.Operator):
    bl_idname = "object.place_cubes"
    bl_label = "Place Cubes"
    
    def execute(self, context):
        n = context.scene.input_number

        if n > 20:
            self.report({'ERROR'}, "The number is out of range")
        else:
            rows = ceil(sqrt(n))
            cols = ceil(n / rows)
            
            for i in range(n):
                x = (i % cols) * 1.1
                y = (i // cols) * 1.1
                bpy.ops.mesh.primitive_cube_add(size=1, location=(x, y, 0))
                
        return {'FINISHED'}


class Delete_cubes(bpy.types.Operator):
    bl_idname = "object.delete_cubes"
    bl_label = "Delete Selected Cubes"

    def execute(self, context):
        bpy.ops.object.delete(use_global=False)
        return {'FINISHED'}


class Merge_cubes(bpy.types.Operator):
    bl_idname = "object.merge_selected"
    bl_label = "Merge Selected Cubes"

    def execute(self, context):
        selected_objects = context.selected_objects
        if len(selected_objects) < 2:
            self.report({'ERROR'}, "Select at least two cubes to merge")
            return {'CANCELLED'}
        
        bpy.ops.object.join()
        obj = context.active_object
        bm = bmesh.new()
        bm.from_mesh(obj.data)
        bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=0.001)
        bm.to_mesh(obj.data)
        bm.free()

        return {'FINISHED'}

