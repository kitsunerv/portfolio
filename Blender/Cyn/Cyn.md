# Blender Character Model – Cyn (Murder Drones Fan Project)

## Blender – Custom Rig – Ongoing Solo Project – 2024–now

This project is a detailed fan recreation of Cyn, a character from the indie web series Murder Drones by Glitch Productions. It began as a way to explore various aspects of character modeling and rigging in Blender, and over time evolved into a full-featured learning project with the goal of producing a model that is ultimately animation-ready.

So far, I’ve focused primarily on modeling and rigging, with materials and texturing coming later. The model currently uses placeholder procedural shaders created in the Blender shader editor, which will be replaced with hand-painted or PBR textures once the rig is finalized.

One of the highlights of the project is the entirely custom rig, which I built from the ground up based on features I liked in Rigify—such as IK/FK switching, finger controls, and clean limb setups—but implemented entirely on my own without relying on auto-rigging systems. I also created a test scene within the project file which contains all the setup experiments and tests I ran to develop and refine the rig.
Custom Scripted Controls:

- IK/FK Switches: Functional on both arms and legs, with intuitive snapping.

- Eye Expression System: The character’s eyes are shapes on a screen; I built a control panel that allows swapping between different expressions using drivers and custom properties.

- Dual-Hand Linking: Cyn has four hands—two primary and two secondary. A toggle allows the secondary hands to mimic the pose of the main ones for synced animation.

While building the rig, I ran into several technical challenges—especially with eye shape switching and the weight painting, which proved especially finicky around the face. The mouth rig is still a work in progress, and has been one of the more complex systems to design cleanly. The hair modeling, while not particularly difficult, has been time-consuming to block out and refine.

This model has been in progress on and off over the past five months, and has taught me a ton about blocking, proportions, retopology, rigging, and driver-based control systems. I’m particularly proud of how far I’ve come without relying on tutorials, just trial, error, and a solid foundation of Blender basics.
Next Steps:

- Finish the mouth rig and finalize the face deformations

- Add screen-accurate accessories and polish silhouette details

- Replace placeholder materials with final textures

- Begin test animation cycles using the rig

This project has not only sharpened my modeling and rigging workflow, it’s also helped me build confidence in solving complex technical challenges on my own.

## a little history of the model

### official model and concept art of Cyn used as references: 


<img src="./images/cyn-concept.webp" width="45%"/>

<img src="./images/cyn_teaser.webp" width="20%"/>
<img src="./images/Cyn_Art.jpg" width="27.5%"/>

*extras*

<img src="./images/heart.webp" width="45%"/>
<img src="./images/hand_tentacle.jpg" width="45%"/>

Why i find the face so complicated:

- from wide toothy grin taking up the whole bottom part of the face

<img src="./images/cyn_grin.webp" width="40%"/>

- to small close lips

<img src="./images/closed_lips.webp" width="40%"/>

- it can also move to the sides

<img src="./images/cyn.jpg" width="40%"/>

### History of the model

first blockouts:

<img src="./images/first_blockout.png" width="20%"/>
<img src="./images/first_robot_hands.png" width="20%"/>

<img src="./images/first_colors.png" width="20%"/>

start of the legs:

<img src="./images/leg_start.png" width="50%"/>

adding more details to the curves i used for the hair:

<img src="./images/hair_v1.png" width="45%"/>
<img src="./images/hair_v2.png" width="45%"/>

fixing the feets: 
 - model view:

<img src="./images/feet_v1_color.png" width="45%"/>
<img src="./images/feet_v2_color.png" width="45%"/>

 - wireframe view:
 
<img src="./images/feet_v1_wire.png" width="45%"/>
<img src="./images/feet_v2_wire.png" width="45%"/>

 starting the details:

<img src="./images/robe_start.png" width="70%"/>

adjusting proportions (skint tone proportions are the adjusted version): 

<img src="./images/new_prop_front.png" width="45%"/>
<img src="./images/new_prop_sides.png" width="45%"/>

 start of retopology (blockout is hiddden):

<img src="./images/start_retopo.png" width="70%"/>

 The first version is complete (made with a bic mixamo rig just to test how the model felt):

<img src="./images/test_render.png" width="70%"/>


teeths upgrade (old vs new):

<img src="./images/teeths_old.png" width="45%"/>
<img src="./images/teeths_new.png" width="45%"/>

shape keys control for the teeths:

<img src="./images/tsk1.png" width="45%"/>
<img src="./images/tsk2.png" width="45%"/>
<img src="./images/tsk3.png" width="45%"/>
<img src="./images/tsk4.png" width="45%"/>

the first version of the eyes: 

<img src="./images/eyes_v1.gif" width="45%"/>

the topology at this point (red lines are the seams for UV mapping):

<img src="./images/old_topo.png" width="45%"/>

a small change but one i wanted to do for a while (made with ibis paint):

<img src="./images/old_chet_icon.png" width="45%"/>
<img src="./images/newer_icon.png" width="45%"/>

new robot hands!:

<img src="./images/new_hand_up_c.png" width="45%"/>
<img src="./images/new_hand_up_w.png" width="45%"/>
<img src="./images/new_hand_down_c.png" width="45%"/>
<img src="./images/new_hand_down_w.png" width="45%"/>

the rings on the finger are there for accuracy with the source material and are toggleable via shapekeys for close up shots

chest icon v2 (made with illustrator):

<img src="./images/new_icon.png" width="45%"/>

new test render with a few miscelanous additions, such as:
 - Null orb (one of Cyn's the main power )
 - black hole(no real reason)
 - Absolute solver symbol (Cyn's power/icon also there for lighting purposes)

 <img src="./images/test_render_2.png" width="90%"/>

 Start of the rig:
- red for IK
- blue for FK
- absolute solver shape as root
- inspired by the rigify rig but entirely custom made
- control panel with FK/IK switch for all limbs

<img src="./images/rig_start.png" width="60%"/>

*extra: modeled and rigged the tentacle she has:*

<img src="./images/tentacle_rig.png" width="20%"/>
<img src="./images/test_render_3.png" width="70%"/>

trying rigs configuarion for the mouth using bendy bones:

<img src="./images/mrig_1_1.png" width="30%"/>
<img src="./images/mrig_1_2.png" width="30%"/>
<img src="./images/mrig_1_3.png" width="30%"/>
<img src="./images/mrig_1_4.png" width="30%"/>
<img src="./images/mrig_1_5.png" width="30%"/>
<img src="./images/mrig_1_6.png" width="30%"/>

*extra: hand tentacle from episode 2, and callback ping scene*

<img src="./images/hand_tentacle.png" width="30%"/>

*extra: start on the core*

<img src="./images/core_start.png" width="30%"/>


the new and improved rig control panel:

<img src="./images/control_panel.png" width="50%"/>

rigging issues: 

<img src="./images/rig_issue_1.png" width="45%"/>
<img src="./images/rig_issue_2.png" width="45%"/>

fixed issue 1:

<img src="./images/issue_1_fix_1.png" width="45%"/>
<img src="./images/issue_1_fix_2.png" width="45%"/>

*extra: progress on the core:*

<img src="./images/core_progress.png" width="60%"/>
<img src="./images/core_flesh.png" width="30%"/>