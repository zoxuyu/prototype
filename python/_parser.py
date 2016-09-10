"""
PROTOTYPE - parser.py

This is the parser list file from the python implementation of the Prototype-Engine.
(C) Zoxuyu
"""

"Place your parser in /python/parsers/"
"Import your parser this way:"
"from parsers.<parsername> import Parser as <shortcut>"
from parsers.zero import Parser as zero
from parsers.prototype import Parser as prototype
"Insert Parsers here, by adding the following line:"
'"<yourcompany>.<package>(.<subpackage).v<versionnumber>": <shortcut>'
'() means optional'
__PARSER_LIST = {
    "zoxuyu.prototype.v1": prototype,
    "zoxuyu.zero.v1": zero,
}
def PARSER_LIST():
    return __PARSER_LIST