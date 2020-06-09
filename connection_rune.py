import core

  # Applying the Token
def app_connect(core_id, end1_id, end2_id):
    core_id.mods.append("connection")

    core_id.connects = [end1_id, end2_id]  # These are the id's of the two cores that it connects

    # Connection Line Visual Variables
    core_id.colour = "#ffffff"
    core_id.thickness = 1
    core_id.transparency = 1

    # Connection Behaviour Variables
    core_id.rubber = False  # This is weather the line denotes that one object belongs to a container
    core_id.container = end1_id  # when rubber = True, this defines which end of the connection is the main container attached to

    core_id.static = False  # This is weather the line deforms when one of its end-points is moved or not

    core_id.behave = "straight"  # This will define how the shape of the line will behave based on where its end-points are (and even where they are wrt the connected objects)


# GENERAL FUNCTIONALITY
# drawing an object with the rune
def draw_connect():
    # ???


# moving an object with the rune
def move_connect(dx, dy, dz):
    # ???


# rotating aan object with the  rune
def rot_connect():
    # ???


# SPECIAL FUNCTIONALITY
def connect(parent_stage, core1_id, core2_id):  # Connects two cores (automatically creates the connection core)
    con_id = '???' # what would be the id of the new connection core??

    x = (core1_id.loc[0] + core2_id.loc[
        0]) / 2  # Calculate the location of the connection's core based on the location of the two cores to be connected
    y = (core1_id.loc[1] + core2_id.loc[1]) / 2
    con_loc = [x, y]

    con_id = core.Core(x, y)  # create new core
    app_connect(con_id, core1_id, core2_id)  # add a connection Rune to it

    core1_id.conns.append(con_id)  # store the connection's id in each connected core
    core2_id.conns.append(con_id)