---
title: "Exporting, backing up and importing data for a Client-Server installation"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_h_backup_export_store_import_data.htm"
file: "admin_h_backup_export_store_import_data"
category: "admin"
---

# Exporting, backing up and importing data for a Client-Server installation

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Exporting, backing up and importing data for a Client-Server installation

The steps to export, back up and import data are not markedly different form those of the Stand-Alone installation.

The only differences are:

  * During the client-server installation you export the settings for each individual user.
  * Back up the ec.ini file and copy it back to the installation folder after the new installation.



In particular, proceed as follows:

  1. Export and back up the data from the existing installation as you would for a stand-alone installation (see [Exporting the current information model](admin_h_backup_export_current_model.htm)).
  2. Back up the file ec.ini (located in the EEC installation folder).
  3. Remove the existing installation.
  4. Install the new EEC version.
  5. Copy the backed-up ec.ini back to the EEC installation folder.
  6. Apply the resources from the compressed resource folder (see [Restoring resources](admin_h_backup_recover_resources.htm)).
  7. Apply the settings (see [Restoring settings](admin_h_backup_recover_user_settings.htm)).



### Note

The settings have to be applied for each user separately.
