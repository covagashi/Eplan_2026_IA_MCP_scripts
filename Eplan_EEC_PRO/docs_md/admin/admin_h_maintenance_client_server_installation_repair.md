---
title: "Repairing a Client-Server installation"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_h_maintenance_client_server_installation_repair.htm"
file: "admin_h_maintenance_client_server_installation_repair"
category: "admin"
---

# Repairing a Client-Server installation

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here: 

## Repairing a Client-Server installation

If EEC was started on a server without first stating the folders workspace and configuration correctly in the ec.ini file, the following steps must be taken to render the EEC operable again:
    1. Shut down EEC.
    2. In the ec.ini file, enter the correct paths for the folders workspace and configuration.
    3. Replace the content of the folder configuration with the content of the archive configuration.bak.zip from the folder install/configuration.

### Note

By starting without the correct settings in ec.ini, a configuration folder was created that is then no longer used. This can be deleted.
