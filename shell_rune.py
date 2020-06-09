
  # Applying the Rune
def app_shell(core_id):
		core_id.runes.append("shell")

		core_id.datum_id = '???'

		  # Shell border visual variables
		core_id.s_colour = "#2a2a89"
		core_id.s_thickness = 1
		core_id.s_transparency =  1
		core_id.s_shape = "rectangle"

		  # Shell border behaviour variables
		core_id.s_size = [30, 15]    # create all the shell variables with default values


	# drawing an object with the rune
def draw_shell():
	# ???

	# moving an object with the rune
def move_shell(core_id, dx, dy, dz):
	# this would be the same as the core_move rigth? Why would the shell change the motion functionality of a core?
	core_id.move_core(dx, dy, dz)

  # rotating aan object with the rune
def rot_shell():
	# ???

def delete_shell():
	# ???