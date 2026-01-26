# PAGE_REVISION_LOG_DATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_REVISION_LOG_DATE(Int32).html

---

Revision date (change tracking) # 11074.

Syntax

**C#**



public PropertyValue PAGE_REVISION_LOG_DATE( 

   int index

) {get; set;}

public:

property PropertyValue^ PAGE_REVISION_LOG_DATE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.DateTime.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Date on which a change was carried out within a revision. A max. of 1,000 allowed. The time is output in the local time of the user in accordance with the set time zone.
