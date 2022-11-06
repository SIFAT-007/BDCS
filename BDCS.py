import os,sys
try:
    os.system("git pull")
    __import__('BDCS').bdcs()
except:
    pass
