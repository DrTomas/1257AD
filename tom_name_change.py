# -*- coding: utf-8 -*-
from ID_troops import *
from module_troops import *

def do_it():
	file = open("flags.txt","w")
	for i in troops:
		id = i[0]
		name = i[1]
		plur = i[2]
		file.write("	  (troop_set_name, \"trp_" + id + "\", \"@" + name + "\"),\n")
		file.write("	  (troop_set_plural_name, \"trp_" + id + "\", \"@" + plur + "\"),\n")
	file.close()

def do_it_again():
	file = open("flags2.txt","w")
	for i in troops:
		ind = " (cav)"
		if ((i[8] == foot_attrib_1) or (i[8] == foot_attrib_2) or (i[8] == foot_attrib_3) or (i[8] == foot_attrib_4) or (i[8] == foot_attrib_5) or (i[8] == foot_attrib_elite)):
			ind = " (inf)"
		elif ((i[8] == ranged_attrib_3) or (i[8] == ranged_attrib_4) or (i[8] == ranged_attrib_5) or (i[8] == ranged_attrib_elite)):
			ind = " (rng)"
		id = i[0]
		name = i[1]
		plur = i[2]
		file.write("	  (troop_set_name, \"trp_" + id + "\", \"@" + name + ind + "\"),\n")
		file.write("	  (troop_set_plural_name, \"trp_" + id + "\", \"@" + plur + ind +"\"),\n")
	file.close()

do_it()
do_it_again()