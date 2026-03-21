# ARTICLE_PLCTYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCTYPE().html

---

PLC type designation # 22105.

Syntax

**C#**



public PropertyValue ARTICLE_PLCTYPE {get; set;}

public:

property PropertyValue^ ARTICLE_PLCTYPE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. PLC type designation of a PLC card. The part allocation during the import of PLC configuration files is carried out on the basis of this property (in as far as no device description file is specified). The entry has to be carried out in exactly the same notation as in the hardware catalog of the manufacturer. In the simplest case the PLC type designation corresponds to the order number. During a part selection or device selection the property is filled with the corresponding value from the parts management. The property is transferred to the main function at a part selection or device selection.
