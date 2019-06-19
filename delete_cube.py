bl_info = {
    "name": "Delete The Default Cube",
    "category": "Object",
    "blender": (2, 80, 0),
}

import bpy

class DELETETHECUBE(bpy.types.Operator):
    """THIS WILL DELETE THE CUBE"""
    
    bl_idname = "object.delete_the_cube"
    bl_label = "Delete The Default Cube"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        locx, locy, locz = bpy.context.active_object.location
        
        #bpy.ops.object.delete(use_global=False)
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, location=(locx+2.1, locy+2.1, 0))
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, location=(locx+2.1, locy, 0))
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, location=(locx, locy+2.1, 0))

        
        return {"FINISHED"}


def register():
    bpy.utils.register_class(DELETETHECUBE)

def unregister():
    bpy.utils.unregister_class(DELETETHECUBE)

if __name__ == "__main__":
    register()
