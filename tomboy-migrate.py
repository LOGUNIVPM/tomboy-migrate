#!/usr/bin/python3

# This script can migrate your old tomboy note hierarchy (tomboynotes/1/1234/asdasd.note) to tomboy-ng hierarchy (tomboynotes/asdasd.note)
# Since the old tomboy used a manifest xml file to track the notes to keep and their latest revision we can parse the old manifest
# and look for the latest, copy it to the new folder. Then tell tomboy-ng to use that (Settings->Set Path to Note Files)
# This script does not use any xml formatting since the manifest file is very simple
# Warning dirty script, use it at your own risk, backup the notes first, tested only on Linux Mint 21
# Author L. Gabrielli 2023

import sys
import os
import re
import shutil

if len(sys.argv) != 4:
    print("USAGE: {0} <manifest file> <source folder> <destination folder>".format(sys.argv[0]))
    exit(-1)

manifest_fname = sys.argv[1]
src_folder = sys.argv[2]
dest_folder = sys.argv[3]

f = open(manifest_fname, 'r')
lines = f.readlines()

for l in lines:
    if '<note' in l:
        id = re.findall(r'id="(.*?)"', l)
        rev = re.findall(r'rev="(.*?)"', l)
        r100 = int(int(str(rev[0])) / 100)
        fcheck = '{0}/{1}/{2}/{3}.note'.format(src_folder,r100,str(rev[0]),str(id[0]))
        print(os.stat(fcheck))
        shutil.copy2(fcheck, dest_folder)
