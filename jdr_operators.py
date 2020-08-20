import bpy
from bpy.types import Operator
from bpy_extras.object_utils import AddObjectHelper

from .jdr_wgt_library import *


"""
FUNCTIONS
"""


def get_pose_bone_list(self, context):
    # Get list of selected pose bones
    selected = bpy.context.selected_pose_bones
    bone_list = [bone.name for bone in selected]
    return bone_list


def get_edit_bone_list(self, context):
    # Get list of selected pose bones
    selected = bpy.context.selected_editable_bones
    bone_list = [bone.name for bone in selected]
    return bone_list


def get_arm_obj(self, context):
    # Get arm object
    bpy.ops.object.mode_set(mode="OBJECT")
    arm_obj = bpy.context.view_layer.objects.active
    return arm_obj


def get_widget_name(wgt_type):
    # Get widget name dependeing on which UI button is used.
    if wgt_type == "All":
        widget_name = "WGT_all"
    elif wgt_type == "Transform":
        widget_name = "WGT_transform"
    elif wgt_type == "Arrows Thick":
        widget_name = "WGT_arrows_thick"
    elif wgt_type == "Arrows Thin":
        widget_name = "WGT_arrows_thin"
    elif wgt_type == "Square":
        widget_name = "WGT_square"
    elif wgt_type == "Circle":
        widget_name = "WGT_circle"
    elif wgt_type == "Cube":
        widget_name = "WGT_cube"
    elif wgt_type == "Prism":
        widget_name = "WGT_prism"
    elif wgt_type == "Sphere Low":
        widget_name = "WGT_sphere_low"
    elif wgt_type == "Sphere High":
        widget_name = "WGT_sphere_high"
    elif wgt_type == "Arrow Thick":
        widget_name = "WGT_arrow_thick"
    elif wgt_type == "Arrow Thin":
        widget_name = "WGT_arrow_thin"
    elif wgt_type == "Double Arrow Thick":
        widget_name = "WGT_double_arrow_thick"
    elif wgt_type == "Double Arrow Thin":
        widget_name = "WGT_double_arrow_thin"
    elif wgt_type == "COG":
        widget_name = "WGT_cog"
    elif wgt_type == "Properties":
        widget_name = "WGT_properties"
    elif wgt_type == "Upper Body":
        widget_name = "WGT_upperbody"
    elif wgt_type == "Lower Body":
        widget_name = "WGT_lowerbody"
    elif wgt_type == "Head":
        widget_name = "WGT_head"
    elif wgt_type == "Jaw":
        widget_name = "WGT_jaw"
    elif wgt_type == "Face":
        widget_name = "WGT_face"
    elif wgt_type == "Eye All":
        widget_name = "WGT_eye_all"
    elif wgt_type == "Foot":
        widget_name = "WGT_foot"
    elif wgt_type == "Clav":
        widget_name = "WGT_clav"
    elif wgt_type == "2D":
        widget_name = "WGT_2dsquare"
    return widget_name


def get_widget(self, context, widget_name, wgt_type):
    # Check if widget already exists.
    all = bpy.context.scene.objects
    widget_list = [wgt for wgt in all if wgt.name == widget_name]
    if widget_list:
        # If it does, get it and make it active.
        widget = bpy.data.objects[widget_name]
        bpy.context.view_layer.objects.active = widget
    else:
        # If not, create widget.
        if wgt_type == "All":
            add_wgt_all(self, context)
        elif wgt_type == "Transform":
            add_wgt_transform(self, context)
        elif wgt_type == "Arrows Thick":
            add_wgt_arrows_thick(self, context)
        elif wgt_type == "Arrows Thin":
            add_wgt_arrows_thin(self, context)
        elif wgt_type == "Square":
            add_wgt_square(self, context)
        elif wgt_type == "Circle":
            add_wgt_circle(self, context)
        elif wgt_type == "Cube":
            add_wgt_cube(self, context)
        elif wgt_type == "Prism":
            add_wgt_prism(self, context)
        elif wgt_type == "Sphere Low":
            add_wgt_sphere_low(self, context)
        elif wgt_type == "Sphere High":
            add_wgt_sphere_high(self, context)
        elif wgt_type == "Arrow Thick":
            add_wgt_arrow_thick(self, context)
        elif wgt_type == "Arrow Thin":
            add_wgt_arrow_thin(self, context)
        elif wgt_type == "Double Arrow Thick":
            add_wgt_double_arrow_thick(self, context)
        elif wgt_type == "Double Arrow Thin":
            add_wgt_double_arrow_thin(self, context)
        elif wgt_type == "COG":
            add_wgt_cog(self, context)
        elif wgt_type == "Properties":
            add_wgt_properties(self, context)
        elif wgt_type == "Upper Body":
            add_wgt_upperbody(self, context)
        elif wgt_type == "Lower Body":
            add_wgt_lowerbody(self, context)
        elif wgt_type == "Head":
            add_wgt_head(self, context)
        elif wgt_type == "Jaw":
            add_wgt_jaw(self, context)
        elif wgt_type == "Face":
            add_wgt_face(self, context)
        elif wgt_type == "Eye All":
            add_wgt_eye_all(self, context)
        elif wgt_type == "Foot":
            add_wgt_foot(self, context)
        elif wgt_type == "Clav":
            add_wgt_clav(self, context)
        elif wgt_type == "2D":
            add_wgt_2dsquare(self, context)
        widget = bpy.context.view_layer.objects.active
        correct_scale(self, context, widget)
    # Unselect widget.
    widget.select_set(False)
    return widget

def correct_scale(self, context, object):
    unit_scale = bpy.data.scenes['Scene'].unit_settings.scale_length
    if round(unit_scale, 2) == 0.01:
        print("Unreal Scale")
    else:
        object.scale = (0.01, 0.01, 0.01)
        bpy.context.view_layer.objects.active = object
        object.select_set(True)
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        object.select_set(False)
        print("Default Scale")
    
    
def assign_widget(context, arm_obj, bone_name, pose, widget, arm):
    # Select rig.
    bpy.context.view_layer.objects.active = arm_obj
    arm_obj.select_set(True)
    # Flip to pose mode.
    bpy.ops.object.posemode_toggle()
    # Assign widget as custom shape.
    pose.bones[bone_name].custom_shape = widget
    # Activate show wire,
    # this attribute is on bone data instead of pose bone.
    arm.bones[bone_name].show_wire = True
    # Turn off bone size.
    pose.bones[bone_name].use_custom_shape_bone_size = False
    bpy.ops.object.mode_set(mode="OBJECT")


def get_wgt_collection(self, context):
    # List of collections.
    scene_collections = bpy.data.collections
    # Get list of collection names.
    collection_list = [
        col.name for col in scene_collections if col.name == "COL_widgets"
    ]
    # Check if any in list of collections is called COL_widgets.
    if collection_list:
        # If there is, get it.
        widget_collection = bpy.data.collections["COL_widgets"]
    else:
        # Create COL_widgets.
        widget_collection = bpy.data.collections.new("COL_widgets")
        # Link it to scene collection.
        bpy.context.scene.collection.children.link(widget_collection)
    return widget_collection


def assign_wgt_collection(widget, widget_collection):
    # List of all collections the widget is in.
    old_collections = widget.users_collection
    if widget_collection not in old_collections:
        # Link Widget to the COL_widgets.
        widget_collection.objects.link(widget)
        # Unlink from all old collections.
        for old in old_collections:
            old.objects.unlink(widget)


def hide_collection(collection):
    # Hide collection
    collection.hide_viewport = True
    collection.hide_render = True


def create_base_rig(self, context):
    # deselect everything incase or it will confuse the 3D cursor later
    bpy.ops.object.select_all(action="DESELECT")
    # return cursor to center
    bpy.ops.view3d.snap_cursor_to_center()
    # create armature
    bpy.ops.object.armature_add(enter_editmode=0, location=(0, 0, 0))
    arm_obj = bpy.context.view_layer.objects.active
    # name rig object
    arm_obj.name = "RIG_base"
    # have armature show in front
    arm_obj.show_in_front = True
    return arm_obj


def get_arm_data(arm_obj):
    # get and identify the armature data
    arm = bpy.data.armatures[arm_obj.data.name]
    # rename armature
    arm.name = "ARM_base"
    return arm


def activate_bone_layers(arm):
    # make sure layers are active incase bones are already present
    arm.layers[0] = True
    arm.layers[1] = True
    arm.layers[2] = True
    arm.layers[5] = True
    arm.layers[6] = True
    arm.layers[7] = True


def new_edit_bone(arm_obj, bone_name, context):
    # go to edit mode
    bpy.ops.object.mode_set(mode="EDIT")
    # create bone bone
    bone = arm_obj.data.edit_bones.new(name=bone_name)
    # make bone orientation match the world
    bone.head = bpy.context.scene.cursor.location
    bone.tail = bone.head
    unit_scale = bpy.data.scenes['Scene'].unit_settings.scale_length
    if round(unit_scale, 2) == 0.01:
        bone.tail.y += 10
    else:
        bone.tail.y += 0.1
    # Fix the roll
    bone.roll = 0
    # turn off deform
    bone.use_deform = False
    return bone


def get_pose_bone(arm_obj, bone_name):
    # Flip to pose mode
    bpy.ops.object.posemode_toggle()
    # get pose bone
    pose_bone = arm_obj.pose.bones[bone_name]
    # Fix the rotation mode
    pose_bone.rotation_mode = "XYZ"
    return pose_bone


def add_copytrans_con(pose_bone, arm_obj, con_target_name):
    # Flip to pose mode
    bpy.ops.object.posemode_toggle()
    # create copy transforms constraint
    constraint = pose_bone.constraints.new("COPY_TRANSFORMS")
    # set constrait target, armature
    constraint.target = arm_obj
    # set constrait target, TGT bone
    constraint.subtarget = con_target_name
    return constraint


def add_copyloc_con(pose_bone, arm_obj, con_target_name):
    # Flip to pose mode
    bpy.ops.object.posemode_toggle()
    # create copy transforms constraint
    constraint = pose_bone.constraints.new("COPY_LOCATION")
    # set constrait target, armature
    constraint.target = arm_obj
    # set constrait target, TGT bone
    constraint.subtarget = con_target_name
    return constraint


def add_copyrot_con(pose_bone, arm_obj, con_target_name):
    # Flip to pose mode
    bpy.ops.object.posemode_toggle()
    # create copy transforms constraint
    constraint = pose_bone.constraints.new("COPY_ROTATION")
    # set constrait target, armature
    constraint.target = arm_obj
    # set constrait target, TGT bone
    constraint.subtarget = con_target_name
    return constraint


def add_copyscale_con(pose_bone, arm_obj, con_target_name):
    # Flip to pose mode
    bpy.ops.object.posemode_toggle()
    # create copy transforms constraint
    constraint = pose_bone.constraints.new("COPY_SCALE")
    # set constrait target, armature
    constraint.target = arm_obj
    # set constrait target, TGT bone
    constraint.subtarget = con_target_name
    return constraint


def assign_to_def_bl(bone_data):
    # assign DEF bones to layer
    bone_data.layers[0] = True
    # unassign DEF bones from other layers
    bone_data.layers[1] = False
    bone_data.layers[2] = False
    bone_data.layers[5] = False
    bone_data.layers[6] = False
    bone_data.layers[7] = False


def assign_to_tgt_bl(bone_data):
    # assign TGT bones to layee
    bone_data.layers[1] = True
    # unassign TGT bones from other layers
    bone_data.layers[0] = False
    bone_data.layers[2] = False
    bone_data.layers[5] = False
    bone_data.layers[6] = False
    bone_data.layers[7] = False


def assign_to_mch_bl(bone_data):
    # assign mch bones to layer
    bone_data.layers[2] = True
    # unassign mch bones from other layers
    bone_data.layers[0] = False
    bone_data.layers[1] = False
    bone_data.layers[5] = False
    bone_data.layers[6] = False
    bone_data.layers[7] = False


def assign_to_depth_bl(bone_data):
    # assign depth bones to layer
    bone_data.layers[5] = True
    # unassign depth bones from other layers
    bone_data.layers[0] = False
    bone_data.layers[1] = False
    bone_data.layers[2] = False
    bone_data.layers[6] = False
    bone_data.layers[7] = False


def assign_to_ctl_bl(bone_data):
    # assign CTL bones to layer
    bone_data.layers[6] = True
    # unassign CTL bones from other layers
    bone_data.layers[0] = False
    bone_data.layers[1] = False
    bone_data.layers[2] = False
    bone_data.layers[5] = False
    bone_data.layers[7] = False


def assign_to_mainoffset_bl(bone_data):
    # assign Main_Offset bone to layer
    bone_data.layers[7] = True
    # unassign Main_Offset bone from other layers
    bone_data.layers[0] = False
    bone_data.layers[1] = False
    bone_data.layers[2] = False
    bone_data.layers[5] = False
    bone_data.layers[6] = False


def delete_default_bone(arm):
    # go to edit mode
    bpy.ops.object.mode_set(mode="EDIT")
    # make a list of any bones with Bone name
    bonelist = [bone for bone in arm.edit_bones if bone.name == "Bone"]
    # create onr if it doesnt exist
    if bonelist:
        bone = arm.edit_bones["Bone"]
        arm.edit_bones.remove(bone)


def get_all_bg(arm_obj):
    # Get bone groups.
    bonegrps = arm_obj.pose.bone_groups
    # Create bone groups.
    allgrp = bonegrps.new(name="All")
    allgrp.color_set = "THEME11"
    return allgrp


def get_center_bg(arm_obj):
    # Get bone groups.
    bonegrps = arm_obj.pose.bone_groups
    # Create bone groups.
    centergrp = bonegrps.new(name="Center")
    centergrp.color_set = "THEME09"
    return centergrp


def get_extras_bg(arm_obj):
    # Get bone groups.
    bonegrps = arm_obj.pose.bone_groups
    # Create bone groups.
    extrasgrp = bonegrps.new(name="Extras")
    extrasgrp.color_set = "THEME03"
    return extrasgrp


def default_bone_layer_viz(arm):
    # Make CTL layer visable
    arm.layers[6] = True
    # hide other layers
    arm.layers[0] = False
    arm.layers[1] = False
    arm.layers[2] = False
    arm.layers[5] = False
    arm.layers[7] = False


def edit_bone_parent(arm, bone_child, bone_parent):
    # Assign bone parent
    arm.edit_bones[bone_child].parent = arm.edit_bones[bone_parent]


def cursor_to_object_centre(self, context, object_name):
    # go to object mode
    bpy.ops.object.mode_set(mode="OBJECT")
    # return cursor to center
    bpy.ops.view3d.snap_cursor_to_center()
    # identify mesh object
    object = bpy.data.objects[object_name]
    # move cursor to centre of object
    # select mesh
    bpy.context.view_layer.objects.active = object
    object.select_set(True)
    # go to edit mode
    bpy.ops.object.mode_set(mode="EDIT")
    # snap 3d cursor to mesh
    bpy.ops.view3d.snap_cursor_to_selected()
    # go to object mode
    bpy.ops.object.mode_set(mode="OBJECT")
    # unselect mesh
    bpy.context.view_layer.objects.active = object
    object.select_set(False)


def rename_to_def(name):
    if "GEO_" in name:
        defname = name.replace("GEO_", "DEF_")
    elif "TGT_" in name:
        defname = name.replace("TGT_", "DEF_")
    elif "CTL_" in name:
        defname = name.replace("CTL_", "DEF_")
    elif "MCH_" in name:
        defname = name.replace("MCH_", "DEF_")
    elif "DEPTH_" in name:
        defname = name.replace("DEPTH_", "DEF_")
    elif "DEF_" in name:
        pass
    else:
        defname = "DEF_{}".format(name)
    return defname


def rename_to_tgt(name):
    if "DEF_" in name:
        tgtname = name.replace("DEF_", "TGT_")
    elif "GEO_" in name:
        tgtname = name.replace("GEO_", "TGT_")
    elif "CTL_" in name:
        tgtname = name.replace("CTL_", "TGT_")
    elif "MCH_" in name:
        tgtname = name.replace("MCH_", "TGT_")
    elif "DEPTH_" in name:
        tgtname = name.replace("DEPTH_", "TGT_")
    elif "TGT_" in name:
        pass
    else:
        tgtname = "TGT_{}".format(name)
    return tgtname


def rename_to_ctl(name):
    if "TGT_" in name:
        ctlname = name.replace("TGT_", "CTL_")
    elif "DEF_" in name:
        ctlname = name.replace("DEF_", "CTL_")
    elif "GEO_" in name:
        ctlname = name.replace("GEO_", "CTL_")
    elif "MCH_" in name:
        ctlname = name.replace("MCH_", "CTL_")
    elif "DEPTH_" in name:
        ctlname = name.replace("DEPTH_", "CTL_")
    elif "CTL_" in name:
        pass
    else:
        ctlname = "CTL_{}".format(name)
    return ctlname


def rename_to_mch(name):
    if "TGT_" in name:
        mchname = name.replace("TGT_", "MCH_")
    elif "DEF_" in name:
        mchname = name.replace("DEF_", "MCH_")
    elif "GEO_" in name:
        mchname = name.replace("GEO_", "MCH_")
    elif "CTL_" in name:
        mchname = name.replace("CTL_", "MCH_")
    elif "DEPTH_" in name:
        mchname = name.replace("DEPTH_", "MCH_")
    elif "MCH_INT_" in name:
        mchname = name.replace("MCH_INT_", "MCH_")
    elif "MCH_" in name:
        pass
    else:
        mchname = "MCH_{}".format(name)
    return mchname


def rename_to_mch_int(name):
    if "TGT_" in name:
        mchname = name.replace("TGT_", "MCH_INT_")
    elif "DEF_" in name:
        mchname = name.replace("DEF_", "MCH_INT_")
    elif "GEO_" in name:
        mchname = name.replace("GEO_", "MCH_INT_")
    elif "CTL_" in name:
        mchname = name.replace("CTL_", "MCH_INT_")
    elif "DEPTH_" in name:
        mchname = name.replace("DEPTH_", "MCH_INT_")
    elif "MCH_INT_" in name:
        pass
    elif "MCH_" in name:
        mchname = name.replace("MCH_", "MCH_INT_")
    else:
        mchname = "MCH_INT_{}".format(name)
    return mchname


def rename_to_depth(name):
    if "TGT_" in name:
        depthname = name.replace("TGT_", "DEPTH_")
    elif "DEF_" in name:
        depthname = name.replace("DEF_", "DEPTH_")
    elif "GEO_" in name:
        depthname = name.replace("GEO_", "DEPTH_")
    elif "CTL_" in name:
        depthname = name.replace("CTL_", "DEPTH_")
    elif "MCH_" in name:
        depthname = name.replace("MCH_", "DEPTH_")
    elif "DEPTH_" in name:
        pass
    else:
        depthname = "DEPTH_{}".format(name)
    return depthname


def duplicate_bone(arm_obj, new_bone_name, arm, copied_bone_name):
    # go to object mode
    bpy.ops.object.mode_set(mode="OBJECT")
    # select rig
    bpy.context.view_layer.objects.active = arm_obj
    arm_obj.select_set(True)
    # go to edit mode
    bpy.ops.object.mode_set(mode="EDIT")
    # create bone
    new_bone = arm_obj.data.edit_bones.new(name=new_bone_name)
    # get copied bone
    copied_bone = arm.edit_bones[copied_bone_name]
    # match to copied bone
    new_bone.head = copied_bone.head
    new_bone.tail = copied_bone.tail
    new_bone.roll = copied_bone.roll
    # turn off deform
    new_bone.use_deform = False
    return new_bone


def add_armature_modifier(object_name, arm_obj):
    # go to object mode
    bpy.ops.object.mode_set(mode="OBJECT")
    # identify mesh object
    object = bpy.data.objects[object_name]
    # add armature modifier
    modifier = object.modifiers.new(name="Armature", type="ARMATURE")
    # assign armature to modifier
    modifier.object = arm_obj
    # set armature as parent
    object.parent = arm_obj
    return modifier


def add_vertex_group(context, object_name, group_name):
    # go to object mode
    bpy.ops.object.mode_set(mode="OBJECT")
    # select mesh
    object = bpy.data.objects[object_name]
    bpy.context.view_layer.objects.active = object
    object.select_set(True)
    # create vertex group with corresponding def bone name
    object.vertex_groups.new(name=group_name)
    # go to edit mode
    bpy.ops.object.mode_set(mode="EDIT")
    # select all verts
    bpy.ops.mesh.select_all(action="SELECT")
    # assign verts to vertex group
    bpy.ops.object.vertex_group_assign()
    # go to object mode
    bpy.ops.object.mode_set(mode="OBJECT")
    bpy.ops.object.select_all(action="DESELECT")


def create_mch_bone(self, context, parent_bone, child_name, arm_obj):
    unit_scale = bpy.data.scenes['Scene'].unit_settings.scale_length
    mch_name = rename_to_mch(child_name)

    mchbone = new_edit_bone(arm_obj, mch_name, context)

    mchbone.head = parent_bone.tail
    mchbone.tail = mchbone.head
    if round(unit_scale, 2) == 0.01:
        mchbone.tail.y += 10
    else:
        mchbone.tail.y += 0.1
    mchbone.roll = 0
    return mchbone


"""
OPERATORS
"""


class JDRiggingOperator:
    bl_options = {"REGISTER", "UNDO"}


class JDRIGGING_OT_base_rig(JDRiggingOperator, Operator, AddObjectHelper):
    """
    Creates a Base Rig (armature) object with All,
    main and main_offset CTL bones and TGT_root bone.
    Sets bones in the hierarchy and creates constraint.
    Also creates and assigns widget objects, bone layers
    and bone groups. Widget objects assigned to a hidden collection.
    Assumes Object mode is active.
    """

    bl_idname = "jdrigging.base_rig_operator"
    bl_label = "Base Rig"
    bl_description = "Creates an Armature object with All, main and main_offset CTL bones and TGT_root bone. Must be used in Object Mode"

    def execute(self, context):
        arm_obj = create_base_rig(self, context)

        arm = get_arm_data(arm_obj)

        bpy.context.view_layer.objects.active = arm_obj
        arm_obj.select_set(True)

        activate_bone_layers(arm)
        unit_scale = bpy.data.scenes['Scene'].unit_settings.scale_length

        # Create TGT_root
        root_name = "TGT_root"
        new_edit_bone(arm_obj, root_name, context)

        # Create CTL_all
        ctlall_name = "CTL_all"
        ctlall = new_edit_bone(arm_obj, ctlall_name, context)
        if round(unit_scale, 2) == 0.01:
            ctlall.tail.y += 25
        else:
            ctlall.tail.y += 0.25
        allpose = get_pose_bone(arm_obj, ctlall_name)

        # Create CTL_main
        ctlmain_name = "CTL_main"
        ctlmain = new_edit_bone(arm_obj, ctlmain_name, context)
        if round(unit_scale, 2) == 0.01:
            ctlmain.tail.y += 20
        else:
            ctlmain.tail.y += 0.2
        mainpose = get_pose_bone(arm_obj, ctlmain_name)

        # Create CTL_main_offset
        ctlmain_offset_name = "CTL_main_offset"
        ctlmain_offset = new_edit_bone(arm_obj, ctlmain_offset_name, context)
        if round(unit_scale, 2) == 0.01:
            ctlmain_offset.tail.y += 15
        else:
            ctlmain_offset.tail.y += 0.15
        main_offsetpose = get_pose_bone(arm_obj, ctlmain_offset_name)

        # go to edit mode
        bpy.ops.object.mode_set(mode="EDIT")
        # set the heirarcy.
        edit_bone_parent(arm, ctlmain_offset_name, ctlmain_name)
        edit_bone_parent(arm, ctlmain_name, ctlall_name)

        # Flip to pose mode
        bpy.ops.object.posemode_toggle()
        # get root pose bone
        rootpose = arm_obj.pose.bones[root_name]
        # constrain the root
        add_copytrans_con(rootpose, arm_obj, ctlmain_offset_name)

        # get the widgets
        # go to object mode
        bpy.ops.object.mode_set(mode="OBJECT")
        wgtall = get_widget(self, context, "WGT_all", "All")
        wgttransform = get_widget(self, context, "WGT_transform", "Transform")
        wgtarrows_thin = get_widget(self, context, "WGT_arrows_thin", "Arrows Thin")
        # deselect everything
        bpy.ops.object.select_all(action="DESELECT")

        # Assign Widgets
        pose = arm_obj.pose
        assign_widget(context, arm_obj, ctlall_name, pose, wgtall, arm)
        assign_widget(context, arm_obj, ctlmain_name, pose, wgttransform, arm)
        assign_widget(context, arm_obj, ctlmain_offset_name, pose, wgtarrows_thin, arm)

        # Get widget collection
        widget_collection = get_wgt_collection(self, context)

        # Assign widgets to collection
        all = bpy.context.scene.objects
        widglist = [wgt for wgt in all if "WGT_" in wgt.name]
        for widget in widglist:
            assign_wgt_collection(widget, widget_collection)

        hide_collection(widget_collection)

        # select rig
        bpy.context.view_layer.objects.active = arm_obj
        arm_obj.select_set(True)
        # Flip to pose mode
        bpy.ops.object.posemode_toggle()
        # get bone data
        alldata = arm_obj.data.bones[ctlall_name]
        maindata = arm_obj.data.bones[ctlmain_name]
        main_offsetdata = arm_obj.data.bones[ctlmain_offset_name]
        rootdata = arm_obj.data.bones[root_name]

        # CTL bone layer
        assign_to_ctl_bl(alldata)
        assign_to_ctl_bl(maindata)
        # main_offset bone layer
        assign_to_mainoffset_bl(main_offsetdata)
        # TGT bone layer
        assign_to_tgt_bl(rootdata)

        # delete default bone
        delete_default_bone(arm)

        # get bone groups
        allgrp = get_all_bg(arm_obj)
        centergrp = get_center_bg(arm_obj)

        # assign bone groups
        allpose.bone_group = allgrp
        mainpose.bone_group = centergrp
        main_offsetpose.bone_group = centergrp

        # clean up
        # Flip to pose mode
        bpy.ops.object.posemode_toggle()
        # Make CTL layer only visable
        default_bone_layer_viz(arm)

        return {"FINISHED"}


class JDRIGGING_OT_new_world_bone(JDRiggingOperator, Operator):
    """
    Creates an edit bone with axis matching the world in the active armature.
    Depending on which button is used, the bone will or will not
    have deform active. Head of bone matches 3D cursor position.
    Assumes Edit mode is active.
    """

    bl_idname = "jdrigging.new_world_bone_operator"
    bl_label = "World Bone"
    bl_description = (
        "Creates an edit bone with axis matching the world. Must be used in Edit Mode"
    )

    bone_type: bpy.props.StringProperty()

    def execute(self, context):
        arm_obj = get_arm_obj(self, context)
        arm = bpy.data.armatures[arm_obj.data.name]

        if self.bone_type == "DEF":
            bone_name = "DEF_bone"
        elif self.bone_type == "noDEF":
            bone_name = "bone"
        bone = new_edit_bone(arm_obj, bone_name, context)

        if self.bone_type == "DEF":
            # turn on deform
            bone.use_deform = True

        bone.select = True
        bone.select_head = True
        bone.select_tail = True
        arm.edit_bones.active = bone
        return {"FINISHED"}


class JDRIGGING_OT_add_ctl_tgt(JDRiggingOperator, Operator):
    """
    Adds CTL and/or TGT bones to selected bones(DEF bones expected,
    but can be used on other bones). If Both are added, TGT a child of CTL
    and selected bone constrained to TGT. CTL's parent will be set to the
    corresponding selected bone parent's CTL. Selected bone's parent will
    be TGT_root if present or as None. If just CTLs are added, selected bones
    are constrained to CTLs instead. If just TGTs are added, TGT's parent will
    be set to the corresponding selected bone parent's TGT.
    Assumes Edit mode is active and bones selected.
    """

    bl_idname = "jdrigging.add_ctl_tgt_operator"
    bl_label = "Add CTL and TGT"
    bl_description = "Adds CTL and/or TGT bones to selected bones. Must be used in Edit Mode and bones selected"

    bone_type: bpy.props.StringProperty()

    def execute(self, context):
        arm_obj = get_arm_obj(self, context)
        arm = bpy.data.armatures[arm_obj.data.name]
        bpy.ops.object.mode_set(mode="EDIT")
        bone_list = get_edit_bone_list(self, context)
        activate_bone_layers(arm)

        tgtbones = []
        ctlbones = []

        if self.bone_type == "BOTH" or self.bone_type == "TGT":
            # create TGT bones
            for bone_name in bone_list:
                tgtname = rename_to_tgt(bone_name)
                tgtbones.append(tgtname)
                duplicate_bone(arm_obj, tgtname, arm, bone_name)

        if self.bone_type == "BOTH" or self.bone_type == "CTL":
            # create CTL bones
            for bone_name in bone_list:
                ctlname = rename_to_ctl(bone_name)
                ctlbones.append(ctlname)
                duplicate_bone(arm_obj, ctlname, arm, bone_name)

        if self.bone_type == "BOTH":
            for tgtname in tgtbones:
                # Set TGT parent as corresponding CTL
                ctlname = rename_to_ctl(tgtname)
                edit_bone_parent(arm, tgtname, ctlname)
        elif self.bone_type == "TGT":
            # assign TGT parent if bone has one
            for bone_name in bone_list:
                if arm.edit_bones[bone_name].parent:
                    parent = arm.edit_bones[bone_name].parent
                    parent_name = parent.name
                    tgtname = rename_to_tgt(bone_name)
                    if parent_name == "TGT_root":
                        edit_bone_parent(arm, tgtname, parent_name)
                    else:
                        tgtparent = rename_to_tgt(parent_name)
                        if tgtparent in tgtbones:
                            edit_bone_parent(arm, tgtname, tgtparent)

        if self.bone_type == "BOTH" or self.bone_type == "CTL":
            # assign ctl parent if bone has one
            for bone_name in bone_list:
                if arm.edit_bones[bone_name].parent:
                    parent = arm.edit_bones[bone_name].parent
                    parent_name = parent.name
                    ctlname = rename_to_ctl(bone_name)
                    if parent_name == "TGT_root":
                        edit_bone_parent(arm, ctlname, parent_name)
                    else:
                        ctlparent = rename_to_ctl(parent_name)
                        if ctlparent in ctlbones:
                            edit_bone_parent(arm, ctlname, ctlparent)

        for bone_name in bone_list:
            if "DEF_" in bone_name:
                rootbones = [bone for bone in arm.edit_bones if bone.name == "TGT_root"]
                if rootbones:
                    arm.edit_bones[bone_name].use_connect = False
                    edit_bone_parent(arm, bone_name, "TGT_root")
                else:
                    arm.edit_bones[bone_name].parent = None

        if self.bone_type == "BOTH" or self.bone_type == "TGT":
            # constrain bone to TGT
            for bone_name in bone_list:
                pose_bone = get_pose_bone(arm_obj, bone_name)
                tgtname = rename_to_tgt(bone_name)
                add_copytrans_con(pose_bone, arm_obj, tgtname)
        elif self.bone_type == "CTL":
            # constrain bone to CTL
            for bone_name in bone_list:
                pose_bone = get_pose_bone(arm_obj, bone_name)
                ctlname = rename_to_ctl(bone_name)
                add_copytrans_con(pose_bone, arm_obj, ctlname)

        for bone_name in tgtbones:
            bone_data = arm_obj.data.bones[bone_name]
            assign_to_tgt_bl(bone_data)

        for bone_name in ctlbones:
            bone_data = arm_obj.data.bones[bone_name]
            assign_to_ctl_bl(bone_data)

        bpy.ops.object.mode_set(mode="EDIT")

        return {"FINISHED"}


class JDRIGGING_OT_add_mch_con(JDRiggingOperator, Operator):
    """
    Adds MCH as parents of selected bones and MCH_INT as children of
    the active bone. Then constrains MCH bones to the MCH_INT.
    This makes an offset constraint, so children of MCH bones retain
    their original positions, but driven by the MCH_INT parent.
    Can also toggle the influence of constraints with follow toggles,
    eg. can have arm inherit torso rotation or not.
    Assumes Edit mode is active and bones selected with one active.
    """

    bl_idname = "jdrigging.add_mch_con_operator"
    bl_label = "Add MCH CON"
    bl_description = "Adds MCH bones to selected bones and adds constraints. Select bones to be constrained first then target last, so it is active. Must be used in Edit Mode."

    con_type: bpy.props.StringProperty()

    def execute(self, context):
        arm_obj = get_arm_obj(self, context)
        arm = bpy.data.armatures[arm_obj.data.name]
        bpy.ops.object.mode_set(mode="EDIT")
        bone_list = get_edit_bone_list(self, context)
        activate_bone_layers(arm)

        mchbones = []
        mch_intbones = []

        parent_name = arm.edit_bones.active.name
        parent_bone = arm.edit_bones[parent_name]

        bone_list.remove(parent_name)
        child_bones = bone_list

        # Create MCH bones
        for child_name in child_bones:
            mchbone = create_mch_bone(self, context, parent_bone, child_name, arm_obj)
            mchbones.append(mchbone.name)

        # Create MCH_INT bones
        for mch_name in mchbones:
            mch_int_name = rename_to_mch_int(name=mch_name)
            mch_intbones.append(mch_int_name)
            duplicate_bone(arm_obj, mch_int_name, arm, mch_name)

        # Make MCHs parent of child bones
        for child_name in child_bones:
            mch_name = rename_to_mch(name=child_name)
            arm.edit_bones[child_name].use_connect = False
            edit_bone_parent(arm, child_name, mch_name)

        # Make MCH_INTs child of parent bones
        for mch_int_name in mch_intbones:
            arm.edit_bones[mch_int_name].use_connect = False
            edit_bone_parent(arm, mch_int_name, parent_name)

        # Flip to pose mode
        bpy.ops.object.posemode_toggle()

        if self.con_type == "TRANS":
            # Add copy transforms contraint
            for mch_name in mchbones:
                pose_bone = arm_obj.pose.bones[mch_name]
                mch_intname = rename_to_mch_int(mch_name)
                add_copytrans_con(pose_bone, arm_obj, mch_intname)

        if self.con_type == "LOCROT":
            # Add copy location and rotation contraint
            for mch_name in mchbones:
                pose_bone = arm_obj.pose.bones[mch_name]
                mch_intname = rename_to_mch_int(mch_name)
                add_copyloc_con(pose_bone, arm_obj, mch_intname)
                add_copyrot_con(pose_bone, arm_obj, mch_intname)

        if self.con_type == "LOC":
            # Add copy location contraint
            for mch_name in mchbones:
                pose_bone = arm_obj.pose.bones[mch_name]
                mch_intname = rename_to_mch_int(mch_name)
                add_copyloc_con(pose_bone, arm_obj, mch_intname)

        if self.con_type == "ROT":
            # Add copy location contraint
            for mch_name in mchbones:
                pose_bone = arm_obj.pose.bones[mch_name]
                mch_intname = rename_to_mch_int(mch_name)
                add_copyrot_con(pose_bone, arm_obj, mch_intname)

        for bone_name in mchbones:
            bone_data = arm_obj.data.bones[bone_name]
            assign_to_mch_bl(bone_data)

        for bone_name in mch_intbones:
            bone_data = arm_obj.data.bones[bone_name]
            assign_to_mch_bl(bone_data)

        # Flip to pose mode
        bpy.ops.object.mode_set(mode="POSE")

        return {"FINISHED"}


class JDRIGGING_OT_add_con(JDRiggingOperator, Operator):
    """
    Adds Constraints to selected bones, with active bone as the target.
    Assumes Pose mode is active and bones selected with one active.
    """

    bl_idname = "jdrigging.add_con_operator"
    bl_label = "Add CON"
    bl_description = "Adds constraints. Select bones to be constrained first then target last, so it is active. Must be used in Pose Mode."

    con_type: bpy.props.StringProperty()

    def execute(self, context):
        arm_obj = get_arm_obj(self, context)
        arm = bpy.data.armatures[arm_obj.data.name]
        bpy.ops.object.mode_set(mode="POSE")
        bone_list = get_pose_bone_list(self, context)

        target_name = arm.bones.active.name
        bone_list.remove(target_name)

        if self.con_type == "TRANS":
            # Add copy transforms contraint
            for bone in bone_list:
                pose_bone = arm_obj.pose.bones[bone]
                add_copytrans_con(pose_bone, arm_obj, target_name)

        if self.con_type == "LOC":
            # Add copy location contraint
            for bone in bone_list:
                pose_bone = arm_obj.pose.bones[bone]
                add_copyloc_con(pose_bone, arm_obj, target_name)

        if self.con_type == "ROT":
            # Add copy location contraint
            for bone in bone_list:
                pose_bone = arm_obj.pose.bones[bone]
                add_copyrot_con(pose_bone, arm_obj, target_name)

        if self.con_type == "SCALE":
            # Add copy location contraint
            for bone in bone_list:
                pose_bone = arm_obj.pose.bones[bone]
                add_copyscale_con(pose_bone, arm_obj, target_name)

        # Flip to pose mode
        bpy.ops.object.mode_set(mode="POSE")

        return {"FINISHED"}


class JDRIGGING_OT_ctle(JDRiggingOperator, Operator, AddObjectHelper):
    """
    Adds CTL, TGT and DEF bones at the centre of each selected object.
    An armature will be created if there is no armature object
    present in the scene. Otherwise, the bones will be added to
    an existing armature. Sets bones in the hierarchy and creates constraint.
    Also creates and/or assigns widget objects, bone layers and bone groups.
    Widget objects are assigned to a hidden collection.
    Assumes Object mode is active and mesh objects are selected.
    """

    bl_idname = "jdrigging.ctle_operator"
    bl_label = "Auto CTL"
    bl_description = "Adds CTL, TGT and DEF bones at center of each selected object. If there is no armature present in the scene, a new one is created, otherwise the bones are added to an existing armature. Must be used in Object Mode"

    wgt_type: bpy.props.StringProperty()

    def execute(self, context):
        unit_scale = bpy.data.scenes['Scene'].unit_settings.scale_length
        # get list of selected objects
        list = [obj.name for obj in bpy.context.selected_objects]
        # deselect everything incase or it will confuse the 3D cursor later
        bpy.ops.object.select_all(action="DESELECT")
        # get list of scene objects
        all = bpy.context.scene.objects
        # get list of armature names if any
        armlist = [arm.name for arm in all if arm.type == "ARMATURE"]
        # check if list of rigs is empty.
        # can also be written as if not len(armlist):
        if armlist:
            arm_obj = bpy.data.objects[armlist[0]]
            bpy.context.view_layer.objects.active = arm_obj
            arm_obj.select_set(True)
        else:
            arm_obj = create_base_rig(self, context)

        # get and identify the armature data
        arm = bpy.data.armatures[arm_obj.data.name]

        # make sure layers are active incase bones are already present
        activate_bone_layers(arm)

        # unselect rig
        arm_obj.select_set(False)

        # create empty lists for DEF TGT CTL bones
        defbones = []
        tgtbones = []
        depthbones = []
        ctlbones = []

        # create DEF bone for each object
        for object_name in list:
            # Snap cursor to centre of object
            cursor_to_object_centre(self, context, object_name)

            # select rig
            bpy.context.view_layer.objects.active = arm_obj
            arm_obj.select_set(True)
            # go to edit mode
            bpy.ops.object.mode_set(mode="EDIT")

            # remove GEO_ prefix if needed and add DEF_
            defname = rename_to_def(object_name)
            # add to list
            defbones.append(defname)
            # create DEF bone
            bone = new_edit_bone(arm_obj, defname, context)
            # turn off deform
            bone.use_deform = True

            # go to object mode
            bpy.ops.object.mode_set(mode="OBJECT")
            # unselect rig
            arm_obj.select_set(False)
        # return cursor to center
        bpy.ops.view3d.snap_cursor_to_center()

        # create TGT bone for each def bone and match it
        for defname in defbones:
            # get matching tgt bone name
            tgtname = rename_to_tgt(defname)
            # add to list
            tgtbones.append(tgtname)

            # create TGT bone
            tgtbone = duplicate_bone(arm_obj, tgtname, arm, defname)
            if round(unit_scale, 2) == 0.01:
                tgtbone.tail.y += 15
            else:
                tgtbone.tail.y += 0.15

        # create CTL bone for each tgt bone and match it
        if self.wgt_type == "2D":
            for tgtname in tgtbones:
                # get matching ctl bone name
                depthname = rename_to_depth(tgtname)
                # add to list
                depthbones.append(depthname)

                # create depth bone
                depthbone = duplicate_bone(arm_obj, depthname, arm, tgtname)
                if round(unit_scale, 2) == 0.01:
                    depthbone.tail.y += 20
                else:
                    depthbone.tail.y += 0.2
                depthpose = get_pose_bone(arm_obj, depthname)
                # lock x, z translate, all rotations and all scale for depths
                depthpose.lock_location[0] = True
                depthpose.lock_location[2] = True
                depthpose.lock_rotation[0] = True
                depthpose.lock_rotation[1] = True
                depthpose.lock_rotation[2] = True
                depthpose.lock_scale[0] = True
                depthpose.lock_scale[1] = True
                depthpose.lock_scale[2] = True

        # create CTL bone for each tgt bone and match it
        for tgtname in tgtbones:
            # get matching ctl bone name
            ctlname = rename_to_ctl(tgtname)
            # add to list
            ctlbones.append(ctlname)

            # create depth bone
            ctlbone = duplicate_bone(arm_obj, ctlname, arm, tgtname)
            if round(unit_scale, 2) == 0.01:
                ctlbone.tail.y += 25
            else:
                ctlbone.tail.y += 0.25
            ctlpose = get_pose_bone(arm_obj, ctlname)
            if self.wgt_type == "2D":
                ctlpose.rotation_mode = "XZY"
                # lock y translate, x, z rotations and y scale for ctls
                ctlpose.lock_location[1] = True
                ctlpose.lock_rotation[0] = True
                ctlpose.lock_rotation[2] = True
                ctlpose.lock_scale[1] = True

        # make TGT_root if it does not exist
        rootname = "TGT_root"
        # go to edit mode
        bpy.ops.object.mode_set(mode="EDIT")
        bonelist = [bone for bone in arm.edit_bones if rootname in bone.name]
        # create one if it doesnt exist
        if bonelist:
            arm.edit_bones[rootname]
        else:
            new_edit_bone(arm_obj, rootname, context)

        delete_default_bone(arm)

        # set bone parents
        # make CTL parent of TGT
        if self.wgt_type != "2D":
            for tgtname in tgtbones:
                # get matching ctl bone name
                ctlname = rename_to_ctl(tgtname)
                edit_bone_parent(arm, tgtname, ctlname)
        else:
            for tgtname in tgtbones:
                # get matching depth bone name
                depthname = rename_to_depth(tgtname)
                edit_bone_parent(arm, tgtname, depthname)
            for depthname in depthbones:
                # get matching ctl bone name
                ctlname = rename_to_ctl(depthname)
                edit_bone_parent(arm, depthname, ctlname)

        # Make all def and ctl bones children of TGT_root
        for defname in defbones:
            edit_bone_parent(arm, defname, rootname)
        for ctlname in ctlbones:
            edit_bone_parent(arm, ctlname, rootname)

        # Contrain DEF bones to corresponding TGT bones
        for defname in defbones:
            # get matching tgt bone name
            tgtname = rename_to_tgt(defname)
            # Flip to pose mode
            bpy.ops.object.posemode_toggle()
            # get pose bones
            defpose = arm_obj.pose.bones[defname]
            # create copy transforms constraint
            add_copytrans_con(defpose, arm_obj, tgtname)

        # add each object to corresponding def bone vertex group
        for object_name in list:
            add_armature_modifier(object_name, arm_obj)
            defname = rename_to_def(object_name)
            add_vertex_group(context, object_name, defname)

        # assign widgets
        widget_name = get_widget_name(self.wgt_type)
        widget = get_widget(self, context, widget_name, self.wgt_type)
        pose = arm_obj.pose
        for ctlname in ctlbones:
            assign_widget(context, arm_obj, ctlname, pose, widget, arm)
        if self.wgt_type == "2D":
            widget_name = "WGT_sphere_low"
            depth_widget = get_widget(self, context, widget_name, "Sphere Low")
            for depthname in depthbones:
                assign_widget(context, arm_obj, depthname, pose, depth_widget, arm)

        widget_collection = get_wgt_collection(self, context)
        assign_wgt_collection(widget, widget_collection)
        if self.wgt_type == "2D":
            assign_wgt_collection(depth_widget, widget_collection)

        # get bone groups
        bonegrps = arm_obj.pose.bone_groups
        grpslist = [bgrp for bgrp in bonegrps if bgrp.name == "Extras"]
        # if there are no bone groups and make them or get them if there
        if grpslist:
            extrasgrp = bonegrps["Extras"]
        else:
            extrasgrp = get_extras_bg(arm_obj)
        grpslist = [bgrp for bgrp in bonegrps if bgrp.name == "Center"]
        if grpslist:
            centergrp = bonegrps["Center"]
        else:
            centergrp = get_center_bg(arm_obj)

        # Flip to pose mode
        bpy.ops.object.posemode_toggle()
        if self.wgt_type != "2D":
            for ctlname in ctlbones:
                pose.bones[ctlname].bone_group = extrasgrp
        else:
            for ctlname in ctlbones:
                pose.bones[ctlname].bone_group = centergrp
            for depthname in depthbones:
                pose.bones[depthname].bone_group = extrasgrp
        # seperate bones into layers
        # DEF bone layer
        for defname in defbones:
            bone_data = arm_obj.data.bones[defname]
            assign_to_def_bl(bone_data)
        # TGT bone layer
        for tgtname in tgtbones:
            bone_data = arm_obj.data.bones[tgtname]
            assign_to_tgt_bl(bone_data)
        bone_data = arm_obj.data.bones[rootname]
        assign_to_tgt_bl(bone_data)
        # depth bone layer
        if self.wgt_type == "2D":
            for depthname in depthbones:
                bone_data = arm_obj.data.bones[depthname]
                assign_to_depth_bl(bone_data)
        # CTL bone layer
        for ctlname in ctlbones:
            bone_data = arm_obj.data.bones[ctlname]
            assign_to_ctl_bl(bone_data)

        # clean up
        default_bone_layer_viz(arm)
        # go to object mode
        bpy.ops.object.mode_set(mode="OBJECT")
        # hide COL_widgets.
        hide_collection(widget_collection)

        return {"FINISHED"}


class JDRIGGING_OT_add_wgt(JDRiggingOperator, Operator, AddObjectHelper):
    """
    Assigns a new widget object as selected bones’ Custom Object.
    If the widget object already exists, the existing object is assigned.
    Widget shape depends on the panel button used.
    Widget objects are assigned to a hidden collection. Widget object creation
    functions are found in jdr_wgt_library.py.
    Assumes Pose mode is active and bones are selected.
    """

    bl_idname = "jdrigging.add_wgt_operator"
    bl_label = "ADD_WGT"
    bl_description = "Assigns a new widget object as seleted bone(s) Custom Object. If the widget object already exists, the existing object is assigned. Must be used in Pose Mode"

    wgt_type: bpy.props.StringProperty()

    def execute(self, context):
        bone_list = get_pose_bone_list(self, context)

        arm_obj = get_arm_obj(self, context)

        # Get the armature data.
        arm = bpy.data.armatures[arm_obj.data.name]
        pose = arm_obj.pose

        widget_name = get_widget_name(self.wgt_type)

        widget = get_widget(self, context, widget_name, self.wgt_type)

        for bone in bone_list:
            assign_widget(context, arm_obj, bone, pose, widget, arm)

        widget_collection = get_wgt_collection(self, context)

        assign_wgt_collection(widget, widget_collection)

        hide_collection(widget_collection)

        # select rig
        bpy.context.view_layer.objects.active = arm_obj
        arm_obj.select_set(True)
        # Flip to pose mode
        bpy.ops.object.posemode_toggle()

        return {"FINISHED"}


class JDRIGGING_OT_addvertgrp(JDRiggingOperator, Operator):
    """
    Adds a vertex group to each selected object. The vertex group name is
    taken from the text box in the panel. All vertices of the object are
    assigned to the group. Useful if you want all selected objects weighted
    to one bone or all objects will have a similar modifier affecting all
    their vertices, eg. mask modifier. Assumes Object mode is active, text in
    the text box and mesh objects are selected.
    """

    bl_idname = "jdrigging.addvertgrp_operator"
    bl_label = "Add Vertex Group"
    bl_description = "Adds a Vertex Group to each selected object. All vertices are assined to the group. Must be used in Object Mode"

    def execute(self, context):
        # get list of selected
        list = [obj.name for obj in bpy.context.selected_objects]
        wm = context.scene
        group_name = wm.vgname
        # add vert group to each object
        for object_name in list:
            add_vertex_group(context, object_name, group_name)

        return {"FINISHED"}
