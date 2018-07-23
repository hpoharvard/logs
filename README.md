Four python scripts:

1. (ip.py) Python script to filter Windows Server ArcGIS Logs to extrapolate only the cs-ref
outside the Harvard Domain. CS(Referrer) - https://msdn.microsoft.com/en-us/library/windows/desktop/aa814385(v=vs.85).aspx - indicate
the site that the user last visited. This site provided a link to the current site. 
Geocoding the IP address of the client that made the request using (http://freegeoip.net/)

2. (crawl.py) Python script to crawl the PIRC Vault folders, identify all tif files and the corrispondent pdf file. If a corrispondet 
PDF file does not exist then a new one will be created. The script uses the img2pdf lib (https://github.com/josch/img2pdf)

3. (crawl_wand) Python script to crawl the PIRC Vault folders, identify all tif files and the corrispondent pdf file. If a corrispondet 
PDF file does not exist then a new one will be created. The script uses the imagemagick (https://www.imagemagick.org/script/index.php) 
and wand lib (http://docs.wand-py.org/en/0.4.1/guide/write.html)

4. (crawl_adobe.py) Python script to crawl the PIRC Vault folders, identify all tif files and the corrispondent pdf file. If a corrispondet 
PDF file does not exist then a new one will be created. The script uses the Interapplication Communication API (https://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/iac_api_reference.pdf) to create the PDF and this python library (https://pypi.org/project/pywin32/) to connect to Adobe Acrobat.
The script accepts a path argument (python -d C:\Temp) 

 