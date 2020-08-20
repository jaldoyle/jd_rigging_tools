<h1>Introduction</h1>

JD Rigging tools is a Blender add on to do simple rigging actions faster. While Blender has some great auto rigging add ons, such as Rigify and Auto-Rig Pro, there arent many to assist create your our own custom rigs. I made this add on for that reason. With it you can  easily make a bone match the world axis with one button, rig multiple objects at once each with their own controller, add a custom object to multiple bones at once from a library object shapes and more!

It is compatable with Blender versions 2.8+. You can download blender <a href="https://www.blender.org/download/" target="_blank">here</a>.

Some of the tools are very specific to my workflow when rigging in Blender. However, my workflow is primarilary based on Pierrick Picaut's tutorial course <a href="https://gumroad.com/p2design#AeQfrF" target="_blank">"The art of effective rigging in Blender"</a>, so anyone who follows the workflow he teaches, should understand the bone heirarcies and naming conventions that the add on creates. I would like to make this add on useful to as many riggers and animators as possible, so if you have suggestions on how the add on could assist your workflow better, please let me know and I will try to implement it. I am still realativley new to Python, add on development and git hub especially, so please be patiant with me if it takes me some time to figure things out. If anyone has edit suggestions to the python files to make it more efficent it would be greatly appreciated.
Rig Create Tools

Base Rig
Creates a Base Rig (armature) object with All, main and main_offset CTL bones and TGT_root bone. Sets bones in the hierarchy and creates constraint. Also creates and assigns widget objects, bone layers and bone groups. Widget objects assigned to a hidden collection. Assumes Object mode is active.

World Bones
Creates an edit bone with axis matching the world in the active armature. Depending on which button is used, the bone will or will not have deform active. Head of bone matches 3D cursor position. Assumes Edit mode is active.

Control & Target Bones
Adds CTL and/or TGT bones to selected bones(DEF bones expected, but can be used on other bones). If Both are added, TGT a child of CTL and selected bone constrained to TGT. CTL's parent will be set to the corresponding selected bone parent's CTL. Selected bone's parent will be TGT_root if present or as None. If just CTLs are added, selected bones are constrained to CTLs instead. If just TGTs are added, TGT's parent will be set to the corresponding selected bone parent's TGT. Assumes Edit mode is active and bones selected.

Mechanical Bones & Constraints
Adds MCH as parents of selected bones and MCH_INT as children of the active bone. Then constrains MCH bones to the MCH_INT. This makes an offset constraint, so children of MCH bones retain their original positions, but driven by the MCH_INT parent. Can also toggle the influence of constraints with follow toggles, eg. can have arm inherit torso rotation or not. Assumes Edit mode is active and bones selected with one active.

Constraints
Adds Constraints to selected bones, with active bone as the target.
Assumes Pose mode is active and bones selected with one active.

CTL Each
Adds CTL, TGT and DEF bones at the centre of each selected object. An armature will be created if there is no armature object present in the scene. Otherwise, the bones will be added to an existing armature. Sets bones in the hierarchy and creates constraint. Also creates and/or assigns widget objects, bone layers and bone groups. Widget objects are assigned to a hidden collection. Assumes Object mode is active and mesh objects are selected.

WGT Adder
Assigns a new widget object as selected bones’ Custom Object. If the widget object already exists, the existing object is assigned. Widget shape depends on the panel button used.
Widget objects are assigned to a hidden collection. Widget object creation functions are found in jdr_wgt_library.py. Assumes Pose mode is active and bones are selected.

Add Vertex Group
Adds a vertex group to each selected object. The vertex group name is taken from the text box in the panel. All vertices of the object are assigned to the group. Useful if you want all selected objects weighted to one bone or all objects will have a similar modifier affecting all their vertices, eg. mask modifier. Assumes Object mode is active, text in the text box and mesh objects are selected.

To Install:

Edit > Preferences > Add-ons. Click Install, select JD_rigging_tools.zip and Install Add-on. Do not unzip the file, install won’t work. Then tick the box next to Rigging: JD_Rigging_Tools.

Disclaimer: 
As I’m currently working to export assets to game engine, I have my Blender unit scale set to 0.01. If your unit scale is set to the default 1, you may need to scale down the objects created with this add on. I may add a feature to vary the scale of objects later on.

