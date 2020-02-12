EESchema Schematic File Version 4
EELAYER 29 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 3 6
Title "PyCubed Mainboard"
Date ""
Rev "v01"
Comp "Stanford University"
Comment1 "rexlab.stanford.edu"
Comment2 "Max Holliday"
Comment3 "Zac Manchester"
Comment4 ""
$EndDescr
Wire Wire Line
	3600 2800 3600 2900
Text GLabel 3600 2800 0    10   BiDi ~ 0
GND
Wire Wire Line
	7200 3300 7200 3200
Wire Wire Line
	6900 2500 6900 3300
Wire Wire Line
	7000 2500 6900 2500
Wire Wire Line
	6900 3300 7200 3300
Connection ~ 7200 3300
Text GLabel 7200 3300 0    10   BiDi ~ 0
GND
Wire Wire Line
	8100 2500 7900 2500
Text GLabel 8100 2500 0    10   BiDi ~ 0
GND
Wire Wire Line
	3500 1600 3500 1400
Text GLabel 3500 1600 0    10   BiDi ~ 0
GND
Wire Wire Line
	3900 2800 3900 2900
Text GLabel 3900 2800 0    10   BiDi ~ 0
GND
Wire Wire Line
	5600 2500 5700 2500
Wire Wire Line
	5700 2500 5700 2700
Wire Wire Line
	5600 2700 5700 2700
Wire Wire Line
	5700 2700 5700 2900
Wire Wire Line
	5200 2900 5700 2900
Wire Wire Line
	5700 2900 5700 3300
Connection ~ 5700 2700
Connection ~ 5700 2900
Text GLabel 5600 2500 0    10   BiDi ~ 0
GND
Wire Wire Line
	3900 5500 3900 5400
Wire Wire Line
	3900 5500 4200 5500
Wire Wire Line
	3200 5400 3900 5400
Connection ~ 3900 5400
Text GLabel 3900 5500 0    10   BiDi ~ 0
GND
Wire Wire Line
	6100 7100 6100 6900
Wire Wire Line
	6100 6400 6100 6900
Wire Wire Line
	5300 6300 6100 6300
Wire Wire Line
	6100 6300 6100 6400
Wire Wire Line
	6100 7100 6300 7100
Connection ~ 6100 6900
Connection ~ 6100 6400
Connection ~ 6300 7100
Text GLabel 6100 7100 0    10   BiDi ~ 0
GND
Wire Wire Line
	2900 6700 2900 6900
Wire Wire Line
	2900 6900 2900 7000
Wire Wire Line
	2000 6900 2300 6900
Wire Wire Line
	2300 6900 2300 6800
Wire Wire Line
	2300 6900 1900 6900
Wire Wire Line
	1900 6900 1900 6800
Connection ~ 2900 6900
Connection ~ 2300 6900
Text GLabel 2900 6700 0    10   BiDi ~ 0
GND
Wire Wire Line
	2900 6000 2600 6000
Wire Wire Line
	1600 5800 1900 5800
Wire Wire Line
	1900 5800 2400 5800
Wire Wire Line
	2400 5800 2600 5800
Wire Wire Line
	2600 5800 2600 6000
Wire Wire Line
	2600 6000 2600 6100
Connection ~ 2600 6000
Connection ~ 1900 5800
Connection ~ 2400 5800
Text GLabel 2900 6000 0    10   BiDi ~ 0
GND
Wire Wire Line
	8650 6200 7950 6200
Connection ~ 7950 6200
Text GLabel 8650 6200 0    10   BiDi ~ 0
GND
Wire Wire Line
	1700 5500 1600 5500
Wire Wire Line
	1600 5500 1300 5500
Wire Wire Line
	2000 6500 2300 6500
Wire Wire Line
	2300 6500 1900 6500
Wire Wire Line
	1900 6500 1300 6500
Wire Wire Line
	1300 6500 1300 5500
Wire Wire Line
	1800 5400 1700 5400
Wire Wire Line
	1700 5400 1700 5500
Wire Wire Line
	2900 6600 2900 6500
Text Label 1300 6300 1    50   ~ 0
VREG_IN
Connection ~ 2900 6500
Connection ~ 1600 5500
Connection ~ 2300 6500
Connection ~ 1900 6500
Wire Wire Line
	3900 5100 3900 5000
Wire Wire Line
	3900 5000 4200 5000
Wire Wire Line
	1800 5200 1800 4900
Wire Wire Line
	1800 4900 3900 4900
Wire Wire Line
	3900 4900 3900 5000
Connection ~ 3900 5000
Text GLabel 3900 5100 0    10   BiDi ~ 0
3.3V
Wire Wire Line
	1400 5800 1400 6100
Wire Wire Line
	1400 6100 1600 6100
Wire Wire Line
	1600 6100 1900 6100
Wire Wire Line
	1900 6100 2000 6100
Connection ~ 1600 6100
Connection ~ 1900 6100
Text GLabel 1400 5800 0    10   BiDi ~ 0
3.3V
Wire Wire Line
	7300 1600 7300 1500
Wire Wire Line
	7300 1500 7600 1500
Wire Wire Line
	7600 1500 7600 1600
Connection ~ 7600 1500
Text GLabel 7300 1600 0    10   BiDi ~ 0
3.3V
Wire Wire Line
	8650 5400 8650 5300
Wire Wire Line
	5300 6700 5300 6900
Wire Wire Line
	5300 6900 5300 7200
Wire Wire Line
	5300 7200 5200 7200
Connection ~ 5300 6900
Text GLabel 5200 7200 0    50   BiDi ~ 0
3.3V
Wire Wire Line
	3300 2300 3200 2300
Text GLabel 3200 2300 0    70   BiDi ~ 0
VSOLAR
Wire Wire Line
	3200 5300 3400 5300
Text GLabel 3400 5300 2    50   BiDi ~ 0
I_BATT
Wire Wire Line
	8050 5800 7950 5800
Wire Wire Line
	7950 5800 7750 5800
Text GLabel 7750 5800 0    50   BiDi ~ 0
ENAB_GPS
Connection ~ 7950 5800
Wire Wire Line
	7000 2800 7200 2800
Wire Wire Line
	7200 2900 7200 2800
Wire Wire Line
	7200 2800 7800 2800
Wire Wire Line
	7800 2800 8100 2800
Wire Wire Line
	7800 2700 7800 2800
Connection ~ 7200 2800
Connection ~ 7800 2800
Wire Wire Line
	7000 2200 7600 2200
Wire Wire Line
	7600 2200 7600 2000
Wire Wire Line
	7000 2100 7100 2100
Wire Wire Line
	7100 2100 7100 1700
Wire Wire Line
	7100 1700 4500 1700
Wire Wire Line
	4500 1700 4300 1700
Wire Wire Line
	4500 1700 4500 1400
Wire Wire Line
	3900 1400 4500 1400
Connection ~ 4500 1700
Wire Wire Line
	4100 2500 4700 2500
Wire Wire Line
	4700 1900 4700 2400
Wire Wire Line
	4700 2400 4700 2500
Wire Wire Line
	5600 2400 4700 2400
Connection ~ 4700 2400
Wire Wire Line
	5600 2200 4100 2200
Wire Wire Line
	3900 2500 3900 2100
Wire Wire Line
	3900 2100 5600 2100
Wire Wire Line
	7000 2400 7400 2400
Wire Wire Line
	7400 2400 7400 2300
Wire Wire Line
	7400 2300 8900 2300
Wire Wire Line
	7400 2400 7400 2500
Wire Wire Line
	7400 2500 7500 2500
Connection ~ 7400 2400
Text GLabel 8900 2300 2    50   BiDi ~ 0
L1_PROG
Wire Wire Line
	4800 2600 5600 2600
Wire Wire Line
	4800 2600 4800 2900
Wire Wire Line
	4800 2900 4600 2900
Connection ~ 4800 2900
Wire Wire Line
	5600 2800 5300 2800
Wire Wire Line
	5300 2800 5300 1900
Wire Wire Line
	5300 1900 5200 1900
Wire Wire Line
	5600 2300 4600 2300
Wire Wire Line
	4600 2500 4600 2300
Wire Wire Line
	4600 2300 3600 2300
Wire Wire Line
	3900 1700 3600 1700
Wire Wire Line
	3600 1700 3600 2300
Wire Wire Line
	3600 2500 3600 2300
Connection ~ 4600 2300
Connection ~ 3600 2300
Wire Wire Line
	7300 2300 7300 2000
Wire Wire Line
	7000 2300 7300 2300
Wire Wire Line
	8500 2800 8900 2800
Text GLabel 8900 2800 2    70   BiDi ~ 0
VBATT
Wire Wire Line
	1600 5100 1600 4900
Wire Wire Line
	1400 4900 1600 4900
Wire Wire Line
	1800 5300 1700 5300
Wire Wire Line
	1700 5300 1700 5100
Wire Wire Line
	1700 5100 1600 5100
Text GLabel 1400 4900 0    50   BiDi ~ 0
VBATT
Connection ~ 1600 5100
Wire Wire Line
	5300 6100 5300 5900
Wire Wire Line
	5300 5900 5400 5900
Text GLabel 5400 5900 2    50   BiDi ~ 0
VBATT
Wire Wire Line
	6300 6100 5400 6100
Wire Wire Line
	5400 6100 5400 6200
Wire Wire Line
	5400 6200 5300 6200
Wire Wire Line
	2900 6200 2800 6200
Wire Wire Line
	2500 6400 2500 6300
Wire Wire Line
	2500 6300 2500 6100
Wire Wire Line
	2900 6300 2800 6300
Wire Wire Line
	2800 6300 2800 6200
Wire Wire Line
	2800 6300 2500 6300
Connection ~ 2800 6300
Connection ~ 2500 6300
Wire Wire Line
	2900 6400 2800 6400
Wire Wire Line
	5300 6500 6300 6500
Wire Wire Line
	6300 6500 6300 6800
Connection ~ 6300 6500
Wire Wire Line
	5300 6400 5800 6400
Wire Wire Line
	5300 6600 5700 6600
Wire Wire Line
	5700 6600 5700 6900
Connection ~ 5700 6900
Wire Wire Line
	8450 6100 8450 5800
Text GLabel 10500 5800 2    50   BiDi ~ 0
GPS_PWR_IN
Wire Wire Line
	7400 2700 7000 2700
Wire Wire Line
	7400 2600 7400 2700
Connection ~ 7400 2700
$Comp
L mainboard:LTC4121-4.2 U6
U 1 0 0551BDC9
P 6100 2400
AR Path="/0551BDC9" Ref="U6"  Part="1" 
AR Path="/5CEC5DDE/0551BDC9" Ref="U6"  Part="1" 
F 0 "U6" H 6000 2800 68  0000 L BNN
F 1 "LTC4121-4.2" H 6000 1800 68  0000 L BNN
F 2 "mainboard:QFN-16-PAD" H 6100 2400 50  0001 C CNN
F 3 "" H 6100 2400 50  0001 C CNN
	1    6100 2400
	1    0    0    -1  
$EndComp
$Comp
L mainboard:GND #GND11
U 1 0 5518330F
P 3600 3000
AR Path="/5518330F" Ref="#GND11"  Part="1" 
AR Path="/5CEC5DDE/5518330F" Ref="#GND011"  Part="1" 
F 0 "#GND011" H 3600 3000 50  0001 C CNN
F 1 "GND" H 3500 2900 59  0000 L BNN
F 2 "" H 3600 3000 50  0001 C CNN
F 3 "" H 3600 3000 50  0001 C CNN
	1    3600 3000
	1    0    0    -1  
$EndComp
$Comp
L mainboard:GND #GND16
U 1 0 12C6E2A1
P 7200 3400
AR Path="/12C6E2A1" Ref="#GND16"  Part="1" 
AR Path="/5CEC5DDE/12C6E2A1" Ref="#GND016"  Part="1" 
F 0 "#GND016" H 7200 3400 50  0001 C CNN
F 1 "GND" H 7100 3300 59  0000 L BNN
F 2 "" H 7200 3400 50  0001 C CNN
F 3 "" H 7200 3400 50  0001 C CNN
	1    7200 3400
	1    0    0    -1  
$EndComp
$Comp
L mainboard:GND #GND18
U 1 0 195191A6
P 8100 2600
AR Path="/195191A6" Ref="#GND18"  Part="1" 
AR Path="/5CEC5DDE/195191A6" Ref="#GND018"  Part="1" 
F 0 "#GND018" H 8100 2600 50  0001 C CNN
F 1 "GND" H 8000 2500 59  0000 L BNN
F 2 "" H 8100 2600 50  0001 C CNN
F 3 "" H 8100 2600 50  0001 C CNN
	1    8100 2600
	1    0    0    -1  
$EndComp
$Comp
L mainboard:IND L4
U 1 0 AD156AE0
P 4900 1900
AR Path="/AD156AE0" Ref="L4"  Part="1" 
AR Path="/5CEC5DDE/AD156AE0" Ref="L4"  Part="1" 
F 0 "L4" H 4810 1900 59  0000 L BNN
F 1 "56uH" H 4810 1760 59  0000 L BNN
F 2 "mainboard:1812" H 4900 1900 50  0001 C CNN
F 3 "" H 4900 1900 50  0001 C CNN
	1    4900 1900
	1    0    0    -1  
$EndComp
$Comp
L mainboard:PTCFUSE1206 F1
U 1 0 28DFDA13
P 8300 2800
AR Path="/28DFDA13" Ref="F1"  Part="1" 
AR Path="/5CEC5DDE/28DFDA13" Ref="F1"  Part="1" 
F 0 "F1" H 8200 2600 63  0000 L BNN
F 1 "1206L200" H 8200 2450 63  0000 L BNN
F 2 "mainboard:1206" H 8300 2800 50  0001 C CNN
F 3 "" H 8300 2800 50  0001 C CNN
	1    8300 2800
	1    0    0    -1  
$EndComp
$Comp
L mainboard:GND #GND10
U 1 0 0087CD10
P 3500 1700
AR Path="/0087CD10" Ref="#GND10"  Part="1" 
AR Path="/5CEC5DDE/0087CD10" Ref="#GND010"  Part="1" 
F 0 "#GND010" H 3500 1700 50  0001 C CNN
F 1 "GND" H 3400 1600 59  0000 L BNN
F 2 "" H 3500 1700 50  0001 C CNN
F 3 "" H 3500 1700 50  0001 C CNN
	1    3500 1700
	1    0    0    -1  
$EndComp
$Comp
L mainboard:DFLS130L D1
U 1 0 073F14D3
P 3400 2300
AR Path="/073F14D3" Ref="D1"  Part="1" 
AR Path="/5CEC5DDE/073F14D3" Ref="D1"  Part="1" 
F 0 "D1" H 3400 2400 59  0000 L BNN
F 1 "DFLS130L" H 3400 2100 59  0000 L BNN
F 2 "mainboard:PWRDI-123" H 3400 2300 50  0001 C CNN
F 3 "" H 3400 2300 50  0001 C CNN
	1    3400 2300
	1    0    0    -1  
$EndComp
$Comp
L mainboard:GND #GND12
U 1 0 8C4C494A
P 3900 3000
AR Path="/8C4C494A" Ref="#GND12"  Part="1" 
AR Path="/5CEC5DDE/8C4C494A" Ref="#GND012"  Part="1" 
F 0 "#GND012" H 3900 3000 50  0001 C CNN
F 1 "GND" H 3800 2900 59  0000 L BNN
F 2 "" H 3900 3000 50  0001 C CNN
F 3 "" H 3900 3000 50  0001 C CNN
	1    3900 3000
	1    0    0    -1  
$EndComp
$Comp
L mainboard:GND #GND14
U 1 0 B9C9B342
P 5700 3400
AR Path="/B9C9B342" Ref="#GND14"  Part="1" 
AR Path="/5CEC5DDE/B9C9B342" Ref="#GND014"  Part="1" 
F 0 "#GND014" H 5700 3400 50  0001 C CNN
F 1 "GND" H 5600 3300 59  0000 L BNN
F 2 "" H 5700 3400 50  0001 C CNN
F 3 "" H 5700 3400 50  0001 C CNN
	1    5700 3400
	1    0    0    -1  
$EndComp
$Comp
L mainboard:R-US_R0603 R11
U 1 0 99AF0EED
P 5000 2900
AR Path="/99AF0EED" Ref="R11"  Part="1" 
AR Path="/5CEC5DDE/99AF0EED" Ref="R11"  Part="1" 
F 0 "R11" H 4850 2959 59  0000 L BNN
F 1 "43K" H 4850 2770 59  0000 L BNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 5000 2900 50  0001 C CNN
F 3 "" H 5000 2900 50  0001 C CNN
	1    5000 2900
	-1   0    0    1   
$EndComp
$Comp
L mainboard:R-US_R0603 R10
U 1 0 69BCA27E
P 4600 2700
AR Path="/69BCA27E" Ref="R10"  Part="1" 
AR Path="/5CEC5DDE/69BCA27E" Ref="R10"  Part="1" 
F 0 "R10" H 4450 2759 59  0000 L BNN
F 1 "330K" H 4450 2570 59  0000 L BNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 4600 2700 50  0001 C CNN
F 3 "" H 4600 2700 50  0001 C CNN
	1    4600 2700
	0    -1   -1   0   
$EndComp
$Comp
L mainboard:R-US_R0603 R8
U 1 0 C507FD3A
P 3700 1400
AR Path="/C507FD3A" Ref="R8"  Part="1" 
AR Path="/5CEC5DDE/C507FD3A" Ref="R8"  Part="1" 
F 0 "R8" H 3550 1459 59  0000 L BNN
F 1 "100K" H 3550 1270 59  0000 L BNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 3700 1400 50  0001 C CNN
F 3 "" H 3700 1400 50  0001 C CNN
	1    3700 1400
	-1   0    0    1   
$EndComp
$Comp
L mainboard:R-US_R0603 R9
U 1 0 EE9F30D5
P 4100 1700
AR Path="/EE9F30D5" Ref="R9"  Part="1" 
AR Path="/5CEC5DDE/EE9F30D5" Ref="R9"  Part="1" 
F 0 "R9" H 3950 1759 59  0000 L BNN
F 1 "40.9K" H 3950 1570 59  0000 L BNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 4100 1700 50  0001 C CNN
F 3 "" H 4100 1700 50  0001 C CNN
	1    4100 1700
	-1   0    0    1   
$EndComp
$Comp
L mainboard:R-US_R0603 R13
U 1 0 A7CEDF52
P 7300 1800
AR Path="/A7CEDF52" Ref="R13"  Part="1" 
AR Path="/5CEC5DDE/A7CEDF52" Ref="R13"  Part="1" 
F 0 "R13" H 7150 1859 59  0000 L BNN
F 1 "470k" H 7150 1670 59  0000 L BNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 7300 1800 50  0001 C CNN
F 3 "" H 7300 1800 50  0001 C CNN
	1    7300 1800
	0    -1   -1   0   
$EndComp
$Comp
L mainboard:R-US_R0603 R15
U 1 0 594DC3AA
P 7600 1800
AR Path="/594DC3AA" Ref="R15"  Part="1" 
AR Path="/5CEC5DDE/594DC3AA" Ref="R15"  Part="1" 
F 0 "R15" H 7450 1859 59  0000 L BNN
F 1 "4.7k" H 7450 1670 59  0000 L BNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 7600 1800 50  0001 C CNN
F 3 "" H 7600 1800 50  0001 C CNN
	1    7600 1800
	0    -1   -1   0   
$EndComp
$Comp
L mainboard:R-US_R0603 R16
U 1 0 9CD734CE
P 7700 2500
AR Path="/9CD734CE" Ref="R16"  Part="1" 
AR Path="/5CEC5DDE/9CD734CE" Ref="R16"  Part="1" 
F 0 "R16" H 7750 2359 59  0000 L BNN
F 1 "6.04K" H 7350 2370 59  0000 L BNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 7700 2500 50  0001 C CNN
F 3 "" H 7700 2500 50  0001 C CNN
	1    7700 2500
	-1   0    0    1   
$EndComp
$Comp
L mainboard:10UF-0603-6.3V-20% C17
U 1 0 0D67D074
P 3600 2700
AR Path="/0D67D074" Ref="C17"  Part="1" 
AR Path="/5CEC5DDE/0D67D074" Ref="C17"  Part="1" 
F 0 "C17" H 3660 2815 70  0000 L BNN
F 1 "10uF" H 3660 2615 70  0000 L BNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 3600 2700 50  0001 C CNN
F 3 "" H 3600 2700 50  0001 C CNN
	1    3600 2700
	1    0    0    -1  
$EndComp
$Comp
L mainboard:2.2UF-0603-10V-20% C19
U 1 0 FE784895
P 3900 2700
AR Path="/FE784895" Ref="C19"  Part="1" 
AR Path="/5CEC5DDE/FE784895" Ref="C19"  Part="1" 
F 0 "C19" H 3960 2815 70  0000 L BNN
F 1 "2.2uF" H 3960 2615 70  0000 L BNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 3900 2700 50  0001 C CNN
F 3 "" H 3900 2700 50  0001 C CNN
	1    3900 2700
	1    0    0    -1  
$EndComp
$Comp
L mainboard:2.2NF_2200PF-0603-50V-10% C20
U 1 0 BD6AC775
P 4100 2400
AR Path="/BD6AC775" Ref="C20"  Part="1" 
AR Path="/5CEC5DDE/BD6AC775" Ref="C20"  Part="1" 
F 0 "C20" H 4160 2515 70  0000 L BNN
F 1 "22nF" H 4160 2315 70  0000 L BNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 4100 2400 50  0001 C CNN
F 3 "" H 4100 2400 50  0001 C CNN
	1    4100 2400
	1    0    0    -1  
$EndComp
$Comp
L mainboard:R-US_R0603 R20
U 1 0 8DC0D790
P 8650 5600
AR Path="/8DC0D790" Ref="R20"  Part="1" 
AR Path="/5CEC5DDE/8DC0D790" Ref="R20"  Part="1" 
F 0 "R20" H 8500 5659 59  0000 L BNN
F 1 "3.3K" H 8500 5470 59  0000 L BNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 8650 5600 50  0001 C CNN
F 3 "" H 8650 5600 50  0001 C CNN
	1    8650 5600
	0    1    1    0   
$EndComp
$Comp
L mainboard:0.1UF-0603-25V-5% C24
U 1 0 524A8DB3
P 7200 3100
AR Path="/524A8DB3" Ref="C24"  Part="1" 
AR Path="/5CEC5DDE/524A8DB3" Ref="C24"  Part="1" 
F 0 "C24" H 7260 3015 70  0000 L BNN
F 1 "22uF" H 7260 2915 70  0000 L BNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 7200 3100 50  0001 C CNN
F 3 "" H 7200 3100 50  0001 C CNN
	1    7200 3100
	1    0    0    -1  
$EndComp
$Comp
L mainboard:GND #GND19
U 1 0 F278BC0E
P 7950 6300
AR Path="/F278BC0E" Ref="#GND19"  Part="1" 
AR Path="/5CEC5DDE/F278BC0E" Ref="#GND019"  Part="1" 
F 0 "#GND019" H 7950 6300 50  0001 C CNN
F 1 "GND" H 7850 6200 59  0000 L BNN
F 2 "" H 7950 6300 50  0001 C CNN
F 3 "" H 7950 6300 50  0001 C CNN
	1    7950 6300
	1    0    0    -1  
$EndComp
$Comp
L mainboard:CAP0603-CAP C23
U 1 0 E5B7FB5B
P 3900 5300
AR Path="/E5B7FB5B" Ref="C23"  Part="1" 
AR Path="/5CEC5DDE/E5B7FB5B" Ref="C23"  Part="1" 
F 0 "C23" H 3960 5415 59  0000 L BNN
F 1 ".1uF" H 3960 5215 59  0000 L BNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 3900 5300 50  0001 C CNN
F 3 "" H 3900 5300 50  0001 C CNN
	1    3900 5300
	1    0    0    -1  
$EndComp
$Comp
L mainboard:3.3V #P+2
U 1 0 637B3A6A
P 4200 5000
AR Path="/637B3A6A" Ref="#P+2"  Part="1" 
AR Path="/5CEC5DDE/637B3A6A" Ref="#P+02"  Part="1" 
F 0 "#P+02" H 4200 5000 50  0001 C CNN
F 1 "3.3V" H 4160 5140 59  0000 L BNN
F 2 "" H 4200 5000 50  0001 C CNN
F 3 "" H 4200 5000 50  0001 C CNN
	1    4200 5000
	1    0    0    -1  
$EndComp
$Comp
L mainboard:GND #GND15
U 1 0 7499CEA7
P 4200 5600
AR Path="/7499CEA7" Ref="#GND15"  Part="1" 
AR Path="/5CEC5DDE/7499CEA7" Ref="#GND015"  Part="1" 
F 0 "#GND015" H 4200 5600 50  0001 C CNN
F 1 "GND" H 4100 5500 59  0000 L BNN
F 2 "" H 4200 5600 50  0001 C CNN
F 3 "" H 4200 5600 50  0001 C CNN
	1    4200 5600
	1    0    0    -1  
$EndComp
$Comp
L mainboard:TPS54226PWPRPWP14_2P31X2P46-L U7
U 1 0 F8B2A26D
P 5400 6700
AR Path="/F8B2A26D" Ref="U7"  Part="1" 
AR Path="/5CEC5DDE/F8B2A26D" Ref="U7"  Part="1" 
F 0 "U7" H 6614 6259 69  0000 L BNN
F 1 "TPS54226PWPRPWP14_2P31X2P46-L" H 7811 7041 69  0000 R TNN
F 2 "mainboard:PWP14_2P31X2P46-L" H 5400 6700 50  0001 C CNN
F 3 "" H 5400 6700 50  0001 C CNN
	1    5400 6700
	-1   0    0    1   
$EndComp
$Comp
L mainboard:IND L3
U 1 0 A8ECB859
P 2200 6100
AR Path="/A8ECB859" Ref="L3"  Part="1" 
AR Path="/5CEC5DDE/A8ECB859" Ref="L3"  Part="1" 
F 0 "L3" H 2310 6100 59  0000 L BNN
F 1 "3.3uH" H 2110 5960 59  0000 L BNN
F 2 "mainboard:1812" H 2200 6100 50  0001 C CNN
F 3 "" H 2200 6100 50  0001 C CNN
	1    2200 6100
	1    0    0    -1  
$EndComp
$Comp
L mainboard:22UF-0805-6.3V-20% C16
U 1 0 DD051D17
P 1900 6000
AR Path="/DD051D17" Ref="C16"  Part="1" 
AR Path="/5CEC5DDE/DD051D17" Ref="C16"  Part="1" 
F 0 "C16" H 1960 6115 70  0000 L BNN
F 1 "22uF" H 1960 5915 70  0000 L BNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 1900 6000 50  0001 C CNN
F 3 "" H 1900 6000 50  0001 C CNN
	1    1900 6000
	1    0    0    -1  
$EndComp
$Comp
L mainboard:22UF-0805-6.3V-20% C15
U 1 0 46B7B6F7
P 1600 6000
AR Path="/46B7B6F7" Ref="C15"  Part="1" 
AR Path="/5CEC5DDE/46B7B6F7" Ref="C15"  Part="1" 
F 0 "C15" H 1660 6115 70  0000 L BNN
F 1 "22uF" H 1660 5915 70  0000 L BNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 1600 6000 50  0001 C CNN
F 3 "" H 1600 6000 50  0001 C CNN
	1    1600 6000
	1    0    0    -1  
$EndComp
$Comp
L mainboard:1.0UF-0603-16V-10% C22
U 1 0 05A8BE12
P 2700 6400
AR Path="/05A8BE12" Ref="C22"  Part="1" 
AR Path="/5CEC5DDE/05A8BE12" Ref="C22"  Part="1" 
F 0 "C22" H 2760 6515 70  0000 L BNN
F 1 "0.1uF" H 2760 6315 70  0000 L BNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 2700 6400 50  0001 C CNN
F 3 "" H 2700 6400 50  0001 C CNN
	1    2700 6400
	0    -1   -1   0   
$EndComp
$Comp
L mainboard:GND #GND13
U 1 0 85B66688
P 2900 7100
AR Path="/85B66688" Ref="#GND13"  Part="1" 
AR Path="/5CEC5DDE/85B66688" Ref="#GND013"  Part="1" 
F 0 "#GND013" H 2900 7100 50  0001 C CNN
F 1 "GND" H 2800 7000 59  0000 L BNN
F 2 "" H 2900 7100 50  0001 C CNN
F 3 "" H 2900 7100 50  0001 C CNN
	1    2900 7100
	1    0    0    -1  
$EndComp
$Comp
L mainboard:3.3V #P+1
U 1 0 6A081B6E
P 1400 5800
AR Path="/6A081B6E" Ref="#P+1"  Part="1" 
AR Path="/5CEC5DDE/6A081B6E" Ref="#P+01"  Part="1" 
F 0 "#P+01" H 1400 5800 50  0001 C CNN
F 1 "3.3V" H 1360 5940 59  0000 L BNN
F 2 "" H 1400 5800 50  0001 C CNN
F 3 "" H 1400 5800 50  0001 C CNN
	1    1400 5800
	1    0    0    -1  
$EndComp
$Comp
L mainboard:R-US_R0603 R17
U 1 0 59AFAF3F
P 6300 6300
AR Path="/59AFAF3F" Ref="R17"  Part="1" 
AR Path="/5CEC5DDE/59AFAF3F" Ref="R17"  Part="1" 
F 0 "R17" H 6150 6359 59  0000 L BNN
F 1 "100K" H 6150 6170 59  0000 L BNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 6300 6300 50  0001 C CNN
F 3 "" H 6300 6300 50  0001 C CNN
	1    6300 6300
	0    1    1    0   
$EndComp
$Comp
L mainboard:R-US_R0603 R14
U 1 0 07A6364C
P 5900 6900
AR Path="/07A6364C" Ref="R14"  Part="1" 
AR Path="/5CEC5DDE/07A6364C" Ref="R14"  Part="1" 
F 0 "R14" H 5750 6959 59  0000 L BNN
F 1 "22.1k" H 5750 6770 59  0000 L BNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 5900 6900 50  0001 C CNN
F 3 "" H 5900 6900 50  0001 C CNN
	1    5900 6900
	-1   0    0    1   
$EndComp
$Comp
L mainboard:R-US_R0603 R12
U 1 0 79C224D8
P 5500 6900
AR Path="/79C224D8" Ref="R12"  Part="1" 
AR Path="/5CEC5DDE/79C224D8" Ref="R12"  Part="1" 
F 0 "R12" H 5350 6959 59  0000 L BNN
F 1 "73.2K" H 5350 6770 59  0000 L BNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 5500 6900 50  0001 C CNN
F 3 "" H 5500 6900 50  0001 C CNN
	1    5500 6900
	-1   0    0    1   
$EndComp
$Comp
L mainboard:3.3NF-0603-100V-10% C25
U 1 0 A91C7A5B
P 6000 6400
AR Path="/A91C7A5B" Ref="C25"  Part="1" 
AR Path="/5CEC5DDE/A91C7A5B" Ref="C25"  Part="1" 
F 0 "C25" H 6060 6515 70  0000 L BNN
F 1 "3.3nF" H 6060 6315 70  0000 L BNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 6000 6400 50  0001 C CNN
F 3 "" H 6000 6400 50  0001 C CNN
	1    6000 6400
	0    -1   -1   0   
$EndComp
$Comp
L mainboard:1.0UF-0603-16V-10% C26
U 1 0 416D5D6D
P 6300 7000
AR Path="/416D5D6D" Ref="C26"  Part="1" 
AR Path="/5CEC5DDE/416D5D6D" Ref="C26"  Part="1" 
F 0 "C26" H 6360 7115 70  0000 L BNN
F 1 "1.0uF" H 6360 6915 70  0000 L BNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 6300 7000 50  0001 C CNN
F 3 "" H 6300 7000 50  0001 C CNN
	1    6300 7000
	1    0    0    -1  
$EndComp
$Comp
L mainboard:3.3V #P+3
U 1 0 48C2C5DB
P 7600 1500
AR Path="/48C2C5DB" Ref="#P+3"  Part="1" 
AR Path="/5CEC5DDE/48C2C5DB" Ref="#P+03"  Part="1" 
F 0 "#P+03" H 7600 1500 50  0001 C CNN
F 1 "3.3V" H 7560 1640 59  0000 L BNN
F 2 "" H 7600 1500 50  0001 C CNN
F 3 "" H 7600 1500 50  0001 C CNN
	1    7600 1500
	1    0    0    -1  
$EndComp
$Comp
L mainboard:MAX4372TEUK+T U5
U 1 0 E3998434
P 3300 5400
AR Path="/E3998434" Ref="U5"  Part="1" 
AR Path="/5CEC5DDE/E3998434" Ref="U5"  Part="1" 
F 0 "U5" H 4019 5049 69  0000 L BNN
F 1 "MAX4372TEUK+T" H 3601 5499 69  0000 L BNN
F 2 "mainboard:21-0057F" H 3300 5400 50  0001 C CNN
F 3 "" H 3300 5400 50  0001 C CNN
	1    3300 5400
	-1   0    0    1   
$EndComp
$Comp
L mainboard:GND #GND17
U 1 0 CBB20165
P 6300 7200
AR Path="/CBB20165" Ref="#GND17"  Part="1" 
AR Path="/5CEC5DDE/CBB20165" Ref="#GND017"  Part="1" 
F 0 "#GND017" H 6300 7200 50  0001 C CNN
F 1 "GND" H 6200 7100 59  0000 L BNN
F 2 "" H 6300 7200 50  0001 C CNN
F 3 "" H 6300 7200 50  0001 C CNN
	1    6300 7200
	1    0    0    -1  
$EndComp
$Comp
L mainboard:R-US_R0603 R19
U 1 0 B6F735ED
P 8250 5800
AR Path="/B6F735ED" Ref="R19"  Part="1" 
AR Path="/5CEC5DDE/B6F735ED" Ref="R19"  Part="1" 
F 0 "R19" H 8100 5859 59  0000 L BNN
F 1 "4.7K" H 8100 5670 59  0000 L BNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 8250 5800 50  0001 C CNN
F 3 "" H 8250 5800 50  0001 C CNN
	1    8250 5800
	1    0    0    -1  
$EndComp
$Comp
L mainboard:R-US_R0603 R18
U 1 0 BCED19F0
P 7950 6000
AR Path="/BCED19F0" Ref="R18"  Part="1" 
AR Path="/5CEC5DDE/BCED19F0" Ref="R18"  Part="1" 
F 0 "R18" H 7800 6059 59  0000 L BNN
F 1 "10K" H 7800 5870 59  0000 L BNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 7950 6000 50  0001 C CNN
F 3 "" H 7950 6000 50  0001 C CNN
	1    7950 6000
	0    1    1    0   
$EndComp
$Comp
L mainboard:3.3V #SUPPLY10
U 1 0 28999800
P 8650 5300
AR Path="/28999800" Ref="#SUPPLY10"  Part="1" 
AR Path="/5CEC5DDE/28999800" Ref="#SUPPLY010"  Part="1" 
F 0 "#SUPPLY010" H 8650 5300 50  0001 C CNN
F 1 "3.3V" H 8610 5440 59  0000 L BNN
F 2 "" H 8650 5300 50  0001 C CNN
F 3 "" H 8650 5300 50  0001 C CNN
	1    8650 5300
	1    0    0    -1  
$EndComp
$Comp
L mainboard:IRLML2803TRPBF Q15
U 1 0 37749090
P 8550 6000
AR Path="/37749090" Ref="Q15"  Part="1" 
AR Path="/5CEC5DDE/37749090" Ref="Q15"  Part="1" 
F 0 "Q15" H 8800 6050 59  0000 L TNN
F 1 "IRLML2803" H 8800 5950 59  0000 L TNN
F 2 "mainboard:SOT-23" H 8550 6000 50  0001 C CNN
F 3 "" H 8550 6000 50  0001 C CNN
	1    8550 6000
	1    0    0    -1  
$EndComp
$Comp
L mainboard:R-US_R2512 R35
U 1 0 285A325E
P 1600 5300
AR Path="/285A325E" Ref="R35"  Part="1" 
AR Path="/5CEC5DDE/285A325E" Ref="R35"  Part="1" 
F 0 "R35" H 1450 5359 59  0000 L BNN
F 1 "0.025" H 1450 5170 59  0000 L BNN
F 2 "Resistor_SMD:R_2512_6332Metric" H 1600 5300 50  0001 C CNN
F 3 "" H 1600 5300 50  0001 C CNN
	1    1600 5300
	0    -1   -1   0   
$EndComp
$Comp
L mainboard:GND #GND60
U 1 0 CF9E7117
P 2400 5900
AR Path="/CF9E7117" Ref="#GND60"  Part="1" 
AR Path="/5CEC5DDE/CF9E7117" Ref="#GND060"  Part="1" 
F 0 "#GND060" H 2400 5900 50  0001 C CNN
F 1 "GND" H 2300 5800 59  0000 L BNN
F 2 "" H 2400 5900 50  0001 C CNN
F 3 "" H 2400 5900 50  0001 C CNN
	1    2400 5900
	1    0    0    -1  
$EndComp
$Comp
L mainboard:R-US_R0603 R40
U 1 0 A8135784
P 7600 2700
AR Path="/A8135784" Ref="R40"  Part="1" 
AR Path="/5CEC5DDE/A8135784" Ref="R40"  Part="1" 
F 0 "R40" H 7450 2759 59  0000 L BNN
F 1 "2.1M" H 7450 2870 59  0000 L BNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 7600 2700 50  0001 C CNN
F 3 "" H 7600 2700 50  0001 C CNN
	1    7600 2700
	-1   0    0    1   
$EndComp
$Comp
L mainboard:R-US_R0603 R41
U 1 0 705317A3
P 7200 2600
AR Path="/705317A3" Ref="R41"  Part="1" 
AR Path="/5CEC5DDE/705317A3" Ref="R41"  Part="1" 
F 0 "R41" H 7150 2659 59  0000 L BNN
F 1 "845K" H 7150 2470 59  0000 L BNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 7200 2600 50  0001 C CNN
F 3 "" H 7200 2600 50  0001 C CNN
	1    7200 2600
	1    0    0    -1  
$EndComp
$Comp
L mainboard:22UF-1210-16V-20% C29
U 1 0 F3F07366
P 2300 6700
AR Path="/F3F07366" Ref="C29"  Part="1" 
AR Path="/5CEC5DDE/F3F07366" Ref="C29"  Part="1" 
F 0 "C29" H 2360 6815 70  0000 L BNN
F 1 "220UF" H 2360 6615 70  0000 L BNN
F 2 "Capacitor_SMD:C_1210_3225Metric" H 2300 6700 50  0001 C CNN
F 3 "" H 2300 6700 50  0001 C CNN
	1    2300 6700
	1    0    0    -1  
$EndComp
$Comp
L mainboard:22UF-1210-16V-20% C30
U 1 0 5F2BDD0C
P 1900 6700
AR Path="/5F2BDD0C" Ref="C30"  Part="1" 
AR Path="/5CEC5DDE/5F2BDD0C" Ref="C30"  Part="1" 
F 0 "C30" H 1960 6815 70  0000 L BNN
F 1 "220UF" H 1960 6615 70  0000 L BNN
F 2 "Capacitor_SMD:C_1210_3225Metric" H 1900 6700 50  0001 C CNN
F 3 "" H 1900 6700 50  0001 C CNN
	1    1900 6700
	1    0    0    -1  
$EndComp
Text Notes 2100 4800 0    59   ~ 0
Battery Current Sensor
Text Notes 8550 4900 0    85   ~ 0
GPS Power
Text Notes 4200 1000 0    85   ~ 0
2s2P Li-Ion Battery Charging Circuit
Text Notes 2800 4400 0    85   ~ 0
Regulator - 3.3V OUT
Text Notes 1200 6300 0    42   ~ 0
VBATT 4.5 to 18V
Text Notes 8300 2200 0    59   ~ 0
PROG\nmonitors charge current using:\nIchrg=988*Vprog/Rprog\n
Wire Wire Line
	2300 6900 2900 6900
Wire Wire Line
	2600 6100 2900 6100
Wire Wire Line
	2300 6500 2900 6500
$Comp
L symbols:NDS8434 U?
U 1 1 5CF356D9
P 9800 5500
AR Path="/5CEC5A72/5CF356D9" Ref="U?"  Part="1" 
AR Path="/5CEC5DDE/5CF356D9" Ref="U11"  Part="1" 
F 0 "U11" H 9800 5500 50  0001 L BNN
F 1 "NDS8434" H 9800 5500 50  0001 L BNN
F 2 "custom-footprints:NDS8434" H 9800 5500 50  0001 L BNN
F 3 "" H 9800 5500 50  0001 L BNN
F 4 "ON Semiconductor" H 9800 5500 50  0001 L BNN "Field4"
F 5 "Unavailable" H 9800 5500 50  0001 L BNN "Field5"
F 6 "None" H 9800 5500 50  0001 L BNN "Field6"
F 7 "NDS8434" H 9800 5500 50  0001 L BNN "Field7"
F 8 "SO-8 ON Semiconductor" H 9800 5500 50  0001 L BNN "Field8"
	1    9800 5500
	1    0    0    -1  
$EndComp
Wire Wire Line
	9300 5800 8650 5800
Connection ~ 8650 5800
Wire Wire Line
	9300 5600 9300 5400
Wire Wire Line
	9300 5400 8650 5400
Connection ~ 9300 5400
Connection ~ 8650 5400
Wire Wire Line
	9300 5400 9300 5200
Wire Wire Line
	10300 5200 10300 5400
Wire Wire Line
	10300 5800 10500 5800
Connection ~ 10300 5800
Connection ~ 10300 5400
Wire Wire Line
	10300 5400 10300 5600
Connection ~ 10300 5600
Wire Wire Line
	10300 5600 10300 5800
Text Notes 8950 6950 0    200  ~ 0
Power
$EndSCHEMATC