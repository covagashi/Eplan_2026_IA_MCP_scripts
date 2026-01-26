# MergeWithNode Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~MergeWithNode.html

---

Merges settings nodes.

Syntax

**C#**



public bool MergeWithNode( 

   SettingNode oSettingNode

)

public:

bool MergeWithNode( 

   SettingNode^ oSettingNode

)


#### Parameters

*oSettingNode*
:   Indicates the settings node to be merged with this one.

#### Return Value

True: Operation was successful.

False: Operation failed.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | The value of the parameter object is NULL. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The object has not been initialized correctly. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The function failed. |

Remarks

All Settings nodes and Settings of oSettingNode are added to this node. Existing settings are NOT overwritten.
