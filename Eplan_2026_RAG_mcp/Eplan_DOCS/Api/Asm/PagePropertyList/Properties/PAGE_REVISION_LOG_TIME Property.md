# PAGE_REVISION_LOG_TIME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_REVISION_LOG_TIME(Int32).html

---

Revision time (change tracking) # 11078.

Syntax

**C#**



public PropertyValue PAGE_REVISION_LOG_TIME( 

   int index

) {get; set;}

public:

property PropertyValue^ PAGE_REVISION_LOG_TIME {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

Time when a page was changed during a revision. The time display can be specified in the project settings. A max. of 1,000 allowed. The time is output in the local time of the user in accordance with the set time zone.
