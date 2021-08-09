
# Problem #4
# Write a function that provides a change directory (cd) function for an abstract file system.

#  Notes:

# Root path is '/'.
# Path separator is '/'.
# Parent directory is addressable as '..'.
# Directory names consist only of English alphabet letters (A-Z and a-z).
# The function should support both relative and absolute paths.
# The function will not be passed any invalid paths.
# Do not use built-in path-related functions.

# Solution4 -> 

For example:

path = Path('/a/b/c/d')

path.cd('../x')

print(path.current_path)


class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        i=0;
        new_pathList=new_path.split('/')
        pathLength=len(new_pathList)
        pathList=self.current_path.split('/')
        #print(new_PathList)
        if new_pathList[0]=='':
            #direct pathname
            del pathList[:]
            pathList.append('/'+new_pathList[1])
            i=i+2
        while(i<pathLength):
            j=len(pathList)-1
            if new_pathList[i]=='..':
                #parent directory
                pathList.pop(j)
            else:
                pathList.append(new_pathList[i])
            i=i+1
        self.current_path="/".join(pathList)

        pass
    
    
path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)