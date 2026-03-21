# FUNCTEMPLATE_CONNPT_DESCRIPTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1504.html

---

Connection point descriptions # 21007.

Syntax

**C#**



public MDPropertyValue FUNCTEMPLATE_CONNPT_DESCRIPTION( 

   int index

) {get; set;}

public:

property MDPropertyValue^ FUNCTEMPLATE_CONNPT_DESCRIPTION {

   MDPropertyValue^ get(int index);

   void set (int index, MDPropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.
