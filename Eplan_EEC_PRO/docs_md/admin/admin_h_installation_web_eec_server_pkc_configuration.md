---
title: "admin_h_installation_web_eec_server_pkc_configuration"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_h_installation_web_eec_server_pkc_configuration.htm"
file: "admin_h_installation_web_eec_server_pkc_configuration"
category: "admin"
---

# admin_h_installation_web_eec_server_pkc_configuration

## Configuring a Web EEC Server with a public key certificate

For companies with distributed structures, a secure connection to the Web EEC Server by means of a signed public key certificate is usually required. This section describes the creation of the certificate and the configuration of the Web EEC Server with a signed public certificate. Requirements:
     * The Tomcat web server service is installed on a server.
     * Web EEC and Web EEC server are installed on the same server.

### Creating a keystore and certificate with Java Keytool

    1. Open a console with administrator rights on the server.
    2. Navigate to the folder of the Java installation where the keytool.exe file is located.
    3. Enter the command to create the keystore and certificate using the following syntax:
        
                keytool -genkeypair -dname "cn=<TOMCAT-SERVER-URL>, ou=<DEPARTMENT>, o=<COMPANY-NAME>, l=<LOCATION-TOWN>,c=<STATE>" -alias <SERVER-ALIAS-NAME> -validity 712 -keyalg RSA -keysize 4096 -ext ExtendedKeyUsage=serverAuth -ext KeyUsage=digitalSignature,keyEncipherment -ext SubjectAlternativeName=DNS:<TOMCAT-SERVER-URL> -keystore <KEYSTORE-NAME>.jks

    4. Replace <TOMCAT-SERVER-URL>, <DEPARTMENT>, <COMPANY-NAME>, <LOCATION-TOWN>, <STATE>, <SERVER-ALIAS-NAME>, <TOMCAT-SERVER-URL> and <KEYSTORE-NAME> with your own specifications.
    5. Enter the password for the keystore.
    6. The file .keystore is located in the same folder as the file keytool.exe.
Additional information about the command syntax of keytool is available at https://docs.oracle.com/en/java/javase/17/docs/specs/man/keytool.html.

### Example

<TOMCAT-SERVER-URL> = webserver.de.flg.int, <DEPARTMENT> = development, <COMPANY-NAME> = EPLAN GmbH & Co. KG, <LOCATION-TOWN> = Stuttgart, <STATE> = DE, <SERVER-ALIAS-NAME> = eec-webserver, <TOMCAT-SERVER-URL> = webserver.de.flg.int, <KEYSTORE-NAME> = webserver_keystore The following command to create the keystore and the certificate results from these specifications:
    
        keytool -genkeypair -dname "cn=webserver.de.flg.int, ou=development, o=EPLAN GmbH & Co. KG, l=Stuttgart,c=DE" -alias eec-webserver -validity 712 -keyalg RSA -keysize 4096 -ext ExtendedKeyUsage=serverAuth -ext KeyUsage=digitalSignature,keyEncipherment -ext SubjectAlternativeName=DNS:webserver.de.flg.int -keystore webserver_keystore.jks

A private certificate is now stored in the new keystore.

### Creating a Certificate Signing Request (CSR file) with Java Keytool

    1. Open a console with administrator rights on the server.
    2. Navigate to the folder of the Java installation where the keytool.exe file is located.
    3. Enter the command to create the Certificate Signing Request using the following syntax:
        
                keytool -certreq -alias <SERVER-ALIAS-NAME> -keystore <KEYSTORE-NAME>.jks -file <SERVER-ALIAS-NAME>.csr -ext SubjectAlternativeName=DNS:<TOMCAT-SERVER-URL>

    4. Replace <SERVER-ALIAS-NAME>, <KEYSTORE-NAME> and <TOMCAT-SERVER-URL> with your own specifications.
    5. Enter the password for the keystore.
    6. The <SERVER-ALIAS-NAME>.csr file is located in the same folder as the keytool.exe file.
Send the CSR file to the appropriate authorized issuing authority. A signed certificate (CRT file) is returned from the authorized issuing authority. The signed certificate contains a certificate chain. A certificate chain can be recognized when looking at the contents by the fact that it contains at least two blocks that start with BEGIN CERTIFICATE and end with END CERTIFICATE.

### Example of a signed certificate with a certificate chain
    
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

### Importing a signed certificate into Keystore

    1. Open a console with administrator rights on the server.
    2. Navigate to the folder of the Java installation where the files keytool.exe and <KEYSTORE-NAME>.jks are located.
    3. Enter the command to import the certificate into the keystore with the following syntax:
        
                keytool -importcert -file <CERTIFICATE-NAME>.crt -keystore <KEYSTORE-NAME>.jks -alias "<SERVER-ALIAS-NAME>"

    4. Replace <CERTIFICATE-NAME>, <KEYSTORE-NAME> and <SERVER-ALIAS-NAME> with your own specifications.
    5. Enter the password for the keystore.
    6. The signed certificate is then successfully stored in the keystore.

### Configuring the connection with the TomCat server

    1. Open the <Tomcat installation folder>/conf/server.xml file with an editor.
    2. Navigate to the entry for an SSL/TLS HTTP/1.1 Connector.
    3. Replace the existing entry with the following lines:
        
                <!-- HTTPS configuration -->
        	<Connector port="443" protocol="HTTP/1.1" SSLEnabled="true" maxThreads="150" scheme="https" secure="true" keystoreFile="<PATH-TO-KEYSTORE>/<KEYSTORE-FILENAME>" keystorePass="<PASSWORD>" clientAuth="false" sslProtocol="TLS" >
        	</Connector>

    4. Replace <PATH-TO-KEYSTORE>/<KEYSTORE-NAME> and <PASSWORD> with your own specifications.
    5. The configuration is complete. Activate the configuration by restarting the Tomcat service.

### Activating the configuration

    1. Open the Task Manager.
    2. Open the Services tab.
    3. Navigate to the entry Tomcat9.
    4. From the popup menu for Tomcat9 select the menu item Restart.
    5. The URL for calling up the Web EEC in the browser has changed through the configuration to [https://<SERVER-ALIAS-NAME>/web/main](https://localhost:443/webec/main)

### Note

To use the secure connection you have to restart the browser.
