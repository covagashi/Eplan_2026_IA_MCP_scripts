# FUNC_CABLING_CP_ADDITIONAL_LENGTH Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_CABLING_CP_ADDITIONAL_LENGTH().html

---

Topology: Connection point extra length # 20241.

Syntax

**C#**



public PropertyValue FUNC_CABLING_CP_ADDITIONAL_LENGTH {get; set;}

public:

property PropertyValue^ FUNC_CABLING_CP_ADDITIONAL_LENGTH {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Additonal value that is added to the length of a connection one time. Here, for example, the length of the last routing point to the item can be entered. This information is taken into account during the route of a cable, and indicates by how much the cable is to protrude from the cable duct.
