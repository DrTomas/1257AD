# -*- coding: utf-8 -*-
from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################
# 249f6c

default_kingdom_relations = [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.02),("forest_bandits", -0.02)]
factions = [
  ("no_faction","No Faction",0, 0.9, [], []),
  ("commoners","Commoners",0, 0.1,[("player_faction",0.1)], []),
  ("outlaws","Outlaws", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [], 0x888888),
# Factions before this point are hardwired into the game end their order should not be changed.

  ("neutral","Neutral",0, 0.1,[("player_faction",0.0)], [],0xFFFFFF),
  ("innocents","Innocents", ff_always_hide_label, 0.5,[("outlaws",-0.05)], []),
  ("merchants","Merchants", ff_always_hide_label, 0.5,[("outlaws",-0.5),], []),

  ("dark_knights","{!}Dark Knights", 0, 0.5,[("innocents",-0.9),("player_faction",-0.4)], []),

  #("culture_1",  "{!}culture_1", 0, 0.9, [], []),
  #("culture_2",  "{!}culture_2", 0, 0.9, [], []),
 # ("culture_3",  "{!}culture_3", 0, 0.9, [], []),
 # ("culture_4",  "{!}culture_4", 0, 0.9, [], []),
  #("culture_5",  "{!}culture_5", 0, 0.9, [], []),
 # ("culture_6",  "{!}culture_6", 0, 0.9, [], []),
  #("culture_7",  "{!}culture_7", 0, 0.9, [], []),
  #("culture_8",  "{!}culture_8", 0, 0.9, [], []),
  #("culture_9",  "{!}culture_9", 0, 0.9, [], []),
  #("culture_10",  "{!}culture_10", 0, 0.9, [], []),
  #("culture_11",  "{!}culture_11", 0, 0.9, [], []),
 # ("culture_12",  "{!}culture_12", 0, 0.9, [], []),
  #("culture_13",  "{!}culture_13", 0, 0.9, [], []),
  #("culture_14",  "{!}culture_14", 0, 0.9, [], []),
  #("culture_15",  "{!}culture_15", 0, 0.9, [], []),
  #("culture_16",  "{!}culture_16", 0, 0.9, [], []),
  #("culture_17",  "{!}culture_17", 0, 0.9, [], []),
  #("culture_18",  "{!}culture_18", 0, 0.9, [], []),
  #("culture_19",  "{!}culture_19", 0, 0.9, [], []),
  #("culture_20",  "{!}culture_20", 0, 0.9, [], []),
  #("culture_21",  "{!}culture_21", 0, 0.9, [], []),
  #("culture_22",  "{!}culture_22", 0, 0.9, [], []),
  #("culture_23",  "{!}culture_23", 0, 0.9, [], []),
  #("culture_24",  "{!}culture_24", 0, 0.9, [], []),
  #("culture_25",  "{!}culture_25", 0, 0.9, [], []),
  #("culture_26",  "{!}culture_26", 0, 0.9, [], []),
  #("culture_27",  "{!}culture_27", 0, 0.9, [], []),
  #("culture_28",  "{!}culture_28", 0, 0.9, [], []),
  #("culture_29",  "{!}culture_29", 0, 0.9, [], []),
  #("culture_30",  "{!}culture_30", 0, 0.9, [], []),
  #("culture_31",  "{!}culture_31", 0, 0.9, [], []),
  #("culture_32",  "{!}culture_32", 0, 0.9, [], []),
  #("culture_33",  "{!}culture_33", 0, 0.9, [], []),
  # ("culture_34",  "{!}culture_31", 0, 0.9, [], []),
  #("culture_37",  "{!}culture_37", 0, 0.9, [], []),
  
  ("culture_finnish",  "{!}culture_finnish", 0, 0.9, [], []),  #
  ("culture_mazovian",  "{!}culture_mazovian", 0, 0.9, [], []), #
  ("culture_serbian",  "{!}culture_serbian", 0, 0.9, [], []), #kingdom_29
  ("culture_welsh",  "{!}culture_welsh", 0, 0.9, [], []), #kingdom_37
  ("culture_teutonic",  "{!}culture_teutonic", 0, 0.9, [], []), #kingdom_1
  ("culture_balkan",  "{!}culture_balkan", 0, 0.9, [], []), #kingdom_30
  ("culture_rus",  "{!}culture_rus", 0, 0.9, [], []), #kingdom_15, kingdom_8
  ("culture_nordic",  "{!}culture_nordic", 0, 0.9, [], []), # kingdom_11, kingdom_14, kingdom_4
  ("culture_baltic",  "{!}culture_baltic", 0, 0.9, [], []), #kingdom_2, kingdom_33, kingdom_34, kingdom_35, kingdom_36
  ("culture_marinid",  "{!}culture_marinid", 0, 0.9, [], []), #kingdom_31 #kingdom_28
  ("culture_mamluke",  "{!}culture_mamluke", 0, 0.9, [], []), #kingdom_25
  ("culture_byzantium",  "{!}culture_byzantium", 0, 0.9, [], []), #kingdom_22, kingdom_26
  ("culture_iberian",  "{!}culture_iberian", 0, 0.9, [], []), #kingdom_16, kingdom_17, kingdom_18, kingdom_21, kingdom_32,
  ("culture_italian",  "{!}culture_italian", 0, 0.9, [], []), #papacy, kingdom_24, kingdom_38, kingdom_39, kingdom_40, kingdom_41
  ("culture_andalus",  "{!}culture_andalus", 0, 0.9, [], []), #kingdom_20
  ("culture_gaelic",  "{!}culture_gaelic", 0, 0.9, [], []),  #kingdom_13
  ("culture_anatolian_christian",  "{!}culture_anatolian", 0, 0.9, [], []),  
  ("culture_anatolian",  "{!}culture_anatolian", 0, 0.9, [], []),
  ("culture_scotish",  "{!}culture_scotish", 0, 0.9, [], []), #kingdom_12
  ("culture_western",  "{!}culture_western", 0, 0.9, [], []), #kingdom_5, kingdom_6, kingdom_7, kingdom_9, kingdom_10, kingdom_19, kingdom_42, kingdom_23
  ("culture_mongol",  "{!}culture_mongol", 0, 0.9, [], []), #kingdom_3, kingdom_27
 # ("culture_hafsid",  "{!}culture_hafsid", 0, 0.9, [], []), 
  
#  ("swadian_caravans","Swadian Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),
#  ("vaegir_caravans","Vaegir Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),

  ("player_faction","Player Faction",0, 0.9, [], [], 0xcccccc),
  ("player_supporters_faction","Player's Supporters",0, 0.9, [("player_faction",1.00),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x468493), #changed name so that can tell difference if shows up on map

  ("kingdom_1",  "Ordo Teutonicus",
  #"Teutonic Order (Livonia and Prussia)",
    0, 0.9,
    [
      ("papacy",0.0),
      ("kingdom_8",-0.2),
      ("kingdom_14",0.10),
      ("kingdom_4",0.10),
      ("kingdom_6",0.50),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
      # ("curonians", -1),
      # ("prussians", -1),
      # ("samogitians", -1),
      # ("yotvingians", -1),
    ],
    [],
    0xe9e9e9
  ),

  ("kingdom_2",  "Regnum Litus",
  #"Kingdom of Lithuania",
    0, 0.9,
    [
	  ("crusade", -0.5),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
	  ("kingdom_33", 0.5),
      # ("curonians", 1),
      # ("prussians", 1),
      # ("samogitians", 1),
      # ("yotvingians", 1),
    ],
    [],
    0xbadeb2
  ),

  ("kingdom_3",  "Altan Ordyn Uls",
  #"Golden Horde",
    0, 0.9,
    [
	  ("crusade", -0.5),
      ("kingdom_2",0.1),
      ("kingdom_8",0.2),
      ("kingdom_7",-1.0),
      ("kingdom_5",-1.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xa33e32
  ),
  ("kingdom_4", "Regnum Daniae",
  #  "Kingdom of Denmark",
    0, 0.9,
    [
      ("papacy",0.0),
      ("kingdom_1",0.10),
      #("kingdom_2",-0.01),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0x9b1a1a
  ),
  ("kingdom_5", "Regnum Poloniae",
  # "Polish Principalities",
    0, 0.9,
    [
      ("papacy",0.0),
      ("kingdom_7",0.10),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
      [],
      0xff0000
  ),
  ("kingdom_6",  "Sacrum Imperium Romanum",
  #"Holy Roman Empire",
    0, 0.9,
    [
      ("papacy",0.0),
      ("kingdom_1",0.50),
      ("kingdom_38",0.50),
      ("kingdom_41",1.0),
      ("kingdom_42",1.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ], [],
    0xffcc00
  ),
  ("kingdom_7",  "Regnum Hungariae",
  #"Kingdom of Hungary",
    0, 0.9,
    [
      ("papacy",0.0),
      ("kingdom_5",0.10),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0x289327
  ),

  ("kingdom_8",  "Novgorod Weliki",
  #"Novgorod Republic",
    0, 0.9,
    [
      ("kingdom_1",-0.20),
      ("kingdom_3",0.1),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
      # ("curonians", 1),
      # ("prussians", 1),
      # ("samogitians", 1),
      # ("yotvingians", 1),
    ],
    [],
    0x9e0b6f
  ),
  ("kingdom_9",  "Regnum Angliae",
  #"Kingdom of England",
    0, 0.9,
    [
      ("papacy",0.0),
      #("kingdom_10",-0.5),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
	  ("kingdom_37", -1),
    ], [],
    0x931124
  ),
  ("kingdom_10",  "Regnum Franciae",
  #"Kingdom of France",
    0, 0.9,
    [
      ("papacy",0.0),
      #("kingdom_9",-0.5),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ], [],
    0x002395
  ),
  ("kingdom_11",  "Kongeriket Norge",
  #"Kingdom of Norway",
    0, 0.9,
    [
      ("papacy",0.0),
      ("kingdom_13",-0.2),
      ("kingdom_12",-0.2),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ], [],
    0x6669d6 
  ),
  ("kingdom_12",  "Regnum Scotiae",
  #"Kingdom of Scotland",
    0, 0.9,
    [
      ("papacy",0.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0x22D8A7
  ),
  ("kingdom_13",  "Scotia Maior",
  #"Gaelic Kingdoms",
    0, 0.9,
    [
      ("papacy",0.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ], [],
    0x77b322
  ),
  ("kingdom_14",  "Konungariket Sverige",
  #"Kingdom of Sweden",
    0, 0.9,
    [
      ("papacy",0.0),
      ("kingdom_1",0.1),
      #("kingdom_2",-0.01),
      ("kingdom_8",-0.2),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0x3254b5
  ),

  ("kingdom_15",  "Regnum Galiciae et Lodomeriae",
  #"Kingdom of Halych-Volhynia",
    0, 0.9,
    [
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xece874
  ),

  ("kingdom_16",  "Regnum Portugaliae",
  #"Kingdom of Portugal",
    0, 0.9,
    [
      ("papacy",0.0),
      ("kingdom_20", -40),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0x003399
  ),
  ("kingdom_17",  "Corona Aragonae",
  #"Crown of Aragon",
    0, 0.9,
    [
      ("papacy",0.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0x07b233
  ),

  ("kingdom_18",  "Regnum Castiliae",
  #"Kingdom of Castille",
    0, 0.9,
    [
      ("papacy",0.0),
      ("kingdom_20", -40),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xd85ac4
  ),
  
  ("kingdom_19",  "Regnum Navarrae",
  #"Kingdom of Navarra",
    0, 0.9,
    [
      ("papacy",0.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xf7f497
  ),

  ("kingdom_20",  "Imarat al Nasri",
  #"Emirate of Granada",
    0, 0.9,
    [
	  ("crusade", -0.5),
      ("kingdom_16", -40),
      ("kingdom_18", -40),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xabc904
  ),

    ("papacy",  "Patrimonium Sancti Petri",
    0, 0.9,
    [
	  ("kingdom_40", 1.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
	 # ("guelphs", 1),
	  
    ],
    [],
    0xfff17a
  ),
  
  ("kingdom_22",  "Basileia ton Rhomaion",
  #"Roman Empire of Nicaea",
    0, 0.9,
    [
      ("kingdom_26",-1.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0x760d0d
  ),

  ("kingdom_23",  "Regnum Hierosolymitanum",
  #"Crusader States",
    0, 0.9,
    [
      ("papacy",0.0),
      ("kingdom_25",-1.0),
      ("kingdom_27",0.1),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
    ],
    [],
    0xf3efb8
  ),

  ("kingdom_24",  "Regnum Siciliae",
  #"Kingdom of Sicily",
    0, 0.9,
    [
      ("papacy",0.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
	  #("guelphs", -1.0),
    ],
    [],
    0x799cb5
  ),

  ("kingdom_25",  "Sultanat al Mamalik",
  #"Mamluk Sultanate",
    0, 0.9,
    [
	  ("crusade", -0.5),
      ("kingdom_23",-1.0),
      ("kingdom_27",-1.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xebe800
  ),

  ("kingdom_26",  "Imperium Romaniae",
  #"Latin Empire",
    0, 0.9,
    [
      ("papacy",0.0),
      ("kingdom_22",-1.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xb26248
  ),


  ("kingdom_27",  "Ilkhanate",
  #"Il-khanate",
    0, 0.9,
    [
	  ("crusade", -0.5),
      ("kingdom_25",-1.0),
      ("kingdom_23",0.1),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xe19004
  ),

  ("kingdom_28",  "Sultanat al Hafsi",
  #"Hafsid Dynasty",
    0, 0.9,
    [
	  ("crusade", -0.5),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xa48460
  ),

  ("kingdom_29",  "Kraljevstvo Srbsko",
  #"Kingdom of Serbia",
    0, 0.9,
    [
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xb38263
  ),

  ("kingdom_30",  "Balgarsko Tsarstvo",
  #"Kingdom of Bulgaria",
    0, 0.9,
    [
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0x76a296
  ),

  ("kingdom_31",  "Sultanat al Marini",
  #"Marinid Dynasty",
    0, 0.9,
    [
	  ("crusade", -0.5),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xc1272d
  ),
  
  ("kingdom_32",  "Repubblica di Venezia",
  #"Republic of Venice",
    0, 0.9,
    [
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xc1172d
  ),  
  
  ("kingdom_33",  "Jotvingiai",
  #"Jotvingians",
    0, 0.9,
    [
	  ("crusade", -0.5),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
	  ("kingdom_2", 0.5),
	  # ("kingdom_34", 1),
      # ("kingdom_33", 1),
      # ("kingdom_36", 1),
	  #("kingdom_1",-0.1),
    ],
    [],
    0x3e7583
  ),
  
  ("kingdom_34",  "Pruteni",
  #"Prussians",
    0, 0.9,
    [
	  ("crusade", -0.5),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
	  ("kingdom_2", 0.5),
      # ("kingdom_34", 1),
      # ("kingdom_35", 1),
      # ("kingdom_36", 1),
	  #("kingdom_1",-0.1),
      # ("kingdom_1",-1.0),
      # ("kingdom_4",-1.0),
      # ("kingdom_14",-1.0),
      # ("kingdom_5",-1.0),
      # ("player_faction",0.0)
    ],
    [],
    0x65c0d7
  ),
  
  
  ("kingdom_35",  "Kursi",
  #"Curonians",
    0, 0.9,
    [
	  ("crusade", -0.5),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
	  ("kingdom_2", 0.5),
	  # ("kingdom_34", 1),
      # ("kingdom_35", 1),
      # ("kingdom_33", 1),
	  #("kingdom_1",-0.1),
    ],
    [],
    0x3e7583
  ),
  
    ("kingdom_36",  "Zemaiciai",
  #"Samagotians",
    0, 0.9,
    [
	  ("crusade", -0.5),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
	  ("kingdom_2", 0.5),
      # ("kingdom_33", 1),
      # ("kingdom_35", 1),
      # ("kingdom_36", 1),
	  #("kingdom_1",-0.1),
    ],
    [],
    0x529cae
  ),




  
    # ("kingdom_34",  "Granducato di Toscana",
	#####"Duchy of Tuscany",

    # 0, 0.9,
    # [
      # ("outlaws",-0.05),
      # ("peasant_rebels", -0.1),
      # ("deserters", -0.02),
      # ("mountain_bandits", -0.05),
      # ("forest_bandits", -0.05),
    # ],
    # [],
    # 0x00aaaa
  # ),

      ("kingdom_37",  "Cymry",
  #"Welsh",
    0, 0.9,
    [
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
	  ("kingdom_9", -1.0),
    ],
    [],
    0x00dc00
  ),  
  
  ("kingdom_38",  "Respublica Ianuensis",
  #"Genoa",
    0, 0.9,
    [
	  ("crusade", -0.5),
      ("kingdom_39",-0.5),
      ("kingdom_6",0.5),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xe1900a
  ),
  
    ("kingdom_39",  "Respublica Pisarum",
	#"Pisa",
    0, 0.9,
    [
      #("papacy",0.0),
      ("kingdom_38", -0.5),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0x07e233
  ),
  
    ("kingdom_40",  "Comuni Guelfi",
	#"Guelphs",
    0, 0.9,
    [
      ("papacy",0.0),
      ("kingdom_41",-0.8),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0x3254e5
  ),
  
    ("kingdom_41",  "Comuni Ghibellini",
	#"Ghibellines",
    0, 0.9,
    [
      ("kingdom_40",-0.80),
      ("kingdom_6",1.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
    ],
    [],
    0x9e026a
  ),
  
    ("kingdom_42",  "České Království",
	#"Bohemia",
    0, 0.9,
    [
      #("kingdom_40",-0.80),
      ("kingdom_6",1.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
    ],
    [],
    0xe8e8e8
  ),
  
  # ("crusade",  "Crusaders",
    # 0, 0.9,
    # [
      # ("outlaws",-0.05),
      # ("peasant_rebels", -0.1),
      # ("deserters", -0.02),
      # ("mountain_bandits", -0.05),
      # ("forest_bandits", -0.05),
	  # ("papacy", -0.5)
    # ],
    # [],
    # 0xfff17a
  # ),

  # ("jihad",  "Jihadists",
    # 0, 0.9,
    # [
      # ("outlaws",-0.05),
      # ("peasant_rebels", -0.1),
      # ("deserters", -0.02),
      # ("mountain_bandits", -0.05),
      # ("forest_bandits", -0.05)
    # ],
    # [],
    # 0xfff17a
  # ),

##  ("kingdom_1_rebels",  "Swadian rebels", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_2_rebels",  "Vaegir rebels",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_3_rebels",  "Khergit rebels", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_4_rebels",  "Nord rebels",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_5_rebels",  "Rhodok rebels",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),

  ("kingdoms_end","{!}kingdoms_end", 0, 0,[], []),

  ("robber_knights",  "{!}robber_knights", 0, 0.1, [], []),

  ("khergits","{!}Khergits", 0, 0.5,[("player_faction",0.0)], []),
  ("black_khergits","{!}Black Khergits", 0, 0.5,[("player_faction",-0.3),("kingdom_1",-0.02),("kingdom_2",-0.02)], []),

##  ("rebel_peasants","Rebel Peasants", 0, 0.5,[("vaegirs",-0.5),("player_faction",0.0)], []),

  ("manhunters","Captivos Proscriptorum", 0, 0.5,[("outlaws",-0.6),("player_faction",0.1)], []),
  ("deserters","Deserti", 0, 0.5,[("manhunters",-0.6),("merchants",-0.5),("player_faction",-0.1)], [], 0x888888),
  ("mountain_bandits","Montes Sicarii", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),
  ("forest_bandits","Silvae Sicarii", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),

  ("undeads","{!}Undeads", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], []),
  ("slavers","{!}Slavers", 0, 0.1, [], []),
  ("peasant_rebels","{!}Peasant Rebels", 0, 1.0,[("noble_refugees",-1.0),("player_faction",-0.4)], []),
  ("noble_refugees","{!}Noble Refugees", 0, 0.5,[], []),

  # ("guelphs","guelphs ", 0, 0.9,
    # [
      # ("papacy", 1),
	  # ("ghibellines", -1),
      # ("kingdom_24",-1.0),
      # ("player_faction",0.0),
    # ],
    # [],
    # 0xfff10a
  # ),
  
  # ("ghibellines","ghibellines", 0, 0.9,
    # [
      # ("papacy", -1.0),
	  # ("guelphs", -1),
      # ("kingdom_24",1.0),
      # ("player_faction",0.0),
    # ],
    # [],
    # 0x6fc0da
  # ),  
  
    ("crusade",  "Crusaders",
    0, 0.9,
    [
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
	  ("papacy", -0.5),
	  ("kingdom_33", -0.5)
    ],
    [],
    0xfff17a
  ),
 
  ("end_minor_faction", "Village Idiots",
  0, 0.9,
  [],
  [],
  0xfff17a
  ),


  # ("kingdom_32",  "Kingdom of Bohemia",
    # 0, 0.9,
    # [
      # ("papacy",0.0),
      # ("kingdom_1",0.50),
      # ("outlaws",-0.05),
      # ("peasant_rebels", -0.1),
      # ("deserters", -0.02),
      # ("mountain_bandits", -0.05),
      # ("forest_bandits", -0.05)
    # ], [],
    # 0xffcc00
  # ),

  #("lordship_of_ireland","Lordship of Ireland", 0, 0.9,[("kingdom_9",1.0),("kingdom_13",-1.0),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x4269f8),
]
