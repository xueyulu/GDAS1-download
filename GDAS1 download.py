from ftplib import FTP
import os

# 1. Set the directory you would like to download the files to
destdir='D:/HYSPLIT/data'

# 2. Set the path to the FTP directory that contains the data you wish to download.
directory = '/archives/gdas1'

# 3. Set the FTP server
ftpdir = 'arlftp.arlhq.noaa.gov'

# 4.Connect and log in to the FTP
ftp = FTP(ftpdir)
ftp.login()

# 5. Change to the directory where the files are on the FTP
ftp.cwd(directory)

# 6.Get a list of the files in the FTP directory
files = ftp.nlst()

# 7.set the needfiles,year,month

# year=['12','13']
# month=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

year=['05']
month=['jan']

needfiles=[s for s in files if s[-5:-3] in year and s[6:9] in month]

# 8.calculate the needfiles number and size
number=len(needfiles)
size=0

for i in needfiles:
    print(i)
    size+=ftp.size(i)

SIZE=round(size/1024/1024/1024,2)

print('You have selected ' +str(number)+' pieces of data,which may about '+str(SIZE)+'G'  )

# 9.Download all the needfiles
os.chdir(destdir)
    
for file in needfiles:
    print('Downloading...' + file)
    ftp.retrbinary('RETR ' + file, open(file, 'wb').write)    
print('Sucessfully Download !')
    
#10.over the Download and Close the FTP connection    
ftp.quit()