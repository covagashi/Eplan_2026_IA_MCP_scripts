# MACROFILE_CHANGEDATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~MACROFILE_CHANGEDATE().html

---

Macro: Modification date # 23019.

Syntax

**C#**



public PropertyValue MACROFILE_CHANGEDATE {get; set;}

public:

property PropertyValue^ MACROFILE_CHANGEDATE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.DateTime.

Remarks

Shows the modification date of the macro file in the Insert center. After a macro has been inserted, the value of this property is not transferred to the page or the macro box and is empty. The time is output in the local time of the user in accordance with the set time zone.
