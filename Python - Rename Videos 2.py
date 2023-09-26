import os
import time
#####################################
def isVideo(file : str) -> bool :
    fileName = file.lower()
    return fileName.endswith(".mp4") or fileName.endswith(".mkv") or fileName.endswith(".avi")
#####################################
def getNewFileName(old : str) -> str :
	remove = ["[EgyBest].","BluRay","WEB-DL",".x264"]	
	for rm in remove :
		old = old.replace(f"{rm}","")					
	remove = ""
	old = old.replace(f"{remove}","")
	old = old.replace("."," ")
	old = old.replace("  "," ")
	old = old.replace(" mp4",".mp4")
	old = old.replace(" mkv",".mkv")
	old = old.replace(" avi",".avi")
	return old
#####################################
def main(*,path : str) -> None :
    mainPath = "/storage/emulated/0/"
    path = mainPath + path
    os.chdir(path)
    for file in os.listdir(path) :
        if isVideo(file) :
            newFileName = getNewFileName(file)
            #os.rename(file,newFileName)
            print(newFileName)
    return 0
#####################################
### MAIN FUNCTION ###
myPath = "Series/"
beginTime = time.time()
main(path = myPath)
endTime = time.time()

finalTime = endTime - beginTime
print("\n----------------------")
print(f"Finished in {finalTime} Seconds")												
print("----------------------")

