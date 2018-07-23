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
import sys, os, time, collections, argparse
from win32com.client.dynamic import Dispatch

parser = argparse.ArgumentParser(description='Add an input path')
parser.add_argument('-d',help='directory to use',action='store')

args = parser.parse_args()

# create log file
def createLOG(info):    
    f.write(info)    
    
# create a new pdf
def makePDF(path, filename):    
    src = os.path.abspath(path + "\\" + filename + ".tif")
    avdoc = Dispatch("AcroExch.AVDoc")
    avdoc.Open(src, src)
    pddoc = avdoc.GetPDDoc()
    pddoc.Save(1, os.path.abspath(path + "\\" + filename + ".pdf")) 
    #pddoc.Close()
    #avdoc.close(-1)  

# crawl folders
def crawlFolders(rootpath):    
    for dirpath, dirnames, filenames in os.walk(rootpath):        
        #print ("ORIGINAL LIST: " + str(filenames), str(len(filenames)))
        if len(filenames) > 1:
            vlist = filenames           
            vlist = list(filter(lambda x: x.split('.')[-1] == 'pdf' or x.split('.')[-1] == 'tif' or x.split('.')[-1] == 'TIF', vlist))            
            
            vlist_noext = []            
            for item in vlist:                    
                vlist_noext.append(item.rsplit('.',1)[0])                     
            
            c  = collections.Counter(vlist_noext)
            vlist_new = ([n for n in c if c[n]==1])
                       
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
               
        else:
            vlist = filenames           
            vlist = list(filter(lambda x: x.split('.')[-1] == 'pdf' or x.split('.')[-1] == 'tif' or x.split('.')[-1] == 'TIF', vlist))
                        
            vlist_noext = []
            for item in vlist:                    
            	vlist_noext.append(item.rsplit('.',1)[0])
            
            c  = collections.Counter(vlist_noext)
            vlist_new = ([n for n in c if c[n]==1])
            
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
            
if __name__ == '__main__':
    filetime = time.strftime("%Y%m%d")
    f = open('vaultlog_' + filetime + '.txt','w')    
    crawlFolders(args.d)
    f.close()
