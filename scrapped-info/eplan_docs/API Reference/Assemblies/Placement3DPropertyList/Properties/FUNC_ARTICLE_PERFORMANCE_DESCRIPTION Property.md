# FUNC_ARTICLE_PERFORMANCE_DESCRIPTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic567.html

---

Performance description, standardized: Description (device, utility, service) # 26426.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_PERFORMANCE_DESCRIPTION( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_PERFORMANCE_DESCRIPTION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

In the context of the standardized performance description, this is the descriptive text of the performance description for a device, a utility or a service.
