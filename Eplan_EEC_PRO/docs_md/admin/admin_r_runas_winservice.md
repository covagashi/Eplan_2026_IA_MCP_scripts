---
title: "Operation as Windows service"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_runas_winservice.htm"
file: "admin_r_runas_winservice"
category: "admin"
---

# Operation as Windows service

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Operation as Windows service

EEC can be installed and operated as a Windows service in the 64-bit version.

### [Requirements](javascript:void\(0\);)

     * .Net in Version 4.x (at least 4.5.2) must be installed on the host computer. The installed version can be displayed, for example, in the Registry Editor, key HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full.

### [Installation](javascript:void\(0\);)

#### [](javascript:void\(0\);)[Installation of Job Server](javascript:void\(0\);)

Follow the description in the Section [Job Server installation](admin_h_installation_job_server.htm) to install the Job Server.

#### [](javascript:void\(0\);)[Installation of the Visual C++ Redistributable](javascript:void\(0\);)

Visual C++ Redistributable 2010, 2012 and 2015 have to be installed on the host computer in the 64-bit version. The installation files are contained in the directory <EEC installation folder>\install\other.

#### [](javascript:void\(0\);)[Eplan License Manager](javascript:void\(0\);)

The current version of the Eplan License Manager has to be installed in the 64-bit version.

#### [](javascript:void\(0\);)[Log on as service](javascript:void\(0\);)

The user with whom the Windows service is to be carried out later requires the authorization: **Log on as service**. The authorization can be configured with Administrator rights by using the Editor for local group policies.

    1. Open the editor for local group policies (for example either via the Microsoft Management Console or by running gpedit.msc).

    1. In the console tree navigate to Local Computer Policies > Computer Configuration > Windows Settings > Security Settings > Local Policies > User Rights Assignment.
    2. Select the Log on as Service entry in the Policy list.
    3. Open the properties of the policy.
    4. Open the Local Security Setting tab.
    5. Use [Add User or Group...] to add the user.
    6. Confirm the settings with [OK].

#### [](javascript:void\(0\);)[COM safety configuration of the EClientService](javascript:void\(0\);)

The user with whom the Windows service is to be carried out later requires start and activation authorization for **EClientService**. The authorization can be configured with Administrator rights by using the Component service management.

    1. Open the editor for component service (for example either via the Microsoft Management Console or by running comexp.msc).

    1. In the console tree navigate to Console Root > Component Services > Computers > My Computer > DCOM Config.
    2. Select EClientService from the list.
    3. Open the properties of the component service.
    4. Open the Security tab.
    5. Mark the option Customize in the Launch and Activation Permission section.
    6. Open the Launch and Activation Permission via [Edit...].
    7. Use [Add User or Group...] to add the user.
    8. Select the Allow check box under Local Launch and Local Activation.
    9. Confirm the settings with [OK].

#### [](javascript:void\(0\);)[Creating and configuring the license default setting file](javascript:void\(0\);)

In order to start the EEC as a service you require a default setting file for the license selection. This can be created with the familiar license selection dialog.

    1. Start the ec.exe file so that the license selection dialog is opened. By default the [Shift] key is kept pressed at the same time.
    2. Select Network license > Create default setting file....
    3. Enter a name for the default setting file.
    4. Select a valid license.
    5. Confirm with [Save].
    6. Abort the launching process.
    7. The path to this default setting file is entered in the ec.ini file (see [de.eplan.eec.licenseFile](admin_r_vmargs_licensefile.htm)): -Dde.eplan.eec.licenseFile=<EEC installation folder>/license.lis

#### [](javascript:void\(0\);)[Configuring EEC headless](javascript:void\(0\);)

The following configuration setting is only for the operation of the job server without interface (see [de.eplan.eec.headless](admin_r_vmargs_headless.htm)).

    1. Open the initialization file (for example ec.ini) with a suitable editor.
    2. Insert the following line below the entry -vmargs:
    
        -Dde.eplan.eec.headless=true

    1. Save the initialization file.

#### [](javascript:void\(0\);)[Installation and start of the Windows service](javascript:void\(0\);)

A PowerShell script _installService.ps1 is available in the directory <EEC installation folder>\install\service for the installation of the Windows service.

    1. Run the script for example by using the following command line call with Administrator rights:
        
                powershell -ExecutionPolicy ByPass .\_installService.ps1

In the process the script creates the required EventLog source EEC, installs the service and starts it. A dialog for querying the user is opened.

    1. Enter the user with which the service is to be executed.

The PowerShell script _uninstallService.ps1 that is executed analog is used to remove the service. The EventLog source is not removed in the process.

### Note

A further log file is available for the analysis of problems during the service start. The storage location can be specified in the configuration file ec.exe.config.

In addition, error messages are also logged in the event log of the host computer.
