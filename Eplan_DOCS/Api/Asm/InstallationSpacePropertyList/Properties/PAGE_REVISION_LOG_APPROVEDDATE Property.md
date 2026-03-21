# PAGE_REVISION_LOG_APPROVEDDATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic484.html

---

Revision: Approved date (change tracking) # 11088.

Syntax

**C#**



public PropertyValue PAGE_REVISION_LOG_APPROVEDDATE( 

   int index

) {get; set;}

public:

property PropertyValue^ PAGE_REVISION_LOG_APPROVEDDATE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.DateTime.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Shows date and time of checking the revision. This property can be entered in the Edit revision data dialog. The index corresponds to the revision index, max. 1,000 entries are possible.
