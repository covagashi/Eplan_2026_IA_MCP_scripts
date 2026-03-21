# InterpretAutomatically(Placement3D,String[],Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1395.html

---

Starts automatic interpretation.

Syntax

**C#**



public void InterpretAutomatically( 

   Placement3D oTarget,

   string[] arrMacrosToSearchForBestMach,

   bool bShowBestMachDlg

)

public:

void InterpretAutomatically( 

   Placement3D^ oTarget,

   array<String^>^ arrMacrosToSearchForBestMach,

   bool bShowBestMachDlg

)


#### Parameters

*oTarget*
:   3D placement for which automatic interpretation willl be started. Cannot be `null`.

*arrMacrosToSearchForBestMach*
:   Array of paths to macros from which the best mathing one will be searched for.

*bShowBestMachDlg*
:   Show best match dialog if true. In other case method selects best match automatically.

Example

Following example shows how to use the method:

**C#**

```
new Placement3DService().InterpretAutomatically(oInstallationTarget2.Children[0], arrMacrosFiles, false);

```
