##########################################################################
# #
# This program is free software; you can redistribute it and/or modify #
# it under the terms of the GNU General Public License as published by #
# the Free Software Foundation; version 2 of the License. #
# #
# This program is distributed in the hope that it will be useful, #
# but WITHOUT ANY WARRANTY; without even the implied warranty of #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the #
# GNU General Public License for more details. #
# #
##########################################################################
"""
    A set of elements needed to build a team :)
"""

def rolename(_value):
    '''
    from the code give back the role name
    '''
    name = None
    if (_value.upper() == "T"):
        name  = "middleblock"
    if (_value.upper() == "L"):
        name  = "libero"
    if (_value.upper() == "A"):
        name  = "setter"
    if (_value.upper() == "S"):
        name = "outside hitter"
    if (_value.upper() == "O"):
        name = "opposite hitter"
    return name   

class Team():
    """
        a class to definie a team
    """
    def __init__(self):
        self.players = {}
        self.teamdata = ()
    def code(self):
        """
            returns the team's code
        """
        return self.teamdata[0]
    def name(self):
        """
            returns the team's name
        """
        return self.teamdata[1]
    def winnedsets(self):
        """
            returns the number of then winned sets
        """
        return int(self.teamdata[2])
    def coach(self):
        """
            returns the coach's name
        """
        return self.teamdata[3]
    def assistant(self):
        """
            returns the coach assistant's name
        """
        return self.teamdata[4]
        
class Player():
    """
        This class define a volleyball player
    """
    def __init__(self, description):
        self.description = tuple(description.split(";"))
        self.touches = Touch()
    def name(self):
        """
            returns the player's name
        """
        name = self.description[9]
        return name
    def number(self):
        """
            returns the player's number
        """
        number = int(self.description[2])
        return number
    def code(self):
        """
            returns the player's code
        """
        code = self.description[8]
        return code
    def role(self):
        """
            returns the player's role code
        """
        role = self.description[10]        
        return role 
    def rotation(self, inset):
        """
            returns the player's position for the gived set
        """
        inset =  inset +2
        rot = self.description[inset]
        if (rot ==""):
            rot = "-"
        return rot
def isvalidhightness(label):
    valid= False
    ff = (Touch.F_SERVICE,
          Touch.F_PASS,
          Touch.F_ATTACK,
          Touch.F_DEFENSE,
          Touch.F_SET,
          Touch.F_ONEATTACK,
          Touch.F_SERVICE,
          Touch.F_BLOCK,
          Touch.F_ONEBLOCK)
    for f in ff:
        if (label==f):
            valid = True
            break
    return valid   
    
def isvalidfoundamental(label):
    valid= False
    ff = (
        Touch.H_HIGHT,
        Touch.H_MIDDLE,
        Touch.H_SPEED,
        Touch.H_LONGSPEED,
        Touch.H_SECONDLINE
    )
    for f in ff:
        if (label==f):
            valid = True
            break
    return valid

class Touch():
    F_SERVICE="B"
    F_PASS="R"
    F_ATTACK="S"
    F_DEFENSE="D"
    F_SET="P"
    F_ONEATTACK="U"
    F_BLOCK="M"
    F_ONEBLOCK="N"
    V_DOUBLEPLUS ="#"
    V_PLUS ="+"
    V_SLASH ="/"
    V_ESCLAMATION="!"
    V_MINUS ="-"
    V_DOUBLEMINUS="--"
    M_POINT="p"
    M_TIMEOUT="T"
    M_CHANGE="C"
    H_HIGHT = "A"
    H_MIDDLE = "M"
    H_SPEED = "V"
    H_LONGSPEED = "T"
    H_SECONDLINE= "L"
    def __init__(self):
        foundamentals = {}
        touches = {}
        touches[Touch.H_HIGHT]= [0,0,0,0,0,0]
        touches[Touch.H_MIDDLE] = [0,0,0,0,0,0]
        touches[Touch.H_SPEED] = [0,0,0,0,0,0]
        touches[Touch.H_LONGSPEED] = [0,0,0,0,0,0]
        touches[Touch.H_SECONDLINE]=  [0,0,0,0,0,0]
        foundamentals = {
            Touch.F_SERVICE:touches,
            Touch.F_PASS:touches,
            Touch.F_ATTACK:touches,
            Touch.F_DEFENSE:touches,
            Touch.F_SET:touches,
            Touch.F_ONEATTACK:touches,
            Touch.F_BLOCK:touches,
            Touch.F_ONEBLOCK:touches     
        }
        self.foundamentals =foundamentals
        
    def indexfromlabel(self,label):
        index = -1
        if (label == Touch.V_DOUBLEPLUS):
            index = 0
        elif (label == Touch.V_PLUS):
            index = 1
        elif (label == Touch.V_SLASH):
            index = 2
        elif (label == Touch.V_ESCLAMATION):
            index =  3
        elif (label == Touch.V_MINUS):
            index = 4
        elif (label == Touch.V_DOUBLEMINUS):
            index = 5
        return  index
    def addtouch(self,touch,hightness,value):
        self.foundamentals[touch][hightness][self.indexfromlabel(value)]\
        += 1
    def touches(self,t,h,v):
        return self.foundamentals[t]


        