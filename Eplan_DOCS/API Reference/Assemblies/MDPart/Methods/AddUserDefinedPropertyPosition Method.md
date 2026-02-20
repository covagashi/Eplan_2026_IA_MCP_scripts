# AddUserDefinedPropertyPosition Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~AddUserDefinedPropertyPosition.html

---

Adds a new UserDefinedPropertyPosition object to the part. It is added to the end of the parts UserDefinedPropertyPositions list.

Syntax

**C#**



public MDUserDefinedPropertyPosition AddUserDefinedPropertyPosition( 

   MDUserDefinedPropertyDefinition userDefinedPropertyDefinition

)

public:

MDUserDefinedPropertyPosition^ AddUserDefinedPropertyPosition( 

   MDUserDefinedPropertyDefinition^ userDefinedPropertyDefinition

)


#### Parameters

*userDefinedPropertyDefinition*

#### Return Value

New added UserDefinedPropertyPosition object.

Exceptions

| Exception | Description |
| --- | --- |
| [MDInvalidArgumentException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDInvalidArgumentException.html) | Thrown if it is not possible to add the UserDefinedPropertyPosition object. |
