#  STACet AX.25 AFSK Packet Engine
#
#    Copyright (C) 2020  Max Burns
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

# --------------------------------------------------------------------------
#   console.py
#       handles text console for entering in commands to STACet
# --------------------------------------------------------------------------
#
# --------------------------------------------------------------------------
# Imports

import cmd
import var
import packet
import afsk
import pyaudio
import audiogen

# --------------------------------------------------------------------------
# Variable setup

BAUD = var.BAUD
MARK = var.MARK
SPACE = var.SPACE
RATE = var.RATE

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1

# --------------------------------------------------------------------------


#
# Class for the console using the cmd package
#
class STACetShell(cmd.Cmd):
    intro = "Welcome to STACet Engine.   Type help or ? to list commands.\n Set your callsign with 'callsign <callsign>'\n"
    prompt = 'STACet>> '
    file = None

    def __init__(self, pipe):
        self.pipe = pipe
        self.callsign = None
        super().__init__()

    def do_exit(self, arg):
        'Exit'
        print("Thanks for using STACet Engine")
        return True
    def do_callsign(self, arg):
        "Set your callsign to use for transmitting with 'callsign <callsign>'\n See current callsign with 'callsign'\n"
        arg = arg.split()
        if not arg:
            if self.callsign == None:
                print("Set your callsign with 'callsign <callsign>'")
            else:
                print(self.callsign)
        else:
            self.callsign = arg[0].upper()

    def do_send(self, arg):
        "form an send a packet with all custom data\n Usage: send then follow prompts\nType -cancel to cancel"
        if self.callsign == None:
            print("Set your callsign with 'callsign <callsign>'")
        else:
            dest,digi,info = "", "", ""
            print("Enter Destination, leaving blank is accpetable\n ex: 'KN6EVU'")
            dest = input(">> ")
            if dest.lower() == "-cancel":
                print("Canceled")
                return
            print("Enter Digipeaters, leaving blank is accpetable\n ex: 'WIDE1-1,WIDE2-1'")
            digi = input(">> ")
            if digi.lower() == "-cancel":
                print("Canceled")
                return
            while info == "":
                print("Enter Packet Info, leaving blank is NOT accpetable\n ex: ':EMAIL :test@example.com Test email'")
                info = input(">> ")
            if info == "-cancel":
                print("Canceled")
            else:
                print("Dest: %s | Source: %s | Digis: %s | %s |" %(dest ,self.callsign ,digi,info))
                pack_data = packet.gen_packet(self.callsign.encode(), dest.encode(), digi.encode(), info.encode())
                audio = afsk.encode(pack_data.unparse())
                audiogen.play(audio, blocking=True)
