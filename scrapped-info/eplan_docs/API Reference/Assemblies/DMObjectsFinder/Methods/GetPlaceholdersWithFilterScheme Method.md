# GetPlaceholdersWithFilterScheme Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPlaceholdersWithFilterScheme.html

---

Returns [Eplan.EplApi.DataModel.Graphics.PlaceHolder](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder.html)s matching given filter from placeholders-navigator.

Syntax

**C#**



public PlaceHolder[] GetPlaceholdersWithFilterScheme( 

   string strFilterScheme

)

public:

array<PlaceHolder^>^ GetPlaceholdersWithFilterScheme( 

   String^ strFilterScheme

)


#### Parameters

*strFilterScheme*
:   Scheme-name of filter placeholders-navigator

#### Return Value

\* If scheme-name is empty, the current filter scheme will be used. \* If scheme-name is null, the method returns elements that are visible if no filter scheme is used in a GUI navigator.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
| [System.ArgumentException](#) | Thrown if filter scheme does not exist. |
| [System.ArgumentNullException](#) | Thrown if strFilterScheme is set to null. |
