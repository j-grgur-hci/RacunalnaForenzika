import sys
import optparse

LOGFILE = "setupapi.dev.log"
KEYWORDS = "[Device Install (Hardware initiated)"
KEYWORD2 = "USBSTOR"

with open(LOGFILE, "r") as in_file:
    for line in in_file:
        if KEYWORDS in line and KEYWORD2 in line:
            data1 = line.split("#")[1].split("&")
            data2 = line.split("#")[2]

            print("Vendor ID:", data1[1])
            print("Product ID:", data1[2])
            print("Revision:", data1[3])
            print("Serial mumber:", data2)
            print(next(in_file).split("start")[1].strip())

