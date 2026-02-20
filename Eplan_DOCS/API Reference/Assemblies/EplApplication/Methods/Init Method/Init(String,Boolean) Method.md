# Init(String,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~Init(String,Boolean).html

---

Initializes the Eplan runtime system.

Syntax

**C#**



public void Init( 

   string strApplicationModifier,

   bool bAllowCallingLicenseDialog

)

public:

void Init( 

   String^ strApplicationModifier,

   bool bAllowCallingLicenseDialog

)


#### Parameters

*strApplicationModifier*
:   This parameter specifies which configuration is to be initialized.

*bAllowCallingLicenseDialog*
:   This parameter specifies whether the license dialog is allowed to be called.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when a problem with licenses appears. |

Remarks

Offline applications require to be Single-Threaded because of COM which are used by P8. Therefore, for example Main() function has to be declared with attribute [STAThread]. Please see MSDN or Google for more information about STAThread. Calling this method changes the current culture (default format for dates, times and numbers) used by the thread to the culture in the GUI.
