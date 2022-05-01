"""
Author: Colin Frisch
File: disassembler.py
Purpose: This module will open and disassemble the GB ROM
"""
import struct
import json

ROMS_PATH = "../ROMS/"
ROM_NAME = ROMS_PATH + "snake.gb" # Make name a command line arg

HEADER_START = 0x0100
HEADER_END = 0x014F 

def load_rom():
    """ Open the ROM file and break into sections """
    with open(ROM_NAME, "rb") as rom:
        data = rom.read()
    
    header = data[HEADER_START:HEADER_END]
    title = struct.unpack_from('>15s', header[0x0034:0x0043])
    print(title)
    

def parse_rom():
    """ Parse ROM's machine code into opcodes """
    with open("../Opcodes.json") as opcodes_file:
        opcodes = json.load(opcodes_file)
        print(opcodes["unprefixed"]["0x00"])

def disassemble():
    """ Load in a ROM file and disassemble it """ 
    #load_rom()
    parse_rom()

disassemble()
