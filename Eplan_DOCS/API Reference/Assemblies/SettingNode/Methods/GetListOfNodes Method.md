# GetListOfNodes Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~GetListOfNodes.html

---

Determines all settings nodes.

Syntax

**C#**



public virtual void GetListOfNodes( 

   ref StringCollection colOfNodes,

   bool bAbsolutPath

)

public:

virtual void GetListOfNodes( 

   StringCollection^% colOfNodes,

   bool bAbsolutPath

)


#### Parameters

*colOfNodes*
:   Container to which existing settings nodes are output.

*bAbsolutPath*
:   Controls the output:

    True: Path of settings is absolute.

    False: Relative paths of settings are output.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | The value of the parameter object is NULL. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The object has not been initialized correctly. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The function failed. |
