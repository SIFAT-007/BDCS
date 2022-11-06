import os,sys
try:
    os.system("git pull")
    __import__("BDMC").bdcs()
except:
    pass
