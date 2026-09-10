import sys
import os
import time
import schedule

def DirectoryScanner(DirectoryPath = "Marvellous"):
    Border = "-"*40
    timestamp = time.ctime()
    
    LogFileName = "Marvellous%s.log"%(timestamp) #s for strinf
    LogFileName = LogFileName.replace(" ","_") #to replace space with _
    LogFileName = LogFileName.replace(":","_") 
    
    
    print("Log file gets created : ",LogFileName)
    

    fobj = open(LogFileName,"w") #file name is changed frequently
    fobj.write(Border+"\n")
    
    fobj.write("Marvellous Automation Script\n")
    fobj.write(Border+"\n\n")
    
    fobj.write("Files from the directory are : \n")
    fobj.write(Border+"\n\n")
    
    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
        for fname in FileName:
            fobj.write(fname+"\n")
            
    fobj.write(Border+"\n")
    fobj.write("Log file gets created at : "+timestamp)
    fobj.write("\n"+Border+"\n")
            
    fobj.close()

def main():
    Border = "-"*40
    print(Border)
    print("Marvellous Automation Script")
    print(Border)
    
    if (len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to travel the directory")
            print("For better usage please check --u flag")
            
            
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("please execute the script as")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")
            
            
        else:
            DirectoryScanner(sys.argv[1])
            schedule.every(1).minute.do(DirectoryScanner,sys.argv[1])
            while True:
                schedule.run_pending()
                time.sleep(1)
    else:
        print("Invalid no. of Arguments")
        print("please use '--h' or '--u' for more info")
        
    print(Border)
    print("Thankyou for using Automation Script")
    print(Border)
    
    
    
if __name__ == "__main__":
    main()