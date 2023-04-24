import bpy


def addcube():
    creator_script = bpy.ops.mesh.primitive_cube_add(size=5, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    return f"{creator_script} created!"

def object_id():
    identification_ = bpy.context.active_object
    identification_.name = "Destinne Cube"
    return f"identified as {identification_}"

def restrictor():
    cube_add = addcube()
    cube_object = object_id()
    if cube_add is True:
        return cube_object
    else:
        return cube_add
    
def key_frame_():
    start_frame = 1
    end_frame = 180
    cube = bpy.context.active_object
    cube.keyframe_insert("location" , frame=start_frame)
    cube.location.z = 5
    cube.keyframe_insert("location" , frame=end_frame)
    
def bounce():
    start_frame = 1
    mid_frame = 90
    end_frame = 180
    cube = bpy.context.active_object
    cube.keyframe_insert("location", frame=start_frame)
    cube.location.z = 10
    cube.keyframe_insert("location", frame=mid_frame)
    cube.location.z = 0
    cube.keyframe_insert("location", frame=end_frame)
        
    
if __name__ == "__main__":
    restrictor()
    bounce()
