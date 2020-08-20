import bpy
from bpy.types import Panel


class JDRiggingPanel:
    # window panel can be accessed from N toolbar
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    # add to existing tab or new one
    bl_category = "JD Rigging Tools"


class JDRIGGING_PT_rigcreate(JDRiggingPanel, Panel):
    # label panel
    bl_label = "Rig Create"
    # name panel to call back on
    bl_idname = "JDRIGGING_PT_rigcreate"

    def draw(self, context):
        layout = self.layout
        layout.operator(
            "jdrigging.base_rig_operator", text="Base Rig", icon="OUTLINER_OB_ARMATURE"
        )

        box = layout.box()
        box.label(text="World Bones")
        row = box.row(align=True)
        world_bone_op = "jdrigging.new_world_bone_operator"
        row.operator(world_bone_op, text="Deform", icon="BONE_DATA").bone_type = "DEF"
        row.operator(
            world_bone_op, text="Non-Deform", icon="BONE_DATA"
        ).bone_type = "noDEF"

        box = layout.box()
        box.label(text="Control & Target Bones")
        row = box.row()
        ctl_tgt_op = "jdrigging.add_ctl_tgt_operator"
        row.operator(
            ctl_tgt_op, text="Add CTL & TGT", icon="BONE_DATA"
        ).bone_type = "BOTH"
        row = box.row(align=True)
        row.operator(ctl_tgt_op, text="Add CTL", icon="BONE_DATA").bone_type = "CTL"
        row.operator(ctl_tgt_op, text="Add TGT", icon="BONE_DATA").bone_type = "TGT"

        box = layout.box()
        box.label(text="Mechanical Bones & Constraints")
        row = box.row()
        mch_con_op = "jdrigging.add_mch_con_operator"
        row.operator(
            mch_con_op, text="MCH Transforms", icon="CON_TRANSLIKE"
        ).con_type = "TRANS"
        row = box.row()
        row.operator(
            mch_con_op, text="MCH Location and Rotaion", icon="CON_TRANSLIKE"
        ).con_type = "LOCROT"
        row = box.row(align=True)
        row.operator(
            mch_con_op, text="MCH Location", icon="CON_LOCLIKE"
        ).con_type = "LOC"
        row.operator(
            mch_con_op, text="MCH Rotation", icon="CON_ROTLIKE"
        ).con_type = "ROT"

        box = layout.box()
        box.label(text="Constraints")
        row = box.row()
        con_op = "jdrigging.add_con_operator"
        row.operator(con_op, text="Transforms", icon="CON_TRANSLIKE").con_type = "TRANS"
        row = box.row(align=True)
        row.operator(con_op, text="Location", icon="CON_LOCLIKE").con_type = "LOC"
        row.operator(con_op, text="Rotation", icon="CON_ROTLIKE").con_type = "ROT"
        row = box.row()
        row.operator(con_op, text="Scale", icon="CON_SIZELIKE").con_type = "SCALE"


class JDRIGGING_PT_ctle3d(JDRiggingPanel, Panel):
    # label panel
    bl_label = "CTL Each"
    # name panel to call back on
    bl_idname = "JDRIGGING_PT_ctle3d"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Select Object(s) and Run")
        grid = layout.grid_flow(
            row_major=True, columns=2, even_columns=True, even_rows=True, align=True
        )
        op_name = "jdrigging.ctle_operator"
        grid.operator(op_name, text="Square CTL", icon="MATPLANE").wgt_type = "Square"
        grid.operator(
            op_name, text="Circle CTL", icon="MESH_CIRCLE"
        ).wgt_type = "Circle"
        grid.operator(op_name, text="Cube CTL", icon="CUBE").wgt_type = "Cube"
        grid.operator(
            op_name, text="Prism CTL", icon="MESH_ICOSPHERE"
        ).wgt_type = "Prism"


class JDRIGGING_PT_ctle2d(JDRiggingPanel, Panel):
    # label panel
    bl_label = "2D CTL Each"
    # name panel to call back on
    bl_idname = "JDRIGGING_PT_ctle2d"
    # make child of first panel
    bl_parent_id = "JDRIGGING_PT_ctle3d"
    # make it closed by default
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator(
            "jdrigging.ctle_operator", text="2D CTL", icon="MATPLANE"
        ).wgt_type = "2D"


class JDRIGGING_PT_add_wgt(JDRiggingPanel, Panel):
    # label panel
    bl_label = "WGT Adder"
    # name panel to call back on
    bl_idname = "JDRIGGING_PT_add_wgt"
    # make it closed by default
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Select Pose Bone(s) and Run")
        grid = layout.grid_flow(
            row_major=True, columns=2, even_columns=True, even_rows=True, align=True
        )
        op_name = "jdrigging.add_wgt_operator"
        grid.operator(op_name, text="All", icon="CURSOR").wgt_type = "All"
        grid.operator(
            op_name, text="Transform", icon="PIVOT_CURSOR"
        ).wgt_type = "Transform"
        grid.operator(
            op_name, text="Arrows Thick", icon="EMPTY_ARROWS"
        ).wgt_type = "Arrows Thick"
        grid.operator(
            op_name, text="Arrows Thin", icon="EMPTY_ARROWS"
        ).wgt_type = "Arrows Thin"
        grid.operator(op_name, text="Square", icon="MATPLANE").wgt_type = "Square"
        grid.operator(op_name, text="Circle", icon="MESH_CIRCLE").wgt_type = "Circle"
        grid.operator(op_name, text="Cube", icon="CUBE").wgt_type = "Cube"
        grid.operator(op_name, text="Prism", icon="MESH_ICOSPHERE").wgt_type = "Prism"
        grid.operator(
            op_name, text="Sphere Low", icon="MESH_UVSPHERE"
        ).wgt_type = "Sphere Low"
        grid.operator(
            op_name, text="Sphere High", icon="SPHERE"
        ).wgt_type = "Sphere High"
        grid.operator(
            op_name, text="Arrow Thick", icon="EMPTY_SINGLE_ARROW"
        ).wgt_type = "Arrow Thick"
        grid.operator(
            op_name, text="Arrow Thin", icon="EMPTY_SINGLE_ARROW"
        ).wgt_type = "Arrow Thin"
        grid.operator(
            op_name, text="Double Arrow Thick", icon="ARROW_LEFTRIGHT"
        ).wgt_type = "Double Arrow Thick"
        grid.operator(
            op_name, text="Double Arrow Thin", icon="ARROW_LEFTRIGHT"
        ).wgt_type = "Double Arrow Thin"
        grid.operator(op_name, text="COG", icon="PROP_CON").wgt_type = "COG"
        grid.operator(
            op_name, text="Properties", icon="SETTINGS"
        ).wgt_type = "Properties"
        grid.operator(
            op_name, text="Upper Body", icon="TRIA_UP"
        ).wgt_type = "Upper Body"
        grid.operator(
            op_name, text="Lower Body", icon="TRIA_DOWN"
        ).wgt_type = "Lower Body"
        grid.operator(op_name, text="Head", icon="USER").wgt_type = "Head"
        grid.operator(op_name, text="Jaw", icon="CUBE").wgt_type = "Jaw"
        grid.operator(op_name, text="Face", icon="FILE_FONT").wgt_type = "Face"
        grid.operator(op_name, text="Eye All", icon="HIDE_OFF").wgt_type = "Eye All"
        grid.operator(op_name, text="Foot", icon="MOD_DYNAMICPAINT").wgt_type = "Foot"
        grid.operator(op_name, text="Clav", icon="CUBE").wgt_type = "Clav"


class JDRIGGING_PT_addvertgrp(JDRiggingPanel, Panel):
    # label panel
    bl_label = "Add Vertex Group"
    # name panel to call back on
    bl_idname = "JDRIGGING_PT_addvertgrp"
    # make it closed by default
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        #  Activate single-column layout
        layout.use_property_split = True

        row = layout.row()
        row.prop(scene, "vgname")
        row = layout.row()
        row.operator(
            "jdrigging.addvertgrp_operator",
            text="Add Vertex Group",
            icon="GROUP_VERTEX",
        )
