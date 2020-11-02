EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Antenna Deployment"
Date "2020-10-11"
Rev "v01"
Comp ""
Comment1 "UC Berkeley QubeSat"
Comment2 ""
Comment3 ""
Comment4 "Author: Jamie Walton"
$EndDescr
$Comp
L openlst-hw:Mounting_Hole_PAD MK1
U 1 1 5F88809F
P 4850 3850
F 0 "MK1" H 4950 3899 50  0000 L CNN
F 1 "Mounting_Hole_PAD" H 4950 3808 50  0000 L CNN
F 2 "MountingHole:MountingHole_3.2mm_M3_Pad" H 4850 3850 50  0001 C CNN
F 3 "" H 4850 3850 50  0001 C CNN
	1    4850 3850
	1    0    0    -1  
$EndComp
$Comp
L openlst-hw:Mounting_Hole_PAD MK2
U 1 1 5F888D11
P 6050 3850
F 0 "MK2" H 6150 3899 50  0000 L CNN
F 1 "Mounting_Hole_PAD" H 6150 3808 50  0000 L CNN
F 2 "MountingHole:MountingHole_3.2mm_M3_Pad" H 6050 3850 50  0001 C CNN
F 3 "" H 6050 3850 50  0001 C CNN
	1    6050 3850
	1    0    0    -1  
$EndComp
Wire Wire Line
	4850 3950 4850 4050
Wire Wire Line
	4850 4050 5550 4050
Wire Wire Line
	5550 4050 5550 4400
Wire Wire Line
	6050 3950 6050 4050
Wire Wire Line
	6050 4050 5650 4050
Wire Wire Line
	5650 4050 5650 4400
$Comp
L Connector_Generic:Conn_01x03 J1
U 1 1 5F88B3BB
P 5650 4600
F 0 "J1" V 5522 4780 50  0000 L CNN
F 1 "Conn_01x03" V 5613 4780 50  0000 L CNN
F 2 "Connector_Coaxial:SMA_Molex_73251-1153_EdgeMount_Horizontal" H 5650 4600 50  0001 C CNN
F 3 "~" H 5650 4600 50  0001 C CNN
	1    5650 4600
	0    1    1    0   
$EndComp
$EndSCHEMATC
