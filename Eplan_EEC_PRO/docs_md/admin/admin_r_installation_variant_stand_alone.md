---
title: "Stand-Alone"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_installation_variant_stand_alone.htm"
file: "admin_r_installation_variant_stand_alone"
category: "admin"
---

# Stand-Alone

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Stand-Alone

You create the Stand-Alone installation option on a workstation computer.

After installing and licensing the application, you can start working immediately (see chapter [Starting](admin_h_installation_stand_alone_start.htm)).

### Note

**The installation, or parts of it, must not be moved, copied or renamed at the file system level.**   
Such changes limit the operability of the application, or prevent the application from being executed.

Stand-Alone installation with EOX file for data storage:

All parts of EEC are installed within a folder structure. An EOX file is used for data storage purposes.

The following image shows the installed folder:

The folders plugins and dropins must always be directly below the installation folder (ec).

After installation EEC has to be licensed, before it can start (see [Licensing](admin_h_installation_licensing.htm) and [Starting](admin_h_installation_stand_alone_start.htm)).

Advantages of the Stand-Alone installation:

There is virtually no installation effort. Without administrative efforts, several EEC versions can be installed easily in parallel on a computer in different folders.

Data storage via EOX file can be realized also as read-only, so that a specific status of the model is maintained.

Disadvantages of the stand-alone installation:

When extending the application area to a team, it becomes more complex to synchronize model data, for example.
