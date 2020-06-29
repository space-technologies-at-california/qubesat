from collections import OrderedDict
import ESR_with_photodiode
import ESR_with_single_photon
import Rabi_with_single_photon
#import Rabi_with_photodiode
import T1_with_single_photon
import PBcontrol as PBctl
import argparse, os

def main():
    config = cmdInput()
    if config['sequence_name'] == 'ESRseq':
        if config['photon_or_photodiode'] == 'photodiode':
            ESR_with_photodiode.run(config)
        elif config['photon_or_photodiode'] == 'photon':
            ESR_with_single_photon.run(config)
    if config['sequence_name'] == 'RabiSeq':
        if config['photon_or_photodiode'] == 'photodiode':
            #Rabi_with_photodiode.run(config)
            x=0
        elif config['photon_or_photodiode'] == 'photon':
            Rabi_with_single_photon.run(config)
    if config['sequence_name'] == 'T1seq':
        if config['photon_or_photodiode'] == 'photodiode':
            #T1_with_photodiode.run(config)
            x=0
        elif config['photon_or_photodiode'] == 'photon':
            T1_with_single_photon.run(config)


def read_config(filename):
    fid = open(filename, 'r')
    lines = fid.readlines()
    fid.close()

    ret_val = OrderedDict()
    for line in lines:
        line = line.replace('\r', '').replace('\n', '')
        split_str = line.split(' = ')

        key = split_str[0]
        value_str = split_str[1].replace(' ', '')

        if value_str.find(',') > -1:
            # array detected
            split_str = value_str.split(',')
            value = []
            for s in split_str:
                try:
                    value.append(float(s))
                except:
                    value.append(s)
        else:
            try:
                value = float(value_str)
            except:
                value = value_str
                if value == "No":
                    value = False

        ret_val[key] = value
    return ret_val

def createCommandLineParser():
    ''' Creates parser for config file. '''
    parser = argparse.ArgumentParser() 
    parser.add_argument('--config', required=False, default='config.txt')
    return parser

def cmdInput():
    ''' Reads command line to configure variables. '''
    parser = createCommandLineParser()
    # try:
    #     args = parser.parse_args()
    #     config = read_config(args.config)
    # except:
    #     print('Fail, check config file')
    #     os.sys.exit(1)
    args = parser.parse_args()
    config = read_config(args.config) 
    return config

if __name__ == "__main__":
    main()