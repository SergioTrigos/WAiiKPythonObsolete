


def move(parent_stage, dx, dy, dz):
		for i in selected:
				runes = i.runes
				for j in runes:
						rune_dict = i.rune_funct.get(j)
						move_f = rune_dict.get('move')  # get the token specific draw function
						move_f()                      # run it
						#Token Specific Functionalities should affect how the object moves... but not make it move, because then the object would move once for every rune it had...
				i.move_core(parent_stage, dx, dy, dz)


def rotate(thx, thy, thz):
		# this gets complicated when you have more than one object selected at once...
		# because the axis of rotation happens at the "center of mass" of the selected group of objects (which must be calculated)
		# a reference frame is "assigned" at the center of mass.
		# then the TTD matrix of each object must be calculated based on their location wrt this reference frame
		for i in selected:
				runes = i.runes
				for j in runes: