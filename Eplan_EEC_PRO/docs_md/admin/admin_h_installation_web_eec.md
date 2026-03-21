---
title: "WebÂ EEC installation"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_h_installation_web_eec.htm"
file: "admin_h_installation_web_eec"
category: "admin"
---

# WebÂ EEC installation

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Web EEC installation

This section describes the installation and configuration of the web-based EEC variant. For further information on the products used, for example, Tomcat, please refer to the documentation of each product.

Overview:

The Web EEC is a web application based on Eclipse Rich Ajax Platform (RAP), which makes it possible to put EEC models on the web.

The following figure gives an overview of the system configuration:

Browser:

The Web EEC is a web application that the user calls up in a web browser. The graphical interface of the application is displayed and executed in the browser window.

Web EEC Server:

The Web EEC requires as an execution environment a web server like Tomcat that implements the servlet specification. The essential Web EEC Serverâs function is to supply to the client and / or browser Form-UI-based user interfaces, process user requests, send function calls to the EEC Server, and process their results accordingly.

EEC Server:

The operation of a Web EEC application requires, apart from the Web EEC Server, an EEC Server. Its essential task is to manage the data and models, as well as provide fundamental EEC functions, such as the execution of commands.

Perform the installation in the following sequence:

  1. [Installing EEC servers](admin_h_installation_web_eec_eec_server.htm)
  2. [Installation and configuration of the Web EEC Server](admin_h_installation_web_eec_server.htm)
  3. [Installing and configuring Web EEC](admin_h_installation_web_eec_configuration.htm)
