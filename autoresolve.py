import string
from process_common import *
from module_troops import *
from module_items import *

# pulls the gigantor values out of the skill blob and returns a 3-tuple
# containing power draw, power strike, and power draw skill values.
def kt_get_power_skills( flags ):
   pdraw = 0
   pstrk = 0
   pthrw = 0
   pdraw_top = knows_power_draw_10 + knows_power_draw_5
   pstrk_top = knows_power_strike_10 + knows_power_strike_5
   pthrw_top = knows_power_throw_10 + knows_power_throw_5
   
   if ( flags & pdraw_top ) > 0:
      pdraw = flags & pdraw_top
      pdraw /= knows_power_draw_1
   if ( flags & pstrk_top ) > 0:
      pstrk = flags & pstrk_top
      pstrk /= knows_power_strike_1
   if ( flags & pthrw_top ) > 0:
      pthrw = flags & pthrw_top
      pthrw /= knows_power_throw_1
   
   return (pdraw, pstrk, pthrw)

# pulls the gigantor values out of the skill blob and returns a 3-tuple
# containing shield, athletics, and ironflesh skill values.
def kt_get_melee_skills( flags ):
   shld = 0
   athl = 0
   irfl = 0
   shld_top = knows_shield_10 + knows_shield_5
   athl_top = knows_athletics_10 + knows_athletics_5
   irfl_top = knows_ironflesh_10 + knows_ironflesh_5
   
   if ( flags & shld_top ) > 0:
      shld = flags & shld_top
      shld /= knows_shield_1
   if ( flags & athl_top ) > 0:
      athl = flags & athl_top
      athl /= knows_athletics_1
   if ( flags & irfl_top ) > 0:
      irfl = flags & irfl_top
      irfl /= knows_ironflesh_1
   
   return (shld, athl, irfl)

# parse troop items and return a tuple containing average item values. 
# we make assumptions on the flags and average gear of the same type
# to get aggregate values.  note that the weights given to items in a
# list that aren't guaranteed with a tf_ flag are a guess.  i'm counting
# no flag as a 0 value in the average which might not be correct.
def kt_parse_troop_items( item_list, flags, ohprof, thprof, poleprof, bowprof, xbowprof, throwprof, pstrike, pdraw, pthrow ):
   mw_value = 0 # melee weapon damage of the greater if multiple
   mw_count = 0 # never seen a guy without a weapon O_O
   rw_value = 0 # ranged weapon damage
   rw_count = 1
   ha_value = 0 # head armor
   ha_count = 1
   ba_value = 0 # body armor
   ba_count = 1
   fa_value = 0 # foot armor
   fa_count = 1
   na_value = 0 # hand armor
   na_count = 1
   sh_value = 0 # shield percentage 0-100
   sh_count = 1
   ho_value = 0 # horse aggregate charge and armor value
   ho_count = 1

   guarantee_horse = 0
   guarantee_ranged = 0
   troop_type = kt_troop_type_footsoldier

   # parse guarantee flags
   if ( flags & tf_guarantee_boots ) > 0:
      fa_count = 0
   if ( flags & tf_guarantee_armor ) > 0:
      ba_count = 0
   if ( flags & tf_guarantee_helmet ) > 0:
      ha_count = 0
   if ( flags & tf_guarantee_horse ) > 0:
      ho_count = 0
      guarantee_horse = 1
   if ( flags & tf_guarantee_shield ) > 0:
      sh_count = 0
   if ( flags & tf_guarantee_ranged ) > 0:
      rw_count = 0
      guarantee_ranged = 1

   # divine the troop type from the guarantee flags.  this isn't 100%.
   if guarantee_horse and guarantee_ranged:
      troop_type = kt_troop_type_mtdarcher
   elif guarantee_horse and not guarantee_ranged:
      troop_type = kt_troop_type_cavalry
   elif not guarantee_horse and guarantee_ranged:
      troop_type = kt_troop_type_archer
   else:
      troop_type = kt_troop_type_footsoldier
   
   # constants
   pierce_flag = pierce << iwf_damage_type_bits
   blunt_flag = blunt << iwf_damage_type_bits

   # parse each item
   # once we know the type, we pull the values from the appropriate places.
   # if we don't know the type, we ignore the item.  we also ignore ammo
   # and books and a handful of other things intentionally.
   for item in item_list:
      item_type = items[item][3] & 0xFF
      if itp_type_horse == item_type:
         ho_count += 1
         chg = get_thrust_damage( items[item][6] )
         arm = get_body_armor( items[item][6] )
         ho_value += chg
         ho_value += (arm+5)/10
      # we only consider the higher of thrust or swing damage
      elif item_type in (itp_type_one_handed_wpn, itp_type_two_handed_wpn, itp_type_polearm):
         mw_count += 1
         swd = get_swing_damage( items[item][6] )
         thd = get_thrust_damage( items[item][6] )
         speed = get_speed_rating( items[item][6] )
         if (swd & pierce_flag) > 0:
            swd &= 0xFF
            swd *= 3
            swd /= 2
         elif (swd & blunt_flag) > 0:
            swd &= 0xFF
            swd *= 5
            swd /= 4
         if (thd & pierce_flag) > 0:
            thd &= 0xFF
            thd *= 3
            thd /= 2
         elif (thd & blunt_flag) > 0:
            thd &= 0xFF
            thd *= 5
            thd /= 4
         # also modify by speed rating and proficiency
         prof = 100
         if item_type == itp_type_one_handed_wpn:
            prof = ohprof
         elif item_type == itp_type_two_handed_wpn:
            prof = thprof
         elif item_type == itp_type_polearm:
            prof = poleprof            
         swd *= speed
         swd *= prof
         thd *= speed
         thd *= prof
         if pstrike > 0:
            swd *= (100 + pstrike * 8)
            swd /= 100
            thd *= (100 + pstrike * 8)
            thd /= 100
         swd /= 10000
         thd /= 10000
         if swd > thd:
            mw_value += swd
         else:
            mw_value += thd
      elif item_type in (itp_type_bow, itp_type_crossbow, itp_type_thrown):
         rw_count += 1
         rdam = get_thrust_damage( items[item][6] )
         # adjust for type
         if (rdam & pierce_flag) > 0:
            rdam &= 0xFF
            rdam *= 3
            rdam /= 2
         elif (rdam & blunt_flag) > 0:
            rdam &= 0xFF
            rdam *= 5
            rdam /= 4
         # adjust for speed and accuracy
         acc = get_leg_armor( items[item][6] )
         spd = get_speed_rating( items[item][6] )
         if acc == 0:
            acc = 100
         rdam *= acc
         rdam *= spd
         # adjust for proficiency
         if item_type == itp_type_bow:
            rdam *= bowprof
            if pdraw > 0:
               pdraw_amt = get_difficulty( items[item][6] )
               pdraw_amt += 4
               if pdraw < pdraw_amt:
                  pdraw_amt = pdraw
               rdam *= (100 + pdraw_amt*14)
               rdam /= 100
         elif item_type == itp_type_crossbow:
            rdam *= xbowprof
         elif item_type == itp_type_thrown:
            rdam *= throwprof
            if pthrow > 0:
               rdam *= (100 + pthrow*10)
               rdam /= 100
         rdam /= 1000000
         rw_value += rdam
      elif itp_type_shield == item_type:
         sh_count += 1
         sh_value += get_weapon_length( items[item][6] )
      elif item_type in (itp_type_head_armor, itp_type_body_armor, itp_type_foot_armor, itp_type_hand_armor):
         if itp_type_head_armor == item_type:            
            ha_count += 1
         elif itp_type_body_armor == item_type:
            ba_count += 1
         elif itp_type_foot_armor == item_type:
            fa_count += 1
         elif itp_type_hand_armor == item_type:
            na_count += 1
            na_value += get_body_armor( items[item][6] )
         else:
            print "ERROR:  item ", items[item][0], " is unknown armor type!" # shouldn't ever get this
         ba_value += get_body_armor( items[item][6] )
         fa_value += get_leg_armor( items[item][6] )
         ha_value += get_head_armor( items[item][6] )

   # do the averaging; values will be rough
   if ba_count > 0:   # nb:  this doesn't catch no body armor + gloves case
      ba_value -= na_value
      ba_value /= ba_count
      if na_count > 0:
         na_value /= na_count
      ba_value += na_value
   if ha_count > 0:
      ha_value /= ha_count
   if fa_count > 0:
      fa_value /= fa_count
   if mw_count > 0:
      mw_value /= mw_count
   if rw_count > 0:
      rw_value /= rw_count
   if sh_count > 0:
      sh_value /= sh_count
   if ho_count > 0:
      ho_value /= ho_count

   return (mw_value, rw_value, ha_value, ba_value, fa_value, sh_value, ho_value, troop_type)

# generates code tuples for setting slots based on values accessible
# during compile.  this gets inserted into the scripts array and parsed
# like any other module code. 
def kt_python_init_troop_slots():
   module_code = []
   
   # figure out our bounds
   underscore_pos = string.find( soldiers_begin, "_" )
   id_str = soldiers_begin[ underscore_pos+1:len(soldiers_begin) ]
   begin_troop = find_troop( troops, id_str )
   underscore_pos = string.find( soldiers_begin, "_" )
   id_str = soldiers_end[ underscore_pos+1 : len(soldiers_end) ]   
   end_troop = find_troop( troops, id_str )
      
   # process for each troop
   for i_troop in range(begin_troop, end_troop+1):
      oneh_prof = (troops[i_troop][9] >> one_handed_bits) & 0x3FF
      twoh_prof = (troops[i_troop][9] >> two_handed_bits) & 0x3FF
      pole_prof = (troops[i_troop][9] >> polearm_bits) & 0x3FF
      arch_prof = (troops[i_troop][9] >> archery_bits) & 0x3FF
      xbow_prof = (troops[i_troop][9] >> crossbow_bits) & 0x3FF
      thrw_prof = (troops[i_troop][9] >> throwing_bits) & 0x3FF
      att_str = (troops[i_troop][8] & 0xFF)
      att_agi = (troops[i_troop][8] & 0xFF00) >> 8
      att_int = (troops[i_troop][8] & 0xFF0000) >> 16
      att_cha = (troops[i_troop][8] & 0xFF000000) >> 24
      # setup special skills (add whatever you care about here as well)
      (skill_pdraw, skill_pstrike, skill_pthrow) = kt_get_power_skills( troops[i_troop][10] )
      (skill_shld, skill_athl, skill_irfl) = kt_get_melee_skills( troops[i_troop][10] )
      mw_value = 0
      rw_value = 0
      ha_value = 0
      ba_value = 0
      fa_value = 0
      sh_value = 0
      ho_value = 0
      troop_type = 0
      (mw_value, rw_value, ha_value, ba_value, fa_value, sh_value, ho_value, troop_type) = kt_parse_troop_items( troops[i_troop][7], troops[i_troop][3], oneh_prof, twoh_prof, pole_prof, arch_prof, xbow_prof, thrw_prof, skill_pstrike, skill_pdraw, skill_pthrow )
      d_val = ha_value + ba_value + fa_value + sh_value
      d_val /= 5
      d_val += skill_irfl*2
      d_val += att_str
      if troop_type in (kt_troop_type_mtdarcher, kt_troop_type_archer):
         o_val = mw_value / 3 + rw_value
      if troop_type in (kt_troop_type_footsoldier, kt_troop_type_cavalry):
         o_val = mw_value + rw_value / 4
      h_val = ho_value
      module_code.append( (troop_set_slot, "trp_"+troops[i_troop][0], kt_slot_troop_o_val, o_val) )
      module_code.append( (troop_set_slot, "trp_"+troops[i_troop][0], kt_slot_troop_d_val, d_val) )
      module_code.append( (troop_set_slot, "trp_"+troops[i_troop][0], kt_slot_troop_h_val, h_val) )
   
      old_val = troops[i_troop][8]
      old_val >>= level_bits
      old_val &= level_mask
      old_val += 12
      old_val *= old_val
      old_val /= 100
      troop_string = "footsoldier"
      if troop_type == kt_troop_type_cavalry:
         troop_string = "cavalry"
      if troop_type == kt_troop_type_archer:
         troop_string = "archer"
      if troop_type == kt_troop_type_mtdarcher:
         troop_string = "mtdarcher"
         
   return module_code[:]
  
   ( "kt_init_troop_slots", kt_python_init_troop_slots() ),

   # kt0:  new strength calculation
   # this script makes use of new slots that are filled out at init time with
   # script code that was generated at compile time.  the range of the values
   # coming out of this script are much larger (about 100x) than the original
   # range.  furthermore, we add a defense calculation and troop count to the
   # returns.
   # INPUT: 
   #      arg1:  party_id
   #      arg2:  exclude leader
   #      arg3:  is siege
   # OUTPUT:
   #      reg0:  offense value
   #      reg1:  defense value (damage redux in percent)
   #      reg2:  troop count
   ( "kt_party_calculate_strength",
   [
      # remember our params
      (store_script_param_1, ":party"),   # party id
      (store_script_param_2, ":exclude_leader"), # also a party id apparently
      (store_script_param, ":is_siege", 3), # so we don't count horses for sieges

      # clear out our returns and temps
      (assign, reg0, 0),
      (assign, reg1, 0),
      (assign, reg2, 0),

      # figure out which stack to start with and how many we have
      (party_get_num_companion_stacks, ":num_stacks", ":party"),
      (assign, ":first_stack", 0),
      (try_begin),
         (neq, ":exclude_leader", 0),
         (assign, ":first_stack", 1),
      (try_end),

      # for each stack that we care about, grab the offense, defense and count
      # and stuff the values into our return registers. 
      (try_for_range, ":i_stack", ":first_stack", ":num_stacks"),
         (party_stack_get_troop_id, ":stack_troop", ":party", ":i_stack"),
         (party_stack_get_size, ":stack_size",":party",":i_stack"),
         (party_stack_get_num_wounded, ":num_wounded",":party",":i_stack"),
         (val_sub, ":stack_size", ":num_wounded"),
         (gt, ":stack_size", 0),
         (assign, ":o_val", 0),
         (assign, ":d_val", 0),
         (assign, ":h_val", 0),
         (assign, ":tr_type", 0),
         (try_begin),
            # if this is not a hero, just read slots
            (neg|troop_is_hero, ":stack_troop"),
            (troop_get_slot, ":o_val", ":stack_troop", kt_slot_troop_o_val),
            (troop_get_slot, ":d_val", ":stack_troop", kt_slot_troop_d_val),
            (troop_get_slot, ":h_val", ":stack_troop", kt_slot_troop_h_val),
            (troop_get_slot, ":tr_type", ":stack_troop", kt_slot_troop_type),
            # zero out horse bonuses for mounted archers.  they aren't
            # supposed to be charging into the fray.
            (try_begin),
               (eq, ":tr_type", kt_troop_type_mtdarcher),
               (assign, ":h_val", 0),
            (try_end),
            # mul by stack size
            (val_mul, ":o_val", ":stack_size"),
            (val_mul, ":d_val", ":stack_size"),
            (val_mul, ":h_val", ":stack_size"),
         (else_try),
            # todo:  heroes have different rules since they don't have troop
            # templates.  for now, we'll use 50 + level*3 for o_val and
            # 20 + level*2 for d_val.  in the future, this should be replaced
            # by a gear lookup.
            (store_character_level, ":level", ":stack_troop"),
            (store_mul, ":o_val", ":level", 3),
            (val_add, ":o_val", 50),
            (store_mul, ":d_val", ":level", 2),
            (val_add, ":d_val", 20),
         (try_end),
         
         # siege checks
         (try_begin),
            # if not sieging, mounted guys get a bonus.
            (eq, ":is_siege", 0),
            (try_begin),
               # mounted archers only get 50% more defense
               (eq, ":tr_type", kt_troop_type_mtdarcher),
               (val_mul, ":d_val", 3),
               (val_div, ":d_val", 2),
            (else_try),
               # cavalry get 50% more attack and defense and add h_val to o_val
               (eq, ":tr_type", kt_troop_type_cavalry),
               (val_mul, ":o_val", 3),
               (val_div, ":o_val", 2),
               (val_add, ":o_val", ":h_val"),
               (val_mul, ":d_val", 3),
               (val_div, ":d_val", 2),
            (try_end),
            (val_add, ":o_val", ":h_val"),
         (try_end),
         
         # add stuff up
         (val_add, reg0, ":o_val"),
         (val_add, reg1, ":d_val"),
         (val_add, reg2, ":stack_size"),
      (try_end),
      
      # calculate damage redux from defense
      (val_div, reg1, reg2), # avg defense
      (val_clamp, reg1, 0, 90), # values outside this range don't work well
      (store_sub, reg1, 100, reg1), # opponent offense should be multiplied by this %
   ]),

   # kt0:  this is a helper that basically calls kt_party_calculate_strength
   # for each attachment to the given party. 
   # INPUT:
   #      arg1:  party_id
   #      arg2:  exclude leader of given stack (not attachments)
   #      arg3:  is_siege
   # OUTPUT:
   #      reg0:  aggregate strength
   #      reg1:  number of attached parties
   ( "kt_party_calculate_strength_with_attachments",
   [
      # remember our params and set some initial values
      (store_script_param_1, ":root_party"),
      (store_script_param_2, ":exclude_leader"),
      (store_script_param, ":is_siege", 3),

      # call the counting script for the given party
      (call_script, "script_kt_party_calculate_strength", ":root_party", ":exclude_leader", ":is_siege"),
      (assign, ":strength_so_far", reg0),
      (assign, ":def_so_far", reg1),
      (assign, ":count_so_far", reg2),
      (val_mul, ":def_so_far", ":count_so_far"),

      # for every attached party, do the same      
      (party_get_num_attached_parties, ":attached_count", ":root_party"),
      (try_for_range, ":rank", 0, ":attached_count"),
         (party_get_attached_party_with_rank, ":attached_party", ":root_party", ":rank"),
         (call_script, "script_kt_party_calculate_strength", ":attached_party", 0, ":is_siege"),
         (val_add, ":strength_so_far", reg0),
         (store_mul, ":def_this_party", reg1, reg2),
         (val_add, ":def_so_far", ":def_this_party"),
         (val_add, ":count_so_far", reg2),
      (try_end),

      # fill out our returns
      (assign, reg0, ":strength_so_far"),
      (val_div, ":def_so_far", ":count_so_far"),
      (assign, reg1, ":def_so_far"),      
      (assign, reg2, ":count_so_far"),
   ]),

   # kt0:  there seem to be multiple ways to calculate how many fit troops
   # there are in an encounter and they all do something slightly different
   # but seem to be used for the same things.  this is a simple consolidation
   # attempt that counts guys the same way that we calculate party strengths.
   # INPUT: 
   #      arg1:  party_id
   #      arg2:  exclude leader
   # OUTPUT:
   #      reg0:  viable troop count
   ( "kt_count_viable_troops",
   [
      # remember our params
      (store_script_param_1, ":party"),   # party id
      (store_script_param_2, ":exclude_leader"), # also a party id apparently

      # clear out our return
      (assign, reg0, 0),

      # figure out which stack to start with and how many we have
      (party_get_num_companion_stacks, ":num_stacks", ":party"),
      (assign, ":first_stack", 0),
      (try_begin),
         (neq, ":exclude_leader", 0),
         (assign, ":first_stack", 1),
      (try_end),

      (try_for_range, ":i_stack", ":first_stack", ":num_stacks"),
         (party_stack_get_troop_id, ":stack_troop", ":party", ":i_stack"),
         (party_stack_get_size, ":stack_size",":party",":i_stack"),
         (party_stack_get_num_wounded, ":num_wounded",":party",":i_stack"),
         (val_sub, ":stack_size", ":num_wounded"),
         (try_begin),
            (gt, ":stack_size", 0),
            (try_begin),
               # if this stack is a hero, check health vs. the viable thresh.
               (troop_is_hero, ":stack_troop"),
               (neg|troop_is_wounded, ":stack_troop"),
               (val_add, reg0, 1),
            (else_try),
               # otherwise just add
               (val_add, reg0, ":stack_size"),
            (try_end),
         (try_end),
      (try_end),

      # reg0 should have the battle-ready count
   ]),
   
   # kt0:  this is a helper that basically calls kt_count_viable_troops for
   # each attachment to the given party.  if the party has no attachments,
   # it just returns the given party's count.
   # INPUT:
   #      arg1:  party_id
   #      arg2:  exclude leader of given stack (not attachments)
   # OUTPUT:
   #      reg0:  viable troop count
   #      reg1:  number of attached parties
   ( "kt_count_viable_troops_with_attachments",
   [
      # remember our params and set some initial values
      (store_script_param_1, ":root_party"),
      (store_script_param_2, ":exclude_leader"),

      # call the counting script for the given party
      (call_script, "script_kt_count_viable_troops", ":root_party", ":exclude_leader"),
      (assign, ":count_so_far", reg0),

      # for every attached party, do the same      
      (party_get_num_attached_parties, ":attached_count", ":root_party"),
      (try_for_range, ":rank", 0, ":attached_count"),
         (party_get_attached_party_with_rank, ":attached_party", ":root_party", ":rank"),
         (call_script, "script_kt_count_viable_troops", ":attached_party", 0),
         (val_add, ":count_so_far", reg0),
      (try_end),

      # fill out our returns
      (assign, reg0, ":count_so_far"),
      (assign, reg1, ":attached_count"),
   ]),