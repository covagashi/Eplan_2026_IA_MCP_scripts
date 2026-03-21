---
title: "Installation variants"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_installation_variants.htm"
file: "admin_r_installation_variants"
category: "admin"
---

# Installation variants

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Installation variants

EEC is set up as a modular system, and can be installed and operating in various configurations. The license agreements for internal and external users applies to all of the installation variants.

     * Stand-Alone: Single workstation application Several modular system developers and / or users with Stand-Alone installations can exchange and / or synchronize their data via EOX files.
     * Client-Server: Multiple-workstation application for small group of users in a local network or in a separate virtual environment. Several modular system developers can work on the same model, without having to synchronize. Not recommended for a configuration of projects across distributed locations.
     * EEC Server: Like Stand-Alone installation, with EOX file for data storage on a Server (Apache Tomcat). Extension to EEC Server via plug-ins and modified ec.ini. Comes with http connection (also SSL-encrypted). Generates target data, as well as Form-UI elements of a project, and makes these available to the user via the Web EEC Server.
     * Job Server: As Stand-Alone installation. Extension to Job Server and/or Worker via plugins. Monitors a directory for the existence of job definitions, and, based on a loaded model executes project manipulations (Create new project, Instantiate components, Execute commands, Generate target data).
     * Web EEC Server: Multiple-workstation application for large groups of users to configure projects across distributed locations. Functional limitations possible with respect to certain disciplines; Graph2D currently not possible; Form-UI with some minor limitations (dialogs), because it is a web application. Requires an EEC server which is accessed remotely. SSL-encrypted communication possible.
     * Windows service: As Stand-Alone installation. Runtime environment for model of the development environment. Generates the target data of a project and makes these available to the user via the REST service.

The installation variants Stand-Alone and Client-Server are offered by the installation wizard, while Web EEC, EEC Server, Job Server and Windows Server are derived from these installation variants.

Caption:

Symbol | Meaning  
---|---  
| Installation file for Eplan Engineering Configuration.  
| Installation package for EEC client.  
| Installation file for EEC client.  
| Configuration file for EEC client installation.  
| EEC installation folder  
| EEC main application  
| Link to an executable file, e.g., main EEC application.  
| Initialization file for the main application  
| Data back end based on an EOX or an EECX file.  
| Folder with plugins for EEC. This corresponds to the DLL files of a classic Windows application.  
| Data storage in database: Folder with private user data, for example, user preferences, work status of created project documents, etc. Data storage with EOX: Folder containing information model, private user data, for example, user preferences, work status of created project documents, etc.  
| Folder with internal administrative data of the EEC, e.g., config.ini  
  
A table of [Important folders and files](admin_r_installation_important_files_folders.htm) can be found in the chapter of that name.
