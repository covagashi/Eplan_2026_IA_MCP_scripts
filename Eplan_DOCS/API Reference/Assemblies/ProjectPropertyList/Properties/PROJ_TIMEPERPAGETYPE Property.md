# PROJ_TIMEPERPAGETYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_TIMEPERPAGETYPE(Int32).html

---

Last modification time per page type # 10251.

Syntax

**C#**



public PropertyValue PROJ_TIMEPERPAGETYPE( 

   int index

) {get; set;}

public:

property PropertyValue^ PROJ_TIMEPERPAGETYPE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 50.

Provides the last modification time of the pages in the project for each page type. The page type is specified via the index (in the help system in the "Page types" section). The time representation can be configured in the project settings. The time is output in the local time of the user in accordance with the set time zone.
