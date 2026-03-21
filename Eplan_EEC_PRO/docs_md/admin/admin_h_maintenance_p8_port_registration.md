---
title: "Open ports for Eplan P8 connection"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_h_maintenance_p8_port_registration.htm"
file: "admin_h_maintenance_p8_port_registration"
category: "admin"
---

# Open ports for Eplan P8 connection

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here: 

## Open ports for Eplan P8 connection

The default port for the Eplan P8 connection is port 80. If this port is already used by another service, the port for the connection to Eplan P8 must be changed.

### Note

If Eplan has never been installed on a host before, Eplan URL registration starts during the installation as of Version 2024. You can change the default port with the Eplan URL registration program and add further ones. The program is located in the folder <Eplan Installation folder>\Bin\EplanUrlActivatoru.exe. The program lists all existing port assignments of the Eplan services. The options known from the platform are available for editing the list. To change the ports via script, the Url keys of the following registry entries must be changed:
    
        HKEY_LOCAL_MACHINE\SOFTWARE\EPLAN\Services\<Text>
    HKEY_LOCAL_MACHINE\SOFTWARE\**Wow6432Node** \EPLAN\Services\<Text>

In addition to the registry entries, the URLs must be registered with netsh.
    
        netsh http add urlacl url=http://+:<Port>/EPLAN_EEC<Text> user=<Domain>\<User>
    netsh http add urlacl url=http://+:<Port>/EPLAN_EEC<Text> user=<Domain>\<User>
