# import stuff
import bpy

# Define a dictionary of old bone names and new bone names
bone_name_mapping = {
    "b__ROOT_bind__": "center_c_n",
    "b__Spine1__": "kosi_c_n",
    "b__Spine2__": "mune_c_n",
    "b__Neck__": "kubi_c_n",
    "b__Head__": "face_c_n",
    "b__Jaw__": "_jaw_c_n",
    "b__R_Eye__": "_eye_r_n",
    "b__L_Eye__": "_eye_l_n",
    "b__Pelvis__": "ketu_c_n",
    "b__L_Thigh__": "asi1_l_n",
    "b__R_Thigh__": "asi1_r_n",
    "b__L_Calf__": "asi2_l_n",
    "b__R_Calf__": "asi2_r_n",
    "b__L_Foot__": "asi3_l_n",
    "b__R_Foot__": "asi3_r_n",
    "b__L_Toe__": "asi4_l_n",
    "b__R_Toe__": "asi4_r_n",
    "b__R_Clavicle__": "kata_r_n",
    "b__L_Clavicle__": "kata_l_n",
    "b__R_UpperArm__": "ude1_r_n",
    "b__L_UpperArm__": "ude1_l_n",
    "b__L_Forearm__": "ude2_l_n",
    "b__R_Forearm__": "ude2_r_n",
    "b__R_Hand__": "ude3_r_n",
    "b__L_Hand__": "ude3_l_n",
}

# Ensure you are in Object Mode and have an armature selected
armature = bpy.context.object

# Enter edit mode to modify bone names
bpy.ops.object.mode_set(mode="EDIT")

# Loop through the bones and rename according to the mapping
for bone in armature.data.edit_bones:
    if bone.name in bone_name_mapping:
        new_name = bone_name_mapping[bone.name]
        bone.name = new_name
        print(f"Renamed bone {bone.name} to {new_name}")

# Special Settings
bpy.context.object.show_in_front = True  # Set the bones to always visible.
bpy.ops.object.mode_set(mode="POSE")  # Go back to object mode.