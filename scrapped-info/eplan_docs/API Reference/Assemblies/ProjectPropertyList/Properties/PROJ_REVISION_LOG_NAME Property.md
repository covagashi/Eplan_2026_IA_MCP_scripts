# PROJ_REVISION_LOG_NAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISION_LOG_NAME(Int32).html

---

Revision name (change tracking) # 10155.

Syntax

**C#**



public PropertyValue PROJ_REVISION_LOG_NAME( 

   int index

) {get; set;}

public:

property PropertyValue^ PROJ_REVISION_LOG_NAME {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Revision name (change tracking), max. 1,000 possible.
