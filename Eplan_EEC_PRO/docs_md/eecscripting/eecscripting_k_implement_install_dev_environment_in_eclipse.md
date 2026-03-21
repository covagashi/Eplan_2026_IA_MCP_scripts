---
title: "Installing the Eclipse development environment"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecscripting_k_implement_install_dev_environment_in_eclipse.htm"
file: "eecscripting_k_implement_install_dev_environment_in_eclipse"
category: "eecscripting"
---

# Installing the Eclipse development environment

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Installing the Eclipse development environment Eclipse cannot be installed unless the workstation has access to JRE or JDK in the current version. The Eclipse installation file is available on the following website: [ https://www.eclipse.org/downloads ](https://www.eclipse.org/downloads).
    1. Download the Eclipse IDE (Eclipse IDE for RCP and RAP Developers).
    2. Install the Eclipse. To do this follow the instructions of the installation wizard.
The specification against which target you are compiling is required for the development of the plug-in.
    1. Launch Eclipse.
    2. In the Workspace Launcher dialog, enter the desired folder for the workspace data.
    3. Open the settings in Window > Preferences.
    4. Navigate to Plug-in Development > Target Platform.
    5. To create a new target platform, click [Add...].
The New Target Definition wizard opens with the Target Definition dialog.
    1. Select Nothing: Start with an empty target definition (Standard).
    2. Confirm with [Next >].
The New Target Definition wizard switches to the Target Content dialog.
    1. Enter any name for the target platform definition in the Project Name field. It is recommended to select a name, that can be assigned to the current EEC version.
    2. Click Add... to add the location where plug-ins should be saved.
The New Target Definition wizard switches to the Add Content wizard.
    1. Select Directory.
    2. Confirm with [Next >].
    1. Enter the installation directory of EEC in the Location field.
    2. Close the wizard by clicking [Finish].
You return to the New Target Definition wizard with the Target Content dialog. The new target has now been entered.
    1. Open the Environment tab.
    2. In the Architecture field, select x86_64.
    3. End the process by clicking [Finish].
You return to the settings for the Target Platform.
    1. Select the new target definition in order to activate it.
    1. Navigate to Java > Installed JREs.
    2. Ensure that the JRE or JDK in the current version is entered and is selected as the standard VM (see [Software and hardware requirements](admin_r_it_reqs_software.htm)). Alternatively an entry in the initialization file can be created (eclipse.ini).
    
        -vm
    <EEC installation folder>jre/bin/javaw.exe

    1. Close the settings by clicking [OK].
As a result Eclipse has been installed successfully in the development environment and the settings have been set.
