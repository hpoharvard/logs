"""
__author__ = "Giovanni Zambotti"
__copyright__ = ""
__credits__ = ["Giovanni Zambotti"]
__license__ = "GPL"
__version__ = "1.0.2"
__maintainer__ = "Giovanni Zambotti"
__email__ = "g.zambotti@gmail.com"
__status__ = "Production"
"""
import sys, os, time, collections, argparse, csv
from win32com.client.dynamic import Dispatch

parser = argparse.ArgumentParser(description='Add an input path')
# add -d argument to specify the directory to crwal
parser.add_argument('-d', help='Directory to use',action='store')
# add -f argument to input the name of the file
parser.add_argument('-f', help='Name of the output file',action='store')

args = parser.parse_args()

# create log file to track all the pdf created and their location
def createLOG(info):    
    f.write(info)    

# create log file to track tif file that could not been created and their location
def createLOGerror(info):    
    e.write(info)    
    
# create a new pdf
def makePDF(path, filename):    
    src = os.path.abspath(path + "\\" + filename + ".tif")
    avdoc = Dispatch("AcroExch.AVDoc")
    try:
        avdoc.Open(src, src)
        pddoc = avdoc.GetPDDoc()
        pddoc.Save(1, os.path.abspath(path + "\\" + filename + ".pdf")) 
        pddoc.Close()
        del pddoc
        avdoc.close(-1)  
        del avdoc
    except:
        print ("could not convert pdf")
        createLOGerror(src + "\n")
# create a new list that contains only unique files 
def uniqueFiles(vlist, dirpath):
    vlist_noext = []            
    for item in vlist:                    
        vlist_noext.append(item.rsplit('.',1)[0])    
    c  = collections.Counter(vlist_noext)
    vlist_new = ([n for n in c if c[n]==1])
    stripExt(vlist_new, vlist, dirpath)

# create a new list a strip out all the extensions             
def stripExt(vlist_new, vlist, dirpath):
    vlist_final = []
    for item in vlist_new:
        for vitem in vlist:
            if item == vitem.rsplit('.',1)[0] and (vitem.rsplit('.',1)[1] == 'tif' or vitem.rsplit('.',1)[1] == 'TIF'):        
                vlist_final.append(item)    
    vlist_final.sort()
    
    if len(vlist_final) == 0:
        print ("All set at: " + dirpath)                
    else:
        print ("Created pdfs @: " + dirpath + "\n")                
        for item in vlist_final:
            print (item + ","+ dirpath)
            createLOG(item + ","+ dirpath + "\n")
            makePDF(dirpath, item)

# crawl folders
def crawlFolders(rootpath):    
    for dirpath, dirnames, filenames in os.walk(rootpath):                
        # crawl all folders with more then a single file        
        if len(filenames) > 1:
            vlist = filenames           
            # create a list of files with pdf, tif, or TIF extensions only 
            vlist = list(filter(lambda x: x.split('.')[-1] == 'pdf' or x.split('.')[-1] == 'tif' or x.split('.')[-1] == 'TIF', vlist))                        
            uniqueFiles(vlist, dirpath)               
        else:
            vlist = filenames           
            vlist = list(filter(lambda x: x.split('.')[-1] == 'pdf' or x.split('.')[-1] == 'tif' or x.split('.')[-1] == 'TIF', vlist))                        
            uniqueFiles(vlist, dirpath)            

if __name__ == '__main__':
    filetime = time.strftime("%Y%m%d")
    f = open(args.f + "_" + filetime + '.csv','wb')
    e = open("errors_" + args.f + "_" + filetime + '.csv','wb')
    crawlFolders(args.d)
    f.close()
    e.close
