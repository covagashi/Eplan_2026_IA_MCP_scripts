# ARTICLE_TIGHTENING_TORQUE_MAX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_TIGHTENING_TORQUE_MAX().html

---

Tightening torque, max. # 26081.

Syntax

**C#**



public MDPropertyValue ARTICLE_TIGHTENING_TORQUE_MAX {get; set;}

public:

property MDPropertyValue^ ARTICLE_TIGHTENING_TORQUE_MAX {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Maximal value of the tightening torque. It is specified in Newton meters. It describes the force with which, for example, a screw is tightened, meaning the force that acts from the drive on the socket. This property applies to the entire part. You can find connection point-specific properties in the connection point pattern.
