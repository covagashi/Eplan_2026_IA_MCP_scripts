# PROJ_REVISION_LOG_DATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISION_LOG_DATE(Int32).html

---

Revision date (change tracking) # 10158.

Syntax

**C#**



public PropertyValue PROJ_REVISION_LOG_DATE( 

   int index

) {get; set;}

public:

property PropertyValue^ PROJ_REVISION_LOG_DATE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.DateTime.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Revision date (change tracking), max. 1,000 allowed. The time is output in the local time of the user in accordance with the set time zone.
