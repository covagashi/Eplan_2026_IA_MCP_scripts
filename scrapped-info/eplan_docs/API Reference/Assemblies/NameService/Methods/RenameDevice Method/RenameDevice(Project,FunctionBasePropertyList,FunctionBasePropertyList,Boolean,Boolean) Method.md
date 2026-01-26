# RenameDevice(Project,FunctionBasePropertyList,FunctionBasePropertyList,Boolean,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1387.html

---

Rename all functions of device.

Syntax

**C#**



public void RenameDevice( 

   Project pProject,

   FunctionBasePropertyList pOldName,

   FunctionBasePropertyList pNewName,

   bool bRenameCDPsAlso,

   bool bKeepDescribingProps

)

public:

void RenameDevice( 

   Project^ pProject,

   FunctionBasePropertyList^ pOldName,

   FunctionBasePropertyList^ pNewName,

   bool bRenameCDPsAlso,

   bool bKeepDescribingProps

)


#### Parameters

*pProject*
:   Project for which functions of device will be renamed.

*pOldName*
:   List of name properties of device that functions will be renamed. Device without DT cannot be renamed so this list cannot be empty. Device must exist otherwise method throws exception.

*pNewName*
:   List of name properties that will be set to functions of device, can be empty.

*bRenameCDPsAlso*
:   If `true` then connection of this device (example: wires of cable) also will be renamed.

*bKeepDescribingProps*
:   IF `true` then describing properties of functions will not be changed.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when cannot find device from pOldName or trying to rename device without DT. |
| [System.ArgumentNullException](#) | Null was passed to a parameter. |
