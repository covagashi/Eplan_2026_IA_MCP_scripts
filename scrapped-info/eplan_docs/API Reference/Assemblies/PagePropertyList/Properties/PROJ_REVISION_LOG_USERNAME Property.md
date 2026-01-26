# PROJ_REVISION_LOG_USERNAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PROJ_REVISION_LOG_USERNAME(Int32).html

---

User name (change tracking) # 10191.

Syntax

**C#**



public PropertyValue PROJ_REVISION_LOG_USERNAME( 

   int index

) {get; set;}

public:

property PropertyValue^ PROJ_REVISION_LOG_USERNAME {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Shows the user name that was specified in the user settings.
