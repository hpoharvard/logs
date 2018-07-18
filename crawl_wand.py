"""
__author__ = "Giovanni Zambotti"
__copyright__ = ""
__credits__ = ["Giovanni Zambotti"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Giovanni Zambotti"
__email__ = "g.zambotti@gmail.com"
__status__ = "Production"


"""
import sys, os, time, collections
from wand.image import Image

#from PIL import Image
#Image.MAX_IMAGE_PIXELS = None

# create log file
def createLOG(info):    
    f.write(info)    
    
# create a new pdf
def makePDF(path, filein, fileout):    
    with Image(filename= path + '\\' +  filein) as img:
        print(img.size)
        with img.clone() as i:            
            i.save(filename= path + '\\' +  fileout + ".pdf")
      

# crawl folders
def crawlFolders(rootpath):    
    for dirpath, dirnames, filenames in os.walk(rootpath):        
        #print ("ORIGINAL LIST: " + str(filenames), str(len(filenames)))
        if len(filenames) > 1:            
            # filter only the files that finished 
            vlist = list(filter(lambda x: x.split('.')[1] == 'pdf' or x.split('.')[1] == 'tif' or x.split('.')[1] == 'TIF', filenames))
            vlist_noext = []            
            for item in vlist:    
                vlist_noext.append(item.split('.')[0])
            #print ("NEW LIST: " + str(vlist_new))
            c  = collections.Counter(vlist_noext)
            vlist_new = ([n for n in c if c[n]==1])

            vlist_final = []
            for item in vlist_new:
                for vitem in vlist:
                    if item == vitem.split('.')[0] and (vitem.split('.')[1] == 'tif' or vitem.split('.')[1] == 'TIF'):        
                        vlist_final.append(item)    
            vlist_final.sort()
            
            if len(vlist_final) == 0:
                print ("All set at: " + dirpath)
                createLOG("All set at: " + dirpath + "\n")
            else:
                #print ("Created pdfs @: " + dirpath + "\n")
                createLOG("Created pdfs @: " + dirpath + "\n")
                for item in vlist_final:
                    #print (dirpath, item)
                    print ("File: " + str(item) + ".tif\n")
                    createLOG("File: " + str(item) + ".pdf\n")
                    # create the PDFs
                    makePDF(dirpath, item + ".tif", item)
                    
        else:                       
            vlist = list(filter(lambda x: x.split('.')[1] == 'pdf' or x.split('.')[1] == 'tif' or x.split('.')[1] == 'TIF', filenames))
            vlist_noext = []
            for item in vlist:    
                vlist_noext.append(item.split('.')[0])
            #print ("NEW LIST: " + str(vlist_new))
            c  = collections.Counter(vlist_noext)
            vlist_new = ([n for n in c if c[n]==1])

            vlist_final = []
            for item in vlist_new:
                for vitem in vlist:
                    if item == vitem.split('.')[0] and (vitem.split('.')[1] == 'tif' or vitem.split('.')[1] == 'TIF'):        
                        vlist_final.append(item)

            vlist_final.sort()
            if len(vlist_final) == 0:
                print ("All set at: " + dirpath)
                createLOG("All set at: " + dirpath + "\n")
            else:
                print ("Created pdfs @: " + dirpath + "\n")
                createLOG("Created pdfs @: " + dirpath + "\n")
                for item in vlist_final:
                    #print (dirpath, item)
                    print ("Name: " + str(item) + ".tif\n")
                    createLOG("File name: " + str(item) + ".pdf\n")
                    # carete the PDFs
                    makePDF(dirpath, item + ".tif", item)
                    
if __name__ == '__main__':
    filetime = time.strftime("%Y%m%d")
    f = open('vaultlog_' + filetime + '.txt','w')
    #a = input('Create a new file')
    crawlFolders(r"C:\Temp\vtest")
    f.close()
