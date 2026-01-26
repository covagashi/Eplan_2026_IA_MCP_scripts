# PROJ_REVISION_LOG_USERCODE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PROJ_REVISION_LOG_USERCODE(Int32).html

---

User code (change tracking) # 10190.

Syntax

**C#**



public PropertyValue PROJ_REVISION_LOG_USERCODE( 

   int index

) {get; set;}

public:

property PropertyValue^ PROJ_REVISION_LOG_USERCODE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Shows the user code that was specified in the user settings.
