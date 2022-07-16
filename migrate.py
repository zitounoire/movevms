import subprocess  
  
def movevms(vms,path):
    
    cmd = 'VBoxManage' 
     
    outputlist = []

    for vm in vms :
        temp = subprocess.Popen([cmd, 'movevm', vm, '--folder', path], stdout = subprocess.PIPE) 
        # get the output as a string
        output = str(temp.communicate()) 
    # store the output in the list
        outputlist.append(output)
    return outputlist
  
if __name__ == '__main__': 
    
    # Get the list of vms from the text file
    vms = list(open('vms.txt'))
    path = "/path/to/new-vm-location/"

    # Iterate over all the vms that we read from the text file
    # and remove all the extra lines. This is just a preprocessing step
    # to make sure there aren't any unnecessary lines.
    
    for i in range(len(vms)):
        vms[i] = vms[i].strip('\n')
    outputlist = movevms(vms,path) 
    
    print(outputlist)


