# FUNC_ARTICLE_MASS_MOMENT_OF_INERTIA_OF_THE_LOAD Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic553.html

---

Mass moment of inertia of the load # 26444.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_MASS_MOMENT_OF_INERTIA_OF_THE_LOAD( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_MASS_MOMENT_OF_INERTIA_OF_THE_LOAD {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Describes the resistance of a load to changes in its rotation around an axis. This is a measure of how difficult it is to change the rotational speed of the load and depends on the mass distribution of the load relative to the axis of rotation. Example: In the case of a rotating flywheel in a machine, the mass moment of inertia indicates the torque required to change the rotational speed of the flywheel.
