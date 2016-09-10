"""
PROTOTYPE - prototype.py

This is the main file from the python implementation of the Prototype-Engine.
(C) Zoxuyu
"""
import argparse

parser = argparse.ArgumentParser(description='Executes Prototype-Application')
parser.add_argument('file', metavar='FILE', type=str,
                    help='the prototype-file to execute')
parser.add_argument("-q", '--quiet', action="store_true", help="Quiet-Mode (no error-output)")

args = parser.parse_args()
QUIET_MODE = args.quiet
FILENAME = args.file

from errors import *
from engine import *
from _parser import *
from results import *

def parseError(type, desc, line):
    if not QUIET_MODE:
        print(type(desc, FILENAME, line))
    else:
        print("\nAn error occured.")
    try:
        raw_input()
    except:
        input()
try:
    engine = Engine(FILENAME, PARSER_LIST())
    try:
        n = 1
        for line in engine.getLines():
            result = engine.parseLine(line)
            if result.failed:
                parseError(PrototypeParserError, result.errorMessage, n)
                break
            n += 1
    except Exception as e:
        parseError(PrototypeError, ""+ str(e), n)
except:
    parseError(EngineError, "", 0)