import os
import sys
import re

_ACTIVE_STAT = 0

def _listPlans() -> str: 
    if os.path.exists("C:\\Windows\\System32\\powercfg.exe"):
        return os.popen("C:\\Windows\\System32\\powercfg.exe /L").read()
        
    else:
        # print("No File")
        sys.exit(-1)

def getPlan() -> list:
    global _ACTIVE_STAT
    global guid_desc
    
    outPutText = _listPlans()
    text = outPutText.split('\n')[3:-1]
    guid_desc = []
    # print(text)
    
    for i in range(0,len(text)):
        line = text[i]
        guids = re.findall(r"GUID: ([\w\d-]{36})", line)
        descriptions = re.findall(r"\((.*?)\)", line)
        guid_desc.append((i,guids[0],descriptions[0]))
        if line[-1] == '*': _ACTIVE_STAT = i
    # print(guid_desc)
    
    return guid_desc

def _change_active_stat(stat:int):
    global _ACTIVE_STAT
    _ACTIVE_STAT = stat
    # print(_ACTIVE_STAT)

def changePlan(id:int) -> bool:
    global guid_desc
    if os.path.exists("C:\\Windows\\System32\\powercfg.exe"):
        os.popen(f"C:\\Windows\\System32\\powercfg.exe /S {guid_desc[id-1][1]}")
        _change_active_stat(id-1)
        return True
        
    else:
        # print("No File")
        return False
    

def getActiveStat() -> int:
    return _ACTIVE_STAT


if __name__ == "__main__":
    getPlan()