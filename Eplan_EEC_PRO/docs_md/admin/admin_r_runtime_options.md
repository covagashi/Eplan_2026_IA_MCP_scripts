---
title: "Runtime options"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_runtime_options.htm"
file: "admin_r_runtime_options"
category: "admin"
---

# Runtime options

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Runtime options

The following figure explains the EEC initialization process:

The main application of EEC is ec.exe, which is located in the EEC installation folder. The main program does not contain any program logic. It ensures the Windows-compliant calling of Eclipse (exe file, display of the application icon when switching with ALT-Tab, etc.).

The ec.exe file starts the Java Virtual Machine (VM) via the program javaw.exe.

The ec.exe file transfers the VM arguments, which are called VMArgs. On the one hand, VMArgs control the VMâs behavior, for example, the maximum RAM. On the other hand, arguments can be transferred to the VM that are interpreted by the application running in the VM (in this case, the EEC).

Eclipse underlying the EEC defines the Eclipse arguments, which control ec.exe, for example, for enabling or disabling the Welcome screen, but which are largely transferred to the VM during the booting of the platform.

Eclipse arguments and VMArgs are transferred to ec.exe for initialization. The effects of the VMArgs placed on the running application can be checked in the running EEC:

    1. Click Help > About Eplan Engineering Configuration > Installation Details > Configuration.

The transfer of the Eclipse arguments and VMArgs to ec.exe is based on the default Eclipse mechanisms. Two mechanisms are supported for the specification of the parameters:

    1. Transfer via batch file.
    2. Initialization file (ec.ini).

### [Initialization by means of a batch file](javascript:void\(0\);)

Three possibilities are available for the initialization of a batch file:

    1. A specific initialization file that contains the specific runtime parameters is named in the batch file.
    2. All the relevant runtime parameters are specified in the batch file. This creates a temporary initialization file for the transfer.
    3. In the batch file an initialization file is specified that contains general runtime parameters which are supplemented by further specifications in the batch file.

### Note

Only the following runtime parameters are supported for initialization via batch file:
    
        --launcher
    -data

### [Input options](javascript:void\(0\);)
    
        @start ec.exe^
    -<Parameter1> <Parameter value1>^
    -<Parameter2>
    -<Parameter3> <Parameter value3>

Remarks:

     * For a better view, the parameters are shown line by line.
     * For the transfer to ec.exe, the line breaks are canceled by the character ^, so that all parameters are in one line from the view of ec.exe.
     * The ^ character removes the line break, which creates the risk that, for example, a parameter value at the end of a line may be linked directly with a parameter of the following line, thus being transferred to ec.exe as a string. A useful way to ensure that a blank is always inserted is to generally start lines with parameters with a blank.
     * Caution: The last line must not contain the ^ character.

### Note

The last line must not contain the ^ character.

### Note

The @ character prevents the console output, which also prevents the console window in addition to the EEC).

### [Example with specific initialization file](javascript:void\(0\);)
    
        @echo off
    ec.exe --launcher.ini D:\Projects\Project1.ini

### [Example with specific runtime parameters](javascript:void\(0\);)
    
        @echo off
    set EEC_PATH=E:\Users\Public\EPLAN\EngineeringConfiguration\2_7_20170621-2047
    set EOX=eox\model.eox
    set EEC=ec.exe
    set WORKSPACE=workspace
    set RESOURCES=resources
    
    pushd %cd%
    cd /d %~dp0
    set dp0_s=%dp0:\=/%
    
    echo -startup > ec.ini
    echo --launcher.library >> ec.ini
    echo -product >> ec.ini
    echo de.eplan.engineeringcenter.product >> ec.ini
    echo -data >> ec.ini
    echo %WORKSPACE% >> ec.ini
    echo -vmargs >> ec.ini
    echo -XX:MaxPermSize=128m >> ec.ini
    echo -Xmx768m >> ec.ini
    echo -Dorg.foederal.sn.connectionURL=eox:///%dp0_s%%EOX%?mode=rw >> ec.ini
    echo -Dde.eplan.eec.global.resourcePath=%dp0_s%%RESOURCES% >> ec.ini
    echo -Dosgi.configuration.cascaded=false >> ec.ini
    echo -Dosgi.nl=en_US >> ec.ini
    cd /d %EEC_PATH% 
    start %EEC% --launcher.ini %dp0%\ec.ini
    popd

### [Example with initialization file supplemented by specific runtime parameters](javascript:void\(0\);)

The initialization file ec_Project1.ini:
    
        -startup 
    --launcher.library 
    -product 
    de.eplan.engineeringcenter.product 
    -data 
    workspace 
    -vmargs 
    -XX:MaxPermSize=128m 
    -Xmx768m

The batch file with runtime parameters:
    
        @echo off
    set EEC_PATH=E:\Users\Public\EPLAN\EngineeringConfiguration\2_7_20170621-2047
    set EOX=eox\model.eox
    
    pushd %cd%
    cd /d %~dp0
    set dp0_s=%dp0:\=/%
    
    copy ec_Project1.ini ec.ini
    
    echo -startup >> ec.ini
    echo -Dorg.foederal.sn.connectionURL=eox:///%dp0_s%%EOX%?mode=rw >> ec.ini
    echo -Dde.eplan.eec.global.resourcePath=%dp0_s%%RESOURCES% >> ec.ini
    echo -Dosgi.configuration.cascaded=false >> ec.ini
    echo -Dosgi.nl=en_US >> ec.ini
    cd /d %EEC_PATH% 
    start %EEC% --launcher.ini %dp0%\ec.ini
    popd

### [Ini file initialization](javascript:void\(0\);)

The Eclipse arguments and VMArgs are specified in an initialization file (for example ec.ini).

The initialization file has the following format:

### [Example](javascript:void\(0\);)
    
        -<Parameter1>
    <Parameter value1> # Comment      
    -<Parameter2>
    -<Parameter3>
    <Parameter value3>
    <...>

Conditions:

     * There is only one parameter per line, which means that blanks in the parameter do not pose a problem.
     * If a parameter has a value, it will be in the following line
     * Lines with a leading blank, as well as empty lines are ignored.
     * Comments are at the end of the line, and start with a #.

### [Example](javascript:void\(0\);)
    
        -data #user data folder
    workspace-user1
    -showlocation
    -pluginCustomization
    configuration\userCustomization.ini
