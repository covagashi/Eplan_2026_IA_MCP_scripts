# ARTICLE_NOMINAL_VOLUME_FLOW Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~ARTICLE_NOMINAL_VOLUME_FLOW().html

---

Nominal flow rate # 26506.

Syntax

**C#**



public PropertyValue ARTICLE_NOMINAL_VOLUME_FLOW {get; set;}

public:

property PropertyValue^ ARTICLE_NOMINAL_VOLUME_FLOW {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Flow rate measured under defined nominal conditions. These are the conditions for which a device was designed with regard to its application when it is not under load. The nominal flow rate indicates how many volumes of a medium (e.g., air, water) flow through a system or a component per unit of time. These are usually specified in cubic meters per hour (m³/h) or liters per minute (l/min).
