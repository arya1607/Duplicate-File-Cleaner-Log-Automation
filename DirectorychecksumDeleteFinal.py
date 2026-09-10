#The return is 32 byte (Each char is hexadecimal)

import sys
import os
import hashlib #to calculate checksum

def CalculateChecksum(FileName):
    
    fobj = open(FileName,"rb")# read
    
    hobj = hashlib.md5() #1
    Buffer = fobj.read(1024) # badli mag example -
    
    while(len(Buffer) > 0):
        hobj.update(Buffer) #2
        Buffer = fobj.read(1024)\
        
    fobj.close
    
    return hobj.hexdigest() #3

        
def FindDuplicate(DirectoryName):
    Ret = False
    
    #check the path exists
    Ret = os.path.exists(DirectoryName)
        
    if Ret == False:
        print("path is invalid")
        return

    #checking is it Directory
    Ret = os.path.isdir(DirectoryName)
    if Ret == False:
        print("It is not a directory")
        return
    
    #Dictionary creation
    Duplicate = {}
        
    #Directory present
    for FolderName, SubFolder ,FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName, fname)#path joined
            
            checksum = CalculateChecksum(fname)#will call for all the files in the folder
            
            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
                
            else:
                Duplicate[checksum] = [fname]
                
    return Duplicate
                
def DeleteDuplicate(DirectoryName):
    MyDict = FindDuplicate(DirectoryName)
    

    Result = list(filter(lambda x : len(x) > 1, MyDict.values())) ###IMPORTANT
    
    Count = 0
    TotalDeleted = 0
    
    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if (Count > 1):
                os.remove(subvalue)
                TotalDeleted = TotalDeleted + 1
            
        Count = 0
    print("Total deleted files : ",TotalDeleted)    
     
def main():
    DeleteDuplicate("Test")
    
if __name__ == "__main__":
    main()
    
#log file add
#scheduling add
#periodically log file
#time execution
