import csv
import getopt
import sys
import os, shutil

# "{name} 0.00 0 0.0 {xmin}.00 {ymin}.00 {xmax}.00 {ymax}.00 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0"
csv_file_path = ""
kitty_string = "{0} 0.00 0 0.0 {1}.00 {2}.00 {3}.00 {4}.00 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0"
kitty_path = ""


def main(argv):
    global csv_file_path
    global kitty_path
    try:
        opts, args = getopt.getopt(argv, "f:")
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    if opts is None:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-f':
            csv_file_path = arg
            kitty_path = csv_file_path[0:-4]
            createFolder(kitty_path)
            converToKitty(csv_file_path)


def converToKitty(file):
    with open(file, 'rt') as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            kittyFile(row)


def kittyFile(data):
    path = kitty_path + "/" + data['filename'][0:-4] + ".txt"
    print(path)
    if ' ' in data['class']:
        class_name = data['class'].replace(' ', '_')
    else:
        class_name = data['class']
    f = open(path, "w+")
    myData = kitty_string.format(class_name, data['xmin'], data['ymin'], data['xmax'], data['ymax'])
    f.write(myData)
    f.close()


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            print('Creating Folder')
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def usage():
    print("python csvtokitty.py -f Path_To_.csv File")


# call main function
if __name__ == "__main__":
    main(sys.argv[1:])
