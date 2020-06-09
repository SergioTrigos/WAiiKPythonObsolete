
  # Applying the Token
def app_container(core_id):
    core_id.mods.append("container")

    core_id.c_state = "closed"  # The state of the container

    core_id.c_content = []  # a list of the id's of all cores stored in this container
    core_id.st_states = {}  # a Dictionary that maps the id's of the rubbered cores with their state (opened/closed)


# GENERAL FUNCTIONALITY
# drawing an object with the rune
def draw_container(core_id):
    (
        ???)  # I think this could be used to create the invisible region around the container where if a core is dragged onto it is will get stored in the container

    if core_id.c_state == "opened":
        for i in core_id.c_content:
            if core_id.st_stater[i] == "opened"
                i.draw()
            else:
                pass
    else:
        pass


# moving an object with the rune
def move_container(dx, dy, dz):
    (???)


# rotating aan object with the  rune
def rot_container():
    (???)


# SPECIAL FUNCTIONALITY
def put_in(cont_id,
           core_id):  # when a core is stored in a container and it is now inside the container so it is no longer vissible
    (???)


def put_out(cont_id, core_id):  # Literaly puts out a core from a container
    # this first checks weather this object is connected (directly of indirectly) with a rubber to this container.
    (???)
    # if it is, then it just changes the vissibility of the object (and the ones before it in a connection chain)
    (???)
    # if it is not, it changes the vissibility of the object, and it removes the object from its container lists.
    (???)


# this could lead to a promt of "connect object to container with a rubber band" or something.

def assign(cont_id,
           core_id):  # when a core becomes "stored" in a container because it gets connected (directly or indirectly) to a rubber connection
    cont_id.content.apend(core_id)
    cont_id.st_states[core_id] = "opened"


(???)


def de_assign(cont_id, core_id):  # when a rubber connection is severed (directly or indirectly) from a core
    # that object's data must be removed from the container's records
    (???)


def open(cont_id):  # Makes all the rubbered cores vissible, and puts out all the un-connected stored cores
    (???)
