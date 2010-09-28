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
    all elements needes to describe a match
"""
from elements import Team, Player, isvalidfoundamental,isvalidhightness


def splitactionseachset(data):
    """
    divide action for each sets
    """
    setplayed = 1
    actioneachset = {}
    actions = []
    for action in data:
        action = action.rstrip() 
        if (action.find("**") > -1):
            actioneachset[setplayed] = actions
            actions = []
            setplayed += 1
        else:
            actions.append(action)
    return actioneachset
    
def collectdata(data, pattern, container):
    """
        from a section of the leg file (pattern)
        returns a tuple from a gived list (container)
        The pattern must be the name of the next section
        Example:
            leg file content
            ...
           [Set]
           True;5 -8;10-16;14-21;20-25;23;
           True;6 -8;13-16;20-21;25-23;26;
           True;8 -7;12-16;16-21;23-25;26;
           True;7 -8;16-15;21-17;25-23;28;
           True;3 -5;4 -10;5 -12;6 -15;10;
           [Player1]
            ...
            You need to extract the data from [Set] to [Player1]
            (all the sets information)
            so:
                
            >>> self.sets = self.__collectdata('[Player1]', self.sets)
    """
    lst = []
    nextdata = ""
    nextdata = ""
    while (nextdata != pattern):
        nextdata = data.readline().rstrip()
        if (nextdata != pattern): 
            lst.append(nextdata)
            container.append(lst)
    return tuple(lst)

def getdata(data, pattern):
    """
        from a section of the leg file (pattern)
        returns a tuple      
        The pattern must be the name of the next section
    """
    lst = []
    nextdata = ""
    while (nextdata != pattern):
        nextdata = data.readline().rstrip()
        if (nextdata != pattern): 
            lst.append(nextdata)
    return tuple(lst)


class Match():
    """
    this class load the leg file ad istance all the objects needed for the analysis
    """
    def __init__(self, infile):
        data = open(infile,'r')
        data.readline()
        self.matchinfo = tuple(data.readline().rstrip().split(";"))
        data.readline()
        self.teams = (Team(), Team())
        teamdata = tuple(data.readline().rstrip().split(";"))
        self.teams[0].teamdata = teamdata
        teamdata = tuple(data.readline().rstrip().split(";"))
        self.teams[1].teamdata = teamdata
        data.readline()
        self.oders = data.readline().rstrip()
        data.readline()
        self.matchcomments = data.readline().rstrip()
        data.readline() 
        self.sets = []

        for infoset in (getdata(data,'[Player1]')):
            aset = Set(infoset)
            self.sets.append(aset)
       
        players = {}            
        for ply  in (getdata(data, '[Player2]')):
            players[int(ply.split(";")[1])] = (Player(ply))
        self.teams[0].players = players

        players = {}
        for ply  in (getdata(data, '[Scout]')):
            players[int(ply.split(";")[1])] = (Player(ply))
        self.teams[1].players = players
     
        actioneachsetdata = splitactionseachset(data)
        
        for setplayed in actioneachsetdata:
            for actiondata in actioneachsetdata[setplayed]:
                act = Action(setplayed)                        
                if (actiondata.find("*P") > -1):
                    self.sets[setplayed -1].setterteam1 = \
                    actiondata.split(";")[0].replace("*P","");
                elif (actiondata.find("aP") > -1):
                    self.sets[setplayed -1].setterteam2 \
                    = actiondata.split(";")[0].replace("aP","");
                elif ((actiondata.find("*z") > -1)):
                    act.setterzoneteam1 = \
                        actiondata.split(";")[0]                
                elif ((actiondata.find("az") > -1)):
                    act.setterzoneteam2 = actiondata.split(";")[0]
                elif ((actiondata.find("*p") > -1) or\
                       actiondata.find("ap") > -1):
                    act.endaction = actiondata.split(";")[0]
                elif (actiondata.find("*T") > -1):
                    pass
                elif (actiondata.find("aT") >-1):
                    pass
                elif (actiondata.find("*C") > -1):
                    pass
                elif (actiondata.find("aC") >- 1):
                    pass
                else:
                    act.addcode(actiondata)
                self.parseaction(act)
                
    def parseaction(self,action):
        codes = action.codes
        for c in codes:
            np= c.player()
            kt= c.kindtouch()
            ht = c.hightnesstouch()
            tv = c.touchvalue()
            if (isvalidfoundamental(kt) and \
                isvalidhightness(ht)):
                if (np != 99):
                    if(np-50) > 0:
                        np = np -50
                        self.teams[1].players[np].touches.addtouch(kt,ht,tv)
                    else:
                        self.teams[0].players[np].touches.addtouch(kt,ht,tv)
                
        
    def summary(self):
        #Match info
        print "%s %s" % (self.kind(), self.season())
        print "%s %s" % (self.daymatch(), self.time())
        print "%s %s" % (self.gym(), self.location())
        print ""
        print "%s - %s" % (self.teams[0].name(), \
                           self.teams[1].name())
        print "%s - %s" % (self.teams[0].winnedsets(),\
                               self.teams[1].winnedsets())
        print ""
        #Set info
        k = 1
        for s in self.sets:
            pp = "" 
            sp  = "Set %i  %s" % (k,s.partialsetpoints(4)) 
            for r in range(3):
                 pp += " " + s.partialsetpoints(r+1)
            print "%s (%s)" % (sp,pp)
            k += 1
        print ""
        #Stats team1
        print self.teams[0].name().upper()
        for pk in self.teams[0].players:
            ret = ""
            for r in range(self.totsets()):
               ret += " " + self.teams[0].players[pk].rotation(r+1)
               stats = self.teams[0].players[pk].touches.touches("S","V","#")
            print "%s %s \t %s" % (pk,\
                            self.teams[0].players[pk].name(),\
                            ret)     
        print ""
        print ""

        print self.teams[1].name().upper()
        for pk in self.teams[1].players:
            ret = ""
            for r in range(self.totsets()):
               ret += " " + self.teams[1].players[pk].rotation(r+1)
               stats = self.teams[1].players[pk].touches.touches("S","V","#")
            print "%s %s \t %s" % (pk,\
                            self.teams[1].players[pk].name(),\
                            ret)             
        
    def daymatch(self):                      
        """
            returns date of match (as string)
        """
        return self.matchinfo[0]

    def winner(self):
        """
            returns the name of the winner
        """
        win = None
        setteam1 = int(self.teams[0].winnedsets)
        setteam2 = int(self.teams[1].winnedsets)

        if (setteam1 > setteam2):
            win = self.teams[0].name
            
        if (setteam2 > setteam1):
            win = self.teams[1].name
        
        return win

    def loser(self):
        """
            returns the name of the loser
        """
        lose = None
        setteam1 = int(self.teams[0].winnedsets)
        setteam2 = int(self.teams[1].winnedsets)

        if (setteam1 < setteam2):
            lose = self.teams[0].name
            
        if (setteam2 < setteam1):
            lose = self.teams[1].name
        
        return lose
        
    def totsets(self):
        """
            returns number of sets played
        """
        return len(self.sets)
    def season(self):
        """
            returns season of the game
        """
        return self.matchinfo[2]
    def kind(self):
        """
            returns the kind of the game
        """
        return self.matchinfo[3]
        
    def location(self):
        """
            returns the game location
             (string)
        """
        return self.oders.split(";")[3]

    def gym(self):
        """
            returns the gym's name of the match
            (string)
        """
        return self.oders.split(";")[4]
    
    def time(self):
        """
            return the start time of the match
            (string)
        """
        return self.matchinfo[1].replace(".00", "", 1)

class Set():
    """
        a class to describe a volleyball set
    """
    def __init__(self, data):
        self.data = data.split(";")
        self.setterteam1 = 0
        self.setterteam2 = 0
        
    def pointsinset(self):
        """
        returns (as string) numbers of point 
        in the gived set (nset)
            
        string format: team1-team2
        Example:
               25-15
        """            
        pnt = self.data[4]
        pnt.replace(" ","")
        return pnt  
        
    def partialsetpoints(self, partial):
        """
            returns (as string) the numbers of points
            in the n (from 1 to 3) partial of the gived set
            
            string format: team1-team2
            Example:
                    5-8
        """
        pnt = None
        if ((partial > 0) or (partial < 4)):
            pnt = self.data[partial]
            pnt.replace(" ","")
        return pnt

        
class Action():
    """
        a class to define a action (from service to the end point)
    """
    def __init__(self,inset):
        self.codes = []
        self.endaction = ""
        self.setterzoneteam1 = 0
        self.setterzoneteam2 = 0 
        self.set = inset
    
    def addcode(self, incode):
        """
            add a code describing a touchball with some metadata
        """
        code = Code(incode)
        self.codes.append(code)

class Code():
    """
        a class to obtain informations from a touch ball and relative metadata
    """
    def __init__(self, code):
        self.code = code.split(";")
        #evalaution = data[0]
        #pointkind = data[1]
        #afterpass = data[2]
        #setterposteam1 = data[3]
        #setterposteam2 = data[4]
        #actiontime = data[7]
        #whichset= data[8]
    def player(self):
        pn = self.code[0][0:2]
        return int(pn)
    
    def kindtouch(self):
        kt = self.code[0][2]
        return kt
    def hightnesstouch(self):
        ht = self.code[0][3]
        return ht
    def touchvalue(self):
        tv = self.code[0][4]
        return tv
    def touchfrom(self):
        return None
    def touchto(self):
        return None
        
    def kindendaction(self):
        """
            kind of endend action (point or breakpoint)
        """
        return self.code[1]
    def isafterpass(self):
        """
            describe if the touch ball is after a pass
            It works for the evaluations #/= for a point 
            (attack, service, block)
            In others evalutionas the answers is always False
        """
        rvalue = False
        if (self.code[2] == "r"):
            rvalue = True
        return rvalue
    def setterposition(self, team):
        """
            give the setter position for
            the team 1 or 2
            Valid input data are 1 and 2
        """
        rpos = -1
        if (team == 1):
            rpos = self.code[3]
        if (team == 2):
            rpos = self.code[4]
        return rpos
    def inputtime(self):
        """
            returns the input time of the code in the form
            hh.mm.ss
        """
        return self.code[7]
    def whichset(self):
        """
            returns the set number of this code
        """
        return int(self.code[8])


        