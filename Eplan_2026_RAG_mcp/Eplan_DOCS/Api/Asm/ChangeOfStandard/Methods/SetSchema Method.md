# SetSchema Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ChangeOfStandard~SetSchema.html

---

Set mapping scheme.

Syntax

**C#**



public void SetSchema( 

   string schemaName,

   string sourceLibraryName,

   string targetLibraryName

)

public:

void SetSchema( 

   String^ schemaName,

   String^ sourceLibraryName,

   String^ targetLibraryName

)


#### Parameters

*schemaName*
:   Name of scheme to be set

*sourceLibraryName*
:   Name of source library

*targetLibraryName*
:   Name of target library

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurs during setting a scheme mapping. |

Remarks

Method sets mapping scheme for given libraries. All libraries mappings should be first set by this method before performing [TransformObjects:Eplan::EplApi::HEServices::ChangeOfStandards:](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ChangeOfStandard~TransformObjects.html). Without it symbols won't be changed. To find the correct scheme for mapping from `sourceLibraryName` to `targetLibraryName`, use [GetMatchingSymbolMappingSchemas:Eplan::EplApi::HEServices::ChangeOfStandards:](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ChangeOfStandard~GetMatchingSymbolMappingSchemas.html).
