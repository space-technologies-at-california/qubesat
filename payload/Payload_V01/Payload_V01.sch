EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 5
Title "QubeSat Payload Mainboard"
Date "2020-07-19"
Rev "V01"
Comp "Space Technologies at California"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 "Author: Vidish Gupta"
$EndDescr
$Sheet
S 1800 2600 1300 1100
U 5F190638
F0 "rf_generator" 98
F1 "rf_generator.sch" 98
F2 "SCLK" I R 3100 2700 50 
F3 "SDATA" I R 3100 2800 50 
F4 "FSYNC" I R 3100 2900 50 
F5 "RESET" I R 3100 3000 50 
F6 "SLEEP" I R 3100 3100 50 
F7 "PSEL" I R 3100 3200 50 
F8 "FSEL" I R 3100 3300 50 
F9 "5V_EXT" I R 3100 3400 50 
F10 "DVDD1" I R 3100 3500 50 
F11 "3,3V_BF" I R 3100 3600 50 
$EndSheet
$Sheet
S 4200 2600 1300 1100
U 5F1CCFD5
F0 "Laser" 98
F1 "Laser.sch" 98
$EndSheet
$Sheet
S 6600 2650 1250 1050
U 5F1CD0EE
F0 "Microcontroller" 98
F1 "Microcontroller.sch" 98
F2 "SCLK" I L 6600 2800 50 
$EndSheet
$Sheet
S 8900 2650 1300 1050
U 5F1CD1BA
F0 "Photodiode" 98
F1 "Photodiode.sch" 98
$EndSheet
Wire Wire Line
	3100 2700 3950 2700
Wire Wire Line
	3950 2700 3950 2400
Wire Wire Line
	3950 2400 6400 2400
Wire Wire Line
	6400 2400 6400 2800
Wire Wire Line
	6400 2800 6600 2800
$EndSCHEMATC
