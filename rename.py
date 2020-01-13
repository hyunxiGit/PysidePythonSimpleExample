import os

def changeName(oldName , newName)
    #example to change name
    #os.rename(r'\\alpha\Zeus\Character_Art\blendshape\assets\r_watkins\scans\rawScans\404623_Neutral_EyesOpen-2\SCAN.obj',r'\\alpha\Zeus\Character_Art\blendshape\assets\r_watkins\scans\rawScans\404623_Neutral_EyesOpen-2\404623_Neutral_EyesOpen-2.obj')    
    my_target_path = r'\\alpha\Zeus\Character_Art\blendshape\assets\r_watkins\scans\rawScans'
     = r'SCAN.obj'
    for root, dirs, files in os.walk(my_target_path, topdown=False):
       for name in files:
           if str(name)== my_target_name :
               
               oldName = os.path.join(root, name)
               r_oldName = r'{}'.format(oldName)
               
               newName = str(root).split('\\')[-1]+'.obj'
               newName = os.path.join(root, newName)
               r_newName = r'{}'.format(newName)

               print 'oldName :'+ r_oldName
               print 'newName :'+ r_newName
    
               os.rename(r_oldName,r_newName)
           #elif str(name).split('.')[-1] == 'obj' :
           #    if str( root).split('\\')[-1]!=str(name).split('.')[0]:
           #        print 'False'
    
