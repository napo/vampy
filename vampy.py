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
        try:
            infile = "examples/test.leg"
            match = Match(infile)
            match.summary()

            
        except IOError as io_error:
            print(io_error)
            sys.exit(1)
    sys.exit(0)
             

if __name__ == "__main__":
    main()
