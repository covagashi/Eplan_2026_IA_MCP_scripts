# Registration

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Registration.html

---

## Manual registration of an add-on

Start Eplan now. In ribbon item File > Extras > Interfaces you will find the category Add-ons > Manage.

*Figure 1: Ribbon option Add-ons*

After clicking on Manage, a dialog ' as shown below ' will appear. By pressing the button  you can select the  install.xml  file from the  CFG  directory.

*Figure 2: Manual registration of an add-on*

The add-on now appears in the add-on list. To register it, you have to check the corresponding check-box in the "Registered" column. Only then will the DLL file stored in the  BIN  folder appear in the list of the API modules dialog and will be loaded.

### Registration of an add-on via an action

It is also possible to register an add-on via an action call. This is based on automatic actions for the Eplan command line functionalities ' also called "command line actions".

Tip:

For further information about "[Automatic actions](AutomaticActions.html)" see our API Help.

For the proper use of that command line action, it is necessary to pass further general command line parameters.

|  |  |
| --- | --- |
| **Parameter** | **Description** |
| Path | The path where the add-on is located |
| InstallFile | The complete path to the  install.xml |

Example:

Registering Add-ons:

XSettingsRegisterAction /Path:c:\MyAddOn

XSettingsRegisterAction /InstallFile: c:\MyAddOn\CFG\Install.xml

After registering the add-on via an action call, you have to verify if the add-on is registered in the add-ons dialog and the belonging add-in files are loaded.

## Automatic registration of an add-on

There are two ways to initiate the automatic registration of an add-on when Eplan is started.

### Automatic registration with registry settings

In the Registry Editor ' see figure 3 ' all Eplan installation can be found at:

HKEY\_LOCAL\_MACHINE / SOFTWARE / EPLAN / EPLAN W3

*Figure 3: Automatic registration with registry settings in the Registry Editor*

An add-on can be found like this:

<Add-on>

<Version>

Autoreg            TRUE

XMLPath            C:\Program Files\EPLAN\ApiTest Add-on\2.9.0\Cfg\install.xml

Autoreg: When this flag is "TRUE", the add-on can register automatically.

XMLPath: The path to  install.xml  of the add-on.

After double clicking on  Autoreg, a dialog ' as shown below ' will appear.

*Figure 4: Value editor*

Now you can set the value for the automatic registration to "TRUE" or "FALSE".

### Automatic registration with company settings

Start Eplan now. Select the ribbon item File and select the option Settings'¦.

*Figure 5: Option Settings...*

After clicking on Settings..., the settings service dialog ' as shown below ' will appear. By navigating to Company > Management > Add-ons you can then register a server path to Eplan.

*Figure 6: Settings: Add-ons*

At the startup of Eplan, this folder is searched for  install.xml  files. When an add-on  install.xml  is found (this means the  install.xml  is in the  CFG  folder, the version matches, etc.), the add-on will be registered.