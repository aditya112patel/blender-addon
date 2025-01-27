import bpy
from bpy.types import Panel

class main_PL_panel(Panel):
    bl_label = "Mesh Builder"
    bl_idname = "mail_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'PLACE CUBES'

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.prop(context.scene, "input_number")
        
        layout.operator("object.place_cubes", text="Place Cubes")
        layout.operator("object.delete_cubes", text="Delete Selected Cubes")
        layout.operator("object.merge_selected", text="Merge Selected Meshes")

