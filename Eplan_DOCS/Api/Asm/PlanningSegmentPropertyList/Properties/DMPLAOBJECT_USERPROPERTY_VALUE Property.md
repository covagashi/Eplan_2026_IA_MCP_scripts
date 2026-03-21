# DMPLAOBJECT_USERPROPERTY_VALUE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic867.html

---

Reception volume # 26224.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_ABSORPTION_VOLUME( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_ABSORPTION_VOLUME {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Volume which a container or a device can receive for collecting a specific amount of fluids or materials. This is relevant for the capacity and storage of materials.
