# PROJ_REVISION_LOG_USERPHONE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISION_LOG_USERPHONE(Int32).html

---

User: Phone number (change tracking) # 10192.

Syntax

**C#**



public PropertyValue PROJ_REVISION_LOG_USERPHONE( 

   int index

) {get; set;}

public:

property PropertyValue^ PROJ_REVISION_LOG_USERPHONE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Shows the phone number that was specified in the user settings.
