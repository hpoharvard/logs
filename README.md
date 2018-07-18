Two python scripts:

1. (ip.py) Python script to filter Windows Server ArcGIS Logs to extrapolate only the cs-ref
outside the Harvard Domain. CS(Referrer) - https://msdn.microsoft.com/en-us/library/windows/desktop/aa814385(v=vs.85).aspx - indicate
the site that the user last visited. This site provided a link to the current site. 
Geocoding the IP address of the client that made the request using (http://freegeoip.net/)

2. (crawl.py) Python script to crawl the PIRC Vault folders, identify all tif files and the corrispondent pdf file. If a corrispondet 
PDF file does not exist then a new one will be created. The script use the img2pdf lib (https://github.com/josch/img2pdf)