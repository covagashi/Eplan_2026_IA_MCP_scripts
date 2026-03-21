---
title: "Installation with command line parameters"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_h_installation_automated.htm"
file: "admin_h_installation_automated"
category: "admin"
---

# Installation with command line parameters

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Installation with command line parameters

Installation can be carried out in a shell with the specification of parameters.

The syntax is: setup_EEC_<version information> /Parameter<=argument> /Parameter<=argument>

The following command line parameters can be used:

Parameter | Description  
---|---  
/SILENT | Performs the installation without user interface, but with progress display for the EEC installation and the license-client installation. Default settings are used.  
/VERYSILENT | Like /SILENT, however, without progress display for EEC installation, but with progress display for license client installation.  
/LANG=de|en | Specifies the language for the installation. You can choose either de for German or en for English.  
/DIR=<installation directory> | Specifies the target directory including the drive for the installation.  
/SAVEINF=<path to .inf file> | Saves the installation settings in the specified inf file  
/LOADINF=<path to .inf file> | Applies the settings of the specified inf file for installation.  
This parameter in combination with /SILENT or /VERYSILENT allows automated installation on distributed computers.
