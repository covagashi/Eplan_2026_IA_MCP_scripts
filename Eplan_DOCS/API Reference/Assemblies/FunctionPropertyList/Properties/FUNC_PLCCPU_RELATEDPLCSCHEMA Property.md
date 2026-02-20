# FUNC_PLCCPU_RELATEDPLCSCHEMA Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCCPU_RELATEDPLCSCHEMA().html

---

PLC-specific settings # 20315.

Syntax

**C#**



public PropertyValue FUNC_PLCCPU_RELATEDPLCSCHEMA {get; set;}

public:

property PropertyValue^ FUNC_PLCCPU_RELATEDPLCSCHEMA {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Displays the PLC scheme that is used with a specific CPU. Functions of a specific CPU are processed under consideration of the PLC scheme belonging to this CPU (PLC addressing, import / export of assignment lists, etc.). The value of this property can only be assigned or changed if the PLC box is the main function and the CPU (ID 20167) property is activated.
