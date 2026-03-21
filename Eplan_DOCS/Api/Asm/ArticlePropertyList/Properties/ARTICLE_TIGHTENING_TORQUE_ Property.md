# ARTICLE_TIGHTENING_TORQUE_ Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TIGHTENING_TORQUE_().html

---

Tightening torque # 26080.

Syntax

**C#**



public PropertyValue ARTICLE_TIGHTENING_TORQUE_ {get; set;}

public:

property PropertyValue^ ARTICLE_TIGHTENING_TORQUE_ {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Value of the tightening torque, specified in Newton meters. Describes the force with which, for example, a screw is tightened, meaning the force that acts from the drive on the output. This property applies to the entire part. You can find connection point-specific properties in the connection point pattern.
