# ImportSymbolLibrary Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Masterdata~ImportSymbolLibrary.html

---

Imports symbol library

Syntax

**C#**



public void ImportSymbolLibrary( 

   string strSource,

   string strDestination

)

public:

void ImportSymbolLibrary( 

   String^ strSource,

   String^ strDestination

)


#### Parameters

*strSource*
:   Path to \*.esl file which should be imported

*strDestination*
:   Path to \*.slk file where symbol library should be stored

Remarks

Import symbol library. When under destination path already some symbol library exists, it will be deleted.
