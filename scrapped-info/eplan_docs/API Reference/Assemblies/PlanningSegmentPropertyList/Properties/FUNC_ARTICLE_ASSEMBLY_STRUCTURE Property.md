# FUNC_ARTICLE_ASSEMBLY_STRUCTURE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic886.html

---

Assembly variant # 20923.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_ASSEMBLYVARIANT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_ASSEMBLYVARIANT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.
