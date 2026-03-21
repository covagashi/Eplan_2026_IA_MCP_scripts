# FUNC_ARTICLE_INRUSH_CURRENT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1172.html

---

Mounting length # 26276.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_INSTALLATION_LENGTH( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_INSTALLATION_LENGTH {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Total length (in mm) of the part of a device or component that is located within a container, for example the length of a sensor.
