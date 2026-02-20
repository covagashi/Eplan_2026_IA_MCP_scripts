# ARTICLE_NOMINAL_VOLUME_FLOW Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_NOMINAL_VOLUME_FLOW().html

---

Nominal flow rate # 26506.

Syntax

**C#**



public MDPropertyValue ARTICLE_NOMINAL_VOLUME_FLOW {get; set;}

public:

property MDPropertyValue^ ARTICLE_NOMINAL_VOLUME_FLOW {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Flow rate measured under defined nominal conditions. These are the conditions for which a device was designed with regard to its application when it is not under load. The nominal flow rate indicates how many volumes of a medium (e.g., air, water) flow through a system or a component per unit of time. These are usually specified in cubic meters per hour (m³/h) or liters per minute (l/min).
