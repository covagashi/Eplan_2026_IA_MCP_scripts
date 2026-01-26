# ARTICLE_TIGHTENING_TORQUE_MIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TIGHTENING_TORQUE_MIN().html

---

Tightening torque, min. # 26082.

Syntax

**C#**



public PropertyValue ARTICLE_TIGHTENING_TORQUE_MIN {get; set;}

public:

property PropertyValue^ ARTICLE_TIGHTENING_TORQUE_MIN {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Minimal value of the tightening torque. It is specified in Newton meters. It describes the force with which, for example, a screw is tightened, meaning the force that acts from the drive on the socket. This property applies to the entire part. You can find connection point-specific properties in the connection point pattern.
