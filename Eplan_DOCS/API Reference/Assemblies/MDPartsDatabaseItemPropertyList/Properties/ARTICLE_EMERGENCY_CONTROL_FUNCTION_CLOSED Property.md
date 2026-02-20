# ARTICLE_EMERGENCY_CONTROL_FUNCTION_CLOSED Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1555.html

---

Emergency control function (closed) # 26054.

Syntax

**C#**



public MDPropertyValue ARTICLE_EMERGENCY_CONTROL_FUNCTION_CLOSED {get; set;}

public:

property MDPropertyValue^ ARTICLE_EMERGENCY_CONTROL_FUNCTION_CLOSED {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Safety function in which a device or system is brought into a closed position in the case of an emergency. Example: A spring return drive that automatically closes the valve in the event of a power failure.
