bl_info = {
        
        "name": "MOTHERFUCKER",
        "category": "Object",
        "blender": (2, 80, 0),



}


import bpy

class MOTHEBITCH(bpy.types.Operator):
    """Description"""
    
    #sdjfksdjfksdjlfjsl
    
    bl_idname = "object.motherbich"
    bl_label = "MOTHER THIS BICH"
    bl_options = {"REGISTER", "UNDO"}
    
    
    
    def execute(self, context):
        
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, location=(2, 0, 0))

        
        return {"FINISHED"}
    

def register():
    bpy.utils.register_class(MOTHEBITCH)

def unregister():
    bpy.utils.unregister_class(MOTHEBITCH)
    
if __name__ == "__main__":
    register()