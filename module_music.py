from header_music import *
####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################

# WARNING: You MUST add mtf_module_track flag to the flags of the tracks located under module directory

tracks = [
  ("bogus", "cant_find_this.ogg", 0, 0),
  ("mount_and_blade_title_screen", "mount_and_blade_title_screen.ogg", mtf_module_track|mtf_sit_main_title|mtf_start_immediately, 0),
  ("captured", "capture.ogg", mtf_module_track, 0),

  ("empty_village", "empty_village.ogg", mtf_module_track|mtf_persist_until_finished, 0),
  ("escape", "escape.ogg", mtf_module_track|mtf_persist_until_finished, 0),
  ("retreat", "retreat.ogg", mtf_module_track|mtf_persist_until_finished|mtf_sit_killed, 0),
  
  #tom
  ("euro_1", "euro_1.ogg", mtf_module_track|mtf_tom_euro|mtf_sit_travel, 0),
  ("euro_2", "euro_2.ogg", mtf_module_track|mtf_tom_euro|mtf_sit_travel, 0),
  ("euro_3", "euro_3.ogg", mtf_module_track|mtf_tom_euro|mtf_sit_travel, 0),
  ("euro_4", "euro_4.ogg", mtf_module_track|mtf_tom_euro|mtf_sit_travel, 0),
  ("euro_5", "euro_5.ogg", mtf_module_track|mtf_tom_euro|mtf_sit_travel, 0),
  ("euro_6", "euro_6.ogg", mtf_module_track|mtf_tom_euro|mtf_sit_travel, 0),
  ("euro_7", "euro_7.ogg", mtf_module_track|mtf_tom_euro|mtf_sit_travel, 0),
  ("euro_8", "euro_8.ogg", mtf_module_track|mtf_tom_euro|mtf_sit_travel, 0),
  ("euro_9", "euro_9.ogg", mtf_module_track|mtf_tom_euro|mtf_sit_travel, 0),
  ("euro_10", "euro_10.ogg", mtf_module_track|mtf_tom_euro|mtf_sit_travel, 0),
  ("euro_11", "euro_11.ogg", mtf_module_track|mtf_tom_euro|mtf_sit_travel, 0),
  ("euro_12", "euro_12.ogg", mtf_module_track|mtf_tom_euro|mtf_sit_travel, 0),
  ("euro_13", "euro_13.ogg", mtf_module_track|mtf_tom_euro|mtf_sit_travel, 0),
  
  ("baltic_1", "baltic_1.ogg", mtf_module_track|mtf_tom_baltic|mtf_sit_travel, 0),
  ("baltic_2", "baltic_2.ogg", mtf_module_track|mtf_tom_baltic|mtf_sit_travel, 0),
  ("baltic_3", "baltic_3.ogg", mtf_module_track|mtf_tom_baltic|mtf_sit_travel, 0),
  ("baltic_4", "baltic_4.ogg", mtf_module_track|mtf_tom_baltic|mtf_sit_travel, 0),
  ("baltic_5", "baltic_5.ogg", mtf_module_track|mtf_tom_baltic|mtf_sit_travel, 0),
  
  ("rus_1", "rus_1.ogg", mtf_module_track|mtf_tom_rus|mtf_sit_travel, 0),
  ("rus_2", "rus_2.ogg", mtf_module_track|mtf_tom_rus|mtf_sit_travel, 0),
  ("rus_3", "rus_3.ogg", mtf_module_track|mtf_tom_rus|mtf_sit_travel, 0),
  ("rus_4", "rus_4.ogg", mtf_module_track|mtf_tom_rus|mtf_sit_travel, 0),
  
  ("saracen_1", "saracen_1.ogg", mtf_module_track|mtf_tom_saracen|mtf_sit_travel, 0),
  ("saracen_2", "saracen_2.ogg", mtf_module_track|mtf_tom_saracen|mtf_sit_travel, 0),
  ("saracen_3", "saracen_3.ogg", mtf_module_track|mtf_tom_saracen|mtf_sit_travel, 0),
  ("saracen_4", "saracen_4.ogg", mtf_module_track|mtf_tom_saracen|mtf_sit_travel, 0),
  ("saracen_5", "saracen_5.ogg", mtf_module_track|mtf_tom_saracen|mtf_sit_travel, 0),
  ("saracen_6", "saracen_6.ogg", mtf_module_track|mtf_tom_saracen|mtf_sit_travel, 0),
  ("saracen_7", "saracen_7.ogg", mtf_module_track|mtf_tom_saracen|mtf_sit_travel, 0),

  ("mong_1", "mong_1.ogg", mtf_module_track|mtf_tom_mong|mtf_sit_travel, 0),
  ("mong_2", "mong_2.ogg", mtf_module_track|mtf_tom_mong|mtf_sit_travel, 0),
  ("mong_3", "mong_3.ogg", mtf_module_track|mtf_tom_mong|mtf_sit_travel, 0),
  ("mong_4", "mong_4.ogg", mtf_module_track|mtf_tom_mong|mtf_sit_travel, 0),
  ("mong_5", "mong_5.ogg", mtf_module_track|mtf_tom_mong|mtf_sit_travel, 0),
  ("mong_6", "mong_6.ogg", mtf_module_track|mtf_tom_mong|mtf_sit_travel, 0),
  ("mong_7", "mong_7.ogg", mtf_module_track|mtf_tom_mong|mtf_sit_travel, 0),
  ("mong_8", "mong_8.ogg", mtf_module_track|mtf_tom_mong|mtf_sit_travel, 0),
  
  # ("travel_byz_1", "travel_byz_1.ogg", mtf_module_track|mtf_culture_byzantine|mtf_sit_travel, 0),
  # ("travel_byz_2", "travel_byz_2.ogg", mtf_module_track|mtf_culture_byzantine|mtf_sit_travel, 0),
  # ("travel_byz_3", "travel_byz_3.ogg", mtf_module_track|mtf_culture_byzantine|mtf_sit_travel, 0),
  # ("travel_byz_4", "travel_byz_4.ogg", mtf_module_track|mtf_culture_byzantine|mtf_sit_travel, 0),
  # ("travel_byz_5", "travel_byz_5.ogg", mtf_module_track|mtf_culture_byzantine|mtf_sit_travel, 0),
  
  # ("travel_all_1", "travel_gen_1.ogg", mtf_module_track|mtf_culture_generic|mtf_sit_travel,0),
  # ("travel_all_2", "travel_gen_2.ogg", mtf_module_track|mtf_culture_generic|mtf_sit_travel,0),
  # ("travel_all_3", "travel_gen_3.ogg", mtf_module_track|mtf_culture_generic|mtf_sit_travel,0),
  # ("travel_all_4", "travel_gen_4.ogg", mtf_module_track|mtf_culture_generic|mtf_sit_travel,0),
  # ("travel_all_5", "travel_gen_5.ogg", mtf_module_track|mtf_culture_generic|mtf_sit_travel,0),

  
  # ("travel_france_1", "travel_france_1.ogg", mtf_module_track|mtf_culture_france, 0),
  # ("travel_france_2", "travel_france_2.ogg", mtf_module_track|mtf_culture_france, 0),
  # ("travel_france_3", "travel_france_3.ogg", mtf_module_track|mtf_culture_france, 0),
  # ("travel_france_4", "travel_france_4.ogg", mtf_module_track|mtf_culture_france, 0),
  # ("travel_france_5", "travel_france_5.ogg", mtf_module_track|mtf_culture_france, 0),
  
  # ("travel_baltic_1", "travel_baltic_1.ogg", mtf_module_track|mtf_culture_baltic, 0),
  # ("travel_baltic_2", "travel_baltic_2.ogg", mtf_module_track|mtf_culture_baltic, 0),
  # ("travel_baltic_3", "travel_baltic_3.ogg", mtf_module_track|mtf_culture_baltic, 0),
  # ("travel_baltic_4", "travel_baltic_4.ogg", mtf_module_track|mtf_culture_baltic, 0),
  # ("travel_baltic_5", "travel_baltic_5.ogg", mtf_module_track|mtf_culture_baltic, 0),

  # ("travel_mongol_1", "travel_mongol_1.ogg", mtf_module_track|mtf_culture_mongol, 0),
  # ("travel_mongol_2", "travel_mongol_2.ogg", mtf_module_track|mtf_culture_mongol, 0),
  # ("travel_mongol_3", "travel_mongol_3.ogg", mtf_module_track|mtf_culture_mongol, 0),
  # ("travel_mongol_4", "travel_mongol_4.ogg", mtf_module_track|mtf_culture_mongol, 0),
  # ("travel_mongol_5", "travel_mongol_5.ogg", mtf_module_track|mtf_culture_mongol, 0),
  
  
  # ("travel_nordic_1", "travel_nordic_1.ogg", mtf_module_track|mtf_culture_nordic, 0),
  # ("travel_nordic_2", "travel_nordic_2.ogg", mtf_module_track|mtf_culture_nordic, 0),
  # ("travel_nordic_3", "travel_nordic_3.ogg", mtf_module_track|mtf_culture_nordic, 0),
  # ("travel_nordic_4", "travel_nordic_4.ogg", mtf_module_track|mtf_culture_nordic, 0),
  # ("travel_nordic_5", "travel_nordic_5.ogg", mtf_module_track|mtf_culture_nordic, 0),

  # ("travel_christian_1", "travel_christian_1.ogg", mtf_module_track|mtf_culture_crusader|mtf_sit_travel, 0),
  # ("travel_christian_2", "travel_christian_2.ogg", mtf_module_track|mtf_culture_crusader|mtf_sit_travel, 0),
  # ("travel_christian_3", "travel_christian_3.ogg", mtf_module_track|mtf_culture_crusader|mtf_sit_travel, 0),
  # ("travel_christian_4", "travel_christian_4.ogg", mtf_module_track|mtf_culture_crusader|mtf_sit_travel, 0),
  # ("travel_christian_5", "travel_christian_5.ogg", mtf_module_track|mtf_culture_crusader|mtf_sit_travel, 0),

  # ("travel_saracen_1", "travel_saracen_1.ogg", mtf_module_track|mtf_culture_saracen|mtf_sit_travel, 0),
  # ("travel_saracen_2", "travel_saracen_2.ogg", mtf_module_track|mtf_culture_saracen|mtf_sit_travel, 0),
  # ("travel_saracen_3", "travel_saracen_3.ogg", mtf_module_track|mtf_culture_saracen|mtf_sit_travel, 0),
  # ("travel_saracen_4", "travel_saracen_4.ogg", mtf_module_track|mtf_culture_saracen|mtf_sit_travel, 0),
  # ("travel_saracen_5", "travel_saracen_5.ogg", mtf_module_track|mtf_culture_saracen|mtf_sit_travel, 0),

  # ("travel_hre_1", "travel_hre_1.ogg", mtf_module_track|mtf_culture_hre, 0),
  # ("travel_hre_2", "travel_hre_2.ogg", mtf_module_track|mtf_culture_hre, 0),
  # ("travel_hre_3", "travel_hre_3.ogg", mtf_module_track|mtf_culture_hre, 0),
  # ("travel_hre_4", "travel_hre_4.ogg", mtf_module_track|mtf_culture_hre, 0),
  # ("travel_hre_5", "travel_hre_5.ogg", mtf_module_track|mtf_culture_hre, 0),
  
  # ("travel_central_1", "travel_central_1.ogg", mtf_module_track|mtf_culture_poland|mtf_sit_travel, 0),
  # ("travel_central_2", "travel_central_2.ogg", mtf_module_track|mtf_culture_poland|mtf_sit_travel, 0),
  # ("travel_central_3", "travel_central_3.ogg", mtf_module_track|mtf_culture_poland|mtf_sit_travel, 0),
  # ("travel_central_4", "travel_central_4.ogg", mtf_module_track|mtf_culture_poland|mtf_sit_travel, 0),
  # ("travel_central_5", "travel_central_5.ogg", mtf_module_track|mtf_culture_poland|mtf_sit_travel, 0),
#tom end
  ("victorious_evil", "victorious_evil.ogg", mtf_module_track|mtf_persist_until_finished, 0),
  
  ("wedding", "wedding.ogg", mtf_persist_until_finished, 0),
  ("coronation", "coronation.ogg", mtf_persist_until_finished, 0),
  
  ("ambient_1", "ambient_1.ogg", mtf_persist_until_finished|mtf_module_track|mtf_sit_fight|mtf_culture_all, 0),
  ("ambient_2", "ambient_2.ogg", mtf_persist_until_finished|mtf_module_track|mtf_sit_fight|mtf_culture_all, 0),
  ("ambient_3", "ambient_3.ogg", mtf_persist_until_finished|mtf_module_track|mtf_sit_fight|mtf_culture_all, 0),
  ("ambient_4", "ambient_4.ogg", mtf_persist_until_finished|mtf_module_track|mtf_sit_fight|mtf_culture_all, 0),
  ("ambient_5", "ambient_5.ogg", mtf_persist_until_finished|mtf_module_track|mtf_sit_fight|mtf_culture_all, 0),
  ("ambient_6", "ambient_6.ogg", mtf_persist_until_finished|mtf_module_track|mtf_sit_fight|mtf_culture_all, 0),
  ("ambient_7", "ambient_7.ogg", mtf_persist_until_finished|mtf_module_track|mtf_sit_fight|mtf_culture_all, 0),
  ("ambient_8", "ambient_8.ogg", mtf_persist_until_finished|mtf_module_track|mtf_sit_fight|mtf_culture_all, 0),
  ("ambient_9", "ambient_9.ogg", mtf_persist_until_finished|mtf_module_track|mtf_sit_fight|mtf_culture_all, 0),
  ("ambient_10", "ambient_10.ogg", mtf_persist_until_finished|mtf_module_track, 0),
  ("ambient_end", "silence.ogg", mtf_persist_until_finished|mtf_module_track, 0),
]

  