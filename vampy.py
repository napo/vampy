"""
    VAMPY
    Volleyball Analysis of a Match in Python
    A tool to analyze a leg file (datavolley format) in python
    Created by Maurizio Napolitano <napo@linux.it>
 """
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

import sys
from volleyballelements import Match, elements
from optparse import OptionParser

def main():
    """
        use -t for a test
    """
    usage = "usage: %prog [options]"
    parser = OptionParser(usage)
    parser.add_option("-t", "--test", action="store_true", \
                     dest="test", help="do a test")
    (options, args) = parser.parse_args()
    if options.test:
#        try:
            infile = "examples/1.leg"
            match = Match(infile)
            print "%s - %s " % (match.daymatch(), match.time())
            print "%s - %s " % (match.location(), match.gym())
            print "%s - %s" % (match.teams[0].name(), match.teams[1].name())
            print "sets played %s" % match.totsets()
            for i in range(match.totsets()):
                print "set %i - %s (%s, %s, %s)" % \
                (i+1,match.sets[i].pointsinset(),match.sets[i].partialsetpoints(1),
                 match.sets[i].partialsetpoints(2),match.sets[i].partialsetpoints(3))  
            print match.teams[0].players[4].name()
            print elements.rolename(match.teams[0].players[1].role())
#        except IOError as io_error:
#            print(io_error)
#            sys.exit(1)
    sys.exit(0)
             

if __name__ == "__main__":
    main()
