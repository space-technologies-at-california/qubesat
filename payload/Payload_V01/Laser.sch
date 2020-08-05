EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 3 5
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L power:GND #PWR0127
U 1 1 5F18C650
P 4450 3550
F 0 "#PWR0127" H 4450 3300 50  0001 C CNN
F 1 "GND" H 4455 3377 50  0000 C CNN
F 2 "" H 4450 3550 50  0001 C CNN
F 3 "" H 4450 3550 50  0001 C CNN
	1    4450 3550
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0128
U 1 1 5F18CD3D
P 4900 3250
F 0 "#PWR0128" H 4900 3100 50  0001 C CNN
F 1 "+5V" H 4915 3423 50  0000 C CNN
F 2 "" H 4900 3250 50  0001 C CNN
F 3 "" H 4900 3250 50  0001 C CNN
	1    4900 3250
	1    0    0    -1  
$EndComp
Wire Wire Line
	4900 3250 5150 3250
Wire Wire Line
	5150 3250 5150 3400
Wire Wire Line
	5150 3400 5300 3400
Connection ~ 5150 3250
Wire Wire Line
	5150 3250 5300 3250
$Comp
L Device:R_POT_US RV1
U 1 1 5F18DE7D
P 5000 3850
F 0 "RV1" V 4795 3850 50  0000 C CNN
F 1 "10k" V 4886 3850 50  0000 C CNN
F 2 "Potentiometer_SMD:Potentiometer_Vishay_TS53YJ_Vertical" H 5000 3850 50  0001 C CNN
F 3 "~" H 5000 3850 50  0001 C CNN
	1    5000 3850
	0    1    1    0   
$EndComp
Wire Wire Line
	4450 3550 5300 3550
Wire Wire Line
	5150 3850 5300 3850
Wire Wire Line
	5300 3700 4850 3700
Wire Wire Line
	4850 3700 4850 3850
Wire Wire Line
	5300 4000 5000 4000
$Comp
L Payload_V01:DJ532-40 LD1
U 1 1 5F1DD2C7
P 6950 4000
F 0 "LD1" V 6854 4147 50  0000 L CNN
F 1 "DJ532-40" V 6945 4147 50  0000 L CNN
F 2 "OptoDevice:LaserDiode_TO18-D5.6-3" H 6950 4000 50  0001 C CNN
F 3 "" H 6950 4000 50  0001 C CNN
	1    6950 4000
	0    1    1    0   
$EndComp
$Comp
L Payload_V01:MLD203CLN U3
U 1 1 5F1DFA85
P 5850 3700
F 0 "U3" H 5850 4415 50  0000 C CNN
F 1 "MLD203CLN" H 5850 4324 50  0000 C CNN
F 2 "" H 5850 3700 50  0001 C CNN
F 3 "" H 5850 3700 50  0001 C CNN
	1    5850 3700
	1    0    0    -1  
$EndComp
Wire Wire Line
	6400 4150 6750 4150
Wire Wire Line
	6750 4150 6750 4200
Wire Wire Line
	6750 4200 6950 4200
Wire Wire Line
	6400 3700 6950 3700
$Comp
L Device:R_US R10
U 1 1 5F1E131A
P 6650 3850
F 0 "R10" V 6445 3850 50  0000 C CNN
F 1 "1k" V 6536 3850 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad1.05x0.95mm_HandSolder" V 6690 3840 50  0001 C CNN
F 3 "~" H 6650 3850 50  0001 C CNN
	1    6650 3850
	0    1    1    0   
$EndComp
Wire Wire Line
	6400 3850 6500 3850
Wire Wire Line
	6800 3850 6800 4000
Wire Wire Line
	6800 4000 6400 4000
Text Label 6450 4000 0    50   ~ 0
LD_CURR
$EndSCHEMATC
