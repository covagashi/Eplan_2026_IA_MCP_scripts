---
title: "Important folders and files"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_installation_important_files_folders.htm"
file: "admin_r_installation_important_files_folders"
category: "admin"
---

# Important folders and files

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Important folders and files

In the following table, data and processes are assigned to specific folders, using a stand-alone installation as an example:

Folders and files | Read-/write rights | Explanations  
---|---|---  
ec.exe | R | Das EEC main applikation is ec.exe. A link to this file appears in the Start menu and, optionally, on the desktop.  
ec.ini | R | Initialization file for ec.exe.  
/configuration/ | RW | In this folder, Eclipse stores user-neutral configuration data that refer to the EEC installation. Like the workspace, this folder, too, belongs precisely to one running Eclipse application. In case of a Client-Server installation, this folder must therefore be located on the client computer. In the initialization file ec.ini this folder is specified with the -configuration argument.  
/plugins/ | R | All plugins of the EEC installation. The sum of plug-ins corresponds to the exe file of conventional applications  
/dropins/ | RW | The following is stored in this folder:
    1. Plug-ins created by the customer that are loaded like normal plug-ins at the start.
    2. Eclipse Extension Locations (dropins/myLocation/eclipse/, dropins/myLocation/eclipse/.eclipseextension, dropins/myLocation/eclipse/plugins or features or both)
    3. For further options, see <http://help.eclipse.org/helios/index.jsp?topic=/org.eclipse.platform.doc.isv/reference/misc/p2_dropins_format.html>  
/workspace/ | RW | Each user needs a private workspace where the user-specific configuration data, created documents, etc. are stored.  
/workspace/.metadata/ | RW | Eclipse stores the user-specific configuration data in this folder. These include the settings (Preferences) set up under Window > Settings, or other user-specific settings, such as the position and size of views, editors, perspectives, the editors most recently opened, etc.  
/resources/ | RW | This folder contains the âcontentsâ of the discipline-specific components, for example, EXF files, AWL files, etc.  
/db/ | RW | This folder contains the files of the database  
/install/ | RW | This folder contains the auxiliary data for the installation and / or use of skills  
/jre/ | R | Java runtime environment  
/jre/bin/javaw.exe | R | Application of the Java Virtual Machine  
  
*) Only available for hybrid installation.
