# PAGE_REVISION_LOG_PROJ_REVNAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic485.html

---

Associated revision name (change tracking) # 11077.

Syntax

**C#**



public PropertyValue PAGE_REVISION_LOG_PROJ_REVNAME( 

   int index

) {get; set;}

public:

property PropertyValue^ PAGE_REVISION_LOG_PROJ_REVNAME {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

Outputs the name of the associated project revision (from change tracking) on a page; max. 1,000 entries are allowed.
