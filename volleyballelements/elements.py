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

        
class Player():
    """
        This class define a volleyball player
    """
    def __init__(self, description):
        self.description = tuple(description.split(";"))
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
        return self.description[inset]
