# Connections(Page[],Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Generate~Connections(Page[],Boolean).html

---

Updates connections on given pages from one project. Project is taken from first page.

Syntax

**C#**



public void Connections( 

   Page[] arrayPages,

   bool bRebuildAllConnections

)

public:

void Connections( 

   array<Page^>^ arrayPages,

   bool bRebuildAllConnections

)


#### Parameters

*arrayPages*
:   Pages with connections to update.

*bRebuildAllConnections*
:   If true rebuilds all connections else updates only.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid project. |
| **ApplicationException** | The internal interface for generating connections could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during connection generation. Please refer to the exception message. |
