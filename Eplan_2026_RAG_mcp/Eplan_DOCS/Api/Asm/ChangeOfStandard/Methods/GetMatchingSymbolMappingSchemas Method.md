# GetMatchingSymbolMappingSchemas Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ChangeOfStandard~GetMatchingSymbolMappingSchemas.html

---

Gets symbol scheme names for given symbol libraries mapping.

Syntax

**C#**



public string[] GetMatchingSymbolMappingSchemas( 

   string sourceLibraryName,

   string targetLibraryName

)

public:

array<String^>^ GetMatchingSymbolMappingSchemas( 

   String^ sourceLibraryName,

   String^ targetLibraryName

)


#### Parameters

*sourceLibraryName*
:   Name of source library

*targetLibraryName*
:   Name of target library

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurs during reading the data. |

Remarks

Method allows to find correct schemes for mapping from `sourceLibraryName` to `targetLibraryName`.
