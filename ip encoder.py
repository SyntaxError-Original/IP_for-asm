import time
import os
import sys
import platform
import signal

def close_terminal():
    parent_pid = os.getppid()                           # Get the Process ID of this file
    if platform.system() == "Windows":
        os.system(f"taskkill /F /PID {parent_pid} /T")  # windows version to kill the proces
    else:
        os.kill(parent_pid, signal.SIGTERM)             # Linux version to kill the process
        
def Main():
    print ("\n\n  Will except any IP address and convert it to HEX")
    print("  then swap the octets from last to first")
    print("  Also it excepts a 4 digit (above 4096)\n  port No. and converts it to HEX")
    print ("  Then swaps the 2 bytes around")
    ip_address = input("\n Enter the Ip Address  : ")
    try:
        portd = int(input(" Enter the port number : "))
    except Exception as e:
        portd =0
        
    octets = ip_address.split(".")        #Split into 4 separate string decimal segments
    hex_list = []
    not_hex_list = []
    
    for octet in octets:
        num = int(octet)
        hex_str = f"{num:02x}"            #Format integer directly into a 2-digit hex string
        hex_list.append(hex_str)
        not_num = ~num & 0xFF             #Apply bitwise NOT and mask to 8 bits to stop neg nums
        not_hex_str = f"{not_num:02x}"    #Format the inverted number into a 2-digit hex string
        not_hex_list.append(not_hex_str)

    print("\n Original Hex:", " ".join(hex_list))
    print(" Preform a  NOT Hex:", " ".join(not_hex_list))
    xa=not_hex_list[0];xb=not_hex_list[1];xc=not_hex_list[2];xd=not_hex_list[3]
    result = ''.join((xd,xc,xb,xa))
    print (" Inverted octets and NOT Hex :",result)
    if portd >= 4096 :
        porth = hex(portd)[2:];porthf=porth[:2];porthl=porth[2:]
        print (f"\n Port No. :{portd}, port No. in HEX: {porth}\n in hex with the first")
        print (" and last bytes swapped          ", ''.join((porthl,porthf)),"\n")
    else:
        print ("\n Either the port No. was blank or it was below 4096 \n")
Main()
while True:
    time.sleep(.5)
    rstart=input(" Would you Like to continue Y/N  :")
    if rstart != "Y":
        if rstart != "y":
            print("\n\n Thanks for playing \n\n   5ynt@x3rr0r")
            time.sleep(3)
            os.system("cls")
            close_terminal()
        else:
            time.sleep(1)
            os.system("cls")
            Main()
    