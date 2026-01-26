# ARTICLE_PIPECLASS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PipingDefinitionPropertyList~ARTICLE_PIPECLASS().html

---

Pipe class # 22224.

Syntax

**C#**



public PropertyValue ARTICLE_PIPECLASS {get; set;}

public:

property PropertyValue^ ARTICLE_PIPECLASS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. The pipe class specifies the range of application in relation to the pressure and temperature, meaning the maximum permissible pressure at which the piping may be operated at a maximum permissible temperature. When doing this, a pipe class contains a fixed number of pipe items, such as pipes, fittings, flanges, nuts, bolts, and gaskets.
