import string

dword      = 0x8000000000000000
dword_mask = 0xffffffffffffffff

density_bits      = 32
fkf_density_mask  = 0xFFFF #16K

#terain condition flags
fkf_plain             = 0x00000004
fkf_steppe            = 0x00000008
fkf_snow              = 0x00000010
fkf_desert            = 0x00000020
fkf_plain_forest      = 0x00000400
fkf_steppe_forest     = 0x00000800
fkf_snow_forest       = 0x00001000
fkf_desert_forest     = 0x00002000
fkf_terrain_mask      = 0x0000ffff

fkf_realtime_ligting  = 0x00010000 #deprecated
fkf_point_up          = 0x00020000 #uses auto-generated point-up(quad) geometry for the flora kind
fkf_align_with_ground = 0x00040000 #align the flora object with the ground normal
fkf_grass             = 0x00080000 #is grass
fkf_on_green_ground   = 0x00100000 #populate this flora on green ground
fkf_rock              = 0x00200000 #is rock 
fkf_tree              = 0x00400000 #is tree -> note that if you set this parameter, you should pass additional alternative tree definitions
fkf_snowy             = 0x00800000
fkf_guarantee         = 0x01000000

fkf_speedtree         = 0x02000000  #NOT FUNCTIONAL: we have removed speedtree support on M&B Warband

fkf_has_colony_props  = 0x04000000  # if fkf_has_colony_props -> then you can define colony_radius and colony_treshold of the flora kind

raf_density_10 = 5
raf_density_30 = 15
raf_density_50 = 25
raf_density_70 = 35
raf_density_400 = 200#100
raf_density_500 = 250#125
raf_density_1000 = 500#250
raf_density_1500 = 750#375

def density(g):
  if (g > fkf_density_mask):
    g = fkf_density_mask
  return ((dword | g) << density_bits)


fauna_kinds = [

  
  ("grass",fkf_grass|fkf_on_green_ground|fkf_guarantee|fkf_align_with_ground|fkf_point_up|fkf_plain|fkf_plain_forest|density(raf_density_1500),[["grass_a","0"],["grass_b","0"],["grass_c","0"],["grass_d","0"],["grass_e","0"]]),
  ("grass_bush",fkf_grass|fkf_align_with_ground|fkf_plain|fkf_steppe|fkf_steppe_forest|density(raf_density_10),[["grass_bush_a","0"],["grass_bush_b","0"]]),
  ("grass_saz",fkf_grass|fkf_on_green_ground|fkf_plain|fkf_steppe|fkf_steppe_forest|density(raf_density_500),[["grass_bush_c","0"],["grass_bush_d","0"]]),
  ("grass_purple",fkf_grass|fkf_plain|fkf_steppe|fkf_steppe_forest|density(raf_density_500),[["grass_bush_e","0"],["grass_bush_f","0"]]),
  ("fern",fkf_grass|fkf_plain_forest|fkf_align_with_ground|density(raf_density_1000),[["fern_a","0"],["fern_b","0"]]),
  ("grass_steppe",fkf_grass|fkf_on_green_ground|fkf_guarantee|fkf_align_with_ground|fkf_point_up|fkf_steppe|fkf_steppe_forest|density(raf_density_1500),[["grass_yellow_a","0"],["grass_yellow_b","0"],["grass_yellow_c","0"],["grass_yellow_d","0"],["grass_yellow_e","0"]]),

  ("grass_bush_g",fkf_grass|fkf_align_with_ground|fkf_steppe|fkf_steppe_forest|fkf_plain|fkf_plain_forest|density(raf_density_400),[["grass_bush_g01","0"],["grass_bush_g02","0"],["grass_bush_g03","0"]]),
  ("grass_bush_h",fkf_grass|fkf_align_with_ground|fkf_plain|fkf_plain_forest|density(raf_density_400),[["grass_bush_h01","0"],["grass_bush_h02","0"],["grass_bush_h03","0"]]),
  ("grass_bush_i",fkf_grass|fkf_align_with_ground|fkf_plain|fkf_plain_forest|density(raf_density_400),[["grass_bush_i01","0"],["grass_bush_i02","0"]]),
  ("grass_bush_j",fkf_grass|fkf_align_with_ground|fkf_steppe|fkf_steppe_forest|fkf_plain|fkf_plain_forest|density(raf_density_400),[["grass_bush_j01","0"],["grass_bush_j02","0"]]),
  ("grass_bush_k",fkf_grass|fkf_align_with_ground|fkf_plain|fkf_plain_forest|density(raf_density_400),[["grass_bush_k01","0"],["grass_bush_k02","0"]]),
  ("grass_bush_l",fkf_align_with_ground|fkf_plain|fkf_plain_forest|density(raf_density_50),[["grass_bush_l01","0"],["grass_bush_l02","0"]]),
  
  ("thorn_a",fkf_align_with_ground|fkf_plain|fkf_plain_forest|density(raf_density_50),[["thorn_a","0"],["thorn_b","0"],["thorn_c","0"],["thorn_d","0"]]),

   ("basak",fkf_plain|fkf_plain_forest|density(raf_density_70),[["basak","0"]]),
  ("common_plant",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|density(raf_density_70),[["common_plant","0"]]),
  ("small_plant",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_align_with_ground|density(raf_density_50),[["small_plant","0"],["small_plant_b","0"],["small_plant_c","0"]]),
  ("buddy_plant",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|density(raf_density_50),[["buddy_plant","0"],["buddy_plant_b","0"]]),
  ("yellow_flower",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_align_with_ground|density(raf_density_50),[["yellow_flower","0"],["yellow_flower_b","0"]]),
  ("spiky_plant",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_align_with_ground|density(raf_density_50),[["spiky_plant","0"]]),
  ("seedy_plant",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|density(raf_density_50),[["seedy_plant_a","0"]]),
  ("blue_flower",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|density(raf_density_30),[["blue_flower","0"]]),
  ("big_bush",fkf_plain|fkf_plain_forest|density(raf_density_30),[["big_bush","0"]]),

  ("bushes02_a",fkf_plain|fkf_plain_forest|density(raf_density_30),[["bushes02_a","bo_bushes02_a"],["bushes02_b","bo_bushes02_b"],["bushes02_c","bo_bushes02_c"]]),
  ("bushes03_a",fkf_plain|fkf_plain_forest|density(raf_density_30),[["bushes03_a","0"],["bushes03_b","0"],["bushes03_c","0"]]),
  ("bushes04_a",fkf_plain|fkf_plain_forest|density(raf_density_70),[["bushes04_a","0"],["bushes04_b","0"],["bushes04_c","0"]]),
  ("bushes05_a",fkf_plain|fkf_plain_forest|density(raf_density_70),[["bushes05_a","0"],["bushes05_b","0"],["bushes05_c","0"]]),
  ("bushes06_a",fkf_plain|fkf_plain_forest|density(raf_density_70),[["bushes06_a","0"],["bushes06_b","0"],["bushes06_c","0"]]),
  ("bushes07_a",fkf_plain|fkf_plain_forest|density(raf_density_70),[["bushes07_a","bo_bushes07_a"],["bushes07_b","bo_bushes07_b"],["bushes07_c","0"]]),
  ("bushes08_a",fkf_plain|fkf_plain_forest|density(raf_density_70),[["bushes08_a","0"],["bushes08_b","0"],["bushes08_c","0"]]),
  ("bushes09_a",fkf_plain|fkf_plain_forest|density(raf_density_70),[["bushes09_a","bo_bushes09_a"],["bushes09_b","bo_bushes09_b"],["bushes09_c","bo_bushes09_c"]]),
  ("bushes10_a",fkf_plain|fkf_plain_forest|density(raf_density_70),[["bushes10_a","bo_bushes10_a"],["bushes10_b","bo_bushes10_b"],["bushes10_c","bo_bushes10_c"]]),
  ("bushes11_a",fkf_plain|fkf_plain_forest|density(raf_density_70),[["bushes11_a","0"],["bushes11_b","0"],["bushes11_c","0"]]),
  ("bushes12_a",fkf_plain|fkf_plain_forest|fkf_align_with_ground|density(raf_density_50),[["bushes12_a","0"],["bushes12_b","0"],["bushes12_c","0"]]),

  ("aspen",fkf_plain|fkf_plain_forest|density(raf_density_70),[["tree_14_a","bo_tree_14_a"],["tree_14_b","bo_tree_14_b"],["tree_14_c","bo_tree_14_c"]]),
  ("pine_1",fkf_plain|fkf_plain_forest|fkf_tree|density(4),[("pine_1_a","bo_pine_1_a",("0","0")),("pine_1_b","bo_pine_1_b",("0","0"))]),
  ("pine_2",fkf_plain|fkf_plain_forest|fkf_tree|density(4),[["pine_2_a","bo_pine_2_a",("0","0")]]),
  ("pine_3",fkf_plain|fkf_plain_forest|fkf_tree|density(4),[["pine_3_a","bo_pine_3_a",("0","0")]]),
  ("pine_4",fkf_plain|fkf_plain_forest|fkf_tree|density(4),[["pine_4_a","bo_pine_4_a",("0","0")]]),
  ("pine_6",fkf_plain|fkf_plain_forest|fkf_tree|density(4),[["pine_6_a","bo_pine_6_a",("0","0")]]),
  ("snowy_pine",fkf_snow|fkf_snow_forest|fkf_tree|density(5),[["tree_snowy_a","bo_tree_snowy_a",("0","0")]]),
  ("snowy_pine_2",fkf_snow|fkf_snow_forest|fkf_tree|density(5),[["snowy_pine_2","bo_snowy_pine_2",("0","0")]]),
  ("small_rock",fkf_plain|fkf_plain_forest|fkf_tree|density(4),[["tree_17_a","bo_tree_17_a",("0","0")],["tree_17_b","bo_tree_17_b",("0","0")],["tree_17_c","bo_tree_17_c",("0","0")]]),
  ("rock_snowy",fkf_snow|fkf_snow_forest|fkf_realtime_ligting|fkf_rock|density(5),[["rock_snowy_a","bo_rock_snowy_a"],["rock_snowy_b","bo_rock_snowy_b"],["rock_snowy_c","bo_rock_snowy_c"],]),

  ("rock",fkf_plain|fkf_plain_forest|density(raf_density_70),[["pine_1_a","bo_pine_1_a",("0","0")],["pine_1_b","bo_pine_1_b",("0","0")],["bushes06_c","0"]]),
  ("rock_snowy2",fkf_snow|fkf_snow_forest|fkf_realtime_ligting|fkf_rock|density(5),[["tree_snowy_b","bo_tree_snowy_b"],["tree_snowy_b","bo_tree_snowy_b"],["tree_snowy_b","bo_tree_snowy_b"],]),


  ("tree_1",fkf_plain|fkf_plain_forest|density(raf_density_70),[("tree_2_a","bo_tree_2_a",("0","0")),("tree_2_b","bo_tree_2_b",("0","0"))]),
  ("tree_3",fkf_snow|fkf_snow_forest|fkf_realtime_ligting|fkf_rock|density(5),[("tree_3_a","0",("0","0")),("tree_3_b","0",("0","0"))]),
  
  ("bush_snowy",fkf_snow|fkf_snow_forest|fkf_realtime_ligting|fkf_rock|density(5),[["tree_3_a","0"],["tree_3_b","0"],]),
  ("bush_snowy2",fkf_snow|fkf_snow_forest|fkf_realtime_ligting|fkf_rock|density(5),[["tree_3_a","0"],["tree_3_b","0"],]),
  ("bush_snowy3",fkf_snow|fkf_snow_forest|fkf_tree|density(5),[["tree_3_a","0",("0","0")],["tree_3_b","0",("0","0")],]),
  ("bush_snowy4",fkf_snow|fkf_snow_forest|fkf_tree|density(5),[["tree_3_a","0",("0","0")],["tree_3_b","0",("0","0")],]),
  ("bush_snowy5",fkf_snow|fkf_snow_forest|fkf_realtime_ligting|fkf_rock|density(5),[["tree_3_a","0"],["tree_3_b","0"],]),
  ("bush_snowy6",fkf_snow|fkf_snow_forest|fkf_tree|density(5),[["tree_3_a","0",("0","0")],["tree_3_b","0",("0","0")],]),
  
  ("grass_snowy1",fkf_snow|fkf_snow_forest|fkf_realtime_ligting|fkf_rock|density(5),[["bushes06_a","0"],]),
  ("grass_snowy1b",fkf_snow|fkf_snow_forest|fkf_realtime_ligting|fkf_rock|density(5),[["wi_bush1","0"],]),
  ("grass_snowy2",fkf_snow|fkf_snow_forest|fkf_realtime_ligting|fkf_rock|density(5),[["wi_bush2a","0"],]),
  ("grass_snowy2b",fkf_snow|fkf_snow_forest|fkf_realtime_ligting|fkf_rock|density(5),[["wi_bush2b","0"],]),
  ("grass_snowy3a",fkf_snow|fkf_snow_forest|fkf_realtime_ligting|fkf_rock|density(5),[["wi_bush3a","0"],]),
  ("grass_snowy3b",fkf_snow|fkf_snow_forest|fkf_realtime_ligting|fkf_rock|density(5),[["wi_bush3b","0"],]),

  ("grass_snowy1",fkf_snow|fkf_snow_forest|fkf_realtime_ligting|fkf_rock|density(5),[["bushes06_b","0"],]),
  ("grass_snowy1b",fkf_snow|fkf_snow_forest|fkf_realtime_ligting|fkf_rock|density(5),[["wi_bush1","0"],]),
  ("grass_snowy2",fkf_snow|fkf_snow_forest|fkf_realtime_ligting|fkf_rock|density(5),[["wi_bush2a","0"],]),
  ("grass_snowy2b",fkf_snow|fkf_snow_forest|fkf_realtime_ligting|fkf_rock|density(5),[["wi_bush2b","0"],]),
  ("grass_snowy3a",fkf_snow|fkf_snow_forest|fkf_realtime_ligting|fkf_rock|density(5),[["wi_bush3a","0"],]),
  ("grass_snowy3b",fkf_snow|fkf_snow_forest|fkf_realtime_ligting|fkf_rock|density(5),[["wi_bush3b","0"],]),

  
  ("tree_4",fkf_plain|fkf_plain_forest|fkf_tree|density(4),[("tree_20_a","bo_tree_20_a",("0","0")),("tree_20_b","bo_tree_20_b",("0","0"))]),
  ("tree_5",fkf_plain|fkf_plain_forest|density(raf_density_70),[("tree_5_a","bo_tree_5_a",("0","0")),("tree_5_b","bo_tree_5_b",("0","0")),("tree_5_c","bo_tree_5_c",("0","0")),("tree_5_d","bo_tree_5_d",("0","0"))]),
  ("tree_6",fkf_plain|fkf_plain_forest|fkf_tree|density(4),[("tree_6_a","bo_tree_6_a",("0","0")),("tree_6_b","bo_tree_6_b",("0","0")),("tree_6_c","bo_tree_6_c",("0","0")),("tree_6_d","bo_tree_6_d",("0","0"))]),
  ("tree_7",fkf_plain|fkf_plain_forest|fkf_tree|density(4),[("tree_7_a","0",("0","0")),("tree_7_b","0",("0","0")),("tree_7_c","0",("0","0"))]),
  ("tree_8",fkf_plain|fkf_plain_forest|fkf_tree|density(4),[("tree_8_a","0",("0","0")),("tree_8_b","0",("0","0"))]),

  
  ("tree_9",fkf_align_with_ground|fkf_plain|fkf_plain_forest|density(raf_density_50),[("thorn_a","0"),("thorn_b","0"),("thorn_c","0")]),
  
  ("tree_10",fkf_plain|fkf_plain_forest|fkf_tree|density(4),[("tree_10_a","bo_tree_10_a",("0","0")),("tree_10_b","bo_tree_10_b",("0","0")),("tree_10_c","bo_tree_10_c",("0","0"))]),
  ("tree_11",fkf_plain|fkf_plain_forest|fkf_tree|density(4),[("tree_11_a","bo_tree_11_a",("0","0")),("tree_11_b","bo_tree_11_b",("0","0")),("tree_11_c","bo_tree_11_c",("0","0"))]),
  ("tree_12",fkf_plain|fkf_plain_forest|fkf_tree|density(4),[("tree_12_a","bo_tree_12_a",("0","0")),("tree_12_b","bo_tree_12_b",("0","0")),("tree_12_c","bo_tree_12_c",("0","0"))]),
  ("tree_14",fkf_plain|fkf_plain_forest|density(raf_density_70),[("tree_14_a","bo_tree_14_a",("0","0")),("tree_14_b","bo_tree_14_b",("0","0")),("tree_14_c","bo_tree_14_c",("0","0"))]),
  

  ("tree_15",fkf_plain|fkf_plain_forest|density(raf_density_70),[("tree_15_a","bo_tree_15_a"),("tree_15_b","bo_tree_15_b"),("tree_15_b","bo_tree_15_b")]),
  ("tree_16",fkf_plain|fkf_plain_forest|density(raf_density_70),[("rock_d","bo_rock_d"),("rock_i","bo_rock_i")]),

  ("tree_17",fkf_plain|fkf_plain_forest|fkf_tree|density(4),[("tree_17_a","bo_tree_17_a",("0","0")),("tree_17_b","bo_tree_17_b",("0","0")),("tree_17_c","bo_tree_17_c",("0","0")),("tree_17_d","bo_tree_17_d",("0","0"))]),

  ("palm",fkf_desert_forest|fkf_tree|density(4),[("palm_a","bo_palm_a",("0","0"))]), #tom new ntb model added 

  
  ("tree_new_1",fkf_plain|fkf_plain_forest|density(raf_density_30),[("tree_5_a","bo_tree_5_a"),("tree_5_b","bo_tree_5_b")]),
  
  ("bush_new_1",fkf_plain|fkf_plain_forest|density(raf_density_70),[["bushes10_a","bo_bushes10_a"],["bushes10_b","bo_bushes10_b"]]),
  ("bush_new_2",fkf_plain|fkf_plain_forest|density(raf_density_70),[["bushes06_a","0"]]),
  ("bush_new_3",fkf_plain|fkf_plain_forest|fkf_tree|density(4),[["rock_h","bo_rock_h",("0","0")],["rock_i","bo_rock_i",("0","0")],["rock_d","bo_rock_d",("0","0")],["rock_f","bo_rock_f",("0","0")],]),
  
  ("bush_new_4",fkf_plain|fkf_plain_forest|density(raf_density_70),[["rock_d","bo_rock_d"],["rock_i","bo_rock_i"]]),

  ("dry_bush",fkf_plain|fkf_plain_forest|density(raf_density_70),[["dry_bush","0"]]),
  ("dry_leaves",fkf_plain|fkf_plain_forest|density(raf_density_70),[["dry_leaves","0"]]),

  ("tree_new_2",fkf_plain|fkf_plain_forest|fkf_tree|density(4),[("tree_11_a","bo_tree_11_a",("0","0")),("tree_11_b","bo_tree_11_b",("0","0"))]),
  ("tree_new_3",fkf_plain|fkf_plain_forest|fkf_tree|density(4),[("tree_11_b","bo_tree_11_b",("0","0")),("tree_11_c","bo_tree_11_c",("0","0"))]),

  ("tree_plane",fkf_plain|fkf_plain_forest|fkf_tree|density(4),[("tree_16_a","bo_tree_16_a",("0","0")),("tree_16_b","bo_tree_16_b",("0","0"))]),
  ("tree_19",fkf_snow|fkf_snow_forest|fkf_realtime_ligting|fkf_rock|density(5),[("tree_19_a","bo_tree_19_a")]),
  ("beech",fkf_plain|fkf_plain_forest|fkf_tree|density(3),[("tree_17_a","bo_tree_17_a",("0","0")),("tree_17_b","bo_tree_17_b",("0","0"))]),

  ("tall_tree",fkf_plain|fkf_plain_forest|fkf_tree|density(4),[("tree_f_1","bo_tree_f_1",("0","0"))]),

  ("tree_e",fkf_plain|fkf_plain_forest|fkf_tree|density(4),[["tree_e_1","bo_tree_e_1",("0","0")],["tree_e_2","bo_tree_e_2",("0","0")],["tree_e_3","bo_tree_e_3",("0","0")]]),
  ("tree_f",fkf_plain|fkf_plain_forest|fkf_tree|density(4),[["tree_f_1","bo_tree_f_1",("0","0")],["tree_f_2","bo_tree_f_2",("0","0")],["tree_f_3","bo_tree_f_3",("0","0")]]),
  ("grape_vineyard",density(0),[("grape_vineyard","bo_grape_vineyard")]),
  ("grape_vineyard_stake",density(0),[("grape_vineyard_stake","bo_grape_vineyard_stake")]),  
  
  ("wheat",fkf_plain|fkf_plain_forest|density(4),[["wheat_a","0"],["wheat_b","0"],["wheat_c","0"],["wheat_d","0"]]),
  
  ("valleyRock_rounded",fkf_rock|density(5),[["valleyRock_rounded_1","bo_valleyRock_rounded_1"],["valleyRock_rounded_2","bo_valleyRock_rounded_2"],["valleyRock_rounded_3","bo_valleyRock_rounded_3"],["valleyRock_rounded_4","bo_valleyRock_rounded_4"]]),
  ("valleyRock_flat",fkf_rock|density(5),[["valleyRock_flat_1","bo_valleyRock_flat_1"],["valleyRock_flat_2","bo_valleyRock_flat_2"],["valleyRock_flat_3","bo_valleyRock_flat_3"],["valleyRock_flat_4","bo_valleyRock_flat_4"],["valleyRock_flat_5","bo_valleyRock_flat_5"],["valleyRock_flat_6","bo_valleyRock_flat_6"]]),
  ("valleyRock_flatRounded_small",fkf_rock|density(5),[["valleyRock_flatRounded_small_1","bo_valleyRock_flatRounded_small_1"],["valleyRock_flatRounded_small_2","bo_valleyRock_flatRounded_small_2"],["valleyRock_flatRounded_small_3","bo_valleyRock_flatRounded_small_3"]]),
  ("valleyRock_flatRounded_big",fkf_rock|density(5),[["valleyRock_flatRounded_big_1","bo_valleyRock_flatRounded_big_1"],["valleyRock_flatRounded_big_2","bo_valleyRock_flatRounded_big_2"]]),
  ]


def save_fauna_kinds():
  file = open("./flora_kinds.txt","w")
  file.write("%d\n"%len(fauna_kinds))
  for fauna_kind in fauna_kinds:
    meshes_list = fauna_kind[2]
    file.write("%s %d %d\n"%(fauna_kind[0], (dword_mask & fauna_kind[1]), len(meshes_list)))
    for m in meshes_list:
      file.write(" %s "%(m[0]))
      if (len(m) > 1):
        file.write(" %s\n"%(m[1]))
      else:
        file.write(" 0\n")
      if ( fauna_kind[1] & (fkf_tree|fkf_speedtree) ):  #if this fails make sure that you have entered the alternative tree definition (NOT FUNCTIONAL in Warband)
        speedtree_alternative = m[2]
        file.write(" %s %s\n"%(speedtree_alternative[0], speedtree_alternative[1]))
    if ( fauna_kind[1] & fkf_has_colony_props ):
      file.write(" %s %s\n"%(fauna_kind[3], fauna_kind[4]))
  file.close()

def two_to_pow(x):
  result = 1
  for i in xrange(x):
    result = result * 2
  return result

fauna_mask = 0x80000000000000000000000000000000
low_fauna_mask =             0x8000000000000000
def save_python_header():
  file = open("./fauna_codes.py","w")
  for i_fauna_kind in xrange(len(fauna_kinds)):
    file.write("%s_1 = 0x"%(fauna_kinds[i_fauna_kind][0]))
    file.write("%x\n"%(fauna_mask | two_to_pow(i_fauna_kind)))
    file.write("%s_2 = 0x"%(fauna_kinds[i_fauna_kind][0]))
    file.write("%x\n"%(fauna_mask | ((low_fauna_mask|two_to_pow(i_fauna_kind)) << 64)))
    file.write("%s_3 = 0x"%(fauna_kinds[i_fauna_kind][0]))
    file.write("%x\n"%(fauna_mask | ((low_fauna_mask|two_to_pow(i_fauna_kind)) << 64) | two_to_pow(i_fauna_kind)))
  file.close()

print "Exporting flora data..."
save_fauna_kinds()
