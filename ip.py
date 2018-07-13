#####################################################################
### Filter Windows Server ArcGIS Logs to extrapolate only the cs-ref
### outside the Harvard Domain. CS(Referrer) indicate
### the site that the user last visited. This site provided a link
### to the current site.
### Geocoding the IP address of the client that made the request
### using (http://freegeoip.net/)
### Author: Giovanni Zambotti
### Date: 1/24/2016
### Email: g.zambotti@gmail.com
#################################################################### 

import os, sys, glob, psycopg2, time, requests, json, geocoder

# connect to postgres 
conn = psycopg2.connect("dbname=logs user=postgres password=postgres")

#################################################################
### loop all the logs file with the Windows Server
#################################################################        

def loopOriginalFiles(path):      
    for fname in glob.glob(path):
        print(fname.split("\\")[5])
        my_file = fname.split("\\")[5]
        #my_file = open(fname.split("\\")[4])        
        removeLines(my_file)
        importCopyFile()        
        remobeOutput()
        print "remove output"
#################################################################
### import files to PostGIS and perform queries to filter them
#################################################################         
        
def importCopyFile():      
    my_file = open("output.txt")        
    importCSV(conn, 'tlog', my_file)
    insert_to_logmaster()
    delete_from_tlog()
    

def remobeOutput():
    os.remove(r"output.txt")
    

#################################################################
### create a copy of the orginal log file and remove the top four
### lines
#################################################################        

def removeLines(my_file):
    output = open("output.txt","a+b")
    f = open(my_file)
    for i, line in enumerate(f):
        if not line.lstrip().startswith('#'):
            #print line
            output.write(line.replace('"',''))
    output.close()

#################################################################
### import arcgis log file into PostGIS tlog table
#################################################################        
  
def importCSV(conn, table_name, file_object):
    #SQL_STATEMENT = """COPY %s from STDIN DELIMITERS '\t' CSV header;"""
    SQL_STATEMENT = """COPY %s from STDIN DELIMITERS ' ' CSV;"""
    cursor = conn.cursor()
    cursor.copy_expert(sql=SQL_STATEMENT % table_name, file=file_object)
    conn.commit()
    cursor.close()

def insert_to_logmaster():
    cur = conn.cursor()
    sql = "insert into tlogmaster select * from tlog where csref NOT LIKE '%map.harvard%' AND csref NOT LIKE '-';"
    cur.execute(sql)
    conn.commit()
    cur.close

def delete_from_tlog():
    cur = conn.cursor()
    sql = "delete from tlog;"
    cur.execute(sql)
    conn.commit()
    cur.close


def iptolocation():    
    cur = conn.cursor()
    #sql = "select * from tip where lat1 is null"
    sql = "select * from tip"
    cur.execute(sql)
    print "Start Time : %s" % time.ctime()
    i = -1
    n = 10000
    for row in cur:
        i += 1
        if i == n:            
            n += 10000
            print '.......pause....', n
            time.sleep(3600)
        print i, row[0], n
        #time.sleep(1)        
        g = geocoder.freegeoip(row[0])
        #print g.json
        dIP = 'unknown'
        dLoc = '0'
        dCity = 'unknown'
        dRegion = 'unknown'
        dCountry = 'unknown'
        #print g.json.get('lat',defaultip), i, row[0], n
        ipupdate(g.json.get('lat',dLoc), g.json.get('lng',dLoc), g.json.get('city',dCity), g.json.get('region_code',dRegion), g.json.get('country_code3',dCountry), g.json.get('ip',dIP))
        
    conn.close()

def ipupdate(lat, lng, c, r, cn, ip):    
    cur = conn.cursor()
    sql = "update tip_up set lat = " + str(lat) + ", lng = " + str(lng) + ", city = '" + c.replace("'", "-") + "', region ='" + r.replace("'", "-") + "', country ='" + cn.replace("'", "-") + "' where cipunique = '" + ip + "'"
    cur.execute(sql)
    conn.commit()
    cur.close    
        
if __name__ == '__main__':    
    #loopOriginalFiles('N:\inetpub\logs\LogFiles\W3SVC1\u_ex15*.log')
    #loopOriginalFiles(r'C:\gis\p2017\log\*.log')
    iptolocation()
    
