EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 2 4
Title "QubeSat Payload Mainboard"
Date "2020-07-22"
Rev "V01"
Comp "By: Vidish Gupta"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Payload_V01:AD9838 U?
U 1 1 5F1B5ED0
P 4900 4550
AR Path="/5F1B5ED0" Ref="U?"  Part="1" 
AR Path="/5F190638/5F1B5ED0" Ref="U?"  Part="1" 
F 0 "U?" H 4900 4600 50  0000 C CNN
F 1 "AD9838" H 4900 4500 50  0000 C CNN
F 2 "" H 4900 3950 50  0001 C CNN
F 3 "" H 4900 3950 50  0001 C CNN
	1    4900 4550
	1    0    0    -1  
$EndComp
$Comp
L Device:C C?
U 1 1 5F1B5ED6
P 4450 2750
AR Path="/5F1B5ED6" Ref="C?"  Part="1" 
AR Path="/5F190638/5F1B5ED6" Ref="C?"  Part="1" 
F 0 "C?" V 4198 2750 50  0000 C CNN
F 1 "1uF" V 4289 2750 50  0000 C CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.05x0.95mm_HandSolder" H 4488 2600 50  0001 C CNN
F 3 "~" H 4450 2750 50  0001 C CNN
	1    4450 2750
	0    1    1    0   
$EndComp
$Comp
L Device:C C?
U 1 1 5F1B5EDC
P 4450 3150
AR Path="/5F1B5EDC" Ref="C?"  Part="1" 
AR Path="/5F190638/5F1B5EDC" Ref="C?"  Part="1" 
F 0 "C?" V 4198 3150 50  0000 C CNN
F 1 "0.1uF" V 4289 3150 50  0000 C CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.05x0.95mm_HandSolder" H 4488 3000 50  0001 C CNN
F 3 "~" H 4450 3150 50  0001 C CNN
	1    4450 3150
	0    1    1    0   
$EndComp
$Comp
L Device:Jumper JP?
U 1 1 5F1B5EE2
P 4950 2750
AR Path="/5F1B5EE2" Ref="JP?"  Part="1" 
AR Path="/5F190638/5F1B5EE2" Ref="JP?"  Part="1" 
F 0 "JP?" H 4950 3014 50  0000 C CNN
F 1 "Jumper" H 4950 2923 50  0000 C CNN
F 2 "" H 4950 2750 50  0001 C CNN
F 3 "~" H 4950 2750 50  0001 C CNN
	1    4950 2750
	1    0    0    -1  
$EndComp
$Comp
L Device:C C?
U 1 1 5F1B5EE8
P 4900 2300
AR Path="/5F1B5EE8" Ref="C?"  Part="1" 
AR Path="/5F190638/5F1B5EE8" Ref="C?"  Part="1" 
F 0 "C?" V 4648 2300 50  0000 C CNN
F 1 "0.1uF" V 4739 2300 50  0000 C CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.05x0.95mm_HandSolder" H 4938 2150 50  0001 C CNN
F 3 "~" H 4900 2300 50  0001 C CNN
	1    4900 2300
	0    1    1    0   
$EndComp
$Comp
L Jumper:Jumper_3_Open JP?
U 1 1 5F1B5EEE
P 5250 1450
AR Path="/5F1B5EEE" Ref="JP?"  Part="1" 
AR Path="/5F190638/5F1B5EEE" Ref="JP?"  Part="1" 
F 0 "JP?" H 5250 1674 50  0000 C CNN
F 1 "Jumper_3_Open" H 5250 1583 50  0000 C CNN
F 2 "" H 5250 1450 50  0001 C CNN
F 3 "~" H 5250 1450 50  0001 C CNN
	1    5250 1450
	1    0    0    -1  
$EndComp
Wire Wire Line
	4650 3400 4650 3150
Wire Wire Line
	4650 3150 4600 3150
Wire Wire Line
	4600 2750 4650 2750
Wire Wire Line
	4650 3150 4650 2750
Connection ~ 4650 3150
Wire Wire Line
	4300 2750 3900 2750
Wire Wire Line
	3900 2750 3900 3150
Wire Wire Line
	3900 3150 4300 3150
Connection ~ 4650 2750
Wire Wire Line
	4900 3400 4900 3050
Wire Wire Line
	4900 3050 5250 3050
Wire Wire Line
	5250 3050 5250 2750
Wire Wire Line
	5250 2750 5250 2300
Wire Wire Line
	5250 2300 5050 2300
Connection ~ 5250 2750
Wire Wire Line
	4150 2300 4750 2300
Wire Wire Line
	5250 2300 5250 1850
Wire Wire Line
	5250 1850 4950 1850
Connection ~ 5250 2300
Text Label 4950 1850 0    50   ~ 0
DVDD_1
Wire Wire Line
	5250 1850 5250 1600
Connection ~ 5250 1850
Wire Wire Line
	5000 1450 4750 1450
Wire Wire Line
	4750 1450 4750 1250
$Comp
L power:VDD #PWR?
U 1 1 5F1B5F0C
P 4750 1250
AR Path="/5F1B5F0C" Ref="#PWR?"  Part="1" 
AR Path="/5F190638/5F1B5F0C" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 4750 1100 50  0001 C CNN
F 1 "VDD" H 4765 1423 50  0000 C CNN
F 2 "" H 4750 1250 50  0001 C CNN
F 3 "" H 4750 1250 50  0001 C CNN
	1    4750 1250
	1    0    0    -1  
$EndComp
Wire Wire Line
	5500 1450 5700 1450
Wire Wire Line
	5700 1450 5700 950 
Text Label 5700 1200 1    50   ~ 0
3.3V_BF
Wire Wire Line
	5700 950  6350 950 
Wire Wire Line
	6350 950  6350 1450
$Comp
L Jumper:Jumper_3_Open JP?
U 1 1 5F1B5F17
P 6100 1450
AR Path="/5F1B5F17" Ref="JP?"  Part="1" 
AR Path="/5F190638/5F1B5F17" Ref="JP?"  Part="1" 
F 0 "JP?" H 6100 1674 50  0000 C CNN
F 1 "Jumper_3_Open" H 6100 1583 50  0000 C CNN
F 2 "" H 6100 1450 50  0001 C CNN
F 3 "~" H 6100 1450 50  0001 C CNN
	1    6100 1450
	1    0    0    -1  
$EndComp
Wire Wire Line
	5850 1450 5850 1200
$Comp
L power:VDDA #PWR?
U 1 1 5F1B5F1E
P 5850 1200
AR Path="/5F1B5F1E" Ref="#PWR?"  Part="1" 
AR Path="/5F190638/5F1B5F1E" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 5850 1050 50  0001 C CNN
F 1 "VDDA" H 5865 1373 50  0000 C CNN
F 2 "" H 5850 1200 50  0001 C CNN
F 3 "" H 5850 1200 50  0001 C CNN
	1    5850 1200
	1    0    0    -1  
$EndComp
$Comp
L Device:C C?
U 1 1 5F1B5F24
P 6050 2850
AR Path="/5F1B5F24" Ref="C?"  Part="1" 
AR Path="/5F190638/5F1B5F24" Ref="C?"  Part="1" 
F 0 "C?" V 5798 2850 50  0000 C CNN
F 1 "0.1uF" V 5889 2850 50  0000 C CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.05x0.95mm_HandSolder" H 6088 2700 50  0001 C CNN
F 3 "~" H 6050 2850 50  0001 C CNN
	1    6050 2850
	0    1    1    0   
$EndComp
Wire Wire Line
	5200 3400 5200 3200
Wire Wire Line
	5200 3200 5900 3200
Wire Wire Line
	5900 3200 5900 2850
Wire Wire Line
	5900 2850 5900 2350
Wire Wire Line
	5900 2350 6100 2350
Connection ~ 5900 2850
Wire Wire Line
	6200 2850 6400 2850
$Comp
L power:GND #PWR?
U 1 1 5F1B5F31
P 6400 2850
AR Path="/5F1B5F31" Ref="#PWR?"  Part="1" 
AR Path="/5F190638/5F1B5F31" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 6400 2600 50  0001 C CNN
F 1 "GND" H 6405 2677 50  0000 C CNN
F 2 "" H 6400 2850 50  0001 C CNN
F 3 "" H 6400 2850 50  0001 C CNN
	1    6400 2850
	1    0    0    -1  
$EndComp
Wire Wire Line
	6100 2350 6100 1600
Wire Wire Line
	6100 2350 6600 2350
Wire Wire Line
	6600 2350 6600 3900
Connection ~ 6100 2350
$Comp
L Device:C C?
U 1 1 5F1B5F3B
P 6100 3900
AR Path="/5F1B5F3B" Ref="C?"  Part="1" 
AR Path="/5F190638/5F1B5F3B" Ref="C?"  Part="1" 
F 0 "C?" V 6352 3900 50  0000 C CNN
F 1 "0.01uF" V 6261 3900 50  0000 C CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.05x0.95mm_HandSolder" H 6138 3750 50  0001 C CNN
F 3 "~" H 6100 3900 50  0001 C CNN
	1    6100 3900
	0    -1   -1   0   
$EndComp
Wire Wire Line
	5950 3900 5600 3900
Wire Wire Line
	6250 3900 6600 3900
$Comp
L Device:C C?
U 1 1 5F1B5F43
P 6400 4100
AR Path="/5F1B5F43" Ref="C?"  Part="1" 
AR Path="/5F190638/5F1B5F43" Ref="C?"  Part="1" 
F 0 "C?" V 6148 4100 50  0000 C CNN
F 1 "0.1uF" V 6239 4100 50  0000 C CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.05x0.95mm_HandSolder" H 6438 3950 50  0001 C CNN
F 3 "~" H 6400 4100 50  0001 C CNN
	1    6400 4100
	0    1    1    0   
$EndComp
Wire Wire Line
	5600 4100 6250 4100
Wire Wire Line
	6550 4100 6850 4100
$Comp
L power:GND #PWR?
U 1 1 5F1B5F4B
P 6850 4100
AR Path="/5F1B5F4B" Ref="#PWR?"  Part="1" 
AR Path="/5F190638/5F1B5F4B" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 6850 3850 50  0001 C CNN
F 1 "GND" H 6855 3927 50  0000 C CNN
F 2 "" H 6850 4100 50  0001 C CNN
F 3 "" H 6850 4100 50  0001 C CNN
	1    6850 4100
	1    0    0    -1  
$EndComp
$Comp
L Device:C C?
U 1 1 5F1B5F51
P 6050 4500
AR Path="/5F1B5F51" Ref="C?"  Part="1" 
AR Path="/5F190638/5F1B5F51" Ref="C?"  Part="1" 
F 0 "C?" V 6300 4500 50  0000 C CNN
F 1 "0.1uF" V 6200 4500 50  0000 C CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.05x0.95mm_HandSolder" H 6088 4350 50  0001 C CNN
F 3 "~" H 6050 4500 50  0001 C CNN
	1    6050 4500
	0    1    1    0   
$EndComp
$Comp
L Device:R_US R?
U 1 1 5F1B5F57
P 6050 4350
AR Path="/5F1B5F57" Ref="R?"  Part="1" 
AR Path="/5F190638/5F1B5F57" Ref="R?"  Part="1" 
F 0 "R?" V 5845 4350 50  0000 C CNN
F 1 "6.8k" V 5936 4350 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad1.05x0.95mm_HandSolder" V 6090 4340 50  0001 C CNN
F 3 "~" H 6050 4350 50  0001 C CNN
	1    6050 4350
	0    1    1    0   
$EndComp
Wire Wire Line
	5900 4350 5900 4500
Wire Wire Line
	6200 4350 6200 4500
Wire Wire Line
	5900 4350 5750 4350
Wire Wire Line
	5750 4350 5750 4300
Wire Wire Line
	5750 4300 5600 4300
Connection ~ 5900 4350
Wire Wire Line
	6200 4350 6450 4350
Connection ~ 6200 4350
$Comp
L power:GND #PWR?
U 1 1 5F1B5F65
P 6450 4350
AR Path="/5F1B5F65" Ref="#PWR?"  Part="1" 
AR Path="/5F190638/5F1B5F65" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 6450 4100 50  0001 C CNN
F 1 "GND" H 6455 4177 50  0000 C CNN
F 2 "" H 6450 4350 50  0001 C CNN
F 3 "" H 6450 4350 50  0001 C CNN
	1    6450 4350
	1    0    0    -1  
$EndComp
Wire Wire Line
	5600 4700 5850 4700
Wire Wire Line
	5850 4700 5850 4850
Wire Wire Line
	5850 4850 6950 4850
$Comp
L Device:R_US R?
U 1 1 5F1B5F6E
P 6950 5000
AR Path="/5F1B5F6E" Ref="R?"  Part="1" 
AR Path="/5F190638/5F1B5F6E" Ref="R?"  Part="1" 
F 0 "R?" H 7018 5046 50  0000 L CNN
F 1 "200" H 7018 4955 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad1.05x0.95mm_HandSolder" V 6990 4990 50  0001 C CNN
F 3 "~" H 6950 5000 50  0001 C CNN
	1    6950 5000
	1    0    0    -1  
$EndComp
$Comp
L Device:C C?
U 1 1 5F1B5F74
P 7300 5000
AR Path="/5F1B5F74" Ref="C?"  Part="1" 
AR Path="/5F190638/5F1B5F74" Ref="C?"  Part="1" 
F 0 "C?" H 7415 5046 50  0000 L CNN
F 1 "0.1uF" H 7415 4955 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.05x0.95mm_HandSolder" H 7338 4850 50  0001 C CNN
F 3 "~" H 7300 5000 50  0001 C CNN
	1    7300 5000
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5F1B5F7A
P 6950 5150
AR Path="/5F1B5F7A" Ref="#PWR?"  Part="1" 
AR Path="/5F190638/5F1B5F7A" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 6950 4900 50  0001 C CNN
F 1 "GND" H 6955 4977 50  0000 C CNN
F 2 "" H 6950 5150 50  0001 C CNN
F 3 "" H 6950 5150 50  0001 C CNN
	1    6950 5150
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5F1B5F80
P 7300 5150
AR Path="/5F1B5F80" Ref="#PWR?"  Part="1" 
AR Path="/5F190638/5F1B5F80" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 7300 4900 50  0001 C CNN
F 1 "GND" H 7305 4977 50  0000 C CNN
F 2 "" H 7300 5150 50  0001 C CNN
F 3 "" H 7300 5150 50  0001 C CNN
	1    7300 5150
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5F1B5F86
P 7900 5150
AR Path="/5F1B5F86" Ref="#PWR?"  Part="1" 
AR Path="/5F190638/5F1B5F86" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 7900 4900 50  0001 C CNN
F 1 "GND" H 7905 4977 50  0000 C CNN
F 2 "" H 7900 5150 50  0001 C CNN
F 3 "" H 7900 5150 50  0001 C CNN
	1    7900 5150
	1    0    0    -1  
$EndComp
Wire Wire Line
	6950 4850 7300 4850
Connection ~ 6950 4850
Connection ~ 7300 4850
Wire Wire Line
	7300 4850 7700 4850
$Comp
L Connector:Conn_Coaxial J?
U 1 1 5F1B5F90
P 7900 4850
AR Path="/5F1B5F90" Ref="J?"  Part="1" 
AR Path="/5F190638/5F1B5F90" Ref="J?"  Part="1" 
F 0 "J?" H 8000 4825 50  0000 L CNN
F 1 "Conn_Coaxial" H 8000 4734 50  0000 L CNN
F 2 "Connector_Coaxial:SMB_Jack_Vertical" H 7900 4850 50  0001 C CNN
F 3 " ~" H 7900 4850 50  0001 C CNN
	1    7900 4850
	1    0    0    -1  
$EndComp
Wire Wire Line
	7900 5050 7900 5150
Wire Wire Line
	5600 5300 5850 5300
Wire Wire Line
	5850 5300 5850 5700
$Comp
L Connector:Conn_Coaxial J?
U 1 1 5F1B5F99
P 6050 5700
AR Path="/5F1B5F99" Ref="J?"  Part="1" 
AR Path="/5F190638/5F1B5F99" Ref="J?"  Part="1" 
F 0 "J?" H 6150 5675 50  0000 L CNN
F 1 "Conn_Coaxial" H 6150 5584 50  0000 L CNN
F 2 "Connector_Coaxial:SMB_Jack_Vertical" H 6050 5700 50  0001 C CNN
F 3 " ~" H 6050 5700 50  0001 C CNN
	1    6050 5700
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5F1B5F9F
P 6050 5900
AR Path="/5F1B5F9F" Ref="#PWR?"  Part="1" 
AR Path="/5F190638/5F1B5F9F" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 6050 5650 50  0001 C CNN
F 1 "GND" H 6055 5727 50  0000 C CNN
F 2 "" H 6050 5900 50  0001 C CNN
F 3 "" H 6050 5900 50  0001 C CNN
	1    6050 5900
	1    0    0    -1  
$EndComp
$Comp
L Device:C C?
U 1 1 5F1B5FA5
P 7200 5950
AR Path="/5F1B5FA5" Ref="C?"  Part="1" 
AR Path="/5F190638/5F1B5FA5" Ref="C?"  Part="1" 
F 0 "C?" H 7315 5996 50  0000 L CNN
F 1 "0.1uF" H 7315 5905 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.05x0.95mm_HandSolder" H 7238 5800 50  0001 C CNN
F 3 "~" H 7200 5950 50  0001 C CNN
	1    7200 5950
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R?
U 1 1 5F1B5FAB
P 7500 5800
AR Path="/5F1B5FAB" Ref="R?"  Part="1" 
AR Path="/5F190638/5F1B5FAB" Ref="R?"  Part="1" 
F 0 "R?" V 7295 5800 50  0000 C CNN
F 1 "300" V 7386 5800 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad1.05x0.95mm_HandSolder" V 7540 5790 50  0001 C CNN
F 3 "~" H 7500 5800 50  0001 C CNN
	1    7500 5800
	0    1    1    0   
$EndComp
$Comp
L Device:R_US R?
U 1 1 5F1B5FB1
P 8300 5650
AR Path="/5F1B5FB1" Ref="R?"  Part="1" 
AR Path="/5F190638/5F1B5FB1" Ref="R?"  Part="1" 
F 0 "R?" H 8232 5604 50  0000 R CNN
F 1 "200" H 8232 5695 50  0000 R CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad1.05x0.95mm_HandSolder" V 8340 5640 50  0001 C CNN
F 3 "~" H 8300 5650 50  0001 C CNN
	1    8300 5650
	-1   0    0    1   
$EndComp
$Comp
L Device:C C?
U 1 1 5F1B5FB7
P 8700 5650
AR Path="/5F1B5FB7" Ref="C?"  Part="1" 
AR Path="/5F190638/5F1B5FB7" Ref="C?"  Part="1" 
F 0 "C?" H 8815 5696 50  0000 L CNN
F 1 "0.1uF" H 8815 5605 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 8738 5500 50  0001 C CNN
F 3 "~" H 8700 5650 50  0001 C CNN
	1    8700 5650
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_Coaxial J?
U 1 1 5F1B5FBD
P 9150 5500
AR Path="/5F1B5FBD" Ref="J?"  Part="1" 
AR Path="/5F190638/5F1B5FBD" Ref="J?"  Part="1" 
F 0 "J?" H 9250 5475 50  0000 L CNN
F 1 "Conn_Coaxial" H 9250 5384 50  0000 L CNN
F 2 "Connector_Coaxial:SMB_Jack_Vertical" H 9150 5500 50  0001 C CNN
F 3 " ~" H 9150 5500 50  0001 C CNN
	1    9150 5500
	1    0    0    -1  
$EndComp
Wire Wire Line
	5600 5100 6050 5100
Wire Wire Line
	6050 5100 6050 5550
Wire Wire Line
	6050 5550 6750 5550
Wire Wire Line
	6750 5550 6750 5800
Wire Wire Line
	6750 5800 7200 5800
Connection ~ 7200 5800
Wire Wire Line
	7200 5800 7350 5800
$Comp
L power:GND #PWR?
U 1 1 5F1B5FCA
P 7200 6100
AR Path="/5F1B5FCA" Ref="#PWR?"  Part="1" 
AR Path="/5F190638/5F1B5FCA" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 7200 5850 50  0001 C CNN
F 1 "GND" H 7205 5927 50  0000 C CNN
F 2 "" H 7200 6100 50  0001 C CNN
F 3 "" H 7200 6100 50  0001 C CNN
	1    7200 6100
	1    0    0    -1  
$EndComp
Wire Wire Line
	5600 4900 6150 4900
Wire Wire Line
	6150 4900 6150 5500
Wire Wire Line
	6150 5500 7800 5500
Connection ~ 8300 5500
Wire Wire Line
	8300 5500 8700 5500
Connection ~ 8700 5500
Wire Wire Line
	8700 5500 8950 5500
Wire Wire Line
	7650 5800 7800 5800
Wire Wire Line
	7800 5800 7800 5500
Connection ~ 7800 5500
Wire Wire Line
	7800 5500 8300 5500
$Comp
L power:GND #PWR?
U 1 1 5F1B5FDB
P 8300 5800
AR Path="/5F1B5FDB" Ref="#PWR?"  Part="1" 
AR Path="/5F190638/5F1B5FDB" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 8300 5550 50  0001 C CNN
F 1 "GND" H 8305 5627 50  0000 C CNN
F 2 "" H 8300 5800 50  0001 C CNN
F 3 "" H 8300 5800 50  0001 C CNN
	1    8300 5800
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5F1B5FE1
P 8700 5800
AR Path="/5F1B5FE1" Ref="#PWR?"  Part="1" 
AR Path="/5F190638/5F1B5FE1" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 8700 5550 50  0001 C CNN
F 1 "GND" H 8705 5627 50  0000 C CNN
F 2 "" H 8700 5800 50  0001 C CNN
F 3 "" H 8700 5800 50  0001 C CNN
	1    8700 5800
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5F1B5FE7
P 9150 5800
AR Path="/5F1B5FE7" Ref="#PWR?"  Part="1" 
AR Path="/5F190638/5F1B5FE7" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 9150 5550 50  0001 C CNN
F 1 "GND" H 9155 5627 50  0000 C CNN
F 2 "" H 9150 5800 50  0001 C CNN
F 3 "" H 9150 5800 50  0001 C CNN
	1    9150 5800
	1    0    0    -1  
$EndComp
Wire Wire Line
	9150 5700 9150 5800
$Comp
L power:GNDD #PWR?
U 1 1 5F1B5FEE
P 4650 5950
AR Path="/5F1B5FEE" Ref="#PWR?"  Part="1" 
AR Path="/5F190638/5F1B5FEE" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 4650 5700 50  0001 C CNN
F 1 "GNDD" H 4654 5795 50  0000 C CNN
F 2 "" H 4650 5950 50  0001 C CNN
F 3 "" H 4650 5950 50  0001 C CNN
	1    4650 5950
	1    0    0    -1  
$EndComp
Wire Wire Line
	4650 5950 4650 5850
Wire Wire Line
	4650 5850 5150 5850
Wire Wire Line
	5150 5850 5150 5950
Connection ~ 4650 5850
Wire Wire Line
	4650 5850 4650 5700
Wire Wire Line
	5150 5700 5150 5850
Connection ~ 5150 5850
$Comp
L Payload_V01:SG-310SCF Y?
U 1 1 5F1B5FFB
P 3200 5700
AR Path="/5F1B5FFB" Ref="Y?"  Part="1" 
AR Path="/5F190638/5F1B5FFB" Ref="Y?"  Part="1" 
F 0 "Y?" H 3225 6125 50  0000 C CNN
F 1 "SG-310SCF" H 3225 6034 50  0000 C CNN
F 2 "" H 3200 5700 50  0001 C CNN
F 3 "" H 3200 5700 50  0001 C CNN
	1    3200 5700
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R?
U 1 1 5F1B6001
P 4000 5350
AR Path="/5F1B6001" Ref="R?"  Part="1" 
AR Path="/5F190638/5F1B6001" Ref="R?"  Part="1" 
F 0 "R?" H 4068 5396 50  0000 L CNN
F 1 "0" H 4068 5305 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad1.05x0.95mm_HandSolder" V 4040 5340 50  0001 C CNN
F 3 "~" H 4000 5350 50  0001 C CNN
	1    4000 5350
	1    0    0    -1  
$EndComp
Wire Wire Line
	3550 5500 4000 5500
Wire Wire Line
	3550 5900 3800 5900
Wire Wire Line
	3800 5900 3800 6000
$Comp
L power:GNDD #PWR?
U 1 1 5F1B600A
P 3800 6000
AR Path="/5F1B600A" Ref="#PWR?"  Part="1" 
AR Path="/5F190638/5F1B600A" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 3800 5750 50  0001 C CNN
F 1 "GNDD" H 3804 5845 50  0000 C CNN
F 2 "" H 3800 6000 50  0001 C CNN
F 3 "" H 3800 6000 50  0001 C CNN
	1    3800 6000
	1    0    0    -1  
$EndComp
Wire Wire Line
	2900 5900 2750 5900
$Comp
L Jumper:Jumper_3_Open JP?
U 1 1 5F1B6011
P 2550 5500
AR Path="/5F1B6011" Ref="JP?"  Part="1" 
AR Path="/5F190638/5F1B6011" Ref="JP?"  Part="1" 
F 0 "JP?" V 2596 5587 50  0000 L CNN
F 1 "Jumper_3_Open" V 2505 5587 50  0000 L CNN
F 2 "" H 2550 5500 50  0001 C CNN
F 3 "~" H 2550 5500 50  0001 C CNN
	1    2550 5500
	0    -1   -1   0   
$EndComp
Wire Wire Line
	2700 5500 2900 5500
Wire Wire Line
	2550 5250 2550 5150
$Comp
L power:VDD #PWR?
U 1 1 5F1B6019
P 2550 5150
AR Path="/5F1B6019" Ref="#PWR?"  Part="1" 
AR Path="/5F190638/5F1B6019" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 2550 5000 50  0001 C CNN
F 1 "VDD" H 2565 5323 50  0000 C CNN
F 2 "" H 2550 5150 50  0001 C CNN
F 3 "" H 2550 5150 50  0001 C CNN
	1    2550 5150
	1    0    0    -1  
$EndComp
Wire Wire Line
	4000 5200 4250 5200
$Comp
L Device:C C?
U 1 1 5F1B6020
P 3200 6800
AR Path="/5F1B6020" Ref="C?"  Part="1" 
AR Path="/5F190638/5F1B6020" Ref="C?"  Part="1" 
F 0 "C?" H 3315 6846 50  0000 L CNN
F 1 "1uF" H 3315 6755 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.05x0.95mm_HandSolder" H 3238 6650 50  0001 C CNN
F 3 "~" H 3200 6800 50  0001 C CNN
	1    3200 6800
	1    0    0    -1  
$EndComp
$Comp
L Device:C C?
U 1 1 5F1B6026
P 2900 6800
AR Path="/5F1B6026" Ref="C?"  Part="1" 
AR Path="/5F190638/5F1B6026" Ref="C?"  Part="1" 
F 0 "C?" H 3015 6846 50  0000 L CNN
F 1 "0.1uF" H 3015 6755 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.05x0.95mm_HandSolder" H 2938 6650 50  0001 C CNN
F 3 "~" H 2900 6800 50  0001 C CNN
	1    2900 6800
	1    0    0    -1  
$EndComp
Wire Wire Line
	1250 6950 1500 6950
Wire Wire Line
	1250 6950 1250 7050
Connection ~ 1250 6950
$Comp
L power:GNDD #PWR?
U 1 1 5F1B602F
P 1250 7050
AR Path="/5F1B602F" Ref="#PWR?"  Part="1" 
AR Path="/5F190638/5F1B602F" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 1250 6800 50  0001 C CNN
F 1 "GNDD" H 1254 6895 50  0000 C CNN
F 2 "" H 1250 7050 50  0001 C CNN
F 3 "" H 1250 7050 50  0001 C CNN
	1    1250 7050
	1    0    0    -1  
$EndComp
Wire Wire Line
	1250 6650 1500 6650
Wire Wire Line
	1500 6650 1750 6650
Connection ~ 1500 6650
Wire Wire Line
	1750 6650 1750 6350
Wire Wire Line
	1750 6350 2300 6350
Connection ~ 1750 6650
Wire Wire Line
	1750 6650 1900 6650
Connection ~ 1250 6650
Text Label 1050 6650 0    50   ~ 0
5V_EXT
Wire Wire Line
	2600 6650 2900 6650
Connection ~ 2900 6650
Wire Wire Line
	2900 6650 3200 6650
Wire Wire Line
	3200 6650 3200 6050
Wire Wire Line
	3200 6050 2550 6050
Wire Wire Line
	2550 6050 2550 5750
Connection ~ 3200 6650
Wire Wire Line
	2900 6950 3200 6950
$Comp
L power:GNDD #PWR?
U 1 1 5F1B6046
P 2900 7050
AR Path="/5F1B6046" Ref="#PWR?"  Part="1" 
AR Path="/5F190638/5F1B6046" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 2900 6800 50  0001 C CNN
F 1 "GNDD" H 2904 6895 50  0000 C CNN
F 2 "" H 2900 7050 50  0001 C CNN
F 3 "" H 2900 7050 50  0001 C CNN
	1    2900 7050
	1    0    0    -1  
$EndComp
$Comp
L power:GNDD #PWR?
U 1 1 5F1B604C
P 2300 7050
AR Path="/5F1B604C" Ref="#PWR?"  Part="1" 
AR Path="/5F190638/5F1B604C" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 2300 6800 50  0001 C CNN
F 1 "GNDD" H 2304 6895 50  0000 C CNN
F 2 "" H 2300 7050 50  0001 C CNN
F 3 "" H 2300 7050 50  0001 C CNN
	1    2300 7050
	1    0    0    -1  
$EndComp
Wire Wire Line
	2300 7050 2300 6950
Wire Wire Line
	2900 7050 2900 6950
Connection ~ 2900 6950
$Comp
L Device:C C?
U 1 1 5F1B6055
P 1500 6800
AR Path="/5F1B6055" Ref="C?"  Part="1" 
AR Path="/5F190638/5F1B6055" Ref="C?"  Part="1" 
F 0 "C?" H 1615 6846 50  0000 L CNN
F 1 "10uF" H 1615 6755 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.05x0.95mm_HandSolder" H 1538 6650 50  0001 C CNN
F 3 "~" H 1500 6800 50  0001 C CNN
	1    1500 6800
	1    0    0    -1  
$EndComp
$Comp
L Reference_Voltage:REF196 U?
U 1 1 5F1B605B
P 2300 6650
AR Path="/5F1B605B" Ref="U?"  Part="1" 
AR Path="/5F190638/5F1B605B" Ref="U?"  Part="1" 
F 0 "U?" H 2644 6696 50  0000 L CNN
F 1 "REF196" H 2350 6400 50  0000 L CNN
F 2 "" H 2300 6600 50  0001 C CIN
F 3 "https://www.analog.com/static/imported-files/data_sheets/REF19xSeries.pdf" H 2300 6600 50  0001 C CIN
	1    2300 6650
	1    0    0    -1  
$EndComp
Wire Wire Line
	1250 6650 1050 6650
$Comp
L Device:C C?
U 1 1 5F1B6062
P 1250 6800
AR Path="/5F1B6062" Ref="C?"  Part="1" 
AR Path="/5F190638/5F1B6062" Ref="C?"  Part="1" 
F 0 "C?" H 1365 6846 50  0000 L CNN
F 1 "0.1uF" H 1365 6755 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.05x0.95mm_HandSolder" H 1288 6650 50  0001 C CNN
F 3 "~" H 1250 6800 50  0001 C CNN
	1    1250 6800
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R?
U 1 1 5F1B6068
P 3950 5050
AR Path="/5F1B6068" Ref="R?"  Part="1" 
AR Path="/5F190638/5F1B6068" Ref="R?"  Part="1" 
F 0 "R?" V 3745 5050 50  0000 C CNN
F 1 "0" V 3836 5050 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad1.05x0.95mm_HandSolder" V 3990 5040 50  0001 C CNN
F 3 "~" H 3950 5050 50  0001 C CNN
	1    3950 5050
	0    1    1    0   
$EndComp
$Comp
L Device:R_US R?
U 1 1 5F1B606E
P 3950 4900
AR Path="/5F1B606E" Ref="R?"  Part="1" 
AR Path="/5F190638/5F1B606E" Ref="R?"  Part="1" 
F 0 "R?" V 3745 4900 50  0000 C CNN
F 1 "0" V 3836 4900 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad1.05x0.95mm_HandSolder" V 3990 4890 50  0001 C CNN
F 3 "~" H 3950 4900 50  0001 C CNN
	1    3950 4900
	0    1    1    0   
$EndComp
$Comp
L Device:R_US R?
U 1 1 5F1B6074
P 3950 4750
AR Path="/5F1B6074" Ref="R?"  Part="1" 
AR Path="/5F190638/5F1B6074" Ref="R?"  Part="1" 
F 0 "R?" V 3745 4750 50  0000 C CNN
F 1 "0" V 3836 4750 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad1.05x0.95mm_HandSolder" V 3990 4740 50  0001 C CNN
F 3 "~" H 3950 4750 50  0001 C CNN
	1    3950 4750
	0    1    1    0   
$EndComp
$Comp
L Device:R_US R?
U 1 1 5F1B607A
P 3950 4350
AR Path="/5F1B607A" Ref="R?"  Part="1" 
AR Path="/5F190638/5F1B607A" Ref="R?"  Part="1" 
F 0 "R?" V 3745 4350 50  0000 C CNN
F 1 "0" V 3836 4350 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad1.05x0.95mm_HandSolder" V 3990 4340 50  0001 C CNN
F 3 "~" H 3950 4350 50  0001 C CNN
	1    3950 4350
	0    1    1    0   
$EndComp
Wire Wire Line
	4250 3900 3800 3900
Wire Wire Line
	4250 4050 3800 4050
Wire Wire Line
	4250 4200 3800 4200
Wire Wire Line
	4250 4350 4100 4350
Wire Wire Line
	4250 4750 4100 4750
Wire Wire Line
	4250 5050 4100 5050
Wire Wire Line
	3800 5050 3450 5050
Wire Wire Line
	4100 4900 4250 4900
Wire Wire Line
	3800 4900 3450 4900
Wire Wire Line
	3800 4750 3450 4750
Wire Wire Line
	3800 4350 3450 4350
Text Label 3800 3900 0    50   ~ 0
SCLK
Text Label 3800 4050 0    50   ~ 0
SDATA
Text Label 3800 4200 0    50   ~ 0
FSYNC
Text Label 3450 4350 0    50   ~ 0
RESET
Text Label 3450 4750 0    50   ~ 0
SLEEP
Text Label 3450 4900 0    50   ~ 0
PSEL
Text Label 3450 5050 0    50   ~ 0
FSEL
$Comp
L Connector:Screw_Terminal_01x02 J?
U 1 1 5F1B6092
P 2900 1300
AR Path="/5F1B6092" Ref="J?"  Part="1" 
AR Path="/5F190638/5F1B6092" Ref="J?"  Part="1" 
F 0 "J?" H 2980 1292 50  0000 L CNN
F 1 "Screw_Terminal_01x02" H 2980 1201 50  0000 L CNN
F 2 "TerminalBlock:TerminalBlock_Altech_AK300-2_P5.00mm" H 2900 1300 50  0001 C CNN
F 3 "~" H 2900 1300 50  0001 C CNN
	1    2900 1300
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J?
U 1 1 5F1B6098
P 2850 2250
AR Path="/5F1B6098" Ref="J?"  Part="1" 
AR Path="/5F190638/5F1B6098" Ref="J?"  Part="1" 
F 0 "J?" H 2930 2242 50  0000 L CNN
F 1 "Screw_Terminal_01x02" H 2930 2151 50  0000 L CNN
F 2 "TerminalBlock:TerminalBlock_Altech_AK300-2_P5.00mm" H 2850 2250 50  0001 C CNN
F 3 "~" H 2850 2250 50  0001 C CNN
	1    2850 2250
	1    0    0    -1  
$EndComp
$Comp
L power:VDD #PWR?
U 1 1 5F1B609E
P 1450 1200
AR Path="/5F1B609E" Ref="#PWR?"  Part="1" 
AR Path="/5F190638/5F1B609E" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 1450 1050 50  0001 C CNN
F 1 "VDD" H 1465 1373 50  0000 C CNN
F 2 "" H 1450 1200 50  0001 C CNN
F 3 "" H 1450 1200 50  0001 C CNN
	1    1450 1200
	1    0    0    -1  
$EndComp
$Comp
L power:VDDA #PWR?
U 1 1 5F1B60A4
P 1400 2150
AR Path="/5F1B60A4" Ref="#PWR?"  Part="1" 
AR Path="/5F190638/5F1B60A4" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 1400 2000 50  0001 C CNN
F 1 "VDDA" H 1415 2323 50  0000 C CNN
F 2 "" H 1400 2150 50  0001 C CNN
F 3 "" H 1400 2150 50  0001 C CNN
	1    1400 2150
	1    0    0    -1  
$EndComp
$Comp
L Device:C C?
U 1 1 5F1B60AA
P 1750 1400
AR Path="/5F1B60AA" Ref="C?"  Part="1" 
AR Path="/5F190638/5F1B60AA" Ref="C?"  Part="1" 
F 0 "C?" H 1865 1446 50  0000 L CNN
F 1 "0.1uF" H 1865 1355 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.05x0.95mm_HandSolder" H 1788 1250 50  0001 C CNN
F 3 "~" H 1750 1400 50  0001 C CNN
	1    1750 1400
	1    0    0    -1  
$EndComp
$Comp
L Device:C C?
U 1 1 5F1B60B0
P 1700 2350
AR Path="/5F1B60B0" Ref="C?"  Part="1" 
AR Path="/5F190638/5F1B60B0" Ref="C?"  Part="1" 
F 0 "C?" H 1815 2396 50  0000 L CNN
F 1 "0.1uF" H 1815 2305 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.05x0.95mm_HandSolder" H 1738 2200 50  0001 C CNN
F 3 "~" H 1700 2350 50  0001 C CNN
	1    1700 2350
	1    0    0    -1  
$EndComp
$Comp
L Device:CP C?
U 1 1 5F1B60B6
P 2150 1400
AR Path="/5F1B60B6" Ref="C?"  Part="1" 
AR Path="/5F190638/5F1B60B6" Ref="C?"  Part="1" 
F 0 "C?" H 2268 1446 50  0000 L CNN
F 1 "10uF" H 2268 1355 50  0000 L CNN
F 2 "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A_Pad1.58x1.35mm_HandSolder" H 2188 1250 50  0001 C CNN
F 3 "~" H 2150 1400 50  0001 C CNN
	1    2150 1400
	1    0    0    -1  
$EndComp
$Comp
L Device:CP C?
U 1 1 5F1B60BC
P 2100 2350
AR Path="/5F1B60BC" Ref="C?"  Part="1" 
AR Path="/5F190638/5F1B60BC" Ref="C?"  Part="1" 
F 0 "C?" H 2218 2396 50  0000 L CNN
F 1 "10uF" H 2218 2305 50  0000 L CNN
F 2 "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A_Pad1.58x1.35mm_HandSolder" H 2138 2200 50  0001 C CNN
F 3 "~" H 2100 2350 50  0001 C CNN
	1    2100 2350
	1    0    0    -1  
$EndComp
$Comp
L power:GNDD #PWR?
U 1 1 5F1B60C2
P 1450 1600
AR Path="/5F1B60C2" Ref="#PWR?"  Part="1" 
AR Path="/5F190638/5F1B60C2" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 1450 1350 50  0001 C CNN
F 1 "GNDD" H 1454 1445 50  0000 C CNN
F 2 "" H 1450 1600 50  0001 C CNN
F 3 "" H 1450 1600 50  0001 C CNN
	1    1450 1600
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5F1B60C8
P 1400 2700
AR Path="/5F1B60C8" Ref="#PWR?"  Part="1" 
AR Path="/5F190638/5F1B60C8" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 1400 2450 50  0001 C CNN
F 1 "GND" H 1405 2527 50  0000 C CNN
F 2 "" H 1400 2700 50  0001 C CNN
F 3 "" H 1400 2700 50  0001 C CNN
	1    1400 2700
	1    0    0    -1  
$EndComp
Wire Wire Line
	1400 2150 1400 2200
Wire Wire Line
	1400 2200 1700 2200
Wire Wire Line
	2500 2200 2500 2250
Wire Wire Line
	2500 2250 2650 2250
Connection ~ 1700 2200
Wire Wire Line
	1700 2200 2100 2200
Connection ~ 2100 2200
Wire Wire Line
	2100 2200 2500 2200
Wire Wire Line
	1400 2700 1400 2500
Wire Wire Line
	1400 2500 1700 2500
Wire Wire Line
	1700 2500 2100 2500
Connection ~ 1700 2500
Wire Wire Line
	2100 2500 2650 2500
Wire Wire Line
	2650 2500 2650 2350
Connection ~ 2100 2500
Wire Wire Line
	1450 1600 1450 1550
Wire Wire Line
	1450 1550 1750 1550
Wire Wire Line
	2700 1550 2700 1400
Connection ~ 1750 1550
Wire Wire Line
	1750 1550 2150 1550
Connection ~ 2150 1550
Wire Wire Line
	2150 1550 2700 1550
Wire Wire Line
	1450 1200 1450 1250
Wire Wire Line
	1450 1250 1750 1250
Wire Wire Line
	2700 1250 2700 1300
Connection ~ 1750 1250
Wire Wire Line
	1750 1250 2150 1250
Connection ~ 2150 1250
Wire Wire Line
	2150 1250 2700 1250
$Comp
L power:GNDD #PWR?
U 1 1 5F1B60EB
P 4150 2300
AR Path="/5F1B60EB" Ref="#PWR?"  Part="1" 
AR Path="/5F190638/5F1B60EB" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 4150 2050 50  0001 C CNN
F 1 "GNDD" H 4154 2145 50  0000 C CNN
F 2 "" H 4150 2300 50  0001 C CNN
F 3 "" H 4150 2300 50  0001 C CNN
	1    4150 2300
	1    0    0    -1  
$EndComp
$Comp
L power:GNDD #PWR?
U 1 1 5F1B60F1
P 3900 3150
AR Path="/5F1B60F1" Ref="#PWR?"  Part="1" 
AR Path="/5F190638/5F1B60F1" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 3900 2900 50  0001 C CNN
F 1 "GNDD" H 3904 2995 50  0000 C CNN
F 2 "" H 3900 3150 50  0001 C CNN
F 3 "" H 3900 3150 50  0001 C CNN
	1    3900 3150
	1    0    0    -1  
$EndComp
Connection ~ 3900 3150
$Comp
L power:GND #PWR?
U 1 1 5F1B60F8
P 5150 5950
AR Path="/5F1B60F8" Ref="#PWR?"  Part="1" 
AR Path="/5F190638/5F1B60F8" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 5150 5700 50  0001 C CNN
F 1 "GND" H 5155 5777 50  0000 C CNN
F 2 "" H 5150 5950 50  0001 C CNN
F 3 "" H 5150 5950 50  0001 C CNN
	1    5150 5950
	1    0    0    -1  
$EndComp
Text Notes 8050 7000 0    197  ~ 39
RF Generator
$EndSCHEMATC
