# ReSubstitutePathForDisplay Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.PathMap~ReSubstitutePathForDisplay.html

---

Substitute values with variables. Returns the changed path. Ignores all variables which are not visible in P8 Dialogs.

Syntax

**C#**



public static string ReSubstitutePathForDisplay( 

   string strPath

)

public:

static String^ ReSubstitutePathForDisplay( 

   String^ strPath

)


#### Parameters

*strPath*
:   Path to be analyzed.

Exceptions

| Exception | Description |
| --- | --- |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Method failed. |
