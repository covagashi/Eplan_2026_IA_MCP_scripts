# Command line parameters

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Command line parameters.html

---

Here is a full list of parameters of the  EPLAN.exe  application.  
By default, it is installed in the  C:\Program Files\EPLAN\Platform\<version>\Bin  directory.

| Parameter | Description |
| --- | --- |
| ``` 
 Auto
 ``` | ``` 
 Eplan is shut down after executing the command line; it has no effects on showing dialogs or the mainframe. 
 ``` |
| ``` 
 Quiet
 ``` | ``` 
 Determines if dialogs are shown while a command line is executed:
  '¢ 0: all dialogs will be shown
  '¢ 1: no dialog will be shown (default)
  '¢ 2: only some special dialogs will be shown, e.g. progress bars
 ``` |
| ``` 
 NoLicenseDialog
 ``` | ``` 
 Turn off calling license dialog. 
 ``` |
| ``` 
 NoUserRightsDialog
 ``` | ``` 
 Turn off calling user rights dialog. If user rights check fails, Eplan application will terminate. This dialog will be shown per default if it is needed. 
 ``` |
| ``` 
 Frame
 ``` | ``` 
 Determines how the Eplan mainframe should be shown: 
  '¢ 0: Hides this window and passes activation to another window.
  '¢ 1: Activates and displays the window. If the window is minimized or maximized, Windows restores it to its original size and position.
  '¢ 2: Activates the window and displays it as an icon.
  '¢ 3: Activates the window and displays it as a maximized window.
  '¢ 4: Displays the window as an icon. The window that is currently active remains active.
  '¢ 5: Activates the window and displays it in its current size and position.
  '¢ 6: Minimizes the window and activates the top-level window in the system's list.
  '¢ 7: Displays the window as an icon. The window that is currently active remains active.
  '¢ 8: Displays the window in its current state. The window that is currently active remains active.
  '¢ 9: Activates and displays the window. If the window is minimized or maximized, Windows restores it to its original size and position. 
 ``` |
| ``` 
 Setup
 ``` | ``` 
 Determines if default settings should be used:
  '¢ 0: USER, STATION, COMPANY settings are restored to their installation default (on file level) and databases are backed (default)
  '¢ 8: the actual adjusted settings will be used (on file level) ONLY FOR INTERNAL USE!
  '¢ category (USER or STATION or COMPANY) is denoted: settings of that category are restored to their installation default (on file level) and the database is backed
  '¢ path: all settings below this location will be deleted and then reloaded from the reference database, but only when more than the category is denoted
  '¢ nobackup: same as setup:0, but no backup of the databases.
 ``` |
| ``` 
 SetupRestore
 ``` | ``` 
 Determines if settings should be restored from last database backup (default: 0): 
  '¢ 0: USER, STATION, COMPANY settings are restored from their last backup (on file level)
  '¢ category (USER or STATION or COMPANY) is denoted: settings of that category are restored from their last backup (on file level)
 ``` |
| ``` 
 User
 ``` | ``` 
 Eplan login user. Settings will be used from this user.
  As value for this parameter please enter the user name.
 ``` |
| ``` 
 Password
 ``` | ``` 
 Eplan login password used for user rights.
  As value for this parameter please enter the user password.
 ``` |
| ``` 
 Station
 ``` | ``` 
 Settings will be used from another station.
  As value for this parameter please enter the station name
 ``` |
| ``` 
 Company
 ``` | ``` 
 Settings will be used from another company.
  As value for this parameter please enter the company name.
 ``` |
| ``` 
 NoLoadWorkspace
 ``` | ``` 
 No workspace is loaded or restored. 
 ``` |
| ``` 
 NoSplash
 ``` | ``` 
 No splash screen is shown on system start. 
 ``` |
| ``` 
 NoRemoting
 ``` | ``` 
 No Eplan Remoting functionalities are available. 
  For more information, please refer to the "Eplan Remoting" chapter. 
 ``` |
| ``` 
 EplanServerPort
 ``` | ``` 
 Set the gRPC server to a specific port number. The port should be in the range: 49152 - 65535. 
  If not set explicitly, the port number is set automatically (taking the first available port from the specified range). It is recommended to set the port manually. 
  For more information, please refer to the "Eplan Remoting" chapter. 
 ``` |
| ``` 
 Language
 ``` | ``` 
 Eplan will be started with chosen GUI language. The language predefined in the settings of Eplan will not be changed.
  As value for this parameter please enter the chosen language (e.g. "de_DE" or "en_US").
 ``` |
| ``` 
 PathsScheme
 ``` | ``` 
 Sets scheme of directories' paths, e.g. "/PathsScheme:PredefinedPathScheme". If a chosen scheme does not exist, the default scheme is used. 
 ``` |
| ``` 
 autoRegAddon
 ``` | ``` 
 New installed add-ons will be registered at startup.
  Possible values: "true" or "false"
 ``` |
| ``` 
 License
 ``` | ``` 
 Name of the file containing the license to use or to borrow ("*.lis")
  As value for this parameter please enter the filename  of the "*.lis" file.
 ``` |
| ``` 
 ReturnLicense
 ``` | ``` 
 Return the borrowed license. The parameter is the name of the file containing the borrowed license. This same file used by "/license"
  As value for this parameter please enter the filename  of the "*.lis" file.
 ``` |
| ``` 
 RequestOfflineLicense
 ``` | ``` 
 Create the request file to borrow license offline ("*.egr"). The parameter is the name of the file containing the license to borrow ("*.lis")
  As value for this parameter please enter the filename  of the "*.lis" file.
 ``` |
| ``` 
 OfflineLicense
 ``` | ``` 
 Use the file containing the borrowed license which is converted from a confirmation file. The parameter is the name of the file containing the license to borrow ("*.lis")
  As value for this parameter please enter the filename  of the "*.lis" file.
 ``` |
| ``` 
 SystemConfiguration
 ``` | ``` 
 Set system configuration scheme.
  As value for this parameter please enter the scheme name of system configuration.
 ``` |
| ``` 
 Variant
 ``` | ``` 
 Product name. It is used to call an Eplan platform-based product:
  '¢ "Electric P8" 
  '¢ Fluid
  '¢ FluidMan
  '¢ ProPanel
  '¢ PPE
  '¢ View
  '¢ CPM
  '¢ FHC
  '¢ Education
  '¢ Trial
 ``` |
| ``` 
 VariantSharedEplDir
 ``` | ``` 
 Product name directory. This is an alternative way of setting product name to "Variant" parameter, for example "C:\\Program Files\\EPLAN\\Preplanning\\<version>"
 ``` |
| ``` 
 AttachDebugger
 ``` | ``` 
 Attach debugger to execution of Eplan.
 ``` |
| ``` 
 WebService
 ``` | ``` 
 Starts a webservice on the specific URL.
  As value for this parameter please enter the URL for the service
 ``` |
| ``` 
 RestartOnCrash
 ``` | ``` 
 Restart Eplan after a crash occurred.
 ``` |
| ``` 
 UseLastOpenedProjects
 ``` | ``` 
 Determines if last opened projects should be opened on start:
  '¢ 0: No projects will be opened.
  '¢ 1: Last used projects will be opened.
  '¢ 2: Last used projects will be opened if no action is passed. Otherwise (i.e. with action parameter), no projects are opened (default).
 ``` |
| ``` 
 <action name>
 ``` | ``` 
 Action that should be executed, all following parameters (starting with "/" or "'") are passed to the action as parameters. 
 ``` |

**Remarks**

```


 By default, when starting P8 from command line with an action, no previously opened projects are opened at the beginning of the session.

 If your installation path is different from the default ("C:\Program Files\EPLAN\Platform\<version>\Bin"), you must modify the code samples below accordingly.

 "<version>" must be replaced with the correct Eplan version, e.g. "2026.0.3" for version 2026.

```

**Example**

```

 "C:\\Program Files\\EPLAN\\Platform\\<version>\\Bin\\EPLAN.exe" /variant:"Electric P8"

 "C:\\Program Files\\EPLAN\\Platform\\<version>\\Bin\\EPLAN.exe" action /Param1:wert1 /Param2:wert2 /Param3

 "C:\\Program Files\\EPLAN\\Platform\\<version>\\Bin\\EPLAN.exe" /Setup:SS_USER_WORKSPACE_NAMED_PATH

 "C:\\Program Files\\EPLAN\\Platform\\<version>\\Bin\\EPLAN.exe" /User:UserXYZ

 "C:\\Program Files\\EPLAN\\Platform\\<version>\\Bin\\EPLAN.exe" /NoLoadWorkspace action /Param1:wert1

 "C:\\Program Files\\EPLAN\\Platform\\<version>\\Bin\\EPLAN.exe" /Language:en_us

 "C:\\Program Files\\EPLAN\\Platform\\<version>\\Bin\\EPLAN.exe" /Auto /Quiet /Frame:2 AnotherAction /ActionPar

 If the license dialog is needed, the flag "NoLicenseDialog" disables calling it.

 "C:\\Program Files\\EPLAN\\Platform\\<version>\\Bin\\EPLAN.exe" /NoLicenseDialog action /Param1:wert1 /Param2:wert2

 If no user rights dialog is needed, the flag "NoUserRightsDialog" disables calling it. If user rights check fails, Eplan application will terminate.

 "C:\\Program Files\\EPLAN\\Platform\\<version>\\Bin\\EPLAN.exe" /NoUserRightsDialog action /Param1:wert1 /Param2:wert2

 Use or borrow a License defined in "myLicense.lis". In "myLicense.lis" you can define a product variant and License modules to use or to borrow for a period of time.

 "C:\\Program Files\\EPLAN\\Platform\\<version>\\Bin\\EPLAN.exe" /License:"D:\\myLicense.lis"

 Return a license

 "C:\\Program Files\\EPLAN\\Platform\\<version>\\Bin\\EPLAN.exe" /ReturnLicense:"D:\\myLicense.lis"

 Request a license file

 "C:\\Program Files\\EPLAN\\Platform\\<version>\\Bin\\EPLAN.exe" /RequestOfflineLicense:"D:\\myLicense.lis"

 Use a license offline

 "C:\\Program Files\\EPLAN\\Platform\\<version>\\Bin\\EPLAN.exe" /OfflineLicense:"D:\\myLicense.lis"

 Use 49200 as port number for the gRPC server (API Remoting)

 "C:\\Program Files\\EPLAN\\Platform\\<version>\\Bin\\EPLAN.exe" /EplanServerPort:49200

```