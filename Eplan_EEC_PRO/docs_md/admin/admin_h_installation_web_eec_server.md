---
title: "Installation and configuration of the Web EEC Server"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_h_installation_web_eec_server.htm"
file: "admin_h_installation_web_eec_server"
category: "admin"
---

# Installation and configuration of the Web EEC Server

Path to the project This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here: 

## Installation and configuration of the Web EEC Server

The Web EEC Server used is Apache Tomcat. This can be downloaded from the following web site in different versions: https://tomcat.apache.org/ Please note the requirements for compatibility with the Java Development Environment (JRE) or the Java Development Kit (JDK) on the page https://tomcat.apache.org/whichversion.html. [Software and hardware requirements > Eplan Engineering Configuration > Apache Tomcat Server for Web EEC Server](../../../../../../../en-US/Infoportal/Content/swreqs/content/htm/swreqs_k_eecpro.htm#TOMCAT)

### Note

The following entries in the initialization file (ec.ini) prevent the successful start of the Apache Tomcat server version 9: -Dorg.eclipse.rap.workbenchAutostart=false -Dorg.osgi.framework.os.name=win Apart from the regular program version, which is started conventionally, there is also a Windows Service Installer, which installs Tomcat as a Windows system service, and also provides an installation wizard. Follow the installation wizard. Note a change to the installation folder from Tomcat Version 9 to Tomcat Version 10: Tomcat Version 9 is installed in the <Tomcat installation folder>\Tomcat <Version>\webapps folder. Tomcat Version 10 and more recent versions are installed in the <Tomcat installation folder>\Tomcat <Version>\webapps-javaee folder. After the successful installation, the configuration of the Tomcat web server starts.
    1. To avoid port conflicts with the EEC Server, a value different from the default 8080 must be entered for the HTTP1.1 Connector Port if the Tomcat web server and the EEC Server are to be installed on the same host.
    2. Confirm your input with [Next >].
    1. Enter the installed version of the Java Virtual Machine.
    2. Confirm your input with [Next >].
    3. Enter the folder for the installation of the Tomcat server.
    4. Complete the installation with [Install].
You must start the Tomcat Monitor to configure the Tomcat web server:
    1. Right-click the symbol of the Tomcat Monitor on the taskbar.
    2. Select Configure from the popup menu.
The Tomcat Monitor opens.
    3. Open the Java tab.
    4. Select the Java Virtual Machine.

### Note

After each update of the Java installation, the Tomcat Monitor has to be opened again, to customize the path to the vm.dll to the update.
    1. Confirm your input with [OK].

### [Updating Apache Tomcat](javascript:void\(0\);)

Apache Tomcat can be installed in parallel for different versions. Each version installs its own service, which differs in the naming. An installed service cannot be renamed. To set up a new service with the same name, the existing one has to be terminated and uninstalled beforehand. Exit the existing Apache Tomcat service:
    1. Open the Task Manager.
    2. Open the Services tab.
    3. Navigate to the entry Tomcat9.
    4. From the popup menu for Tomcat9 select the menu item Stop.
Uninstall the existing Apache Tomcat service:
    1. Open a command prompt (console) with administrator rights.
    2. Enter the following command:
sc delete <Service name>
    1. Replace <Service name> with the name of the service, for example Tomcat9.
    2. In the case of success, the command prompt reports success.
Restart Windows for this change to take effect. Install a different version of Apache Tomcat as described above.
