from pycubed import cubesat
import os, storage, time
import adafruit_sdcard

# check if SD card found
if not cubesat.hardware['SDcard']:
    print('No SD Card Detected. Press Ctrl+C to halt')
    while True:
        time.sleep(1)

# This helper function will print the contents of the SD
def print_directory(path, tabs=0):
    for file in os.listdir(path):
        stats = os.stat(path + "/" + file)
        filesize = stats[6]
        isdir = stats[0] & 0x4000

        if filesize < 1000:
            sizestr = str(filesize) + " by"
        elif filesize < 1000000:
            sizestr = "%0.1f KB" % (filesize / 1000)
        else:
            sizestr = "%0.1f MB" % (filesize / 1000000)

        prettyprintname = ""
        for _ in range(tabs):
            prettyprintname += "   "
        prettyprintname += file
        if isdir:
            prettyprintname += "/"
        print('{0:<40} Size: {1:>10}'.format(prettyprintname, sizestr))

        # recursively print directory contents
        if isdir:
            print_directory(path + "/" + file, tabs + 1)

def unique_file():
        try:
            name = 'DATA_000'
            files = []
            for i in range(0,50):
                _filename = name[:-2]+str(int(i/10))+str(int(i%10))+'.txt'
                if _filename not in os.listdir('/sd/'):
                    with open('/sd/'+_filename, 'a') as f:
                        time.sleep(0.01)
                    filename = '/sd/'+_filename
                    print('filename is:', filename)
                    return True
        except Exception as e:
            print('[ERROR] Unique File:', e)
            return False

def save(dataset=[1, 2, 3, 4, 5], savefile='/sd/DATA_000.txt'):
        open(savefile, 'w').close() # delete contents
        try:
            with open(savefile, 'a') as file:
                for item in dataset:
                    if isinstance(item,float):
                        file.write('{:.9E} '.format(item))
                    else:
                        file.write('{} '.format(item))
                file.write('\n')
            return True
        except Exception as e:
            print('[ERROR] SD Save:', e)
            return False

def read(readfile='/sd/DATA_000.txt'):
    try:
        with open(readfile, 'r') as file:
            print(file.read())
        return True
    except Exception as e:
        print('[ERROR] SD Read:', e)
        return False

def update_status(status=0):
    save(dataset=['is_deployed:', status])

update_status()
read("/sd/DATA_000.txt")
print("Files on filesystem:")
print("====================")
print_directory("/sd")
