# import stuff
import bpy

# Define a dictionary of old bone names and new bone names
bone_name_mapping = {
    "b__ROOT_bind__": "center_c_n",
    "b__Spine1__": "kosi_c_n",
    "b__Spine2__": "mune_c_n",
    "b__Neck__": "kubi_c_n",
    "b__Head__": "face_c_n",
    "b__CAS_JawComp__": "_jaw_c_n",
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
    "b__R_Thumb0__": "oya1_r_n",
    "b__R_Thumb1__": "oya2_r_n",
    "b__R_Thumb2__": "oya3_r_n",
    "b__L_Thumb0__": "oya1_l_n",
    "b__L_Thumb1__": "oya2_l_n",
    "b__L_Thumb2__": "oya3_l_n",
    "b__R_Pinky0__": "koyu1_r_n",
    "b__R_Pinky1__": "koyu2_r_n",
    "b__R_Pinky2__": "koyu3_r_n",
    "b__L_Pinky0__": "koyu1_l_n",
    "b__L_Pinky1__": "koyu2_l_n",
    "b__L_Pinky2__": "koyu3_l_n",
    "b__R_Ring0__": "kusu1_r_n",
    "b__R_Ring1__": "kusu2_r_n",
    "b__R_Ring2__": "kusu3_r_n",
    "b__L_Ring0__": "kusu1_l_n",
    "b__L_Ring1__": "kusu2_l_n",
    "b__L_Ring2__": "kusu3_l_n",
    "b__R_Mid0__": "naka1_r_n",
    "b__R_Mid1__": "naka2_r_n",
    "b__R_Mid2__": "naka3_r_n",
    "b__L_Mid0__": "naka1_l_n",
    "b__L_Mid1__": "naka2_l_n",
    "b__L_Mid2__": "naka3_l_n",
    "b__R_Index0__": "hito1_r_n",
    "b__R_Index1__": "hito2_r_n",
    "b__R_Index2__": "hito3_r_n",
    "b__L_Index0__": "hito1_l_n",
    "b__L_Index1__": "hito2_l_n",
    "b__L_Index2__": "hito3_l_n",
    "b__CAS_L_Breast__": "munemus_r_sup",
    "b__CAS_R_Breast__": "munemus_l_sup",
    "b__L_ShoulderTwist__": "kata_twist_l_sup",
    "b__R_ShoulderTwist__": "kata_twist_r_sup",
    "b__R_InBrow__": "_eyebrow_r_n",
    "b__L_InBrow__": "_eyebrow_l_n",
    "b__R_MidBrow__": "_eyebrow2_r_n",
    "b__R_OutBrow__": "_eyebrow3_r_n",
    "b__L_MidBrow__": "_eyebrow2_l_n",
    "b__L_OutBrow__": "_eyebrow3_l_n",
    "b__R_UpLid__": "_eyelid_r_n",
    "b__L_UpLid__": "_eyelid_l_n",
    "b__UpLip__": "_lip_top_c_n",
    "b__R_UpLip__": "_lip_top_r_n",
    "b__L_UpLip__": "_lip_top_l_n",
    "b__LoLip__": "_lip_btm_c_n",
    "b__R_LoLip__": "_lip_btm_r_n",
    "b__L_LoLip__": "_lip_btm_l_n",
    "b__L_Mouth__": "_lip_side_l_n",
    "b__R_Mouth__": "_lip_side_r_n",
    "b__CAS_NoseTip__": "_nose_top_c_n",
    "b__CAS_Chin__": "_chin_c_n",
    "b__L_LoLid__": "_eyelid_und2_l_n",
    "b__R_LoLid__": "_eyelid_und2_r_n",
    "b__R_ThighTwist__": "asi1_twist_r_sup",
    "b__L_ThighTwist__": "asi1_twist_l_sup",
    "b__R_Cheek__": "_cheek_btm1_r_n",
    "b__L_Cheek__": "_cheek_btm1_l_n",
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
# Set the bones to always visible.
bpy.context.object.show_in_front = True
# Go back to object mode.
bpy.ops.object.mode_set(mode="POSE")
 
 