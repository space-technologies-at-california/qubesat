# README  qdSpectro v1.0.1 
Copyright 2018 Diana Prado Lopes Aude Craik (MIT License)

This software package is intended to be used alongside the protocol described in the paper entitled "Quantum diamond spectrometer for nanoscale NMR and ESR spectroscopy" (currently under review for publication in Nature Protocols, 2019). The paper presents a protocol for building a spectrometer based on nitrogen vacancy (NV) centers in diamond and describes the installation and running procedure for this software package and associated hardware. This readme file gives a summary of the system requirements and installation/running guidelines for qdSpectro, but the user should also read the full protocol instructions on the paper (henceforth referred to as the protocol paper).

This file is structured as follows:
1. System Requirements
    * A list of the required non-standard peripheral hardware that directly communicates with qdSpectro (additional equipment - not listed here - is needed to complete assembly of the NV-diamond spectrometer, as described in the protocol paper)
    * A list of qdSpectro's software dependencies, which must also be installed.
2. Installation guide
3. Instructions for use
    * Running experiments with qdSpectro
    * Using togglePBchan.py
4. Current version patches and updates

## 1. System requirements:

### Non-standard hardware
*  National Instruments data acquisition card (DAQ), with a sampling rate of at least 250 kSa/s (e.g., National Instruments NI USB-6229 or NI USB-6211). qdSpectro has been tested with NI USB-6229 and NI USB-6211. The code is designed to work with National Instruments DAQs and will require modification by the user if other data acquisition systems are used.
* 500MHz PulseBlaster card (Spincore PulseBlasterESR PRO 500 MHz). qdSpectro has only been tested with the Spincore PulseBlasterESR PRO 500MHz card, but should be compatible with other SpinCore PulseBlaster cards. Other signal generators can be used but will require modification of the qdSpectro code by the user.
* SRS SG384 signal generator. qdSpectro has been designed to work with an SRS SG384 signal generator and has only been tested with this and the SG 386 models. It should be compatible with other SRS SG3800 or SG3900 models, but has not been tested with these. Other pulse generators can be used, but will require modification of the qdSpectro code by the user.
* National Instruments USB/GPIB converter (qdSpectro was tested with National Instruments GPIB-USB-HS). This is to be used to connect the SRS signal generator to your PC.
		
### Software dependencies
Operating system:
* The instructions for software installation described here and in the protocol paper are for a Windows PC (qdSpectro has been tested on Windows 10). Whilst the package should be portable to Linux or Mac operating systems, it has not been tested in these platforms and may require some user modification.
		
Packages:
* Python 3 version 3.6.3 or later (tested with version 3.6.3) and of a bitness which matches the computer’s bitness (i.e., install 64-bit Python if running it on a 64-bit computer). https://www.python.org/
* Notepad++ or any other text editor of your choice for viewing and editing Python scripts. https://notepad-plus-plus.org/
		
Drivers:
* National Instruments NI-DAQmx driver (tested with version 17.1.1 with NI DAQ card NI USB-6229) - the user should download an NI-DAQmx driver which is compatible with their chosen DAQ card. https://www.ni.com/dataacquisition/nidaqmx.htm
* SpinAPI: SpinCore API and Driver Suite for the PulseBlaster card (tested with version 20171214). http://www.spincore.com/support/spinapi/SpinAPI_Main.shtml
* National Instrument drivers for the USB/GPIB converter (listed under hardware requirements above) used for GPIB communication between the PC and the SRS signal generator. qdSpectro has been tested with the National Instruments GPIB-USB-HS converter, which requires the NI-VISA and NI-488.2 drivers to be installed (qdSpectro has been tested with version 16.0 of both, although later versions are also expected to work).
		
Libraries for peripheral instrument control:
* SpinAPI Python3 wrapper – SpinCore’s Python wrapper for C functions in SpinAPI, which can be used to communicate with and control the PulseBlaster Card. qdSpectro has been tested with the version of spinapi.py made available by Spincore on the link below (as of Feb 8th, 2018). 
http://www.spincore.com/support/SpinAPI_Python_Wrapper/Python_Wrapper_Main.shtml
If the aforementioned link is no longer active, the required version of spinapi.py can still be retrieved here:	https://web.archive.org/web/20190208140542/http://www.spincore.com/support/SpinAPI_Python_Wrapper/spinapi.py
* NI-VISA library (tested with version 16.0) – this library should be installed with the drivers for the  NI GPIB/USB converter but, if not, it can be downloaded from the National Instruments website: http://www.ni.com/download/ni-visa-16.0/6184/en/ (link for version 16.0). This library must be installed to enable qdSpectro to communicate with the SRS signal generator via GPIB. ***Important: The bitness of this library must match the Python bitness.***
* PyVISA version 1.8 or later (tested with version 1.8) - a python wrapper for the NI-VISA library, which allows the library to be called from Python scripts https://pypi.python.org/pypi/PyVISA
		
Python libraries for data manipulation and graphical display:
* Matplotlib (tested with version 2.1.2)– a python library for plotting https://matplotlib.org/index.html
* NumPy (tested with version 1.14.0) – a python library for scientific computing http://www.numpy.org/
		
## 2. Installation guide
Note: Time to complete the full installation procedure is typically 1-3 hours, mostly due to peripheral driver dependencies and required hardware setup.
*	Download and install Python 3 version 3.6.3 or later from https://www.python.org/. The Python bitness must match both the NI-VISA library’s bitness and the computer’s bitness. The protocol paper which qdSpectro accompanies describes how to run Python scripts from a Windows Command Prompt and how to edit the scripts using Notepad++, a text editor. The user may opt to run and edit the scripts from an Integrated Development Environment (IDE) instead, or to use a different editor. 
To check that the Python installation was successful, run Python by typing python into a Windows Command Prompt and pressing Enter. This should return the Python version number and bitness. To exit Python, type exit() (or hold down the Ctrl key and press the Z key) followed by Enter.
*	Download and install Notepad++ from https://notepad-plus-plus.org/.
*	Choose a folder in which to install qdSpectro. This folder is henceforth referred to as the working directory. Download qdSpectro from https://gitlab.com/dplaudecraik/qdSpectro and save it in the working directory. Users are encouraged to download the latest version and check the readme file of the package for any version-specific changes to installation instructions.
*	Download the SpinAPI Python3 wrapper from http://www.spincore.com/support/SpinAPI_Python_Wrapper/Python_Wrapper_Main.shtml 
(if this link is no longer active, the required version of spinapi.py can still be retrieved here: https://web.archive.org/web/20190208140542/http://www.spincore.com/support/SpinAPI_Python_Wrapper/spinapi.py )
***Important: Save the file as spinapi.py in the working directory.***
* 	Download and install the required drivers for the NI USB/GPIB converter (for the NI GPIB-USB-HS converter used to test qdSpectro, the drivers are NI-VISA and NI-488.2). If these drivers do not include the NI-VISA library, download and install the library from the National Instruments website:e.g. http://www.ni.com/download/ni-visa-16.0/6184/en/ (for version 16.0). 
***Important: Ensure that the bitness of the NI-VISA library matches the Python bitness (i.e., install 64-bit NI-VISA if running it on a 64-bit computer).***
*	From a Windows Command Prompt, install pyVISA by running ```python -m pip install -U pyvisa```
*	Check that the library was successfully installed by starting Python (by typing python into the command prompt and pressing Enter) and then running
```import visa```.
If no errors appear, the installation was successful.
*	From a Windows Command Prompt, install matplotlib by running
```python -m pip install -U matplotlib```.
Check that the library was successfully installed by starting Python and then running 
```import matplotlib```.
If no errors appear, the installation was successful.
*	From a Windows Command Prompt, install numpy by running
```python -m pip install -U numpy```.
Check that the library was successfully installed by starting Python and then running 
```import numpy```.
If no errors appear, the installation was successful.
*	Follow the instructions in the “Installation” section of the PulseBlaster manual (e.g., page 9 of the PulseBlasterESR-PRO manual version from September 4th, 2017). This includes downloading the SpinAPI package, inserting the PulseBlaster card into an available Peripheral Component Interconnect (PCI) slot in the computer and testing the PulseBlaster using one of the test programs SpinCore provides.
*	Follow the installation instructions for the National Instruments DAQ (e.g., Chapter 1 of the NI USB-621x manual version from April 2009). This includes downloading the NI-DAQmx driver and connecting the DAQ card to the computer via USB.
* 	Connect the GPIB port of the SRS signal generator to a USB port on the PC using the GPIB/USB converter. Enable the GPIB interface on the SRS signal generator and select its GPIB address by following the GPIB setup instructions in the SRS manual (e.g.,for models in the SG 380 series, see page 46 of the SG380 series manual Revision 2.04). Open qdSpectro's connectionConfig.py and, under the “SRS connections” section of this script, edit the variables GPIBaddr and modelName to be the GPIB address and model name of your SRS signal generator (e.g.,GPIBaddr=27, modelName=‘SG384’).   
*   Follow the instructions in the protocol paper to complete the hardware setup, including making the necessary connections from the DAQ, PulseBlaster and SRS signal generator to your diamond spectrometer apparatus and editing connectionConfig.py (as instructed in paper) to configure qdSpectro accordingly.
	
## 3. Instructions for use:

### Running experiments with qdSpectro:
Once the qdSpectro package is downloaded, the working directory should contain the files listed below.
User-input configuration files:
* connectionConfig.py – configuration file for PulseBlaster, DAQ and SRS connections to the PC. This file is edited by the user, as directed in the protocol, before any of the package scripts are run.
* __config.py – experiment configuration files. Each experiment has its own configuration file (e.g., the configuration file for the ESR experiment is ESRconfig.py), which consists mainly of a “user input” section, where the user can edit experimental parameters and configure options relating to how the data will be processed, plotted and saved.   

Main control and auxiliary libraries: 
* mainControl.py – all experiments described in this protocol are run from the mainControl.py script, which takes an experiment-specific configuration file as an argument. Given the input parameters defined in the configuration file, mainControl.py runs the experiment, generates plots and saves the results. 
* DAQcontrol.py – contains functions that configure the DAQ
* SRScontrol.py – contains functions that control the SRS signal generator
* PBcontrol.py – contains functions that configure and program the PulseBlaster card
* sequenceControl.py – contains functions that create the pulse sequences required to run the experiments in this protocol

Before running any experiments with qdSpectro, the user should read the readme file provided with the version of package they have downloaded, where any upgrades and patches will be described, and edit connectionConfig.py, as directed in the protocol paper.
	
To run an experiment with qdSpectro:
1. Open the relevant ___config.py file in notepad++. Read the description of the experimental parameters and data-processing options defined in this script.
2.	Edit the experimental parameters and configure the data-processing options in the “User Inputs” section of this script, as required. 
3. To run the experiment, open a windows command prompt and, from the working directory, run:
```python mainControl.py __config```
4.	To quit an experiment before it finishes running, press Ctrl+C.

A note on units: units for user-input parameters (entered in step ii above) are specified in the comments accompanying the user-input section of the ___config.py files. For added clarity, we also note here that the default unit for time variables in version 1.0 of the qdSpectro package (the current version at the time of writing) is nanoseconds. The user may either enter time variables in nanoseconds or use one of the following unit multipliers: ns = 1, us = 1e3, ms = 1e6. For example, if setting the variable endTau to 10 microseconds, the user may either enter endTau = 10000 or endTau = 10*us in the user-input section of the relevant ___config.py file. The latter format is used throughout the instructions given in this paper. For completeness, we also note that, in version 1.0 of qdSpectro, microwave frequencies are entered in hertz (e.g. if setting the variable startFreq to 2.7GHz, the user should enter startFreq=2.7e9) and microwave powers in dBm (e.g. if setting the variable microwavePower to 0 dBm, the user should enter microwavePower=0). Users running a different version of qdSpectro should refer to that version's readme file for any version-specific user-input instructions.
	
### Using togglePBchan.py:
At several points throughout the setup of the apparatus for the NV diamond spectrometer described in the protocol paper, PulseBlaster (PB) channels have to be toggled on and off. Use the script togglePBchan.py in the qdSpectro package to toggle any PulseBlaster channel. In a Windows Command Prompt, start Python from the working directory and run togglePBchan.py. A key will be displayed relating a letter to a PulseBlaster channel, as below:
* A = PB channel connected to the switch on the RF source driving the AOM
* M = PB channel connected to the switch on the MW output of the SRS signal generator
* I = PB channel connected to the switch on the I input of the SRS signal generator
* Q = PB channel connected to the switch on the Q input of the SRS signal generator
* D = PB channel connected to the DAQ’s sample clock input
* S = PB channel connected to the DAQ’s start trigger input
To turn on a given PB channel, type in the letter corresponding to it and press Enter. To turn the channel off, type in the same key again. Check the functionality by measuring the PB output voltage on an oscilloscope.

## 4. Current version patches and updates
v1.0.1: Minor documentation fixes in user-input section of T1config.py.