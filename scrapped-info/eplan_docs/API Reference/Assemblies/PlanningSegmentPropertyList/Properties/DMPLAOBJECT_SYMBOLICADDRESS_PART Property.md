# DMPLAOBJECT_SYMBOLICADDRESS_PART Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic864.html

---

Technical description # 44006.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_TECHNICAL_DESCRIPTION {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_TECHNICAL_DESCRIPTION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

You can enter any characteristic and particular features (multi-lingual). Is used for output in reports.

Example: Three-phase motor 11 kW; star-delta control; one direction.
