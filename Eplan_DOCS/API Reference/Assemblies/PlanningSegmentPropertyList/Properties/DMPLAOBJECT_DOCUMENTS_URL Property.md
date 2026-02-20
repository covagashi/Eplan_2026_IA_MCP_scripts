# DMPLAOBJECT_DOCUMENTS_URL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~DMPLAOBJECT_DOCUMENTS_URL(Int32).html

---

Documents: File / hyperlink # 44068.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_DOCUMENTS_URL( 

   int index

) {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_DOCUMENTS_URL {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 20.

File name or hyperlink of an external document. Any external documents can be stored at a planning object or structure segment. You can output these documents in the reports as hyperlinks.
