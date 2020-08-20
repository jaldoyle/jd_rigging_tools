"""
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

bl_info = {
    "name": "JD_Rigging_Tools",
    "author": "Josh Doyle <joshalidoyle@gmail.com>",
    "description": "Rigging Tools",
    "blender": (2, 83, 0),
    "version": (1, 3),
    "location": "View3D > Toolbar > JD Rigging Tools",
    "warning": "If broken please report",
    "category": "Rigging",
}

import bpy

from .jdr_panel import JDRIGGING_PT_rigcreate
from .jdr_panel import JDRIGGING_PT_ctle3d
from .jdr_panel import JDRIGGING_PT_ctle2d
from .jdr_panel import JDRIGGING_PT_add_wgt
from .jdr_panel import JDRIGGING_PT_addvertgrp

from .jdr_operators import JDRIGGING_OT_base_rig
from .jdr_operators import JDRIGGING_OT_ctle
from .jdr_operators import JDRIGGING_OT_addvertgrp
from .jdr_operators import JDRIGGING_OT_add_wgt
from .jdr_operators import JDRIGGING_OT_new_world_bone
from .jdr_operators import JDRIGGING_OT_add_ctl_tgt
from .jdr_operators import JDRIGGING_OT_add_mch_con
from .jdr_operators import JDRIGGING_OT_add_con

classes = [
    JDRIGGING_PT_rigcreate,
    JDRIGGING_PT_ctle3d,
    JDRIGGING_PT_ctle2d,
    JDRIGGING_PT_add_wgt,
    JDRIGGING_PT_addvertgrp,
    JDRIGGING_OT_base_rig,
    JDRIGGING_OT_ctle,
    JDRIGGING_OT_addvertgrp,
    JDRIGGING_OT_add_wgt,
    JDRIGGING_OT_new_world_bone,
    JDRIGGING_OT_add_ctl_tgt,
    JDRIGGING_OT_add_mch_con,
    JDRIGGING_OT_add_con,
]


def register():

    bpy.types.Scene.vgname = bpy.props.StringProperty(
        name="Vertex Group Name", default=""
    )

    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():

    del bpy.types.Scene.vgname

    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
