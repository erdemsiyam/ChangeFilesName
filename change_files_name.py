import os

def changeFilesName(path,oldName,newName,extension):
    """ explain: this is main function.
        params:
            path: str [the path of files]
            oldName: str [the common files' name to change]
            newName: str [the new name corresponding to the old name]
            extension: str [the common files' extension to change]
    """
   
    # take a look to the path and take all files name
    filesNames = bringFilesNameFromPath(path)
    
    # take names of files which we try to change their names.
    containOldNameFiles = findFilesThatWeInNeed(filesNames,oldName,extension)

    #change their names
    saveFilesName(path,containOldNameFiles,oldName,newName)


def bringFilesNameFromPath(path):
    """ explain: take a look to the path and take all files name
        params:
            path: str [the path of files]
    """
    try:
        files = []
        for _,_,x in os.walk(path):
            files.append(x)
        return files
    except Exception as error:
        print(error)
        return []


def findFilesThatWeInNeed(filesNames,oldName,extension):
    """ explain: take names of files which we try to change their names. 
        params:
            filesNames: list<str> [the all files names to research]
            oldName: str [the common files' name to change]
            extension: str [the common files' extension to change]
    """
    
    containOldNameFiles = []
    for i in filesNames[0]:
        if i.find(oldName)>-1 and i.endswith(extension):
            containOldNameFiles.append(i)
    return containOldNameFiles


def saveFilesName(path,containOldNameFiles,oldName,newName):
    """ explain : change names of the files
        vars:
            path: str [the path of files]
            containOldNameFiles: list<str> [the name of the files that have to change their name]
            oldName: str [the common files' name to change]
            newName: str [the new name corresponding to the old name]
    """
    try:
        for oldestName in containOldNameFiles:
            newestName = oldestName.replace(oldName,newName)
            os.rename(os.path.join(path,oldestName),os.path.join(path,newestName))
    except Exception as error:
        print(error)


# example
changeFilesName('C:\\Users\\Erdem\\Downloads\\PrisonBreakS01','Prison.Break.','','.srt')