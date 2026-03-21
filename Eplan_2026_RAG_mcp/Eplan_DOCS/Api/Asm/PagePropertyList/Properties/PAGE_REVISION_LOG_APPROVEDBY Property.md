# PAGE_REVISION_LOG_APPROVEDBY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_REVISION_LOG_APPROVEDBY(Int32).html

---

Revision: Approved by (change tracking) # 11087.

Syntax

**C#**



public PropertyValue PAGE_REVISION_LOG_APPROVEDBY( 

   int index

) {get; set;}

public:

property PropertyValue^ PAGE_REVISION_LOG_APPROVEDBY {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Shows the editor who has checked the revision. This property can be entered in the Edit revision data dialog; it is not translatable. The index corresponds to the revision index, max. 1000 entries are possible.
