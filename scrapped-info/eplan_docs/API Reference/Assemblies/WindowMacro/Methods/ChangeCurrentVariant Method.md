# ChangeCurrentVariant Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~ChangeCurrentVariant.html

---

Change current representation type and variant of macro This function is more efficient as changing the Properties RepresentationType and Variant separately besides, this function throws an exception, if the variant does not exist

Syntax

**C#**



public void ChangeCurrentVariant( 

   WindowMacro.Enums.RepresentationType nRepType,

   int nVariant

)

public:

void ChangeCurrentVariant( 

   WindowMacro.Enums.RepresentationType nRepType,

   int nVariant

)


#### Parameters

*nRepType*
:   Input parameter - Representation Type

*nVariant*
:   Input parameter - Variant id

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when parameters are not valid. p.e. a wrong Representation type or variant. |
