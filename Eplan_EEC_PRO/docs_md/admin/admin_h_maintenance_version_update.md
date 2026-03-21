---
title: "Change to Current EEC Version"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_h_maintenance_version_update.htm"
file: "admin_h_maintenance_version_update"
category: "admin"
---

# Change to Current EEC Version

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here: 

## Change to Current EEC Version

To transfer the user data and settings from an older EEC version to the current one, different steps are required depending on the installation variant.

## General

These steps have to be performed for all installations:
    1. Export settings from the old EEC and import them into the new EEC.
    2. Modify settings for suitable disciplines.
    3. Modify the initialization data (ec.ini).
    4. Copy self-produced plugins into the folder \dropins.
    5. Copy resources to the new EEC (possibly an existing export has to be modified accordingly).

## ECAD

    1. Copy license default setting file (when simultaneously switching to current Eplan Electric P8 version).
    2. Create macros, basic project templates and macro project templates with the compatible P8 version.
    3. Synchronize discipline components.

## Job Server

    1. Install EEC for Job Server and/or Job Server Worker.
    2. Install plugins for Job Server and/or Job Server Worker.
    3. Customize the initialization file (ec.ini) for Job Server and/or Job Server Worker.

## Windows Service

    1. Creating and configuring the license default setting file.
    2. Terminate and uninstall the old service (with PowerShell -ExecutionPolicy ByPass.\uninstallService.ps1).
    3. Install and start the new service (with PowerShell -ExecutionPolicy ByPass.\installService.ps1).

## Web EEC

    1. Install the new version of Tomcat.
    2. Unpack the webec.war file in the Tomcat folder.
    3. Customize the web.xml file or import from the old Tomcat.
    4. Start Tomcat.
    5. Import settings from the old initialization file (ec.ini).
    6. As of Version 2.9 the Remoteserver plugin is installed automatically.
