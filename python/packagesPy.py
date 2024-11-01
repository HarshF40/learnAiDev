#to get all the packages visit pypi.org 
#pip is a package manager for python

import cowsay
import sys

if len(sys.argv) == 2 :
    cowsay.trex("Hello " + sys.argv[1])