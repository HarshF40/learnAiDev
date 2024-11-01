import sayings
import sys

if len(sys.argv) != 2:
    sys.exit()

sayings.hello(sys.argv[1])
sayings.goodbye(sys.argv[1])