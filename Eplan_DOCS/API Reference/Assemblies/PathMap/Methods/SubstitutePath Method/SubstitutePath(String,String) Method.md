# SubstitutePath(String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.PathMap~SubstitutePath(String,String).html

---

Substitutes variables with their values for a partuclar Project. Returns the changed path.

Syntax

**C#**



public static string SubstitutePath( 

   string strPath,

   string strProjectPath

)

public:

static String^ SubstitutePath( 

   String^ strPath,

   String^ strProjectPath

)


#### Parameters

*strPath*
:   Path to be analyzed

*strProjectPath*
:   Complete ProjectPath to be analyzed

Exceptions

| Exception | Description |
| --- | --- |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Method failed. |
