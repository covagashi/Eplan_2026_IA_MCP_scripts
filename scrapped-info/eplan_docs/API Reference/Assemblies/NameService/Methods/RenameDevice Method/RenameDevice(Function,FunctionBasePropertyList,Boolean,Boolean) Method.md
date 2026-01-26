# RenameDevice(Function,FunctionBasePropertyList,Boolean,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1388.html

---

Rename all functions of device.

Syntax

**C#**



public void RenameDevice( 

   Function pFunction,

   FunctionBasePropertyList pNewName,

   bool bRenameCDPsAlso,

   bool bKeepDescribingProps

)

public:

void RenameDevice( 

   Function^ pFunction,

   FunctionBasePropertyList^ pNewName,

   bool bRenameCDPsAlso,

   bool bKeepDescribingProps

)


#### Parameters

*pFunction*
:   Function from device which name will be changed.

*pNewName*
:   Name that will be set to functions of device.

*bRenameCDPsAlso*
:   If `true` then connection of this device (example: wires of cable) also will be renamed.

*bKeepDescribingProps*
:   IF `true` then describing properties of functions will not be changed.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Invalid parameters were found. |
| [System.ArgumentNullException](#) | Null was passed to a parameter. |
