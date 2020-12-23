from time import sleep
from datetime import date, datetime

"""Scares Andre into thinking computer will blow up"""

print("#"*30)
print("SYSTEM ERROR: MAC OS BIG SUR")
print("#"*30)
sleep(15)
print("Error Replication loading...")
sleep(5)
for i in range(1,13):
    print("Sys Review #{}: ".format(i)+str(date.today())+str(datetime.now()))
    sleep(0.5)

print("-"*30)
print("Administrative permissions blocked.\nSystem default initializing.")
print("-"*30)
sleep(3)
ans = input("Was this action intended? (y/n): ")
print("#"*30)
sleep(0.8)
print(datetime.now())
print("Authentication Halted.\nPlease refer to https://support.apple.com/mac/repair/service for support.")
sleep(10)
print("#"*30)
print("ERROR: SYSTEM HARDDRIVE CORRUPTED.")
print("#"*30)
sleep(8)
print("\nDEVICE SELF DESTRUCT:\n")
sleep(1)
for i in range(5,0,-1):
    print("AUTO DESTRCUT in "+str(i)+" seconds.".rjust(10,"."))
    if i == 1:
        print("\nPLEASE STAND BACK\n".rjust(25,"."))
    sleep(1)
sleep(5)
print("I ain neva seen 2 pretty besfrens...")