---
title: "Client-Server"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_installation_variant_client_server.htm"
file: "admin_r_installation_variant_client_server"
category: "admin"
---

# Client-Server

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Client-Server

For the installation option Client Server you distribute the EEC components to at least two computers. A server is used to provide the model data (data back end) and/or the executable files of the EEC application. One or more workstation computers can execute the EEC and access the model data of the server.

The application and the resources do not necessarily have to be located on one server, but can be installed on two different servers:

Preparation A preparation or setup process step. (ISO) Down Arrow System-spec. generator Preparation A preparation or setup process step. (ISO) Down Arrow System-spec. generator Functional configuration generator Model Dimensioned 2D CAD Drawing generator generator Mechatronic components param Model Discipline-spec. configuration image/svg+xml EEC Workstation Link ec.ini configuration workspace Data access Refers to File server for application File server for resources resources >read/write< ec.exe ec.ini configuration plug-ins dropins proxy: EEC anyName.eox ../anyFolder >read/write< >read/write< May contain r/w r r/w

A file server provides the application with plug-ins and resources as Windows shares. Depending on whether the application or the resources are on the share, users will have either read-only or also write access to the respective share.

Another file server provides the resources that are accessed during the runtime.

The client-server installation involves two steps:

     * First, the servers are installed by starting the installation on the server that provides the share with the application. During the installation, the target location of the resources must be specified.
     * The data back end is then set up. Once all server-based steps are complete, the client installation is realized on each workstation. This is done via another setup wizard that is installed in the subfolder ec_client_setup of the application.

The installation of the client creates on each workstation a separate ec.ini file, as well as links to the application on the application share.

The above figure shows the folders and the process data traffic of the client-server installation. The read and write rights required for the individual areas are shown.

If EEC is started on the workstation, it reads the folders and files of the application, such as plugins, dropins, features or configuration. Locally, EEC creates caches, and stores the settings in a separate configuration folder. EEC has read and write access to the resources. For data storage with EOX files, it is possible to specify read-only or also write access. Client-computer-specific parts of the configuration folder and the workspace folder are always stored locally on the workstations in order to prevent noncompliance with Windows security policies, for example, regarding trusted assemblies (see Microsoft: [Code Access Security Policy Tool](http://msdn.microsoft.com/de-de/library/cb6t8dtz\(VS.80\).aspx)).

### Note

The installation, or parts of it, must not be moved, copied or renamed at the file system level. Such changes limit the operability of the application, or prevent the application from being executed.

Advantages of the Client-Server installation:

Lowest possible administration effort: All key data are stored centrally, and can be stored and updated there.

Disadvantages of the Client-Server installation:

When starting, application data (plug-ins) must be loaded from the server. This can lead to longer starting times. Each client computer requires a valid license.
