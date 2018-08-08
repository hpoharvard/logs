Four python scripts:

1. [ip.py] Python script to filter Windows Server ArcGIS Logs to extrapolate only the cs-ref
outside the Harvard Domain. CS(Referrer) - https://msdn.microsoft.com/en-us/library/windows/desktop/aa814385(v=vs.85).aspx - indicate
the site that the user last visited. This site provided a link to the current site. 
Geocoding the IP address of the client that made the request using (http://freegeoip.net/)

2. [crawl.py] Python script to crawl the PIRC Vault folders, identify all tif files and the corrispondent pdf file. If a correspondent 
PDF file does not exist then a new one will be created. The script uses the img2pdf lib (https://github.com/josch/img2pdf)

3. [crawl_wand.py] Python script to crawl the PIRC Vault folders, identify all tif files and the corrispondent pdf file. If a correspondent 
PDF file does not exist then a new one will be created. The script uses the imagemagick (https://www.imagemagick.org/script/index.php) 
and wand lib (http://docs.wand-py.org/en/0.4.1/guide/write.html)

4. [crawl_adobe.py] Python script to crawl the PIRC Vault folders, identify all tiff files and the correspondent pdf file. If a correspondent PDF file does not exist, a new one will be created using the Adobe Acrobat DC. The PDF will be created using the Adobe Acrobat DC settings. The script uses the Interapplication Communication API (https://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/iac_api_reference.pdf) to create the PDF and this python library (https://pypi.org/project/pywin32/, http://nullege.com/codes/search/win32com, https://github.com/mhammond/pywin32) to connect to Adobe Acrobat.
The script accepts two arguments. The -d argument allow to specify the path, while the –f argument allow to specify name of the output file. Ex: (python crawl_adobe.py -d C:\Temp –f demo). The script requirements are:
	* Miniconda (https://conda.io/miniconda.html)
	* create conda env (conda create -n pirc python=2.7.15)
	* pywin32 (https://anaconda.org/anaconda/pywin32 - conda install -c anaconda pywin32)
	* args (https://anaconda.org/conda-forge/args - conda install -c conda-forge args)
	* activate pirc env (activate pirc)

Steps to run the script:
1. Open Anaconda Prompt (Start >> Anaconda Prompt)
2. Type >> activate pirc
3. Change to the script directory >> cd C:\Temp
4. Type >> python crawl_adobe.py -d C:\Temp –f demo




 