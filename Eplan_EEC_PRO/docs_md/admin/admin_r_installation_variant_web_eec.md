---
title: "WebÂ EEC"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_installation_variant_web_eec.htm"
file: "admin_r_installation_variant_web_eec"
category: "admin"
---

# WebÂ EEC

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Web EEC

The installation option Web EEC can be installed and distributed on different servers, or just on a single computer.

After the installation of the application as a stand-alone installation on the EEC Server, further manual installation steps are required (see [Installing EEC servers](admin_h_installation_web_eec_eec_server.htm)).

On the page of the EEC Server, the file ec.ini must be adjusted in such a way that the data of the user interface of a model provided can be sent to the Web EEC Server on the basis of an EOX file. In addition to the EOX file used, one must specify read-only or also write access. For communications, the host of the EEC Server, the port, and waiting time must be defined. The identical port number must be stated in the file web.xml of the Tomcat Server. The port must be different from the port for the communication between the clients and the Web EEC Server if the Web EEC Server and the EEC Server have been set up on the same computer.

On the page of the Web EEC Server, at first, a Tomcat web server must be installed (see [Installing and configuring Web EEC](admin_h_installation_web_eec_configuration.htm)).

Then, the port for client communications must be configured, and Java options set up.

The Web EEC Server and EEC Server can be installed on different computers, or on the same computer. If the servers are installed on different computers, then the created files must be located on a file system which is accessible by both computers.
