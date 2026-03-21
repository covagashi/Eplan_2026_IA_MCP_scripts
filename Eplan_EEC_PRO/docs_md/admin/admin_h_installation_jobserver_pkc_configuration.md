---
title: "Configuring a Job Server with a public key certificate"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_h_installation_jobserver_pkc_configuration.htm"
file: "admin_h_installation_jobserver_pkc_configuration"
category: "admin"
---

# Configuring a Job Server with a public key certificate

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Configuring a Job Server with a public key certificate

For companies with distributed structures, a secure connection to the Job Server by means of a signed public key certificate is usually required. This section describes the creation of the certificate and the configuration of the Job Server with a signed public certificate.

Preconditions:

  * The Job Server is installed on a server.



### [Creating a keystore and certificate with Java Keytool](javascript:void\(0\);)

  1. Open a console with administrator rights on the server.
  2. Navigate to the folder of the Java installation where the keytool.exe file is located.
  3. Enter the command to create the keystore and certificate using the following syntax:
    
        keytool -genkeypair -dname "cn=<JOB-SERVER-URL>, ou=<DEPARTMENT>, o=<COMPANY-NAME>, l=<LOCATION-TOWN>,c=<STATE>" -alias <JOB-SERVER-ALIAS-NAME> -validity 712 -keyalg RSA -keysize 4096 -ext ExtendedKeyUsage=serverAuth -ext KeyUsage=digitalSignature,keyEncipherment -ext SubjectAlternativeName=DNS:<JOB-SERVER-URL> -keystore <KEYSTORE-NAME>.jks

  4. Replace <JOB-SERVER-URL>, <DEPARTMENT>, <COMPANY-NAME>, <LOCATION-TOWN>, <STATE>, <JOB-SERVER-ALIAS-NAME> and <KEYSTORE-NAME> with your own specifications.
  5. Enter the password for the keystore.
  6. The file .keystore is located in the same folder as the file keytool.exe.




A private certificate is now stored in the new keystore.

### [Creating a Certificate Signing Request (CSR file) with Java Keytool](javascript:void\(0\);)

  1. Open a console with administrator rights on the server.
  2. Navigate to the folder of the Java installation where the keytool.exe file is located.
  3. Enter the command to create the Certificate Signing Request using the following syntax:
    
        keytool -certreq -alias <SERVER-ALIAS-NAME> -keystore <KEYSTORE-NAME>.jks -file <SERVER-ALIAS-NAME>.csr -ext SubjectAlternativeName=DNS:<TOMCAT-SERVER-URL>

  4. Replace <SERVER ALIAS-NAME>, <KEYSTORE-NAME>, <SERVER ALIAS-NAME> and <TOMCAT-SERVER-URL> with your own specifications.
  5. Enter the password for the keystore.
  6. The <SERVER-ALIAS-NAME>.csr file is located in the same folder as the keytool.exe file.




Send the CSR file to the appropriate authorized issuing authority.

A signed certificate (CRT file) is returned from the authorized issuing authority.

The signed certificate contains a certificate chain. A certificate chain can be recognized when looking at the contents by the fact that it contains at least two blocks that start with BEGIN CERTIFICATE and end with END CERTIFICATE.

### [Example of a signed certificate with a certificate chain](javascript:void\(0\);)
    
    
    -----BEGIN CERTIFICATE-----
    MIIGVzCCBT+gAwIBAgITbQA6dz5jedRlyde5UgAAADp3PjANBgkqhkiG9w0BAQsF
    ADBYMRMwEQYKCZImiZPyLGQBGRYDaW50MRMwEQYKCZImiZPyLGQBGRYDZmxnMRIw
    
    	...
    
    2Km685y4zOhD4a2Z4GgZbDiiUscDt/cPFK833PN+fOJG+nM3J/C2Ld3WuFgz2Fkg
    Re4wyba9MPOTZTmRBcgsLDqmLi0zc8Adq4JeNB8Z9x8b/U6YcD95rEwDcA==
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    MIIXqAYJKoZIhvcNAQcCoIIXmTCCF5UCAQExADCCBm4GCSqGSIb3DQEHAaCCBl8E
    AQsFADBYMRMwEQYKCZImiZPyLGQBGRYDaW50MRMwEQYKCZImiZPyLGQBGRYDZmxn
    
    	...
    
    gUX8SnZNOw/VnA81WXcSg3lZBi2I3QC10bbKFP4S41z+2Cu8T8Q4U4ewu0VeGakt
    l9XPQ8pEDClKmzEA
    -----END CERTIFICATE-----

### [Importing a signed certificate into Keystore](javascript:void\(0\);)

  1. Open a console with administrator rights on the server.
  2. Navigate to the folder of the Java installation where the files keytool.exe and <KEYSTORE-NAME>.jks are located.
  3. Enter the command to import the certificate into the keystore with the following syntax:
    
        keytool -importcert -file <CERTIFICATE-NAME>.crt -keystore <KEYSTORE-NAME>.jks -alias "<SERVER-ALIAS-NAME>"

  4. Replace <CERTIFICATE-NAME>, <KEYSTORE-NAME> and <SERVER-ALIAS-NAME> with your own specifications.
  5. Enter the password for the keystore.
  6. The signed certificate is then successfully stored in the keystore.




### [Configuring the connection with the Job Server](javascript:void\(0\);)

  1. On the server open the initialization file (ec.ini) of the Job Server installation with an editor.
  2. Add the following runtime options:
    
        -Dde.eplan.eec.jobserver.disablehttps=false
    -Dde.eplan.eec.jobserver.httpsPort=<SSL PORT>
    -Dde.eplan.eec.jobserver.port=<PORT>
    -Dde.eplan.eec.jobserver.aliasurl=https://<JOB-SERVER-ALIAS-NAME>
    -Dde.eplan.eec.jobserver.private.aliasurl=http://<JOB-SERVER-ALIAS-NAME>:<PORT>

  3. Replace <SSL PORT> and <JOB-SERVER-ALIAS-NAME> with your own specifications.
  4. The configuration of the initialization file is complete.




### [Entering keystore and password in the preferences](javascript:void\(0\);)

  1. Start the Job Server.
  2. Open the menu Window > Settings.
  3. Navigate to the entry Job Server.
  4. Enter the file name and the password for the keystore in the HTTPS support section.



### Note

To use the secure connection you have to restart the Job Server.
