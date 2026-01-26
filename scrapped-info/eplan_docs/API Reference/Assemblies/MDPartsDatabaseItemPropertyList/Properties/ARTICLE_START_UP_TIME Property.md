# ARTICLE_START_UP_TIME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_START_UP_TIME().html

---

Switch-on time # 26192.

Syntax

**C#**



public MDPropertyValue ARTICLE_START_UP_TIME {get; set;}

public:

property MDPropertyValue^ ARTICLE_START_UP_TIME {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Time interval which has elapsed between the application of the control signal (electrical or pneumatic) and the pressure increase at the corresponding valve outlet until 10% of the specified working pressure is reached.
