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

#--------------------------------------------------------------------------
#   test_send.py
#       sends a test packet
#--------------------------------------------------------------------------
#
# --------------------------------------------------------------------------
# Imports

import afsk
import packet
import audiogen
import time

# --------------------------------------------------------------------------

dest = b"QSAT"
callsign = b"KN6EVU"
digi = b""

for i in range(5):

    info = b"Testing packet: Sending packet %b" % (str(i).encode())

    print(("Dest: %s | Source: %s | Digis: %s | %s |"
           % (dest.decode(), callsign.decode(), digi.decode(), info.decode())))

    pack_data = packet.gen_packet(callsign, dest, digi, info)

    audio = afsk.encode(pack_data.unparse())
    audiogen.play(audio, blocking=True)
    time.sleep(.5)
