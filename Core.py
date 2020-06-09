import math


# User's id (Userid) and User's Object Number (UserON) are variables obtained from the user's profile

class Core:
    def __init__(self, x, y):
        self.loc = [x, y, 0]  # Location wrt parent object

        self.ori = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]  # orientation matrix

        self.pos = [[self.ori[0, 0], self.ori[1, 0], self.ori[2, 0], self.pos[0]],
                    # position (location + position) matrix... we could probably optimize this with a linear algebra module
                    [self.ori[0, 1], self.ori[1, 1], self.ori[2, 1], self.pos[1]],
                    [self.ori[0, 2], self.ori[1, 2], self.ori[2, 2], self.pos[2]],
                    [0, 0, 0, 1]]
        self.angles = [0, 0, 0]  # This stores the angles by which an object has been rotated

        self.shell = point()  # a point...class? I guess it is an image of a point so yeah
        self.scale = 1

    self.runes = []  # listof mods
    self.conns = []  # list of connections

    self.vis = True  # this defines weather an object is hiden/shown (mostly used for vessels)

    # The following Values and Methods are Rune Independent
    # I don't think the info bellow needs to be stored in the database... I'm not sure we need the menu's state to be stored/defined here... but if we do then here they are:
    self.menu = False  # False = closed, True = Opened
    self.act_menu = False  # False = closed, True = Opened
    self.rune_list = False  # False = closed, True = Opened

    self.selc = False  # if selected : True


# RUNE INDEPENDENT METHODS
# object menu
def open_menu(self):
    self.menu = True


def close_menu(self):
    self.menu = False

    # Action sub-menu, this one has "delete object", "copy object", and "connection list" features in it
    def open_act(self):
        self.act_menu = True


def close_act(self):
    self.act_menu = False


# Token List, this includes the "add tokens" button, and the tokens that have already been applied to the object
def open_runelist(self):
    self.rune_list = True


def close_runelist(self):
    self.rune_list = False

    # FUNCTIONALITY MASTER METHODS   -
    # CORE Functionalities

    def draw_core(self,
                  parent_stage):  # this is the emptu core's draw function, but it can be used by runes that do not change the draw funcitonality
        self.loc  # object's location wrt parent stage
        (???)  # find location of object wrt global stage  (I have the math for this)!!!

    def move_core(self, parent_stage, dx, dy,
                  dz):  # this is the empty core's move function, but it can be used by runes that do not change the move funcitonality
        # here I am checking if the object is already at a locational limit before moving it
        if dx > 0
            if self.loc[0] < parent_stage.limR[0]  # limR, limL, limT LimB are the limits in the Parent Stage's map
                self.loc[0] += dx
        else
            self.loc[0] > parent_stage.limL[0]
            self.loc[0] += dx
        if dy > 0
            if self.loc[1] < parent_stage.limH[1]
                self.loc[1] += dy
        else
            if self.loc[1] > parent_stage.limL[1]
                self.loc[1] += dy
        if dz > 0
            if self.loc[2] < parent_stage.limD[2]
                self.loc[2] += dz
        else
            if self.loc[2] > parent_stage.limD[2]
                self.loc[2] += dz

    def rotate_core(self, thx, thy, thz):
        self.angles[0] += thx
        self.angles[1] += thy
        self.angles[3] += thz  # first store the angle by wich the object is and has being rotated
        cx = math.cos(thx)
        sx = math.sin(thx)
        cy = math.cos(thy)
        sy = math.sin(thy)
        cz = math.cos(thz)
        sz = math.sin(thz)
        R = [[cz * cy, cz * sy * sx - sz * cx, cz * sy * cx + sz * sx],
             [sz * cy, sz * sy * sx + cz * cx, sz * sy * cx - cz * sx],
             [-sy, cy * sx, cy * cx]]
        self.pos = R * self.pos  # This is a matrix multiplication, so we will most likely need a linear algebra module to perform it.

    # RUNE DEPENDENT Functionalities

    # this vvv is the main funcitonality dictionary that maps runes to their specific functionality functions
    rune_funct = {'shell': {'draw': draw_shell, 'move': move_shell, },
                  'connection': {'draw': draw_connection, 'move': move_connection, },
                  'container': {'draw': draw_container, 'move': move_container, },
                  'stage': {'draw': draw_stage, 'move': move_stage, }}

    # these are rune-specific functionality functions that are applied to ONE object at a time (so not need for special "multiple selection" cases)
    def draw(self, cls, parent_stage):
        # get list of object's Tokens
        runess = self.runes
        if runes =[]  # if there are no tokens
        self.draw_core(parent_stage)

    else:
    for i in runes
        rune_dict = cls.rune_funct.get(i)
        draw_f = rune_dict.get('draw')  # get the token specific draw function
        draw_f()  # run it
