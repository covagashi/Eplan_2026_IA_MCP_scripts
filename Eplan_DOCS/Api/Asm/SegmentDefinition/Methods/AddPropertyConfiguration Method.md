# AddPropertyConfiguration Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinition~AddPropertyConfiguration.html

---

Adds new property configuration for given user defined property definition.

Syntax

**C#**



public PropertyConfiguration AddPropertyConfiguration( 

   UserDefinedPropertyDefinition pPropertyDef

)

public:

PropertyConfiguration^ AddPropertyConfiguration( 

   UserDefinedPropertyDefinition^ pPropertyDef

)


#### Parameters

*pPropertyDef*
:   User defined property definition for which configuration is beening added. Can't be `null`.

#### Return Value

Property configuration for given user defined property definition.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown if any of parameters is `null`. |

Remarks

If property configuration for given property id already exists then it is rewrite with new one.
