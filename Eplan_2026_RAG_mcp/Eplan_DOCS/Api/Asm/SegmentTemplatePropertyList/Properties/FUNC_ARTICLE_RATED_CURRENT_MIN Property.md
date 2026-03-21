# FUNC_ARTICLE_RATED_CURRENT_MIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1243.html

---

Nominal drive torque # 26467.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_RATED_DRIVING_TORQUE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_RATED_DRIVING_TORQUE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Maximum torque that a motor drive can continuously output to the drive shaft without overloading or damage occurring. The torque is specified in Newton meters (Nm).
