# DMPLAOBJECT_DOCUMENTS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplatePropertyList~DMPLAOBJECT_DOCUMENTS(Int32).html

---

Documents # 44007.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_DOCUMENTS( 

   int index

) {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_DOCUMENTS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 20.

Any external documents can be stored at a planning object or structure segment. You can output these documents in the reports as hyperlinks.
