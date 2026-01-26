# ReSubstitutePath(String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.PathMap~ReSubstitutePath(String,String).html

---

Substitute values with variable strVariableName. Returns the changed path.

Syntax

**C#**



public static string ReSubstitutePath( 

   string strVariableName,

   string strPath

)

public:

static String^ ReSubstitutePath( 

   String^ strVariableName,

   String^ strPath

)


#### Parameters

*strVariableName*
:   Indicates the name of the variable. The variable has to be passed without P8 variable pointing marks - $().

*strPath*
:   Path to be analyzed.

Exceptions

| Exception | Description |
| --- | --- |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Method failed. |
