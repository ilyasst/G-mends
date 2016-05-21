#!/usr/bin/env python
from gcodeParser import *


if __name__ == '__main__':
    path = "test.gcode"

    parser = GcodeParser()
    model = parser.parseFile(path)

    print model
