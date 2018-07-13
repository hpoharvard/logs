Two python scripts:

1. (ip.py) Python script to filter Windows Server ArcGIS Logs to extrapolate only the cs-ref
outside the Harvard Domain. CS(Referrer) - https://msdn.microsoft.com/en-us/library/windows/desktop/aa814385(v=vs.85).aspx - indicate
the site that the user last visited. This site provided a link to the current site. 
Geocoding the IP address of the client that made the request using (http://freegeoip.net/)

2. (crawl.py) Python script to crawl a folders, identify all tif files and if there is an equivalent pdf file, if not
create a pdf file. The script use the img2pdf lib (https://github.com/josch/img2pdf)