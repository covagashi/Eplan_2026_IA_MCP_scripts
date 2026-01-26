# ArticleReference Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~ArticleReference.html

---

Sets the ArticleReference at the reference position of the ArticleReference.

Syntax

**C#**



public ArticleReference ArticleReference {set;}

public:

property ArticleReference^ ArticleReference {

   void set (    ArticleReference^ value);

}


Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the ArticleReference cannot be set |
| [System.ArgumentNullException](#) | Thrown when `articleRef` is `null`. |
| [FixedDeviceException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FixedDeviceException.html) | Thrown if [IsFixedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~IsFixedDevice.html) is true. |

Remarks

Stores the article in the project Stored the article reference data at the Function
