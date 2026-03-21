# DMPLAOBJECT_DEFINITIONDISPLAYNAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1076.html

---

Documents: Designation # 44069.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_DOCUMENTS_DESIGNATION( 

   int index

) {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_DOCUMENTS_DESIGNATION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 20.

Designation of an external document. Any external documents can be stored at a planning object or structure segment. You can output these documents in the reports as hyperlinks.
