---
title: "Client-Server-Installation"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_h_installation_client_server.htm"
file: "admin_h_installation_client_server"
category: "admin"
---

# Client-Server-Installation

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Client-Server-Installation

Familiarize yourself first with the special characteristics of the Client-Server installation. For this, you will find an overview and background information in [Installation variants](admin_r_installation_variants.htm).

The installation is carried out as follows:

  1. Choose the distribution of the EEC parts adapted to your requirements and IT structure to one or several servers.
  2. Create the folders for resources.
  3. Share the created folders for remote access.



### Note

Mapped drives or UNC paths cannot be specified during the server installation. For the server installation the Setup file is to be copied to the server and there installed locally.

  1. Copy the installation file to the server on which the application is to be located later on.
  2. Start the installation file.
  3. Select the language of the installation wizard.
  4. Click [OK].
  5. Acknowledge the following information page with [Next >].
  6. Accept the license agreement.
  7. Click [Next >].
  8. Select the installation variant Client-Server-Installation.
  9. Click [Next >].
  10. Enter the target folder for the installation.
  11. Click [Next >].
  12. Enter the folder in which the resources are to be saved.
  13. Click [Next >].
  14. Complete the installation overview with [Install].



### Note

Please note that localhost always points to the computer on which the process is currently executed.

If the UNC paths are not available, these can be edited subsequently in the initialization file (for example ec.ini).

Afterwards EEC has to be licensed, bevore it can start (see [Licensing](admin_h_installation_licensing.htm) and [Starting](admin_h_installation_client_server_start.htm)).

### Note

Never start a Client-Server installation without the correct setting of the folders Workspace and Configuration in the file ec.ini!

Every client has its own ec.ini!

If this has already happened, follow the instructions in the chapter [Repairing a Client-Server installation](admin_h_maintenance_client_server_installation_repair.htm).

Optimizations:

Property | Comment  
---|---  
RAM | See initialization parameter [-xmx](admin_r_vmargs_xmx.htm)
