
  # Applying the Rune
def app_stage(core_id):
    core_id.runes.append("stage")

    # frame
    core_id.f_size = [30, 15]  # create all the shell variables with default values
    core_id.f_colour = "#2a2a89"
    core_id.thickness = 1
    core_id.f_transparency = 1
    core_id.f_shape = "rectangle"

    # map
    core_id.m_size = core_id.f_dimensions  # map and frame have the same size by default
    core_id.m_dimensions = 2  # The defult map has 2 dimensions : x and y
    core_id.m_colour = "#1b1b5e"
    core_id.m_transparency = 1
    core_id.m_shape = "rectangle"
    core_id.m_scale = core_id.m_dimensions / core_id.f_dimensions
    core_id.m_pos = [core_id.f_size[0] / 2, core_id.f_size[
        1] / 2]  # This is the position of the map wrt the frame (The frame's perspective of the map)

    core_id.s_content = []  # A list of all the 1st level objects in the Stage


# GENERAL FUNCTIONALITY
# drawing an object with the rune
def draw_stage(core_id):
    # First draw the stage:
    # ???
    # Then draw all the objects contained in the stage:
    for i in core_id.s_content:
        if i.vis == True:
            i.draw()
    else:
        pass


# moving an object with the rune
def move_stage(dx, dy, dz):
    # ???


# rotating aan object with the rune
def rot_stage():
    # ???

# SPECIAL FUNCTIONALITY