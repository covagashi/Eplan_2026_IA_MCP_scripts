# PROJ_REVISION_LOG_TIME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISION_LOG_TIME(Int32).html

---

Revision time (change tracking) # 10159.

Syntax

**C#**



public PropertyValue PROJ_REVISION_LOG_TIME( 

   int index

) {get; set;}

public:

property PropertyValue^ PROJ_REVISION_LOG_TIME {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

Time when a project was changed during a revision. The time display can be specified in the project settings. A max. of 1,000 records allowed. The time is output in the local time of the user in accordance with the set time zone.
