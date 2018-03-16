from header_common import *
from header_operations import *
from header_triggers import *
from header_scenes import *
from module_constants import *

####################################################################################################################
#  Each scene record contains the following fields:
#  1) Scene id {string}: used for referencing scenes in other files. The prefix scn_ is automatically added before each scene-id.
#  2) Scene flags {int}. See header_scenes.py for a list of available flags
#  3) Mesh name {string}: This is used for indoor scenes only. Use the keyword "none" for outdoor scenes.
#  4) Body name {string}: This is used for indoor scenes only. Use the keyword "none" for outdoor scenes.
#  5) Min-pos {(float,float)}: minimum (x,y) coordinate. Player can't move beyond this limit.
#  6) Max-pos {(float,float)}: maximum (x,y) coordinate. Player can't move beyond this limit.
#  7) Water-level {float}. 
#  8) Terrain code {string}: You can obtain the terrain code by copying it from the terrain generator screen
#  9) List of other scenes accessible from this scene {list of strings}.
#     (deprecated. This will probably be removed in future versions of the module system)
#     (In the new system passages are used to travel between scenes and
#     the passage's variation-no is used to select the game menu item that the passage leads to.)
# 10) List of chest-troops used in this scene {list of strings}. You can access chests by placing them in edit mode.
#     The chest's variation-no is used with this list for selecting which troop's inventory it will access.
#  town_1   Sargoth     #plain
#  town_2   Tihr        #steppe
#  town_3   Veluca      #steppe
#  town_4   Suno        #plain
#  town_5   Jelkala     #plain
#  town_6   Praven      #plain
#  town_7   Uxkhal      #plain
#  town_8   Reyvadin    #plain
#  town_9   Khudan      #snow
#  town_10  Tulga       #steppe
#  town_11  Curaw       #snow
#  town_12  Wercheg     #plain
#  town_13  Rivacheg    #plain
#  town_14  Halmar      #steppe
#  town_15  Yalen
#  town_16  Dhirim
#  town_17  Ichamur
#  town_14_1  Narra
#  town_19  Shariz
#  town_20  Durquba
#  town_21  Ahmerrad
#  town_22  Bariyye
####################################################################################################################

# dhirim
# rivacheg

#
#
#
# native town 21
# town_25_1 town_25_2
# very big 0x0000000030001080000d23480000034e00004b34000059be
# so so 0x0000000030000e0000085e170000034e00004b34000059be
# original 1 0x00000000300010800003e8fa0000034e00004b34000059be
# original 2 0x0000000229600c80000d234800003efe00004b34000059be

scenes = [
  ("random_scene",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[]),
  # ("conversation_scene",0,"encounter_spot", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    # [],[]),
  ("conversation_scene",sf_generate,"none", "none", (-40,-40),(40,40),-100,"0x0000000032c045050002308c0000769a0000644f00004095",
    [],[]),
    
  ("water",0,"none", "none", (-1000,-1000),(1000,1000),-0.5,"0",
    [],[]),
  ("random_scene_steppe",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5, "0x000000023160050000079dea00003efe00004b34000059be",
    [],[], "outer_terrain_steppe"),
  ("random_scene_plain",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000023160050000079dea00003efe00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000024620050000079dea00003efe00004b34000059be",
    [],[], "outer_terrain_snow"),
  ("random_scene_desert",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000023160050000079dea00003efe00004b34000059be",
    [],[], "outer_terrain_desert_b"),
  ("random_scene_steppe_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000230000500000775de0000034e00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),0.0,"0x00000000b42005000004bd320000079a00004b3400007dd2",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002cc600500000775de0000034e00004b34000059be",
    [],[], "outer_terrain_snow"),
  ("random_scene_desert_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000230000500000775de0000034e00004b34000059be",
    [],[], "outer_terrain_desert_b"),
  # ("scene_sea",sf_generate,"none", "none", (0,0),(240,240),-0.5,"0x0000000350114b8000098a5d0000358380001fde0000108b",
    # [],[]),
	
  ("scene_sea",sf_generate,"none", "none", (0,0),(240,240),-0.5,"0x0000000350114b8000098a5d0000358380001fde0000108b",
    [],[], "outer_terrain_sea"),
    
  ("scene_sea_player_nord_vs_generic",sf_generate,"none", "none", (0,0),(240,240),-0.5,"0x0000000350114b8000098a5d0000358380001fde0000108b",
    [],[], "outer_terrain_sea"),
  ("scene_sea_player_nord_vs_eastern",sf_generate,"none", "none", (0,0),(240,240),-0.5,"0x0000000350114b8000098a5d0000358380001fde0000108b",
    [],[], "outer_terrain_sea"),
  ("scene_sea_player_generic_vs_nordic",sf_generate,"none", "none", (0,0),(240,240),-0.5,"0x0000000350114b8000098a5d0000358380001fde0000108b",
    [],[], "outer_terrain_sea"),
  ("scene_sea_player_generic_vs_eastern",sf_generate,"none", "none", (0,0),(240,240),-0.5,"0x0000000350114b8000098a5d0000358380001fde0000108b",
    [],[], "outer_terrain_sea"),
  ("scene_sea_player_eastern_vs_nordic",sf_generate,"none", "none", (0,0),(240,240),-0.5,"0x0000000350114b8000098a5d0000358380001fde0000108b",
    [],[], "outer_terrain_sea"),
  ("scene_sea_player_eastern_vs_generic",sf_generate,"none", "none", (0,0),(240,240),-0.5,"0x0000000350114b8000098a5d0000358380001fde0000108b",
    [],[], "outer_terrain_sea"),

  ("camp_scene",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("camp_scene_horse_track",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("four_ways_inn",sf_generate,"none", "none", (0,0),(120,120),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af",
    [],[], "outer_terrain_town_thir_1"),
  ("test_scene",sf_generate,"none", "none", (0,0),(120,120),-100,"0x0230817a00028ca300007f4a0000479400161992",
    [],[], "outer_terrain_plain"),
  ("quick_battle_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x30401ee300059966000001bf0000299a0000638f", 
    [],[], "outer_terrain_plain"),
  ("quick_battle_2",sf_generate,"none", "none", (0,0),(120,120),-100,"0xa0425ccf0004a92a000063d600005a8a00003d9a", 
    [],[], "outer_terrain_steppe"),
  ("quick_battle_3",sf_generate,"none", "none", (0,0),(120,120),-100,"0x4c6024e3000691a400001b7c0000591500007b52", 
    [],[], "outer_terrain_snow"),
  ("quick_battle_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00001d63c005114300006228000053bf00004eb9", 
    [],[], "outer_terrain_plain"),
  ("quick_battle_5",sf_generate,"none", "none", (0,0),(120,120),-100,"0x3a078bb2000589630000667200002fb90000179c", 
    [],[], "outer_terrain_plain"),
  ("quick_battle_6",sf_generate,"none", "none", (0,0),(120,120),-100,"0xa0425ccf0004a92a000063d600005a8a00003d9a", 
    [],[], "outer_terrain_steppe"),
  ("quick_battle_7",sf_generate,"none", "none", (0,0),(100,100),-100,"0x314d060900036cd70000295300002ec9000025f3",
    [],[],"outer_terrain_plain"),
  ("salt_mine",sf_generate,"none", "none", (-200,-200),(200,200),-100,"0x2a07b23200025896000023ee00007f9c000022a8",  
    [],[], "outer_terrain_steppe"),
  ("novice_ground",sf_indoors,"training_house_a", "bo_training_house_a", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("zendar_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[], "outer_terrain_plain"),
  ("dhorak_keep",sf_generate,"none", "none", (0,0),(120,120),-100,"0x33a7946000028ca300007f4a0000479400161992",
    ["exit"],[]),
  ("reserved4",sf_generate,"none", "none", (0,0),(120,120),-100,"28791",
    [],[]),
  ("reserved5",sf_generate,"none", "none", (0,0),(120,120),-100,"117828",
    [],[]),
  ("reserved6",sf_generate,"none", "none", (0,0),(100,100),-100,"6849",
    [],[]),
  ("reserved7",sf_generate,"none", "none", (0,0),(100,100),-100,"6849",
    [],[]),
  ("reserved8",sf_generate,"none", "none", (0,0),(100,100),-100,"13278",
    [],[]),
  ("reserved9",sf_indoors,"thirsty_lion", "bo_thirsty_lion", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("reserved10",0,"none", "none", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("reserved11",0,"none", "none", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("reserved12",sf_indoors,"thirsty_lion", "bo_thirsty_lion", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("training_ground",sf_generate,"none", "none", (0,0),(120,120),-100,"0x30000500400360d80000189f00002a8380006d91",
    [],["tutorial_chest_1", "tutorial_chest_2"], "outer_terrain_plain_1"),
  ("tutorial_1",sf_indoors,"tutorial_1_scene", "bo_tutorial_1_scene", (-100,-100),(100,100),-100,"0",
    [],[]),
##  ("tutorial_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003a04ce140005e17a000030030000780e00006979",
##    [],[], "outer_terrain_plain"),
  ("tutorial_2",sf_indoors,"tutorial_2_scene", "bo_tutorial_2_scene", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("tutorial_3",sf_indoors,"tutorial_3_scene", "bo_tutorial_3_scene", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("tutorial_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x30000500400360d80000189f00002a8380006d91",
    [],[], "outer_terrain_plain"),
  ("tutorial_5",sf_generate,"none", "none", (0,0),(120,120),-100,"0x3a06dca80005715c0000537400001377000011fe",
    [],[], "outer_terrain_plain"),

  ("tutorial_6",sf_generate,"none", "none", (0,0),(120,120),-100,"0x3a06dca80005715c0000537400001377000011fe",
    [],[], "outer_terrain_plain"),

  ("tutorial_7",sf_generate,"none", "none", (0,0),(120,120),-100,"0x3a06dca80005715c0000537400001377000011fe",
    [],[], "outer_terrain_plain"),

  ("tutorial_8",sf_generate,"none", "none", (0,0),(120,120),-100,"0x3a06dca80005715c0000537400001377000011fe",
    [],[], "outer_terrain_plain"),

  ("tutorial_9",sf_generate,"none", "none", (0,0),(120,120),-100,"0x3a06dca80005715c0000537400001377000011fe",
    [],[], "outer_terrain_plain"),


  ("training_ground_horse_track_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000000337553240004d53700000c0500002a0f80006267",
    [],[], "outer_terrain_plain"),
  ("training_ground_horse_track_2",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000000301553240004d5370000466000002a0f800073f1",
    [],[], "outer_terrain_plain"),
  #Kar
  ("training_ground_horse_track_3",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000000400c12b2000515470000216b0000485e00006928",
    [],[], "outer_terrain_snow"),
  #Steppe
  ("training_ground_horse_track_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000000200b60320004a5290000180d0000452f00000e90",
    [],[], "outer_terrain_steppe"),
  #Plain
  ("training_ground_horse_track_5",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003008208e0006419000000f730000440f00003c86",
    [],[], "outer_terrain_plain"),

  ("training_ground_horse_track_5",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003008208e0006419000000f730000440f00003c86",
    [],[], "outer_terrain_plain"),

  ("training_ground_horse_track_6",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003008208e0006419000000f730000440f00003c86",
    [],[], "outer_terrain_plain"),
    
  ("training_ground_horse_track_7",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003008208e0006419000000f730000440f00003c86",
    [],[], "outer_terrain_plain"),
    
  ("training_ground_horse_track_8",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003008208e0006419000000f730000440f00003c86",
    [],[], "outer_terrain_plain"),

  ("training_ground_horse_track_9",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003008208e0006419000000f730000440f00003c86",
    [],[], "outer_terrain_plain"),
  ("training_ground_horse_track_10",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003008208e0006419000000f730000440f00003c86",
    [],[], "outer_terrain_plain"),
  ("training_ground_horse_track_11",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003008208e0006419000000f730000440f00003c86",
    [],[], "outer_terrain_plain"),
  ("training_ground_horse_track_12",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003008208e0006419000000f730000440f00003c86",
    [],[], "outer_terrain_plain"),
  ("training_ground_horse_track_13",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003008208e0006419000000f730000440f00003c86",
    [],[], "outer_terrain_plain"),
  ("training_ground_horse_track_14",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003008208e0006419000000f730000440f00003c86",
    [],[], "outer_terrain_plain"),
  ("training_ground_horse_track_15",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003008208e0006419000000f730000440f00003c86",
    [],[], "outer_terrain_plain"),
  ("training_ground_horse_track_16",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003008208e0006419000000f730000440f00003c86",
    [],[], "outer_terrain_plain"),
  ("training_ground_horse_track_17",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003008208e0006419000000f730000440f00003c86",
    [],[], "outer_terrain_plain"),
  ("training_ground_horse_track_18",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003008208e0006419000000f730000440f00003c86",
    [],[], "outer_terrain_plain"),

  ("training_ground_ranged_melee_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000001350455c20005194a000041cb00005ae800000ff5",
    [],[], "outer_terrain_plain"),
  ("training_ground_ranged_melee_2",sf_generate,"none", "none", (0,0),(120,120),-100,"0x0000000532c8dccb0005194a000041cb00005ae800001bdd",
    [],[], "outer_terrain_plain"),
  #Kar
  ("training_ground_ranged_melee_3",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000054327dcba0005194a00001b1d00005ae800004d63",
    [],[], "outer_terrain_snow"),
  #Steppe
  ("training_ground_ranged_melee_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000012247dcba0005194a000041ef00005ae8000050af",
    [],[], "outer_terrain_steppe"),
  #Plain
  ("training_ground_ranged_melee_5",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000001324a9cba0005194a000041ef00005ae800003c55",
    [],[], "outer_terrain_plain"),

  ("training_ground_ranged_melee_6",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000001324a9cba0005194a000041ef00005ae800003c55",
    [],[], "outer_terrain_plain"),

  ("training_ground_ranged_melee_7",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000001324a9cba0005194a000041ef00005ae800003c55",
    [],[], "outer_terrain_plain"),

  ("training_ground_ranged_melee_8",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000001324a9cba0005194a000041ef00005ae800003c55",
    [],[], "outer_terrain_plain"),

  ("training_ground_ranged_melee_9",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000001324a9cba0005194a000041ef00005ae800003c55",
    [],[], "outer_terrain_plain"),
  ("training_ground_ranged_melee_10",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000001324a9cba0005194a000041ef00005ae800003c55",
    [],[], "outer_terrain_plain"),
  ("training_ground_ranged_melee_11",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000001324a9cba0005194a000041ef00005ae800003c55",
    [],[], "outer_terrain_plain"),
  ("training_ground_ranged_melee_12",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000001324a9cba0005194a000041ef00005ae800003c55",
    [],[], "outer_terrain_plain"),
  ("training_ground_ranged_melee_13",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000001324a9cba0005194a000041ef00005ae800003c55",
    [],[], "outer_terrain_plain"),
  ("training_ground_ranged_melee_14",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000001324a9cba0005194a000041ef00005ae800003c55",
    [],[], "outer_terrain_plain"),
  ("training_ground_ranged_melee_15",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000001324a9cba0005194a000041ef00005ae800003c55",
    [],[], "outer_terrain_plain"),
  ("training_ground_ranged_melee_16",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000001324a9cba0005194a000041ef00005ae800003c55",
    [],[], "outer_terrain_plain"),
  ("training_ground_ranged_melee_17",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000001324a9cba0005194a000041ef00005ae800003c55",
    [],[], "outer_terrain_plain"),
  ("training_ground_ranged_melee_18",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000001324a9cba0005194a000041ef00005ae800003c55",
    [],[], "outer_terrain_plain"),

  ("zendar_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    ["the_happy_boar","","zendar_merchant"],[], "outer_terrain_plain_1"),
#  ("zendar_center",0,"sargoth_square", "bo_sargoth_square", (-24,-22),(21,13),-100,"0",
#    ["the_happy_boar","","zendar_merchant"],[]),
  ("the_happy_boar",sf_indoors,"interior_town_house_f", "bo_interior_town_house_f", (-100,-100),(100,100),-100,"0",
    ["zendar_center"],["zendar_chest"]),
  ("zendar_merchant",sf_indoors,"interior_town_house_i", "bo_interior_town_house_i", (-100,-100),(100,100),-100,"0",
    [],[]),

# Tvern names:
  #the shy monkey
  #the singing pumpkin
  #three swords
  #red stag
  #the bard's corner


#interior_tavern_a
#  town_1   Sargoth     #plain
#  town_2   Tihr        #plain
#  town_3   Veluca      #steppe
#  town_4   Suno        #plain  
#  town_5   Jelkala     #plain
#  town_6   Praven      #plain
#  town_7   Uxkhal      #plain
#  town_8   Reyvadin    #plain
#  town_9   Khudan      #snow
#  town_10  Tulga       #steppe
#  town_11  Curaw       #snow
#  town_12  Wercheg     #plain
#  town_13  Rivacheg    #plain
#  town_14  Halmar      #steppe

  # native town 21
  ("town_arab_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x0000000150051a800004190400003f8c0000352b000014d8",
    [],[],"outer_terrain_desert_b"),    
  ("town_arab_castle",sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_arab_prison",sf_indoors,"interior_prison_n", "bo_interior_prison_n", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_arab_walls",sf_generate,"none", "none", (0,0),(100,100),500,"0x0000000150051a800004190400003f8c0000352b000014d8",
    [],[],"outer_terrain_desert_b"),
  ("town_arab_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000150051a800004190400003f8c0000352b000014d8",
    [],[],"0"),
  ("town_arab_tavern",sf_indoors, "interior_town_house_steppe_g", "bo_interior_town_house_steppe_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_arab_store",sf_indoors, "interior_town_house_steppe_g", "bo_interior_town_house_steppe_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_arab_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_desert_b"),
  ###
  
  ("town_arab_castle_west",sf_indoors, "arabian_interior_keep_a_new", "bo_arabian_interior_keep_a_new", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_castle_crusade_1",sf_indoors, "interior_castle_i_new", "bo_interior_castle_i_new", (-100,-100),(100,100),-100,"0",
    ["exit"],[]), #town 4
  ("town_castle_crusade_2",sf_indoors, "interior_castle_q_new", "bo_interior_castle_q_new", (-100,-100),(100,100),-100,"0",
    ["exit"],[]), #11
	
  #native town 16
  ("town_euro_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130001887000334d0000073ed00004f1a00007a35",
    [],[],"outer_terrain_steppe"),        
  ("town_euro_castle",sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_euro_tavern",sf_indoors, "interior_tavern_b", "bo_interior_tavern_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_euro_store",sf_indoors, "interior_town_house_i", "bo_interior_town_house_i", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_euro_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_euro_prison",sf_indoors,"interior_prison_k", "bo_interior_prison_k", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  # ("town_euro_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001c98d0005b56d000072a70000240a00001e09",
    # [],[],"outer_terrain_steppe"),
  # ("town_euro_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300005008006b1b000007dd800006630000031bd",
    # [],[],"outer_terrain_plain"),
    # ugh
    # ("town_euro_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300005008006b1b000007dd800006630000031bd",
    # [],[],"outer_terrain_steppe"),

    #native
    ("town_euro_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001c98d0005b56d000072a70000240a00001e09",
    [],[],"outer_terrain_steppe"),

  # ("town_euro_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005004003ccf600005d24800076620000238e",
    # [],[],"outer_terrain_plain"),
  ("town_euro_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_steppe"),
  ###
  
 ("town_italy_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200011af00065192000067110000688300003435",
    [],[],"outer_terrain_plain"),
 ("town_italy_castle",sf_indoors, "italy_interior", "bo_italy_interior", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
 ("town_italy_walls_new",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001200005010006b9b00000605d00004ab10000537e",
    [],[],"outer_terrain_plain"),
  ("town_italy_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001200005010006b9b00000605d00004ab10000537e",
    [],[],"outer_terrain_steppe"),

  # native town 11
  ("town_nordic_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x400790b20002c8b0000050d500006f8c00006dbd",
    [],[],"outer_terrain_snow_mountain"),
  ("town_nordic_castle",sf_indoors, "interior_castle_i", "bo_interior_castle_i", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  # town 3
  ("town_nordic_tavern",sf_indoors, "interior_rhodok_houses_b", "bo_interior_rhodok_houses_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_nordic_store",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_nordic_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x40001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_snow_mountain"),
  ("town_nordic_prison",sf_indoors,"dungeon_a", "bo_dungeon_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_nordic_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000140015033000651900000159f0000619800006af6",
    [],[],"outer_terrain_snow_mountain"),
  ("town_nordic_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x400211130001e07800002ad400001172000035c4",
    [],[],"outer_terrain_snow_mountain"),
	
  ("town_nordic_center_new",sf_generate,"none", "none",(0,0),(100,100),-100,"0x0000000230000500800789e60000196800000fb600002ad5",
    [],[],"outer_terrain_snow_mountain"),
  ("town_nordic_walls_new",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230000500800789e60000196800000fb600002ad5",
    [],[],"outer_terrain_snow_mountain"),
  ###
  
  # native town 2
  ("town_baltic_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000003300045000004e93d000053100000628200007e05",
    [],[],"outer_terrain_plain"),
  ("town_baltic_castle",sf_indoors,"viking_interior_keep_a", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("town_baltic_tavern",sf_indoors,"viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[],"outer_terrain_plain"),
  ("town_baltic_store",sf_indoors,"viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_baltic_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_baltic_prison",sf_indoors,"interior_prison_cell_a", "bo_interior_prison_cell_a", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_baltic_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000003300045000004e93d000053100000628200007e05",
    [],[],"outer_terrain_plain"),
  ("town_baltic_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
  ###
  
  # native town 10
  ("town_mongol_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000000200016da000364d9000060f500007591000064e7",
    [],[],"outer_terrain_steppe"),
  ("town_mongol_castle",sf_generate, "none", "none", (-100,-100),(100,100),-100,"0x00000007300005000002308c00004a840000624700004fda",
    ["exit"],["castle_1_seneschal"]),
  ("town_mongol_tavern",sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_mongol_store",sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_mongol_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_steppe"),
  ("town_mongol_prison",sf_indoors,"interior_prison_o", "bo_interior_prison_o", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_mongol_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200011af00065192000067110000688300003435",
    [],[],"outer_terrain_steppe"),
  ("town_mongol_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000420000500000334ce00001d1100003d0600000d27",
    [],[],"outer_terrain_steppe"),
  ("town_mongol_room",sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ###
  
  # native town 15
  ("town_eastern_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x0000000030024e108003fd0100007bd300006c31000061aa",
    [],[],"outer_terrain_plain"),
  ("town_eastern_castle",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("town_eastern_tavern",sf_indoors, "interior_rhodok_houses_d", "bo_interior_rhodok_houses_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_eastern_store",sf_indoors, "interior_rhodok_houses_b", "bo_interior_rhodok_houses_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_eastern_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_eastern_prison",sf_indoors,"interior_prison_f", "bo_interior_prison_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_eastern_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030024e108003fd0100007bd300006c31000061aa",
    [],[],"outer_terrain_plain"),
  ("town_eastern_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_steppe"),
  ###

  #rip from e1200 - nuernberg
  ("nuernberg_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300491830004a529000036230000312a00003653",
    [],[],"outer_terrain_plain"),        
  ("nuernberg_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300491830004a529000036230000312a00003653",
    [],[],"outer_terrain_plain"),        
  ("nuernberg_castle",sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("nuernberg_tavern",sf_indoors, "interior_tavern_b", "bo_interior_tavern_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("nuernberg_store",sf_indoors, "interior_town_house_i", "bo_interior_town_house_i", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("nuernberg_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("nuernberg_prison",sf_indoors,"interior_prison_k", "bo_interior_prison_k", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
# CASTLES #

  # native castle 35
  # ("castle_walls_euro",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130031be30006f9bc00000aae00000fb80000243f",
    # [],[],"outer_terrain_plain"),
  ("castle_walls_euro",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005004003ccf600005d24800076620000238e",
    [],[],"outer_terrain_plain"),
  ("castle_interior_euro",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_prison_euro",sf_indoors,"interior_prison_f", "bo_interior_prison_f", (-100,-100),(100,100),-100,"0",
    [],[]),

  # castle 9
  ("castle_walls_iberia",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0048e000004d93700004f91000065980000229b",
    [],[],"outer_terrain_castle_9"),
  ("castle_interior_iberia",sf_indoors, "interior_castle_l", "bo_interior_castle_l", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_prison_iberia",sf_indoors,"interior_prison_d", "bo_interior_prison_d", (-100,-100),(100,100),-100,"0",
    [],[]),

  # castle 11
  ("castle_walls_nordic",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030044e900003dd02000077b20000400100005697",
    [],[],"outer_terrain_plain"),
  ("castle_interior_nordic",sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_prison_nordic",sf_indoors,"interior_prison_k", "bo_interior_prison_k", (-100,-100),(100,100),-100,"0",
    [],[]),

  # castle 4
  ("castle_walls_eastern",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030044e900003dd02000077b20000400100005697",
    [],[],"outer_terrain_plain"),
  ("castle_interior_eastern",sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_prison_eastern",sf_indoors,"interior_prison_l", "bo_interior_prison_l", (-100,-100),(100,100),-100,"0",
    [],[]),

  # castle 8
  ("castle_walls_italy",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300d060900036cd70000295300002ec9000025f3",
    [],[],"outer_terrain_plain"),
  ("castle_interior_italy",sf_indoors, "interior_castle_t", "bo_interior_castle_t", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_prison_italy",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    [],[]),

  # castle 40
  ("castle_walls_mongol",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000012007985300055550000064d500005c060000759e",
    [],[],"outer_terrain_steppe"),
  ("castle_interior_mongol",sf_indoors, "interior_castle_g_square_keep", "bo_interior_castle_g_square_keep", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_prison_mongol",sf_indoors,"interior_prison_n", "bo_interior_prison_n", (-100,-100),(100,100),-100,"0",
    [],[]),

  # castle 42
  # ("castle_walls_arab",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000005a039fb20005114400004f690000467a00004400",
    # [],[],"0"),
  # ("castle_walls_arab",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000005a039fb20005114400004f690000467a00004400",
    # [],[],"0"),
  ("castle_walls_arab",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005004003ccf600005d24800076620000238e",
    [],[],"0"),
  ("castle_interior_arab",sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_prison_arab",sf_indoors,"interior_prison_o", "bo_interior_prison_o", (-100,-100),(100,100),-100,"0",
    [],[]),

	
  # Kernave
  ("walls_kernave",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300005000005715a000030a800000c2d00005510",
    [],[],"outer_terrain_plain"),
    
  # Moscow
  ("walls_moscow",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013005213200077dda0000733300002edf000052ba",
    [],[],"outer_terrain_snow"),
  ("interior_moscow",sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),

  # Motte and bailey 1
  # ("walls_motte_bailey_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230025b8d0006459400006a3700002adb00007091",
    # [],[],"outer_terrain_plain"),
  ("walls_motte_bailey_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023007b23200049d2a00003c37000040ef000037cd",
    [],[],"outer_terrain_castle_9"),
  ("interior_motte_bailey_2",sf_indoors, "interior_castle_y", "bo_interior_castle_y", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("prison_motte_bailey_2",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),

  # Motte and bailey 2
  ("walls_motte_bailey_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300658bc0007bded000025520000093800006114",
    [],[], "outer_terrain_plain"),
  ("interior_motte_bailey_1",sf_indoors, "interior_castle_y", "bo_interior_castle_y", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("prison_motte_bailey_1",sf_indoors,"interior_prison_b", "bo_interior_prison_b", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("walls_tonbridge",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030044e900003dd02000077b20000400100005697",
    [],[],"outer_terrain_plain"),

  ("walls_pevensey",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013006199a0004e5370000494f000028fc00006cf6",
    [],[],"outer_terrain_plain"),

  ("walls_york",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013005213200077dda0000733300002edf000052ba",
    [],[],"outer_terrain_plain"),

  ("walls_carlisle",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130025cb20006097f00005b1400000e2f00005fd9",
    [],[],"outer_terrain_plain"),

  ("walls_llansteffan",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b009723200059d6800005f4f0000757f000069cd",
    [],[],"outer_terrain_plain"),
    
  ("walls_beaumaris",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130021f63000721ca000055be000079d90000156d",
    [],[],"outer_terrain_plain"),
    
  ("walls_conwy",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013007b232000715c50000084c00001b5b000018ec",
    [],[],"outer_terrain_plain"),    

  ("walls_wenden",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001b0000500000725ca000058880000728e00001ac1",
    [],[],"outer_terrain_plain"),    
    
  ("walls_arensburg",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130000500000715c30000572600002a00000013ce",
    [],[],"outer_terrain_plain"),    

  ("walls_dorpat",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300005010008320c00001f5c0000732500007d80",
    [],[],"outer_terrain_plain"),    

  ("walls_tunsberg",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300005008006b1b000007dd800006630000031bd",
    [],[],"outer_terrain_plain"),    
	
  ("walls_munchen",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300005008006b1b000007dd800006630000031bd",
    [],[],"outer_terrain_plain"),    
	
  ("walls_hohenburg",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300005008006b1b000007dd800006630000031bd",
    [],[],"outer_terrain_plain"),    

  ("walls_vladimir",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000033000050000058dd400000eed00006ce200002910",
    [],[],"outer_terrain_plain"),
    
  ("walls_vladimir_snow",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000033000050000058dd400000eed00006ce200002910",
    [],[],"outer_terrain_snow"),
#!!Villages !!#

  # drtomas
  ("village_iberia",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000012007a83200049924000049bd00001f7a00006c57",
    [],[],"outer_terrain_steppe"),
  
  # drtomas
  ("village_euro",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300005008006b1b000007dd800006630000031bd",
    [],[],"outer_terrain_plain"),
  
  # drtomas
  ("village_eastern",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300a4563800a92a6000052450000152200007e28",
    [],[],"outer_terrain_plain"),

  # drtomas
  ("village_eastern2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002400a4563800a92a6000052450000152200007e28",
    [],[],"outer_terrain_snow"),
	
  # drtomas
  ("village_nordic",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000014007b26300059563000051e000001aa4000034ee",
    [],[],"outer_terrain_snow_mountain"),

  # drtomas
  ("village_italy",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130069b270004dd390000689b00002d3b00001876",
    [],[],"outer_terrain_steppe"),

  # drtomas - obsolete
  # ("village_byz2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130069b270004dd390000689b00002d3b00001876",
    # [],[],"outer_terrain_steppe"),	
  # ugh
  ("village_byz",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000009de7900000f300000446800005b1f",
    [],[],"outer_terrain_steppe"),		
	
  # drtomas
  ("village_mongol",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000006b1aa000002e100000d1000003d96",
    [],[],"outer_terrain_steppe"),
  ("village_mongol_plains",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000006b1aa000002e100000d1000003d96",
    [],[],"outer_terrain_plain"),
  ("village_mongol_snow",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000006b1aa000002e100000d1000003d96",
    [],[],"outer_terrain_snow"),
  ("village_mongol_desert",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000006b1aa000002e100000d1000003d96",
    [],[],"0"),

  # drtomas
  ("village_arab",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500410320005a96800006b5300004edc00000d11",
    [],[],"0"),

	#Ugh 
  ("village_euro2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300005008006b1b000007dd800006630000031bd",
    [],[],"outer_terrain_plain"),
	
	#Ugh - fjord
  ("village_nordic2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300005008006b1b000007dd800006630000031bd",
    [],[],"outer_terrain_plain"),
	
	#Ugh - Seaside
  ("village_nordic3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300005008006b1b000007dd800006630000031bd",
    [],[], 0),

	#warbastard - england
  ("village_england",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000007d1f1000068a500005daa00003eea",
    [],[],"outer_terrain_plain"),

	
  
  ("field_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000033a059a5a0009525600002005000060e300001175",
    [],[],"outer_terrain_plain"),
  ("field_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000033a079a3f000a3a8000006dfd000030a100006522",
    [],[],"outer_terrain_steppe"),
  ("field_3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30054da28004050000005a76800022aa00002e3b",
    [],[],"outer_terrain_steppe"),
  ("field_4",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30054da28004050000005a76800022aa00002e3b",
    [],[],"outer_terrain_steppe"),
  ("field_5",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30054da28004050000005a76800022aa00002e3b",
    [],[],"outer_terrain_steppe"),

  ("test2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b0078cb20003fd0000005e480000288c0000286f",
    [],[],"outer_terrain_steppe"),

    ("test3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b00511d98004b12e0000039f00004e6300005c7d",
    [],[],"outer_terrain_plain"),

# multiplayer
  ("multi_scene_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),
  ("multi_scene_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000012002a0b20004992700006e54000007fe00001fd2",
    [],[],"outer_terrain_steppe"),
  ("multi_scene_3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002e0b20005154500006e540000235600007b55",
    [],[],"outer_terrain_plain"),
  ("multi_scene_4",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300659630003c8f300003ca000006a8900003c89",
    [],[],"outer_terrain_plain"),
  ("multi_scene_5",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
    [],[],"outer_terrain_plain"),
  ("multi_scene_6",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300494b200048524000059e80000453300001d32",
    [],[],"outer_terrain_plain"),
  ("multi_scene_7",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130010e0e0005fd84000011c60000285b00005cbe",
    [],[],"outer_terrain_plain"),
  ("multi_scene_8",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000020004db18004611400005c918000397b00004c2e",
    [],[],"outer_terrain_plain"),
  ("multi_scene_9",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000400032320003c0f300001f9e000011180000031c",   
    [],[],"outer_terrain_snow"),
  ("multi_scene_10",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003009cde1000599630000423b00005756000000af",
    [],[],"outer_terrain_plain"),
  ("multi_scene_11",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af",
    [],[],"outer_terrain_plain"),
  ("multi_scene_12",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013003d7e30005053f00003b4e0000146300006e84",
    [],[],"outer_terrain_beach"),
  ("multi_scene_13",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),
  ("multi_scene_14",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000040000c910003e8fa0000538900003e9e00005301",
    [],[],"outer_terrain_snow"),
  ("multi_scene_15",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000500b1d158005394c00001230800072880000018f",
    [],[],"0"),       
  ("multi_scene_16",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000d007abd20002c8b1000050c50000752a0000788c",
    [],[],"0"),
  ("multi_scene_17",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_plain"),
  ("multi_scene_18",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x00000000b00037630002308c00000c9400005d4c00000f3a",
    [],[],"outer_terrain_plain"),
  
  ("random_multi_plain_medium",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000001394018dd000649920004406900002920000056d7",
    [],[], "outer_terrain_plain"),
  ("random_multi_plain_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000013a001853000aa6a40004406900002920001e4f81",
    [],[], "outer_terrain_plain"),
  ("random_multi_steppe_medium", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0,0),(100, 100), -0.5, "0x0000000128601ae300063d8f0004406900002920001e4f81",
    [],[], "outer_terrain_steppe"),
  ("random_multi_steppe_large", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0,0),(100, 100), -0.5, "0x000000012a00d8630009fe7f0004406900002920001e4f81",
    [],[], "outer_terrain_steppe"),

  ("multiplayer_maps_end",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),

  ("wedding",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0", [],[]),
  ("lair_steppe_bandits",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000200c69ac80043d0d0000556b0000768400003ea9",
    [],[],"outer_terrain_steppe"), #a box canyon with a spring? -tents...
  ("lair_taiga_bandits",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000004c079c3e000499280000420f0000495d000048d6",
    [],[],"outer_terrain_snow"),
  ("lair_desert_bandits",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000005024cd120005595400003882000037a90000673e",
    [],[],"0"), #an encampment in the woods
  ("lair_forest_bandits",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b00326d90003ecfb0000657e0000213500002461",
    [],[],"outer_terrain_plain"), #a cliffside ledge or cave overlooking a valley
  ("lair_mountain_bandits",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000200434070004450c000022bf00006ad6000060ed",
    [],[],"outer_terrain_steppe"),
  ("lair_sea_raiders",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b00562e200040900000063f40000679f00006cda",
    [],[],"sea_outer_terrain_1"), #the longships beached on a hidden cove


  ("quick_battle_scene_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000023002dee300045d1d000001bf0000299a0000638f", 
    [],[], "outer_terrain_plain"),
  ("quick_battle_scene_2",sf_generate,"none", "none", (0,0),(120,120),-100,"0x0000000250001d630005114300006228000053bf00004eb9", 
    [],[], "0"),
  ("quick_battle_scene_3",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000023002b76300046d2400000190000076300000692a", 
    [],[], "outer_terrain_plain"),
  ("quick_battle_scene_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000025a00f23700057d5f00006d6a000050ba000036df", 
    [],[], "0"),
  ("quick_battle_scene_5",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000012007985300055550000064d500005c060000759e",
    [],[],"outer_terrain_plain"),
  ("quick_battle_maps_end",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),

  ("tutorial_training_ground",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003000050000046d1b0000189f00002a8380006d91",
    [],[], "outer_terrain_plain"),
    
  ("town_1_room",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_14_1_room",sf_indoors,"viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_11_2_room",sf_indoors,"viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_4_1_room",sf_indoors,"viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("town_10_1_room",sf_indoors, "interior_town_house_d", "bo_interior_town_house_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_42_room",sf_indoors, "interior_town_house_d", "bo_interior_town_house_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),


  ("town_30_room",sf_indoors, "interior_town_house_d", "bo_interior_town_house_d", (-100,-100),(100,100),-100,"0",
  ["exit"],[]),

  ("town_40_room",sf_indoors, "interior_town_house_d", "bo_interior_town_house_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  

  ("town_9_room",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_13_room",sf_indoors, "interior_house_b", "bo_interior_house_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),    
    
  ("town_5_room",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_6_1_room",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("town_21_room",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),


  ("town_29_room",sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),


  ("meeting_scene_steppe",sf_generate,"none", "none", (-40,-40),(40,40),-100,"0x0000000023410500000258960000238e000013db00004d3e",
    [],[]),
  ("meeting_scene_plain",sf_generate,"none", "none", (-40,-40),(40,40),-100,"0x0000000032c045050002308c0000769a0000644f00004095",
    [],[]),
  ("meeting_scene_snow",sf_generate,"none", "none", (-40,-40),(40,40),-100,"0x000000004336cf260002308c00000f6b00007b6a00007656",
    [],[]),
  ("meeting_scene_desert",sf_generate,"none", "none", (-40,-40),(40,40),-100,"0x00000000500b55880002308c0000262e000075530000667f",
    [],[]),
  ("meeting_scene_steppe_forest",sf_generate,"none", "none", (-40,-40),(40,40),-100,"0x00000000aa0791b20002308c00006f9400000ab5000007fa",
    [],[]),
  ("meeting_scene_plain_forest",sf_generate,"none", "none", (-40,-40),(40,40),-100,"0x00000000b2878bb20002308c00006ad30000401500004a5a",
    [],[]),
  ("meeting_scene_snow_forest",sf_generate,"none", "none", (-40,-40),(40,40),-100,"0x00000000cc678eb20002308c0000526a000030020000778f",
    [],[]),
  ("meeting_scene_desert_forest",sf_generate,"none", "none", (-40,-40),(40,40),-100,"0x00000000da079cb20002308c00005c51000030a400001520",
    [],[]),
  ("meeting_scene_sea",sf_generate,"none", "none", (-40,-40),(40,40),-100,"0x00000000500b55880002308c0000262e000075530000667f",
    [],[]),
    
  # ("meeting_scene_steppe",0,"ch_meet_steppe_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    # [],[]),
  # ("meeting_scene_plain",0,"ch_meet_plain_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    # [],[]),
  # ("meeting_scene_snow",0,"ch_meet_snow_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    # [],[]),
  # ("meeting_scene_desert",0,"ch_meet_desert_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    # [],[]),
  # ("meeting_scene_steppe_forest",0,"ch_meet_steppe_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    # [],[]),
  # ("meeting_scene_plain_forest",0,"ch_meet_plain_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    # [],[]),
  # ("meeting_scene_snow_forest",0,"ch_meet_snow_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    # [],[]),
  # ("meeting_scene_desert_forest",0,"ch_meet_desert_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    # [],[]),

  ("enterprise_tannery",sf_generate,"ch_meet_steppe_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0x000000012004480500040902000041cb00005ae800000ff5",
    [],[]),
  ("enterprise_winery",sf_indoors,"winery_interior", "bo_winery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_mill",sf_indoors,"mill_interior", "bo_mill_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_smithy",sf_indoors,"smithy_interior", "bo_smithy_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_dyeworks",sf_indoors,"weavery_interior", "bo_weavery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_linen_weavery",sf_indoors,"weavery_interior", "bo_weavery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_wool_weavery",sf_indoors,"weavery_interior", "bo_weavery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_brewery",sf_indoors,"brewery_interior", "bo_brewery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_oil_press",sf_indoors,"oil_press_interior", "bo_oil_press_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
    
  ("walls_treyden",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013000050000078de5000062850000521200006fde",
    [],[],"outer_terrain_plain"),    

  ("pagan_stronghold_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002b000865b8007bded0000255200002de200006114",
    [],[],"outer_terrain_plain"),    

  ("walls_lemsahl",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300005000008020200000131000072ef00004e00",
    [],[],"outer_terrain_plain"),

  ("walls_marienwerder",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300005000006ddb700000dfc0000798300005855",
    [],[],"outer_terrain_plain"),

  ("walls_seiminiskeliai",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000003300005000007c1f200001bf400007f4500005810",
    [],[],"outer_terrain_plain"),

  ("walls_taurapilis",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000033000050000089e230000523900005daa00005f17",
    [],[],"outer_terrain_plain"),

  ("walls_taurapilis_snow",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000033000050000089e230000523900005daa00005f17",
    [],[],"outer_terrain_snow"),	
	
  ("walls_seiminiskeliai_snow",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000003300005000007c1f200001bf400007f4500005810",
    [],[],"outer_terrain_snow"),
	
  ("walls_balt",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000033000050000089e230000523900005daa00005f17",
    [],[],"outer_terrain_plain"),	
	
  ("walls_mann",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005004003ccf600005d24800076620000238e",
    [],[], 0),
  ("walls_scot",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005004003ccf600005d24800076620000238e",
    [],[], 0),
	
  ("acre_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000150051a800004190400003f8c0000352b000014d8",
    [],[],"0"),
  ("acre_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x0000000150051a800004190400003f8c0000352b000014d8",
    [],[],"0"),    

  ("walls_mansoura",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000005a039fb20005114400004f690000467a00004400",
    [],[],"0"),

  ("walls_lublin",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000003300005800007ddf9000075e4000061fe000060b2",
    [],[],"outer_terrain_plain"),
	
  ("walls_ladoga",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000003c00005000007a9ea00006843000060b100006db2",
    [],[],"outer_terrain_snow"),

  ("london_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000009de7900000f300000446800005b1f",
  [],[],"outer_terrain_plain"),
  ("london_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000009de7900000f300000446800005b1f",
    [],[],"outer_terrain_plain"),
	
  ("vilnius_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000003300005000008c230000041540000681800000709",
    [],[],"outer_terrain_plain"),
  ("vilnius_walls",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000003300005000008c230000041540000681800000709",
    [],[],"outer_terrain_plain"),    
	
  ("smyrna_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000003200000000009d2740000318f00005ae800003c55",
    [],[],"outer_terrain_plain"),
  ("smyrna_walls",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000003200000000009d2740000318f00005ae800003c55",
    [],[],"outer_terrain_plain"),    	

  ("aleppo_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000150051a800004190400003f8c0000352b000014d8",
    [],[],"outer_terrain_desert_b"),	
  ("aleppo_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000150051a800004190400003f8c0000352b000014d8",
    [],[],"outer_terrain_desert_b"),	
	
  #stevehoos
  ("center_saphet",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000007a0000500000b92eb00006c8c800050dc00006a7b",
    [],[],"outer_terrain_plain"),	
  ("walls_saphet",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000007a0000500000b92eb00006c8c800050dc00006a7b",
    [],[],"outer_terrain_plain"),	
	
  #stevehoos
  ("center_jerusalem",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000003d0000500000c5f17000072a40000715400005901",
    [],[],"outer_terrain_plain"),	
  ("walls_jerusalem",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000003d0000500000c5f17000072a40000715400005901",
    [],[],"outer_terrain_plain"),	
	
  #stevehoos
  ("center_antioch",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000006a0004708000b7ee30000320900000e4400006e01",
    [],[],"outer_terrain_plain"),	
  ("walls_antioch",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000006a0004708000b7ee30000320900000e4400006e01",
    [],[],"outer_terrain_plain"),	
	
  #stevehoos
  ("walls_karak",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000075003d8c04008fe16000044970000789700005381",
    [],[],"outer_terrain_desert_b"),	
	
  #Halgrim
  ("walls_pskov",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000751d400000eed00006ce200002910",
    [],[],"outer_terrain_plain"),	
	
  #Halgrim
  ("walls_opole",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000033000050000055529000027100000758200000b0c",
    [],[],"outer_terrain_plain"),	
	
  #mike - vonafton
  ("castle_cold",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000040000000000fffff000041ef00005ae800003c55",
    [],[],"outer_terrain_snow"),
  #mike - vonafton
  ("walls_lake",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000040000000000fffff000041ef00005ae800003c55",
    [],[],"outer_terrain_snow"),
  #mike - vonafton
  ("walls_brandenburg",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000a0000500000d2348000075860000097200001e2f",
    [],[],"outer_terrain_plain"),
  #mike - vonafton
  ("walls_montefort",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000020000000000fffff000041ef00005ae800003c55",
    [],[],"outer_terrain_steppe"),
	
  ("york_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000007b9ee00000715000022d200004168",
    [],[],"outer_terrain_plain"),	
  ("york_walls",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000000300005000007b9ee00000715000022d200004168",
    [],[],"outer_terrain_plain"),    
	
  ("to_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130001887000334d0000073ed00004f1a00007a35",
    [],[],"outer_terrain_plain"),    	
  ("to_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130001887000334d0000073ed00004f1a00007a35",
    [],[],"outer_terrain_plain"),   
  ("to_interior",sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),	

  ("constantinople_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130001887000334d0000073ed00004f1a00007a35",
    [],[],"outer_terrain_steppe"),    
	
  ("venice_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000200016da000364d9000060f500007591000064e7",
    [],[],"0"),    
	
  ("town_euro_center_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130001887000334d0000073ed00004f1a00007a35",
    [],[],"outer_terrain_steppe"),    
  ("town_euro_center_3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130001887000334d0000073ed00004f1a00007a35",
    [],[],"outer_terrain_steppe"),    
  ("town_euro_center_4",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130001887000334d0000073ed00004f1a00007a35",
    [],[],"outer_terrain_steppe"),	
	
  ("aachen_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300005008006b1b000007dd800006630000031bd",
    [],[],"outer_terrain_plain"),
  ("aachen_walls",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000002300005008006b1b000007dd800006630000031bd",
    [],[],"outer_terrain_plain"),    
	
  ("bristol_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x000000003000050000052546000061fa0000501900000598",
    [],[], 0),  	
  ("bristol_walls",sf_generate,"none", "none",(0,0),(100,100),-100,"0x000000003000050000055154000051000000293700005882",
    [],[], 0),  
	
  ("oslo_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300005008006b1b000007dd800006630000031bd",
    [],[],"outer_terrain_snow"),

  ("den_bosch",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130069b270004dd390000689b00002d3b00001876",
    [],[],"outer_terrain_plain"),

  ("walls_arwa",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002dee300045d1d000001bf0000299a0000638f",
    [],[],"outer_terrain_plain"),

  ("walls_krak",sf_generate,"none", "none", (0,0),(100,100),-500,"0x000000013007b232000715c50000084c00001b5b000018ec",
    [],[],"outer_terrain_plain"),
    
  ("walls_generic_french",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005004003ccf600005d24800076620000238e",
    [],[],"outer_terrain_plain"),

  ("walls_hedingham",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300658bc0007bded000025520000093800006114",
    [],[],"outer_terrain_plain"),

  ("rus_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000003300005000008c230000041540000681800000709",
    [],[],"outer_terrain_plain"),	
  ("rus_snow_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000003400005000008c230000041540000681800000709",
    [],[],"outer_terrain_snow"),	

  ("rus_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000003300005000008c230000041540000681800000709",
    [],[],"outer_terrain_plain"),	
  ("rus_snow_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000003400005000008c230000041540000681800000709",
    [],[],"outer_terrain_snow"),	
	
  ("walls_ragnhildsholmen",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b0000500000a556a00006a7700006d2a00002be8",
    [],[],"outer_terrain_plain"),		
	
  ("byzantine_walls_belfry",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000020024e100003fd0100007bd300006c31000061aa ",
    [],[],"outer_terrain_steppe"),		
  ("byzantine_walls_one_ladder",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000020024e100003fd0100007bd300006c31000061aa ",
    [],[],"outer_terrain_steppe"),		
  ("byzantine_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000020024e100003fd0100007bd300006c31000061aa ",
    [],[],"outer_terrain_steppe"),		
	
  ("player_castle_central_Europe_tier1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000003b00005010004b52d00006d3000003879000009f9",
    [],[],"outer_terrain_plain"),
  ("player_castle_central_Europe_tier2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000003b00005010004b52d00006d3000003879000009f9",
    [],[],"outer_terrain_plain"),
  ("player_castle_central_Europe_tier3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000003b00005010004b52d00006d3000003879000009f9",
    [],[],"outer_terrain_plain"),
	
  ("player_castle_french_tier1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002b00005010004b52d00006d3000003879000009f9",
    [],[],"outer_terrain_plain"),
  ("player_castle_french_tier2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002b00005010004b52d00006d3000003879000009f9",
    [],[],"outer_terrain_plain"),
  ("player_castle_french_tier3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002b00005010004b52d00006d3000003879000009f9",
    [],[],"outer_terrain_plain"),
	
  ("player_castle_desert_tier1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002a00005010004b52d00006d3000003879000009f9",
    [],[],"outer_terrain_desert_b"),
  ("player_castle_desert_tier2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002a00005010004b52d00006d3000003879000009f9",
    [],[],"outer_terrain_desert_b"),
  ("player_castle_desert_tier3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002a00005010004b52d00006d3000003879000009f9",
    [],[],"outer_terrain_desert_b"),

  ("castle_player_nordic_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000024c6a4ce3000475190000524500005e1f00007e28",
    [],[],"outer_terrain_snow_mountain"),
  ("castle_player_nordic_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002404a4ce3000475190000524500005e1f00007e28",
    [],[],"outer_terrain_snow_mountain"),
  ("castle_player_nordic_3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002404a4ce3000475190000524500005e1f00007e28",
    [],[],"outer_terrain_snow_mountain"),
	
	##Imports from native
	##Euro
  ("castle_1_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30054da28004050000005a76800022aa00002e3b",
    [],[],"outer_terrain_steppe"),
  ("castle_1_interior",sf_indoors, "dungeon_entry_a", "bo_dungeon_entry_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_1_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    [],[]),
	
  ("castle_3_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030044e900003dd02000077b20000400100005697",
    [],[],"outer_terrain_plain"),
  ("castle_3_interior",sf_indoors, "interior_castle_m", "bo_interior_castle_m", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_3_prison",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    [],[]),
	
  ("castle_11_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030044e900003dd02000077b20000400100005697",
    [],[],"outer_terrain_plain"),
  ("castle_11_interior",sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_11_prison",sf_indoors,"interior_prison_k", "bo_interior_prison_k", (-100,-100),(100,100),-100,"0",
    [],[]),
	
  ("castle_12_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230054f630005fd820000222a00003de000005f00",
    [],[],"outer_terrain_town_thir_1"),
  ("castle_12_interior",sf_indoors, "interior_castle_y", "bo_interior_castle_y", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_12_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]), #

  ("castle_mike_random",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000020000000000fffff000041ef00005ae800003c55",
    [],[],"outer_terrain_plain"),
	
  ("castle_13_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230054f630005fd820000222a00003de000005f00",
    [],[],"outer_terrain_plain"),
  ("castle_13_interior",sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_13_prison",sf_indoors,"interior_prison_j", "bo_interior_prison_j", (-100,-100),(100,100),-100,"0",
    [],[]),
	
  ("castle_15_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023007941f0005415000007e650000225f00003b3e",
    [],[],"outer_terrain_plain"),
  ("castle_15_interior",sf_indoors, "interior_castle_p", "bo_interior_castle_p", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_15_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    [],[]),
	
  ("castle_20_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013006199a0004e5370000494f000028fc00006cf6",
    [],[],"outer_terrain_plain"),
  ("castle_20_interior",sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_20_prison",sf_indoors,"interior_prison_d", "bo_interior_prison_d", (-100,-100),(100,100),-100,"0",
    [],[]),
	
  ("castle_21_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230011ab20005d57800003a2600004b7a000071ef",
    [],[],"outer_terrain_plain"),
  ("castle_21_interior",sf_indoors, "interior_castle_c", "bo_interior_castle_c", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_21_prison",sf_indoors,"interior_prison_d", "bo_interior_prison_d", (-100,-100),(100,100),-100,"0",
    [],[]),
	
  ("castle_23_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300658bc0007bded000025520000093800006114",
    [],[], "outer_terrain_steppe"),
  ("castle_23_interior",sf_indoors, "interior_castle_y", "bo_interior_castle_y", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_23_prison",sf_indoors,"interior_prison_b", "bo_interior_prison_b", (-100,-100),(100,100),-100,"0",
    [],[]),
	
	#scandinavians
  ("castle_18_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000240079f9e0005695a0000035f00003ef400004aa8",
    [],[],"outer_terrain_snow"),
  ("castle_18_interior",sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_18_prison",sf_indoors,"interior_prison_k", "bo_interior_prison_k", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_19_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000014004d81100057963000062ce0000255800004c09",
    [],[],"outer_terrain_snow"),
  ("castle_19_interior",sf_indoors, "interior_castle_c", "bo_interior_castle_c", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_19_prison",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    [],[]),
	
  ("castle_29_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000006400796b20005053e000042ed0000199b000037cd",
    [],[],"outer_terrain_snow"),
  ("castle_29_interior",sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_29_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    [],[]),
	
  ("castle_39_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000014007a0320005695f0000601c00007a8800001a17",
    [],[],"outer_terrain_snow"),
  ("castle_39_interior",sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_39_prison",sf_indoors,"interior_prison_k", "bo_interior_prison_k", (-100,-100),(100,100),-100,"0",
    [],[]),
	
	#Eastern
  ("castle_37_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130025cb20006097f00005b1400000e2f00005fd9",
    [],[],"outer_terrain_plain"),
  ("castle_37_interior",sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_37_prison",sf_indoors,"interior_prison_l", "bo_interior_prison_l", (-100,-100),(100,100),-100,"0",
    [],[]),

	##arabian
  ("castle_2_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa00363638005c16d00003c82000037e000002303",
    [],[],"outer_terrain_steppe"),
  ("castle_2_interior",sf_indoors, "interior_castle_u", "bo_interior_castle_u", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_2_prison",sf_indoors,"interior_prison_d", "bo_interior_prison_d", (-100,-100),(100,100),-100,"0",#### B bkullanilmayacak
    [],[]),
	
  ("castle_42_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000005a039fb20005114400004f690000467a00004400",
    [],[],"0"),
  ("castle_42_interior",sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_42_prison",sf_indoors,"interior_prison_o", "bo_interior_prison_o", (-100,-100),(100,100),-100,"0",
    [],[]),
	
  ("castle_43_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000005a0ae6480004952400003e1800005d9f00002c7e",
    [],[],"0"),
  ("castle_43_interior",sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_43_prison",sf_indoors,"interior_prison_o", "bo_interior_prison_o", (-100,-100),(100,100),-100,"0",
    [],[]),
	
  ("castle_45_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000254c2ec0000042509000016da0000017200000ed3",
    [],[],"0"),
  ("castle_45_interior",sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_45_prison",sf_indoors,"interior_prison_n", "bo_interior_prison_n", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_46_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000254c2ec0000042509000016da0000017200000ed3",
    [],[],"0"),
  ("castle_46_interior",sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_46_prison",sf_indoors,"interior_prison_o", "bo_interior_prison_o", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_47_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000005a07b2320002b8ad000036c80000409d00001987",
    [],[],"0"),
  ("castle_47_interior",sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_47_prison",sf_indoors,"interior_prison_n", "bo_interior_prison_n", (-100,-100),(100,100),-100,"0",
    [],[]),
	
##iberia pool
#       9 Steppe
  ("castle_9_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0048e000004d93700004f91000065980000229b",
    [],[],"outer_terrain_steppe"),
  ("castle_9_interior",sf_indoors, "interior_castle_l", "bo_interior_castle_l", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_9_prison",sf_indoors,"interior_prison_d", "bo_interior_prison_d", (-100,-100),(100,100),-100,"0",
    [],[]),
	
  ("castle_17_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000220045d9b0005d9760000034a00002a3e00006fbd",
    [],[],"outer_terrain_steppe"),
  ("castle_17_interior",sf_indoors, "interior_castle_l", "bo_interior_castle_l", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_17_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    [],[]),
	
  ("castle_22_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003000ad340004d537000024650000253c00000461",
    [],[],"outer_terrain_steppe"),
  ("castle_22_interior",sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  ("castle_22_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),
	#imports from native end
	
	("1257_combat_swamp_0",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002b00005000007c1f0000063ae00001a6200002a91",
    [],[], "outer_terrain_plain"),
    ("1257_combat_swamp_1",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002b00005000007c1f0000033140000117b00001d9e",
    [],[], "outer_terrain_plain"),
	("1257_combat_swamp_2",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002b00005000007c1f00000736a00002d8800002dd1",
    [],[], "outer_terrain_plain"),
	("1257_combat_swamp_3",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002300005638007d5fd00003bf10000087600002cda",
    [],[], "outer_terrain_plain"),
	("1257_combat_swamp_4",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002b00005000007c1f000007bba0000695c00000752",
    [],[], "outer_terrain_plain"),
	("1257_combat_swamp_5",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002b00005000007c1f000007bba00001b390000427e",
    [],[], "outer_terrain_plain"),
	("1257_combat_swamp_6",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002b00005000007c1f000007bba00001b390000427e",
    [],[], "outer_terrain_plain"),
	("1257_combat_swamp_7",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002b00005000007c1f00000249e000037fd00005048",
    [],[], "outer_terrain_plain"),
	("1257_combat_swamp_8",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002b00005000007c1f0000023270000158800001278",
    [],[], "outer_terrain_plain"),
	("1257_combat_swamp_9",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002b00005000007c1f00000040900003b150000457b",
    [],[], "outer_terrain_plain"),
	

	("1257_combat_rocky_desert_0",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(280,280),-0.5,"0x0000000350000500000775de0000034e00004b34000059be",
    [],[], "outer_terrain_desert_b"), #0
	("1257_combat_iberian_0",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003200005000007c1f0000063ae00001a6200002a91",
    [],[], "outer_terrain_steppe"),
	("1257_combat_steppe_0",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003200005000007c1f000000de2000025c700002b3b",
    [],[], "0"),
	("1257_combat_steppe_1",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003200005000007c1f000000de2000025c700002b3b",
    [],[], "0"), #RANDOM! For diffent things
	("1257_combat_steppe_2",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003200005000007c1f000000de2000025c700002b3b",
    [],[], "0"), #swampy?
	("1257_combat_steppe_3",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003200005000007c1f000000de2000025c700002b3b",
    [],[], "0"), #swampy?
	#european plain battlefield
	("1257_combat_euro_0",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000330c005000007a9f2000071ce00003476000031c1",
    [],[], "outer_terrain_plain"),
	("1257_combat_euro_1",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003328005000007c1f000004ff90000139700001717",
    [],[], "outer_terrain_plain"),
	("1257_combat_euro_2",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003328005000007c1f00000041400000414000044fa",
    [],[], "outer_terrain_plain"),
	("1257_combat_euro_3",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003328005000007c1f0000059d600000414000014f8",
    [],[], "outer_terrain_plain"),
	
	("1257_combat_iberian_hillside_0",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003200005000007c1f000007b2f00000f9300003486",
    [],[], "outer_terrain_steppe"),
	("1257_combat_iberian_hillside_1",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003200005000007c1f0000041ef00006e3600007b86",
    [],[], "outer_terrain_steppe"),
	("1257_combat_iberian_hillside_2",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003200005000007c1f0000041ef00006e3600007b86",
    [],[], "outer_terrain_steppe"),
	("1257_combat_iberian_hillside_3",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003200005000007c1f000007b2f00000f9300003486",
    [],[], "outer_terrain_steppe"),
	("1257_combat_iberian_hillside_4",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003200005000007c1f0000041ef00006e3600007b86",
    [],[], "outer_terrain_steppe"),
	("1257_combat_iberian_hillside_5",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003200005000007c1f0000041ef00006e3600007b86",
    [],[], "outer_terrain_steppe"),	
	("1257_combat_iberian_hillside_6",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003200005000007c1f000007b2f00000f9300003486",
    [],[], "outer_terrain_steppe"),
	("1257_combat_iberian_hillside_7",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003200005000007c1f0000041ef00006e3600007b86",
    [],[], "outer_terrain_steppe"),
	("1257_combat_iberian_hillside_8",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003200005000007c1f0000041ef00006e3600007b86",
    [],[], "outer_terrain_steppe"),		
	
	
	("1257_combat_euro_hillside_0",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003300005008007f5fd00007d88000069f000002b96",
    [],[], "outer_terrain_plain_mountain"),
	("1257_combat_euro_hillside_1",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003300005000007f5fd00007d88000069f000002b96",
    [],[], "outer_terrain_plain_mountain"),
	("1257_combat_euro_hillside_2",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003300005008007f5fd00007d88000069f000002b96",
    [],[], "outer_terrain_plain_mountain"),
	("1257_combat_euro_hillside_3",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003300005000007f5fd00007d88000069f000002b96",
    [],[], "outer_terrain_plain_mountain"),
	("1257_combat_euro_hillside_4",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003300005000007f5fd00007d88000069f000002b96",
    [],[], "outer_terrain_plain_mountain"),
	
	("1257_combat_mountain_0",sf_generate,"none", "none", (0,0),(240,240),-0.5,"0x00000000300005000009de7900000f300000446800005b1f",
    [],[], "outer_terrain_plain_mountain"),
	("1257_combat_mountain_1",sf_generate,"none", "none", (0,0),(240,240),-0.5,"0x00000000300005000009de7900000f300000446800005b1f",
    [],[], "outer_terrain_plain_mountain"),
	("1257_combat_mountain_2",sf_generate,"none", "none", (0,0),(240,240),-0.5,"0x00000000300005000009de7900000f300000446800005b1f",
    [],[], "outer_terrain_plain_mountain"),
	("1257_combat_mountain_3",sf_generate,"none", "none", (0,0),(240,240),-0.5,"0x00000000300005000009de7900000f300000446800005b1f",
    [],[], "outer_terrain_plain_mountain"),
	("1257_combat_mountain_4",sf_generate,"none", "none", (0,0),(240,240),-0.5,"0x00000000300005000009de7900000f300000446800005b1f",
    [],[], "outer_terrain_plain_mountain"),
	("1257_combat_mountain_5",sf_generate,"none", "none", (0,0),(240,240),-0.5,"0x00000000300005000009de7900000f300000446800005b1f",
    [],[], "outer_terrain_snow_mountain"),
	("1257_combat_mountain_6",sf_generate,"none", "none", (0,0),(240,240),-0.5,"0x00000000300005000009de7900000f300000446800005b1f",
    [],[], "outer_terrain_snow_mountain"),
	("1257_combat_mountain_7",sf_generate,"none", "none", (0,0),(240,240),-0.5,"0x00000000300005000009de7900000f300000446800005b1f",
    [],[], "outer_terrain_plain_mountain"),
	("1257_combat_mountain_8",sf_generate,"none", "none", (0,0),(240,240),-0.5,"0x00000000300005000009de7900000f300000446800005b1f",
    [],[], "outer_terrain_plain_mountain"),
	("1257_combat_mountain_9",sf_generate,"none", "none", (0,0),(240,240),-0.5,"0x00000000300005000009de7900000f300000446800005b1f",
    [],[], "outer_terrain_plain_mountain"),
	
	("1257_combat_river_0",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000023c6005638007d5fd00003bf10000087600002cda",
    [],[], "outer_terrain_plain"),
	
	("1257_combat_mountain_desert_0",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(280,280),-0.5,"0x0000000350000500000775de0000034e00004b34000059be",
    [],[], "outer_terrain_desert_b"), #0
	("1257_combat_mountain_desert_1",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(280,280),-0.5,"0x0000000350000500000775de0000034e00004b34000059be",
    [],[], "outer_terrain_desert_b"), #0
	("1257_combat_forest_0",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(280,280),-0.5,"0x00000003b00005010006398e00006d3000003879000009f9",
    [],[], "outer_terrain_plain"), #0
	
	("sitd_battle_nile_1",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000220000500000809fd000048a800004dcc000005b6",
    [],[], "outer_terrain_desert_b"),
	("sitd_battle_nile_2",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000220000500000809fd000048a800004dcc000005b6",
	[],[], "outer_terrain_desert_b"),
	("sitd_battle_nile_3",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000220000500000809fd000048a800004dcc000005b6",
	[],[], "outer_terrain_desert_b"),
	("sitd_battle_nile_4",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000220000500000809fd000048a800004dcc000005b6",
	[],[], "outer_terrain_desert_b"),
	
	("1257_combat_snow_0",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000340000500000779e000001dcd00006b6b00001810",
    [],[], "outer_terrain_snow"),
	("1257_combat_snow_1",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000340190681000779e0000075cd000023b500007244",
    [],[], "outer_terrain_snow"),
	("1257_combat_snow_2",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000340190601000779e00000398100001e3600007abd",
    [],[], "outer_terrain_snow"),
	("1257_combat_snow_3",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003400d8600000779e0000024a90000601100006e21",
    [],[], "outer_terrain_snow"),
	("1257_combat_snow_4",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000340094580000779e00000510e000018b10000773d",
    [],[], "outer_terrain_snow"),
	("1257_combat_snow_5",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000340190500000779e00000565c00006463000035bf",
    [],[], "outer_terrain_snow"),
	("1257_combat_snow_6",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000340018500000779e00000510e0000565c00006463",
    [],[], "outer_terrain_snow"),
	("1257_combat_snow_7",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000340000500000779e000004d9d00001b66000035bf",
    [],[], "outer_terrain_snow"),
	#temp for now
	("manor", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000003b00005010004b52d00006d3000003879000009f9",
    [],[], "outer_terrain_plain"),
	
	#village manor
	("manor_central_european_linen_workshop", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000003b00005010004b52d00006d3000003879000009f9",
    [],[], "outer_terrain_plain"),
	("manor_central_european_farm", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000003b00005010004b52d00006d3000003879000009f9",
    [],[], "outer_terrain_plain"),
	("manor_central_european_mines", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000003b00005010004b52d00006d3000003879000009f9",
    [],[], "outer_terrain_plain"),
	("manor_central_european_trader", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000003b00005010004b52d00006d3000003879000009f9",
    [],[], "outer_terrain_plain"),
	
	#town manor
	("manor_central_european_horse_breeder", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000003b00005010004b52d00006d3000003879000009f9",
    [],[], "outer_terrain_plain"),
	("manor_central_european_fletchery", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000003b00005010004b52d00006d3000003879000009f9",
    [],[], "outer_terrain_plain"),
	("manor_central_european_weapon_smith", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000003b00005010004b52d00006d3000003879000009f9",
    [],[], "outer_terrain_plain"),
	("manor_central_european_armour_smith", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000003b00005010004b52d00006d3000003879000009f9",
    [],[], "outer_terrain_plain"),
	
	#desert village manor
	("manor_desert_linen_workshop", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000002a00005010004b52d00006d3000003879000009f9",
    [],[], "outer_terrain_desert_b"),
	("manor_desert_farm", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000002a00005010004b52d00006d3000003879000009f9",
    [],[], "outer_terrain_desert_b"),
	("manor_desert_mines", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000002a00005010004b52d00006d3000003879000009f9",
    [],[], "outer_terrain_desert_b"),
	("manor_desert_trader", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000002a00005010004b52d00006d3000003879000009f9",
    [],[], "outer_terrain_desert_b"),
	
	#desrt town manor
	("manor_desert_horse_breeder", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000002a00005010004b52d00006d3000003879000009f9",
    [],[], "outer_terrain_desert_b"),
	("manor_desert_fletchery", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000002a00005010004b52d00006d3000003879000009f9",
    [],[], "outer_terrain_desert_b"),
	("manor_desert_weapon_smith", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000002a00005010004b52d00006d3000003879000009f9",
    [],[], "outer_terrain_desert_b"),
	("manor_desert_armour_smith", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000002a00005010004b52d00006d3000003879000009f9",
    [],[], "outer_terrain_desert_b"),
	
	#nordic village manor
	("manor_nordic_linen_workshop", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000000b00005010004b52d000025e800004065000017d3",
    [],[], "outer_terrain_sea"),
	("manor_nordic_farm", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000000b00005010004b52d000025e800004065000017d3",
    [],[], "outer_terrain_sea"),
	("manor_nordic_mines", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000000b00005010004b52d000025e800004065000017d3",
    [],[], "outer_terrain_sea"),
	("manor_nordic_trader", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000000b00005010004b52d000025e800004065000017d3",
    [],[], "outer_terrain_sea"),
	
	#nordic town manor
	("manor_nordic_horse_breeder", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000000b00005010004b52d000025e800004065000017d3",
    [],[], "outer_terrain_sea"),
	("manor_nordic_fletchery", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000000b00005010004b52d000025e800004065000017d3",
    [],[], "outer_terrain_sea"),
	("manor_nordic_weapon_smith", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000000b00005010004b52d000025e800004065000017d3",
    [],[], "outer_terrain_sea"),
	("manor_nordic_armour_smith", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000000b00005010004b52d000025e800004065000017d3",
    [],[], "outer_terrain_sea"),
	
	#steppe village manor
	("manor_steppe_linen_workshop", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000000200005630005e5760000490400003374000065f6",
    [],[], "outer_terrain_sea"),
	("manor_steppe_farm", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000000200005630005e5760000490400003374000065f6",
    [],[], "outer_terrain_sea"),
	("manor_steppe_mines", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000000200005630005e5760000490400003374000065f6",
    [],[], "outer_terrain_sea"),
	("manor_steppe_trader", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000000200005630005e5760000490400003374000065f6",
    [],[], "outer_terrain_sea"),
	
	#steppe town manor
	("manor_steppe_horse_breeder", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000000200005630005e5760000490400003374000065f6",
    [],[], "outer_terrain_sea"),
	("manor_steppe_fletchery", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000000200005630005e5760000490400003374000065f6",
    [],[], "outer_terrain_sea"),
	("manor_steppe_weapon_smith", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000000200005630005e5760000490400003374000065f6",
    [],[], "outer_terrain_sea"),
	("manor_steppe_armour_smith", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000000200005630005e5760000490400003374000065f6",
    [],[], "outer_terrain_sea"),
	
	("manor_Monastery", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000003300005008007f5fd00007d88000069f000002b96",
    [],[], "outer_terrain_plain"),
	
	("manor_test", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000003300005008007f5fd00007d88000069f000002b96",
    [],[], "outer_terrain_plain"),
	("manor_fortified_euro_plains", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x0000000330000500000b0ac2000035c40000650700002963",
    [],[], "outer_terrain_plain"),
	("manor_fortified_euro_snow", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x0000000340000500000b0ac2000035c40000650700002963",
    [],[], "outer_terrain_snow"),
	("manor_fortified_euro_steppe", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x0000000320000500000b0ac2000035c40000650700002963",
    [],[], "outer_terrain_steppe"),
	("manor_fortified_euro_desert", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x0000000350000500000b0ac2000035c40000650700002963",
    [],[], "0"),
	("manor_fortified_byzantium", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x0000000320000500000b0ac2000035c40000650700002963",
    [],[], "0"),
	("manor_fortified_baltic", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x0000000330000500000a9aa800003cbc0000204700001a32",
    [],[], "0"),
	("manor_fortified_rus", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x0000000350000500000b0ac2000035c40000650700002963",
    [],[], "0"),
	("manor_fortified_scand", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x0000000350000500000b0ac2000035c40000650700002963",
    [],[], "0"),
	("manor_fortified_latin", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x0000000320000500000b0ac2000035c40000650700002963",
    [],[], "0"),
	("manor_fortified_arabian", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x0000000350000500000b0ac2000035c40000650700002963",
    [],[], "0"),
	("manor_fortified_iberian", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x0000000320000500000b0ac2000035c40000650700002963",
    [],[], "0"),
	("manor_fortified_crusader", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x0000000320000500000b0ac2000035c40000650700002963",
    [],[], "0"),
	("manor_fortified_teutonic", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x0000000330000500000b0ac2000035c40000650700002963",
    [],[], "0"),#+
	
	("manors_end", sf_generate|sf_randomize, "none", "none", (0,0),(280,280),-0.5,"0x0000000330000500000b0ac2000035c40000650700002963",
    [],[], "outer_terrain_plain"),	
	("manor_feudal", sf_generate, "none", "none", (0,0),(280,280),-0.5,"0x00000003300005008007f5fd00007d88000069f000002b96",
    [],[], "outer_terrain_plain"),
	
	
	#placeholders
    
	  ("town_euro_center_4",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130001887000334d0000073ed00004f1a00007a35",
    [],[],"outer_terrain_plain"),    
	  ("town_euro_center_5",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130001887000334d0000073ed00004f1a00007a35",
    [],[],"outer_terrain_plain"),    
	  ("town_euro_center_6",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130001887000334d0000073ed00004f1a00007a35",
    [],[],"outer_terrain_plain"),    
	  ("town_euro_center_7",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130001887000334d0000073ed00004f1a00007a35",
    [],[],"outer_terrain_plain"),    
	  ("town_euro_center_8",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130001887000334d0000073ed00004f1a00007a35",
    [],[],"outer_terrain_plain"),    
	  ("town_euro_center_9",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130001887000334d0000073ed00004f1a00007a35",
    [],[],"outer_terrain_plain"),  
	  ("town_euro_center_10",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130001887000334d0000073ed00004f1a00007a35",
    [],[],"outer_terrain_plain"),  
	  ("town_euro_center_11",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130001887000334d0000073ed00004f1a00007a35",
    [],[],"outer_terrain_plain"),  
	
	#for villages
	("campside_plain",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000bc6005000002589600004a0a00000e0600004687",
    [],[],"outer_terrain_plain"),  
	("campside_snow",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000cc7185000002589600003f0a00000e0600004687",
    [],[],"outer_terrain_snow"),  
	("campside_steppe",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000ac6005000002589600004a0a00000e0600004687",
    [],[],"outer_terrain_steppe"),  
	("campside_desert",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000005c635c8d0002589600003f0a00000e0600004687",
    [],[],"0"),  
	("campside_mongol",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000ac6005000002589600004a0a00000e0600004687",
    [],[],"outer_terrain_steppe"),  	
	
	("byzantine_castle",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000020024e100003fd0100007bd300006c31000061aa",
    [],[],"outer_terrain_steppe"),
	("village_byzantine",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023007b23280067d9d0000685580001a0b000013a4",
    [],[],"outer_terrain_steppe"),
	("castle_interior_byz",sf_indoors, "byzantine_interior", "bo_byzantine_interior", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
	("town_interior_byz",sf_indoors, "byzantine_interior", "bo_byzantine_interior", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_1_seneschal"]),
  	# ("balt_town_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000003300045000004e93d000053100000628200007e05",
    # [],[],"outer_terrain_steppe"), 

   	# ("balt_town_siege",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000003300045000004e93d000053100000628200007e05",
    # [],[],"outer_terrain_steppe"),  
	
	###HOUSING
	("town_house_euro",sf_indoors, "interior_town_house_a", "bo_interior_town_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
	("town_house_arabian",sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
	("town_house_eastern",sf_indoors, "interior_town_house_i", "bo_interior_town_house_i", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
]
