# IsMainFunction Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~IsMainFunction.html

---

Gets/Sets a flag which indicates a main function of the device.

Syntax

**C#**



public bool IsMainFunction {get; set;}

public:

property bool IsMainFunction {

   bool get();

   void set (    bool value);

}


Exceptions

| Exception | Description |
| --- | --- |
| [System.InvalidOperationException](#) | Thrown when this property is being modified on a non covered function template. |

Remarks

\* A device in a project may consist of more than one functions cross-referenced together by their device tag (i.e. the device's name). Non-main functions in the device are called 'auxiliary' functions. \* Only main functions of a device can have article information (i.e. article references).
