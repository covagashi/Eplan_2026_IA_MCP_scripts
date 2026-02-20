# StoreExternalFilesOfCurrentVariant Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro~StoreExternalFilesOfCurrentVariant.html

---

Copies external files into project images directory

Syntax

**C#**



public void StoreExternalFilesOfCurrentVariant()

public:

void StoreExternalFilesOfCurrentVariant();


Remarks

The method could be necessary for example when inserting macro by windowMacro.Page.CopyTo method. In this case embedded files are skipped if they are not stored in project directory.
