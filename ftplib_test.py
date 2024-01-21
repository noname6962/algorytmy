import ftplib


#laczenie sei z serwerem
ftp = ftplib.FTP()
ftp.connect('ftp.dlptest.com')
ftp.login('dlpuser', 'rNrKYTX9g7z3RgJRmxWuGHbeu')

with open("test2.txt", 'w') as file:
    file.write("siemka")

with open("test2.txt", 'rb') as files:
    ftp.storbinary("STOR test2.txt", files)

with open("test3.txt", 'w') as file1:
    ftp.retrlines("RETR test2.txt", file1.write)

with open("test3.txt", 'r') as file2:
    print(file2.read())

