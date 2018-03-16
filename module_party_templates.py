from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001
pf_manor = icon_manor_icon|pf_label_small|pf_is_static|pf_hide_defenders
#pf_manor = icon_manor_icon|pf_label_small|pf_hide_defenders

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
  ("none","none",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("rescued_prisoners","Rescued Prisoners",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("enemy","Enemy",icon_gray_knight,0,fac_undeads,merchant_personality,[]),
  ("hero_party","Hero Party",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed. 
####################################################################################################################
##  ("old_garrison","Old Garrison",icon_vaegir_knight,0,fac_neutral,merchant_personality,[]),
  ("village_defenders","Village Defenders",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,10,20),(trp_peasant_woman,0,4)]),

  ("cattle_herd","Cattle Herd",icon_cattle|carries_goods(10),0,fac_neutral,escorted_merchant_personality,[(trp_cattle,80,120)]),  
##  ("vaegir_nobleman","Vaegir Nobleman",icon_vaegir_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_vaegir_knight,2,6),(trp_vaegir_horseman,4,12)]),
##  ("swadian_nobleman","Swadian Nobleman",icon_gray_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_swadian_knight,2,6),(trp_swadian_man_at_arms,4,12)]),
# Ryan BEGIN
  ("looters","Fures",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_looter,15,50)]),
  #("looters","Roving Robber Knight Band",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_mercenary_knight, 1, 2), (trp_looter,5,18)]),
# Ryan END
  ("manhunters","Manhunters",icon_gray_knight,0,fac_manhunters,soldier_personality,[(trp_manhunter,9,40)]),
  ("curonians",     "Kursi",     icon_axeman|carries_goods(2),0, fac_kingdom_35, soldier_personality, [(trp_balt_skirmisher,7,10),(trp_balt_footman,7,10),(trp_balt_jav,7,10),(trp_balt_veteran_jav,1,4),(trp_balt_billman,7,10),(trp_balt_spearman,7,10)]),
  ("prussians",     "Pruteni",      icon_axeman|carries_goods(2),0, fac_kingdom_34, soldier_personality, [(trp_balt_skirmisher,7,10),(trp_balt_footman,7,10),(trp_balt_jav,7,10),(trp_balt_veteran_jav,1,4),(trp_balt_billman,7,10),(trp_balt_spearman,7,10)]),
  ("samogitians",   "Zemaiciai",  icon_axeman|carries_goods(2),0, fac_kingdom_36, soldier_personality, [(trp_balt_skirmisher,7,10),(trp_balt_footman,7,10),(trp_balt_jav,7,10),(trp_balt_veteran_jav,1,4),(trp_balt_billman,7,10),(trp_balt_spearman,7,10)]),
  ("yotvingians",   "Jotvingiai",   icon_axeman|carries_goods(2),0, fac_kingdom_33, soldier_personality, [(trp_balt_skirmisher,7,10),(trp_balt_footman,7,10),(trp_balt_jav,7,10),(trp_balt_veteran_jav,1,4),(trp_balt_billman,7,10),(trp_balt_spearman,7,10)]),
  #("yotvingians",   "Jotvingiai",   icon_axeman|carries_goods(2),0, fac_kingdom_35, soldier_personality, [(trp_nordic_veteran_swordsman,90,100)]), 
  ("welsh",   "Cymry",   icon_axeman|carries_goods(2),0, fac_kingdom_37, soldier_personality, [(trp_merc_welsh_bowman,24,31)]),
  ("guelphs", "Guelphs", icon_gray_knight,0, fac_kingdom_40, soldier_personality, [(trp_iberian_knight,1,8), (trp_iberian_billman,15,30), (trp_iberian_veteran_crossbowman,10,15), (trp_iberian_veteran_spearman,10,15), (trp_iberian_light_cavalry,10, 15)]),
  ("ghibellines", "Ghibellines", icon_gray_knight,0, fac_kingdom_41, soldier_personality, [(trp_iberian_knight,1,4), (trp_merc_euro_guisarmer,10,15), (trp_merc_euro_range,10,15), (trp_merc_euro_spearman,10,15), (trp_iberian_light_cavalry,10, 15)]),
  ("crusaders", "Crusaders", icon_crusaders,0, fac_crusade, soldier_personality, [(trp_euro_horse_4, 10, 25), (trp_euro_spearman_2, 150, 200), (trp_merc_euro_range, 50, 100), (trp_merc_euro_guisarmer, 50, 100), (trp_merc_euro_spearman, 50, 100), (trp_merc_euro_horse, 25, 50)]),
  ("merc_party", "Angry band of alchoholics", icon_gray_knight|pf_show_faction, 0 , fac_commoners, soldier_personality,[]),
  ("crusader_raiders", "Crusaders", icon_crusaders|pf_show_faction, 0 , fac_kingdom_23, soldier_personality,[(trp_iberian_knight,1,4), (trp_iberian_light_cavalry,5, 10), (trp_iberian_town_footman_1, 10, 15), (trp_iberian_veteran_spearman, 5, 8), (trp_iberian_veteran_crossbowman, 5, 15), (trp_iberian_billman, 1,10),]),
  ("jihadist_raiders", "Jihadists", icon_khergit|pf_show_faction, 0 , fac_kingdom_25, soldier_personality,[(trp_bedouin_spearman,8,20),(trp_halqa_archer,5,8),(trp_bedouin_cav_2,4,10),(trp_halqa_cav_2,1,3),(trp_mamluke_turkoman_2,10,15)]),
  ("teutonic_raiders", "Crusaders", icon_crusaders|pf_show_faction, 0 , fac_kingdom_1, soldier_personality,[(trp_teu_horse_3, 1, 3), (trp_teu_town_2_2,2,6),(trp_teu_ger_1,3,10),(trp_teu_ger_2_1,5,10),(trp_teu_town_2_1,10,16),(trp_teu_town_3_2,5,8) ]),
  #village
  #("empty", "Fields", pf_manor,0, fac_commoners, bandit_personality, [(trp_manor_master, 1, 2)]), #this should be outside the range of a regular manor?
  ("manor", "Manor", pf_manor,0, fac_commoners, bandit_personality, [(trp_manor_master, 1, 2)]),
  ("farm", "Farm", pf_manor,0, fac_commoners, bandit_personality, [(trp_manor_master, 1, 2)]),
  ("linen", "Linen Workshop", pf_manor,0, fac_commoners, bandit_personality, [(trp_manor_master, 1, 2)]),
  ("salt", "Salt Trader", pf_manor,0, fac_commoners, bandit_personality, [(trp_manor_master, 1, 2)]),
  ("furs", "Hunter", pf_manor,0, fac_commoners, bandit_personality, [(trp_manor_master, 1, 2)]),
  ("iron", "Iron Trader", pf_manor,0, fac_commoners, bandit_personality, [(trp_manor_master, 1, 2)]),
  ("silk", "Silk Trader", pf_manor,0, fac_commoners, bandit_personality, [(trp_manor_master, 1, 2)]),
  #village - upgrade
  ("iron_mine", "Iron Mine", pf_manor,0, fac_commoners, bandit_personality, [(trp_manor_master, 1, 2)]),
  ("salt_mine", "Salt Mine", pf_manor,0, fac_commoners, bandit_personality, [(trp_manor_master, 1, 2)]),
  #town
  ("weapon", "Weapon Smithy", pf_manor,0, fac_commoners, bandit_personality, [(trp_manor_master, 1, 2)]),
  ("armor", "Armor Smithy", pf_manor,0, fac_commoners, bandit_personality, [(trp_manor_master, 1, 2)]),
  ("fletchery", "Fletchery", pf_manor,0, fac_commoners, bandit_personality, [(trp_manor_master, 1, 2)]),
  # ("whorehouse", "Brothel Village", pf_manor,0, fac_commoners, soldier_personality, []),

  #("whorehouse", "Brothel Village", pf_manor,0, fac_commoners, soldier_personality, []),
  
 # ("mercenery_camp", "Mercenary Camp", icon_merc_icon|pf_label_small|pf_is_static|pf_always_visible|pf_hide_defenders ,0, fac_commoners, soldier_personality, []),
  ("breeder", "Horse Breeder", pf_manor ,0, fac_commoners, soldier_personality, []),
  ("monastery", "Monastery", pf_manor,0, fac_commoners, soldier_personality, []), #moved for now
  
  #("blacksmith", "Blacksmith Village", pf_manor ,0, fac_commoners, soldier_personality, []),
 # ("trading_village", "Trading Village", pf_manor ,0, fac_commoners, soldier_personality, []),
  
  ("peasant_rebels_euro", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,soldier_personality,[]),
  # ("peasant_rebels_euro", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,soldier_personality,[(trp_rebel_leader,3,9),(trp_euro_village_recruit, 225, 340),(trp_euro_town_recruit, 75, 112)]),
  # ("peasant_rebels_scot", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,soldier_personality,[(trp_rebel_leader,3,9),(trp_scottish_village_recruit, 225, 340),(trp_euro_town_recruit, 75, 112)]), 
  # ("peasant_rebels_eastern", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,soldier_personality,[(trp_rebel_leader,3,9),(trp_rus_vil_1, 225, 340),(trp_rus_town_1, 150, 112)]),
  # ("peasant_rebels_nordic", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,soldier_personality,[(trp_rebel_leader,3,9),(trp_nordic_village_recruit, 225, 340),(trp_nordic_town_recruit, 150, 112)]),
  # ("peasant_rebels_mamluke", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,soldier_personality,[(trp_rebel_leader,3,9),(trp_halqa_recruit,100,125), (trp_bedouin_recruit,100,125),]),
  # ("peasant_rebels_marinid", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,soldier_personality,[(trp_rebel_leader,3,9),(trp_marinid_village_rabble,300,450)]),
  # ("peasant_rebels_andalus", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,soldier_personality,[(trp_rebel_leader,3,9),(trp_andalus_village_recruit,300,450)]),
  # ("peasant_rebels_mongol", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,soldier_personality,[(trp_rebel_leader,3,9),(trp_tatar_tribesman,300,450)]),
  # ("peasant_rebels_baltic", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,soldier_personality,[(trp_rebel_leader,3,9),(trp_balt_recruit,300,450)]),
    
##  ("peasant","Peasant",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,1,6),(trp_peasant_woman,0,7)]),

#  ("black_khergit_raiders","Black Khergit Raiders",icon_khergit_horseman_b|carries_goods(2),0,fac_black_khergits,bandit_personality,[(trp_black_khergit_guard,1,10),(trp_black_khergit_horseman,5,5)]),
  ("steppe_bandits","Sicarii Orientis",icon_khergit|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_steppe_bandit,15,58)]),
  ("taiga_bandits","Sicarii Borealis",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_taiga_bandit,15,58)]),
  ("desert_bandits","Sicarii Vasti",icon_vaegir_knight|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_desert_bandit,15,58)]),
  ("forest_bandits","Silvae Sicarii",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_forest_bandit,15,52)]),
  ("mountain_bandits","Montes Sicarii",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_mountain_bandit,15,60)]),
  ("sea_raiders","Piratae",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_sea_raider,20,50)]),
  ("robber_knights","Roving Robber Knight Band",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_euro_horse_4, 1, 2), (trp_raider,5,12)]),

  ("deserters","Deserti",icon_vaegir_knight|carries_goods(3),0,fac_deserters,bandit_personality,[]),
    
  ("merchant_caravan","Merchant Caravan",icon_gray_knight|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_merc_euro_horse,5,15)]),
  ("troublesome_bandits","Troublesome Bandits",icon_axeman|carries_goods(9)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_bandit,14,55)]),
  ("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,24,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
  ("kidnapped_girl","Kidnapped Girl",icon_woman|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),

##  ("farmers","Farmers",icon_peasant,0,fac_innocents,merchant_personality,[(trp_farmer,11,22),(trp_peasant_woman,16,44)]),
  ("village_farmers","Village Farmers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_farmer,8,18)]),
##  ("refugees","Refugees",icon_woman_b,0,fac_innocents,merchant_personality,[(trp_refugee,19,48)]),
##  ("dark_hunters","Dark Hunters",icon_gray_knight,0,fac_dark_knights,soldier_personality,[(trp_dark_knight,4,42),(trp_dark_hunter,13,25)]),

  ("spy_partners", "Unremarkable Travellers", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_merc_euro_horse,5,11)]),
  ("runaway_serfs","Runaway Serfs",icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_farmer,6,7), (trp_peasant_woman,3,3)]),
  ("spy", "Ordinary Townsman", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
  ("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),
##  ("conspirator", "Conspirators", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator,3,4)]),
##  ("conspirator_leader", "Conspirator Leader", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator_leader,1,1)]),
##  ("peasant_rebels", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,bandit_personality,[(trp_peasant_rebel,33,970)]),
##  ("noble_refugees", "Noble Refugees", icon_gray_knight|carries_goods(12)|pf_quest_party,0,fac_noble_refugees,merchant_personality,[(trp_noble_refugee,3,5),(trp_noble_refugee_woman,5,7)]),


  ("forager_party","Foraging Party",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("scout_party","Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
  ("patrol_party","Custodes",icon_gray_knight|carries_goods(2)|pf_show_faction,0,fac_commoners,soldier_personality,[]),
#  ("war_party", "War Party",icon_gray_knight|carries_goods(3),0,fac_commoners,soldier_personality,[]),
  ("messenger_party","Messenger",icon_gray_knight|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("raider_party","Raiders",icon_gray_knight|carries_goods(16)|pf_quest_party,0,fac_commoners,bandit_personality,[]),
  ("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
  ("kingdom_caravan_party","Caravan",icon_mule|carries_goods(45)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_merc_euro_horse,1,8)]),
  ("prisoner_train_party","Prisoner Train",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("default_prisoners","Default Prisoners",0,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),

  ("routed_warriors","Routed Enemies",icon_vaegir_knight,0,fac_commoners,soldier_personality,[]),


# Caravans
  ("center_reinforcements","Reinforcements",icon_axeman|carries_goods(16),0,fac_commoners,soldier_personality,[(trp_merc_euro_spearman,9,50)]), #tom - was town_recruit
  
  ("kingdom_hero_party","War Party",icon_flagbearer_a|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
  


# Reinforcements
#  ("default_reinforcements_a","default_reinforcements_a",0,0,fac_commoners,0,[(trp_caravan_guard,1,10),(trp_watchman,3,16),(trp_farmer,9,24)]),
#  ("default_reinforcements_b","default_reinforcements_b",0,0,fac_commoners,0,[(trp_mercenary,1,7),(trp_caravan_guard,3,10),(trp_watchman,3,15)]),
#  ("default_reinforcements_c","default_reinforcements_c",0,0,fac_commoners,0,[(trp_hired_blade,1,7),(trp_mercenary,3,10),(trp_caravan_guard,3,15)]),

  # Teutonic
  ("kingdom_teutonic_reinforcements_a", "{!}kingdom_teutonic_reinforcements_a", 0, 0, fac_kingdom_1, soldier_personality, [(trp_teu_horse_1,1,3), (trp_teu_village_recruit,4,9),(trp_teu_town_1,4,9)]),
  ("kingdom_teutonic_reinforcements_b", "{!}kingdom_teutonic_reinforcements_b", 0, 0, fac_kingdom_1, soldier_personality, [(trp_teu_town_2_2,2,6),(trp_teu_ger_1,1,3),(trp_teu_balt_1,1,3),(trp_teu_town_2_1,1,3)]),
  ("kingdom_teutonic_reinforcements_c", "{!}kingdom_teutonic_reinforcements_c", 0, 0, fac_kingdom_1, soldier_personality, [(trp_teu_horse_4, 3,6)]),

  # Lithuania
  ("kingdom_baltic_reinforcements_a", "{!}kingdom_baltic_reinforcements_a", 0, 0, fac_kingdom_2, soldier_personality, [(trp_balt_noble_recruit,1,3),(trp_balt_skirmisher,4,10),(trp_balt_footman,4,8)]),
  ("kingdom_baltic_reinforcements_b", "{!}kingdom_baltic_reinforcements_b", 0, 0, fac_kingdom_2, soldier_personality, [(trp_balt_archer,1,3),(trp_balt_jav,1,3),(trp_balt_veteran_jav,1,3),(trp_balt_billman,1,3),(trp_balt_spearman,1,3),(trp_balt_noble_1,1,3)]),
  ("kingdom_baltic_reinforcements_c", "{!}kingdom_baltic_reinforcements_c", 0, 0, fac_kingdom_2, soldier_personality, [(trp_balt_medium_cavalry,1,2),(trp_balt_noble_3, 1,3)]),

  # tatars
  ("kingdom_mongol_reinforcements_a", "{!}kingdom_mongol_reinforcements_a", 0, 0, fac_kingdom_3, soldier_personality, [(trp_tatar_skirmisher,5,14),(trp_tatar_tribesman,3,7)]),
  ("kingdom_mongol_reinforcements_b", "{!}kingdom_mongol_reinforcements_b", 0, 0, fac_kingdom_3, soldier_personality, [(trp_tatar_horse_archer,3,8),(trp_tatar_horseman, 1, 5),(trp_tatar_lancer, 1, 2)]),
  ("kingdom_mongol_reinforcements_c", "{!}kingdom_mongol_reinforcements_c", 0, 0, fac_kingdom_3, soldier_personality, [(trp_tatar_veteran_horse_archer,1,2),(trp_tatar_heavy_lancer,1,1)]),

  # Denmark
  ("kingdom_nordic_reinforcements_a", "{!}kingdom_nordic_reinforcements_a", 0, 0, fac_kingdom_4, soldier_personality, [(trp_nordic_village_recruit,5,12),(trp_nordic_town_recruit,6,9)]),
  ("kingdom_nordic_reinforcements_b", "{!}kingdom_nordic_reinforcements_b", 0, 0, fac_kingdom_4, soldier_personality, [(trp_nordic_veteran_archer,1,2),(trp_nordic_crossbowman,1,3),(trp_nordic_billman,1,3),(trp_nordic_veteran_spearman,1,3),(trp_nordic_spearman,1,3)]),
  ("kingdom_nordic_reinforcements_c", "{!}kingdom_nordic_reinforcements_c", 0, 0, fac_kingdom_4, soldier_personality, [(trp_nordic_knight, 1,2),(trp_nordic_swords_sergeant,2,3)]),
  
  # Poland
  ("kingdom_western_reinforcements_a", "{!}kingdom_western_reinforcements_a", 0, 0, fac_kingdom_5, soldier_personality, [(trp_euro_horse_1,3,7),(trp_euro_village_recruit,3,7),(trp_euro_town_recruit,3,7)]),
  ("kingdom_western_reinforcements_b", "{!}kingdom_western_reinforcements_b", 0, 0, fac_kingdom_5, soldier_personality, [(trp_euro_archer_2,1,3),(trp_euro_xbow_2,1,3),(trp_euro_guisarm_2,1,3),(trp_euro_spearman_3,1,3),(trp_euro_spearman_2,1,3)]),
  ("kingdom_western_reinforcements_c", "{!}kingdom_western_reinforcements_c", 0, 0, fac_kingdom_5, soldier_personality, [(trp_euro_horse_2, 2,5)]),

  # Novgorod
  ("kingdom_rus_reinforcements_a", "{!}kingdom_rus_reinforcements_a", 0, 0, fac_kingdom_8, soldier_personality, [(trp_rus_horse_1,1,3),(trp_rus_vil_1,6,13),(trp_rus_town_1,2,5)]),
  ("kingdom_rus_reinforcements_b", "{!}kingdom_rus_reinforcements_b", 0, 0, fac_kingdom_8, soldier_personality, [(trp_rus_vil_3_2,2,6),(trp_rus_vil_3_1,1,3),(trp_rus_town_4_2,1,3),(trp_rus_town_3_2,1,3)]),
  ("kingdom_rus_reinforcements_c", "{!}kingdom_rus_reinforcements_c", 0, 0, fac_kingdom_8, soldier_personality, [(trp_rus_horse_2,1,2),(trp_rus_horse_4, 1,3)]),

  # Scotland #TOM
  ("kingdom_scot_reinforcements_a", "{!}kingdom_scot_reinforcements_a", 0, 0, fac_kingdom_12, soldier_personality, [(trp_euro_horse_1,1,3),(trp_scottish_village_recruit,4,9),(trp_euro_town_recruit,4,9)]),
  ("kingdom_scot_reinforcements_b", "{!}kingdom_scot_reinforcements_b", 0, 0, fac_kingdom_12, soldier_personality, [(trp_euro_archer_2,1,3),(trp_euro_xbow_2,1,3),(trp_scottish_clansman,1,3),(trp_euro_spearman_2,1,3),(trp_scottish_forinsec_spearman,1,3)]),
  ("kingdom_scot_reinforcements_c", "{!}kingdom_scot_reinforcements_c", 0, 0, fac_kingdom_12, soldier_personality, [(trp_euro_horse_2, 2,5)]),

  # Ireland
  ("kingdom_gaelic_reinforcements_a", "{!}kingdom_gaelic_reinforcements_a", 0, 0, fac_kingdom_13, soldier_personality, [(trp_gaelic_light_cavalry,1,3),(trp_gaelic_village_recruit,4,9),(trp_gaelic_village_recruit,4,9)]),
  ("kingdom_gaelic_reinforcements_b", "{!}kingdom_gaelic_reinforcements_b", 0, 0, fac_kingdom_13, soldier_personality, [(trp_gaelic_archer_1,1,3),(trp_gaelic_archer_2,1,3),(trp_gaelic_infantry_2,1,3),(trp_gaelic_spearman_2,1,3),(trp_merc_gaelic_spearman,1,3)]),
  ("kingdom_gaelic_reinforcements_c", "{!}kingdom_gaelic_reinforcements_c", 0, 0, fac_kingdom_13, soldier_personality, [(trp_gaelic_knight, 2,5)]),

  ("kingdom_iberain_reinforcements_a", "{!}kingdom_iberain_reinforcements_a", 0, 0, fac_kingdom_16, soldier_personality, [(trp_iberian_light_cavalry,1,3),(trp_iberian_village_recruit,4,9),(trp_iberian_town_recruit,4,9)]),
  ("kingdom_iberain_reinforcements_b", "{!}kingdom_iberain_reinforcements_b", 0, 0, fac_kingdom_16, soldier_personality, [(trp_iberian_archer,1,3),(trp_iberian_veteran_crossbowman,1,3),(trp_iberian_billman,1,3),(trp_iberian_spears_sergeant,1,3),(trp_iberian_veteran_spearman,1,3)]),
  ("kingdom_iberain_reinforcements_c", "{!}kingdom_iberain_reinforcements_c", 0, 0, fac_kingdom_16, soldier_personality, [(trp_iberian_knight, 2,5)]),

  ("kingdom_italian_reinforcements_a", "{!}kingdom_italian_reinforcements_a", 0, 0, fac_kingdom_40, soldier_personality, [(trp_italian_light_cavalry,1,3),(trp_italian_village_recruit,4,9),(trp_italian_town_recruit,4,9)]),
  ("kingdom_italian_reinforcements_b", "{!}kingdom_italian_reinforcements_b", 0, 0, fac_kingdom_40, soldier_personality, [(trp_italian_archer,1,3),(trp_italian_veteran_crossbowman,1,3),(trp_italian_billman,1,3),(trp_iberian_spears_sergeant,1,3),(trp_italian_veteran_spearman,1,3)]),
  ("kingdom_italian_reinforcements_c", "{!}kingdom_italian_reinforcements_c", 0, 0, fac_kingdom_40, soldier_personality, [(trp_italian_knight, 2,5)]),
  
  ("kingdom_andalus_reinforcements_a", "{!}kingdom_andalus_reinforcements_a", 0, 0, fac_kingdom_20, soldier_personality, [(trp_andalus_village_recruit,13,32)]), # was 9, 21
  ("kingdom_andalus_reinforcements_b", "{!}kingdom_andalus_reinforcements_b", 0, 0, fac_kingdom_20, soldier_personality, [(trp_andalus_spearman_1, 2, 5),(trp_andalus_spearman_2, 2, 5),(trp_andalus_town_xbow_1, 3, 12)]), # 3, 7 2, 8
  ("kingdom_andalus_reinforcements_c", "{!}kingdom_andalus_reinforcements_c", 0, 0, fac_kingdom_20, soldier_personality, [(trp_andalus_horse_4 ,2,5)]),

  ("kingdom_byzantium_reinforcements_a", "{!}kingdom_byzantium_reinforcements_a", 0, 0, fac_kingdom_22, soldier_personality, [(trp_byz_castle_1,1,3),(trp_byz_village_1,4,9),(trp_byz_town_1,4,9)]),
  ("kingdom_byzantium_reinforcements_b", "{!}kingdom_byzantium_reinforcements_b", 0, 0, fac_kingdom_22, soldier_personality, [(trp_byz_village_3_1,1,3),(trp_byz_village_3_2,1,3),(trp_byz_town_3_1,2,6),(trp_byz_town_3_2,1,3)]),
  ("kingdom_byzantium_reinforcements_c", "{!}kingdom_byzantium_reinforcements_c", 0, 0, fac_kingdom_22, soldier_personality, [(trp_byz_castle_4, 2,5)]),

  ("kingdom_mamluke_reinforcements_a", "{!}kingdom_mamluke_reinforcements_a", 0, 0, fac_kingdom_25, soldier_personality, [(trp_halqa_recruit,4,9), (trp_mamluke_turkoman_1,1,3), (trp_bedouin_recruit,4,9), (trp_mamluke_turkoman_1,0,1)]),
  ("kingdom_mamluke_reinforcements_b", "{!}kingdom_mamluke_reinforcements_b", 0, 0, fac_kingdom_25, soldier_personality, [(trp_bedouin_spearman,1,3),(trp_halqa_archer,1,3),(trp_bedouin_cav_2,1,3),(trp_halqa_cav_2,1,3),(trp_mamluke_turkoman_2,1,3)]),
  ("kingdom_mamluke_reinforcements_c", "{!}kingdom_mamluke_reinforcements_c", 0, 0, fac_kingdom_25, soldier_personality, [(trp_mamluke_turkoman_3, 2,5)]),

  ("kingdom_marinid_reinforcements_a", "{!}kingdom_marinid_reinforcements_a", 0, 0, fac_kingdom_28, soldier_personality, [(trp_marinid_village_rabble,13,32)]), # was 9, 21
  ("kingdom_marinid_reinforcements_b", "{!}kingdom_marinid_reinforcements_b", 0, 0, fac_kingdom_28, soldier_personality, [(trp_marinid_light_spearmen, 2, 5),(trp_marinid_light_lancer, 2, 5),(trp_marinid_mounted_skirmisher_2, 3, 12)]), # 3, 7 2, 8
  ("kingdom_marinid_reinforcements_c", "{!}kingdom_marinid_reinforcements_c", 0, 0, fac_kingdom_28, soldier_personality, [(trp_marinid_mounted_skirmisher_2 ,3,6),(trp_marinid_mounted_skirmisher_2, 3,6)]),

  # Serbia
  ("kingdom_serbian_reinforcements_a", "{!}kingdom_serbian_reinforcements_a", 0, 0, fac_kingdom_29, soldier_personality, [(trp_serbian_horse_1,1,6),(trp_serbian_vil_recruit,6,11),(trp_serbian_town_recruit,2,4)]),
  ("kingdom_serbian_reinforcements_b", "{!}kingdom_serbian_reinforcements_b", 0, 0, fac_kingdom_29, soldier_personality, [(trp_serbian_vil_spearman,2,6),(trp_serbian_vil_archer,1,3),(trp_serbian_vil_spearman_veteran,1,3),(trp_serbian_vil_axeman,1,3), (trp_serbian_vil_archer,1,3)]),
  ("kingdom_serbian_reinforcements_c", "{!}kingdom_serbian_reinforcements_c", 0, 0, fac_kingdom_29, soldier_personality, [(trp_serbian_horse_2,1,2),(trp_serbian_horse_4, 1,3)]),

  # Bulgars
  ("kingdom_balkan_reinforcements_a", "{!}kingdom_balkan_reinforcements_a", 0, 0, fac_kingdom_30, soldier_personality, [(trp_balkan_horse_1,1,3),(trp_balkan_vil_1,2,7),(trp_balkan_town_1,6,11)]),
  ("kingdom_balkan_reinforcements_b", "{!}kingdom_balkan_reinforcements_b", 0, 0, fac_kingdom_30, soldier_personality, [(trp_balkan_vil_3_2_1,2,6),(trp_balkan_vil_3_1,1,3),(trp_balkan_town_3_1,1,3),(trp_balkan_town_3_2,1,3)]),
  ("kingdom_balkan_reinforcements_c", "{!}kingdom_balkan_reinforcements_c", 0, 0, fac_kingdom_30, soldier_personality, [(trp_balkan_horse_2,1,2),(trp_balkan_horse_4, 1,3)]),

  ("kingdom_welsh_reinforcements_a", "{!}kingdom_welsh_reinforcements_a", 0, 0, fac_kingdom_37, soldier_personality, [(trp_welsh_horse_1,1,2),(trp_welsh_recruit,5,10),(trp_welsh_archer_1,4,9) ]),
  ("kingdom_welsh_reinforcements_b", "{!}kingdom_welsh_reinforcements_b", 0, 0, fac_kingdom_37, soldier_personality, [(trp_welsh_archer_2,3,6),(trp_welsh_horse_2,1,1),(trp_welsh_spearman_1,1,2),(trp_welsh_spearman_2,1,2),(trp_welsh_archer_1,1,2)]),
  ("kingdom_welsh_reinforcements_c", "{!}kingdom_welsh_reinforcements_c", 0, 0, fac_kingdom_37, soldier_personality, [(trp_welsh_archer_2,1,2),(trp_welsh_horse_4, 1,3)]),

  ("steppe_bandit_lair" ,"Steppe Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_steppe_bandit,15,58)]),
  ("taiga_bandit_lair","Tundra Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_taiga_bandit,15,58)]),
  ("desert_bandit_lair" ,"Desert Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_desert_bandit,15,58)]),
  ("forest_bandit_lair" ,"Forest Bandit Camp",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_forest_bandit,15,58)]),
  ("mountain_bandit_lair" ,"Highway Bandit Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_mountain_bandit,15,58)]),
  ("sea_raider_lair","Sea Raider Landing",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_sea_raider,15,50)]),
  ("robber_knight_lair","Robber Knight's Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_euro_horse_4, 1, 1),(trp_raider,15,25)]),
  ("looter_lair","Kidnappers' Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_looter,15,25)]),

  ("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon_axeman|carries_goods(2)|pf_is_static,0,fac_outlaws,bandit_personality,[(trp_sea_raider,15,50)]),

  ("leaded_looters","Band of robbers",icon_axeman|carries_goods(8)|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_looter_leader,1,1),(trp_looter,3,3)]),

  ("pagan_stronghold",   "Pagan Stronghold", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_balt_skirmisher,5,7),(trp_balt_footman,5,7),(trp_balt_jav,5,7),(trp_balt_veteran_jav,1,3),(trp_balt_billman,5,7),(trp_balt_spearman,5,7)]),

   ##diplomacy begin
  ("dplmc_spouse","Your spouse",icon_woman|pf_civilian|pf_show_faction,0,fac_neutral,merchant_personality,[]),

  ("dplmc_gift_caravan","Your Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_merc_euro_horse,10,35)]),
#recruiter kit begin
   ("dplmc_recruiter","Recruiter",icon_gray_knight|pf_show_faction,0,fac_neutral,merchant_personality,[(trp_dplmc_recruiter,1,1)]),
#recruiter kit end
   ##diplomacy end
  ("crusaders_teutonic", "{!}crusaders_teutonic", 0, 0, fac_kingdom_23, soldier_personality, [(trp_teu_horse_3,1,6), (trp_teu_horse_4,1,3)]), 
  ("crusaders_templar", "{!}crusaders_templar", 0, 0, fac_kingdom_23, soldier_personality, [(trp_templar_half_brother,1,6), (trp_templar_knight,1,3)]), 
  ("crusaders_hospitaller", "{!}crusaders_hospitaller", 0, 0, fac_kingdom_23, soldier_personality, [(trp_hospitaller_half_brother,1,6), (trp_hospitaller_knight,1,3)]), 
  ("crusaders_lazarus", "{!}crusaders_lazarus", 0, 0, fac_kingdom_23, soldier_personality, [(trp_saint_lazarus_half_brother,1,6), (trp_saint_lazarus_knight,1,3)]), 
  ("crusaders_santiago", "{!}crusaders_santiago", 0, 0, fac_kingdom_23, soldier_personality, [(trp_santiago_half_brother,1,6), (trp_santiago_knight,1,3)]), 
  ("crusaders_calatrava", "{!}crusaders_calatrava", 0, 0, fac_kingdom_23, soldier_personality, [(trp_calatrava_half_brother,1,6), (trp_calatrava_knight,1,3)]), 
  ("crusaders_saint_thomas", "{!}crusaders_saint_thomas", 0, 0, fac_kingdom_23, soldier_personality, [(trp_saint_thomas_half_brother,1,6), (trp_saint_thomas_knight,1,3)]), 
   
  ("teutonic_reinforcements_a", "{!}teutonic_reinforcements_a", 0, 0, fac_kingdom_23, soldier_personality, [(trp_teu_horse_1,1,3), (trp_teu_village_recruit,4,9),(trp_teu_town_1,4,9)]),
  ("teutonic_reinforcements_b", "{!}teutonic_reinforcements_b", 0, 0, fac_kingdom_23, soldier_personality, [(trp_teu_town_2_2,2,6),(trp_teu_ger_1,1,3),(trp_teu_balt_1,1,3),(trp_teu_town_2_1,1,3)]),
  ("teutonic_reinforcements_c", "{!}teutonic_reinforcements_c", 0, 0, fac_kingdom_23, soldier_personality, [(trp_teu_horse_4, 3,6)]),

  ("templar_reinforcements_a", "{!}templar_reinforcements_a", 0, 0, fac_kingdom_23, soldier_personality, [(trp_crusader_turkopole,1,3), (trp_iberian_village_recruit,4,9),(trp_iberian_town_recruit,4,9)]),
  ("templar_reinforcements_b", "{!}templar_reinforcements_b", 0, 0, fac_kingdom_23, soldier_personality, [(trp_iberian_archer,1,3),(trp_iberian_veteran_crossbowman,1,3),(trp_iberian_billman,1,3),(trp_iberian_spears_sergeant,1,3),(trp_iberian_veteran_spearman,1,3)]),
  ("templar_reinforcements_c", "{!}templar_reinforcements_c", 0, 0, fac_kingdom_23, soldier_personality, [(trp_templar_knight, 3,6)]),

  ("hospitaller_reinforcements_a", "{!}hospitaller_reinforcements_a", 0, 0, fac_kingdom_23, soldier_personality, [(trp_crusader_turkopole,1,3), (trp_iberian_village_recruit,4,9),(trp_iberian_town_recruit,4,9)]),
  ("hospitaller_reinforcements_b", "{!}hospitaller_reinforcements_b", 0, 0, fac_kingdom_23, soldier_personality, [(trp_iberian_archer,1,3),(trp_iberian_veteran_crossbowman,1,3),(trp_iberian_billman,1,3),(trp_iberian_spears_sergeant,1,3),(trp_iberian_veteran_spearman,1,3)]),
  ("hospitaller_reinforcements_c", "{!}hospitaller_reinforcements_c", 0, 0, fac_kingdom_23, soldier_personality, [(trp_hospitaller_knight, 3,6)]),

  ("kingdom_21_reinforcements_a", "{!}kingdom_21_reinforcements_a", 0, 0, fac_papacy, soldier_personality, [(trp_euro_horse_1,1,3),(trp_euro_village_recruit,4,9),(trp_euro_town_recruit,4,9)]),
  ("kingdom_21_reinforcements_b", "{!}kingdom_21_reinforcements_b", 0, 0, fac_papacy, soldier_personality, [(trp_euro_archer_2,1,3),(trp_euro_xbow_2,1,3),(trp_euro_guisarm_2,1,3),(trp_euro_spearman_3,1,3),(trp_euro_spearman_2,1,3)]),
  ("kingdom_21_reinforcements_c", "{!}kingdom_21_reinforcements_c", 0, 0, fac_papacy, soldier_personality, [(trp_euro_horse_2, 2,5)]),

  ("roman_reinforcements_a", "{!}roman_reinforcements_a", 0, 0, fac_kingdom_22, soldier_personality, [(trp_byz_castle_1,1,3),(trp_byz_village_1,4,9),(trp_byz_town_1,4,9)]),
  ("roman_reinforcements_b", "{!}roman_reinforcements_b", 0, 0, fac_kingdom_22, soldier_personality, [(trp_byz_village_3_1,1,3),(trp_byz_village_3_2,1,3),(trp_byz_town_3_1,2,6),(trp_byz_town_3_2,1,3)]),
  ("roman_reinforcements_c", "{!}roman_reinforcements_c", 0, 0, fac_kingdom_22, soldier_personality, [(trp_byz_castle_2,1,2),(trp_byz_castle_4, 2,3),(trp_varangian_guard, 1, 5)]),

  ("armenian_reinforcements_c", "{!}armenian_reinforcements_c", 0, 0, fac_kingdom_23, soldier_personality, [(trp_anatolian_heavy_cavalry, 2,5)]),

  ("seljuk_reinforcements_c", "{!}seljuk_reinforcements_c", 0, 0, fac_kingdom_27, soldier_personality, [(trp_anatolian_turkoman_3, 2,5)]),
   
  ("almogabar", "{!}Lance", 0, 0, fac_neutral, soldier_personality, [(trp_merc_almogabar, 20, 20)]),
  ("welsh_merc", "{!}Lance", 0, 0, fac_neutral, soldier_personality, [(trp_merc_welsh_bowman, 20, 25), (trp_merc_welsh_bowman_commander, 1, 5)]),
  ("sicilian_merc_1", "{!}Lance", 0, 0, fac_neutral, soldier_personality, [(trp_merc_sicily_infantry_2, 5, 5),(trp_merc_sicily_infantry_1, 15, 15)]),
  ("sicilian_merc_2", "{!}Lance", 0, 0, fac_neutral, soldier_personality, [(trp_merc_sicily_foot_archer_2, 5, 5),(trp_merc_sicily_foot_archer_1, 15, 15)]),
  ("sicilian_merc_3", "{!}Lance", 0, 0, fac_neutral, soldier_personality, [(trp_merc_sicily_horse_archer_2, 5, 5),(trp_merc_sicily_horse_archer_1, 15, 15)]),
  ("zanata_merc", "{!}Lance", 0, 0, fac_neutral, soldier_personality, [(trp_merc_maghreb_horse, 10, 10),(trp_merc_maghreb_spearman, 10, 10),(trp_merc_maghreb_range, 10, 10)]),

  #################MERC COMPANIES
  ##generic
  ("generic_euro", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_merc_euro_spearman, 12, 15),(trp_merc_euro_guisarmer, 5, 7),(trp_merc_euro_range, 6, 10),(trp_merc_euro_horse, 3, 7)]),
  ("generic_balt", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_merc_balt_spearman, 12, 15),(trp_merc_balt_guisarmer, 5, 7),(trp_merc_balt_range, 6, 10),(trp_merc_balt_horse, 3, 7)]),
  ("generic_maghreb", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_merc_maghreb_spearman, 14, 23),(trp_merc_maghreb_range, 6, 10),(trp_merc_maghreb_horse, 3, 7)]),
  ("generic_rus", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_merc_rus_spearman, 12, 15),(trp_merc_rus_guisarmer, 5, 7),(trp_merc_rus_range, 6, 10),(trp_merc_rus_horse, 3, 7)]),
  ("generic_latin", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_merc_latin_spearman, 10, 13),(trp_merc_latin_guisarmer, 4, 6),(trp_merc_latin_range, 5, 8),(trp_merc_latin_horse, 2, 5), (trp_merc_latin_light, 7, 12)]),
  ("generic_balkan", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_merc_balkan_spearman, 12, 15),(trp_merc_balkan_guisarmer, 5, 7),(trp_merc_balkan_range, 6, 10),(trp_merc_balkan_horse, 3, 7)]),
  ("generic_scan", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_merc_scan_spearman, 12, 15),(trp_merc_scan_guisarmer, 5, 7),(trp_merc_scan_range, 6, 10),(trp_merc_scan_horse, 3, 7)]),
  ("generic_gaelic", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_merc_gaelic_spearman, 12, 15),(trp_merc_gaelic_axeman_1, 5, 7),(trp_merc_gaelic_spearman_2, 6, 10),(trp_merc_gaelic_axeman_2, 3, 7)]),
  ("generic_mamluk", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_merc_mamluke_spearman, 12, 15),(trp_merc_mamluke_javalin, 7, 10),(trp_merc_mamluke_range, 5, 7),(trp_merc_mamluke_syrian, 3, 7)]),
  ##historical
  ("company_genoese", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_genoese_crossbowman, 25, 32),(trp_genoese_crossbowman_commander, 1, 5)]),
  ("company_brabantine", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_merc_brabantine_spearman, 12, 15),(trp_merc_brabantine_guisarm, 4, 7),(trp_merc_brabantine_xbow, 6, 10)]),
  ("company_welsh", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_merc_welsh_bowman, 12, 15),(trp_merc_kern_infantry, 10, 15),(trp_merc_welsh_bowman_commander, 1, 3)]),
  ("company_mamlukes", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_mamluke_medium_horse_archer, 5, 8),(trp_mamluke_heavy_horse_archer, 2, 3),(trp_mamluke_elite_horse_archer, 1, 3)]),
  ("company_sicily", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_merc_sicily_infantry_1, 12, 15),(trp_merc_sicily_infantry_2, 4, 7),(trp_merc_sicily_foot_archer_1, 6, 10), (trp_merc_sicily_foot_archer_2, 1, 5),(trp_merc_sicily_horse_archer_1, 1, 5),(trp_merc_sicily_horse_archer_2, 1, 5)]),
  ("company_cuman", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_cuman_skirmisher, 12, 15),(trp_cuman_horseman, 4, 7),(trp_cuman_horse_archer, 6, 10),(trp_cuman_veteran_horse_archer, 3, 7),(trp_cuman_lancer, 1, 3),(trp_cuman_heavy_lancer, 1, 3)]),
  ("company_georgian", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_georgian_lancer, 12, 18),(trp_goergian_horse_archer, 10, 18)]),
  ("company_turkopoles", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_crusader_turkopole, 18, 32)]),
  ("company_varangian", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_varangian_guard, 18, 32)]),
  ("company_kwarezmian", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_kwarezmian_range, 12, 15),(trp_kwarezmian_light_horse, 10, 18),(trp_kwarezmian_medium_horse, 6, 8)]),
  ("company_mordovian", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_mordovian_foot, 12, 18),(trp_mordovian_range, 4, 7),(trp_mordovian_horse, 6, 10)]),
  ("company_kipchak", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_kipchak_range, 10, 15),(trp_kipchak_light_horse, 5, 9),(trp_kipchak_medium_horse, 5, 7)]),
  ##crusader
  ("company_teutons", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_teu_horse_3, 1, 6), (trp_teu_horse_4, 1, 2)]),
  ("company_hospitalier", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_hospitaller_half_brother, 1, 6), (trp_hospitaller_knight, 1, 2)]),
  ("company_templar", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_templar_half_brother, 1, 6), (trp_templar_knight, 1, 2)]),
  ("company_lazarus", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_saint_lazarus_half_brother, 1, 6), (trp_saint_lazarus_knight, 1, 2)]),
  ("company_santiago", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_santiago_half_brother, 1, 6), (trp_santiago_knight, 1, 2)]),
  ("company_calatrava", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_calatrava_half_brother, 1, 6), (trp_calatrava_knight, 1, 2)]),
  ("company_thomas", "{!}Company", 0, 0, fac_neutral, soldier_personality, [(trp_saint_thomas_half_brother, 1, 6), (trp_saint_thomas_knight, 1, 2)]),

  ("mongolian_camp","Mongolian horde",icon_khergit|pf_label_small|carries_goods(5)|pf_show_faction,0,fac_commoners,soldier_personality,[(trp_tatar_veteran_horse_archer,1,2),(trp_tatar_heavy_lancer,1,1),(trp_tatar_skirmisher,10,14),(trp_tatar_tribesman,8,13)]),
]
