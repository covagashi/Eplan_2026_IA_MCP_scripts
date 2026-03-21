# PROJ_REVISION_LOG_USEREMAIL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PROJ_REVISION_LOG_USEREMAIL(Int32).html

---

User: E-mail address (change tracking) # 10193.

Syntax

**C#**



public PropertyValue PROJ_REVISION_LOG_USEREMAIL( 

   int index

) {get; set;}

public:

property PropertyValue^ PROJ_REVISION_LOG_USEREMAIL {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Shows the e-mail address that was specified in the user settings.
