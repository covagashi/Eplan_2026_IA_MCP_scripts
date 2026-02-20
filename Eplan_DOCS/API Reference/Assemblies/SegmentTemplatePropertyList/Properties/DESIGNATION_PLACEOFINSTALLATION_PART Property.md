# DESIGNATION_PLACEOFINSTALLATION_PART Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1074.html

---

Basic segment definition: Displayed name # 44042.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_BASEDEFINITIONDISPLAYNAME {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_BASEDEFINITIONDISPLAYNAME {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

This property is read-only..

Displayed name of the basic segment definition, e.g., "Structure segment" or "Planning object".
