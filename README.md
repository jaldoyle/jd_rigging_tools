[![Header](https://github.com/jaldoyle/jd_rigging_tools/blob/master/images/YT_thumbnail_3.jpg)](https://youtu.be/9C9oDs0Qc3s)

# Introduction

JD Rigging tools is a Blender Addon to do simple rigging actions faster. While Blender has some great auto rigging Addons, such as Rigify and [Auto-Rig Pro](https://blendermarket.com/products/auto-rig-pro?ref=2), 
there aren't many to assist creating your own custom rigs. I made this Addon for that reason. With it you can easily make a bone matching the world axis with one click, 
rig multiple objects at once each with their own controllers, add a custom object to multiple bones at once from a library of object shapes and more!

Compatible with Blender versions 2.8+. You can download blender [here](https://www.blender.org/download/).

Some of the tools are very specific to my workflow when rigging in Blender. However, my workflow is primarily based on Pierrick Picaut's tutorial course 
["The art of effective rigging in Blender"](https://gumroad.com/p2design#AeQfrF), so anyone who follows the workflow he teaches should understand the bone hierarchies and naming conventions that the Addon creates. I would like to make this Addon useful to as many riggers and animators as possible, so if you have suggestions on how the Addon could assist your workflow better, please let me know and I will try to implement it. I am still relatively new to Python, Addon development and GitHub especially, so please be patient with me if it takes me some time to figure things out. If anyone has edit suggestions to the python files to make it more efficient it would be greatly appreciated.

# Installation

![Install](https://github.com/jaldoyle/jd_rigging_tools/blob/master/images/install.jpg)

In Blender go to Edit > Preferences > Add-ons. Click Install, select JD_rigging_tools.zip and Install Add-on. Do not unzip the file, install won’t work. Then tick the box next to Rigging: JD_Rigging_Tools.

# Features

![Install](https://github.com/jaldoyle/jd_rigging_tools/blob/master/images/jdr_panel.jpg)

### Rig Create Tools

#### Base Rig
Creates a Base Rig (armature) object with All, main and main_offset CTL bones and TGT_root bone. Sets bones in the hierarchy and creates constraint. Also creates and assigns widget objects, bone layers and bone groups. Widget objects assigned to a hidden collection. Assumes Object mode is active.

#### World Bones
Creates an edit bone with axis matching the world in the active armature. Depending on which button is used, the bone will or will not have deform active. Head of bone matches 3D cursor position. Assumes Edit mode is active.

#### Control & Target Bones
Adds CTL and/or TGT bones to selected bones(DEF bones expected, but can be used on other bones). If Both are added, TGT a child of CTL and selected bone constrained to TGT. CTL's parent will be set to the corresponding selected bone parent's CTL. Selected bone's parent will be TGT_root if present or as None. If just CTLs are added, selected bones are constrained to CTLs instead. If just TGTs are added, TGT's parent will be set to the corresponding selected bone parent's TGT. Assumes Edit mode is active and bones selected.

#### Mechanical Bones & Constraints
Adds MCH as parents of selected bones and MCH_INT as children of the active bone. Then constrains MCH bones to the MCH_INT. This makes an offset constraint, so children of MCH bones retain their original positions, but driven by the MCH_INT parent. Can also toggle the influence of constraints with follow toggles, eg. can have arm inherit torso rotation or not. Assumes Edit mode is active and bones selected with one active.

#### Constraints
Adds Constraints to selected bones, with active bone as the target.
Assumes Pose mode is active and bones selected with one active.

### CTL Each
Adds CTL, TGT and DEF bones at the centre of each selected object. An armature will be created if there is no armature object present in the scene. Otherwise, the bones will be added to an existing armature. Sets bones in the hierarchy and creates constraint. Also creates and/or assigns widget objects, bone layers and bone groups. Widget objects are assigned to a hidden collection. Assumes Object mode is active and mesh objects are selected.

### WGT Adder
Assigns a new widget object as selected bones’ Custom Object. If the widget object already exists, the existing object is assigned. Widget shape depends on the panel button used.
Widget objects are assigned to a hidden collection. Widget object creation functions are found in jdr_wgt_library.py. Assumes Pose mode is active and bones are selected.

### Add Vertex Group
Adds a vertex group to each selected object. The vertex group name is taken from the text box in the panel. All vertices of the object are assigned to the group. Useful if you want all selected objects weighted to one bone or all objects will have a similar modifier affecting all their vertices, eg. mask modifier. Assumes Object mode is active, text in the text box and mesh objects are selected.
