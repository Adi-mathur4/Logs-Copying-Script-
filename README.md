# Logs-Copying-Script-
Windows automation script in python for copying some particular files from local system to the server.


**Working of the Script**

1 -> The script install 7-zip on the system. This is integrated into the script to reduce the size of the file that needs to be sent over the newtrok resulting in less time for file transfer.
2 -> Then the script connects the system to a wifi which depends on the .xml file imported in the script.
3 -> The script then renames the file that need to be transfered with the name of the system.
4 -> The the script zips the file usinf 7 zip that we installed in step 1.
5 -> Once the zip file is created, the script makes a connection with the server using robocopy and the send the files over the connection with progress shown on the cmd.
