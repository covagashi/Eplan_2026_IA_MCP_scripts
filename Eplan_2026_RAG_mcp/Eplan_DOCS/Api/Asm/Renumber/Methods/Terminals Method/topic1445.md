# Terminals(Project,TerminalsSequence,TerminalsPotential,TerminalsPotential,TerminalsPotential,MultipleTerminals,TerminalsWithAlphabeticalCharacters,String,Int32,Int32,String,String,Boolean,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1445.html

---

Method for renumbering terminals specified by the collection pFunctions.

Syntax

**C#**



public void Terminals( 

   Project pProject,

   Renumber.Enums.TerminalsSequence eSequence,

   Renumber.Enums.TerminalsPotential ePotential_N,

   Renumber.Enums.TerminalsPotential ePotential_PE,

   Renumber.Enums.TerminalsPotential ePotential_SH,

   Renumber.Enums.MultipleTerminals eMultipleTerminals,

   Renumber.Enums.TerminalsWithAlphabeticalCharacters eTerminalsWithAlphabeticalCharacters,

   string strScheme,

   int nStartValue,

   int nIncrement,

   string strPrefix,

   string strSufix,

   bool bOnlyNumberMarkedOnes,

   bool bAlsoNumberedByPLC

)

public:

void Terminals( 

   Project^ pProject,

   Renumber.Enums.TerminalsSequence eSequence,

   Renumber.Enums.TerminalsPotential ePotential_N,

   Renumber.Enums.TerminalsPotential ePotential_PE,

   Renumber.Enums.TerminalsPotential ePotential_SH,

   Renumber.Enums.MultipleTerminals eMultipleTerminals,

   Renumber.Enums.TerminalsWithAlphabeticalCharacters eTerminalsWithAlphabeticalCharacters,

   String^ strScheme,

   int nStartValue,

   int nIncrement,

   String^ strPrefix,

   String^ strSufix,

   bool bOnlyNumberMarkedOnes,

   bool bAlsoNumberedByPLC

)


#### Parameters

*pProject*
:   Project in which all terminals will be renumbered.

*eSequence*
:   Mode to use for numbering, given by a member of enum TerminalsSequence.

*ePotential\_N*
:   Parameter to determine, N terminals will be treated during numbering. Use value from enum [Renumber.Enums.TerminalsPotential](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Renumber+Enums+TerminalsPotential.html).

*ePotential\_PE*
:   Parameter to determine, how PE terminals will be treated during numbering. Use value from enum [Renumber.Enums.TerminalsPotential](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Renumber+Enums+TerminalsPotential.html).

*ePotential\_SH*
:   Parameter to determine, how SH terminals will be treated during numbering. Use value from enum [Renumber.Enums.TerminalsPotential](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Renumber+Enums+TerminalsPotential.html).

*eMultipleTerminals*
:   Parameter enum for numbering terminals with "Allow same designations" property .

*eTerminalsWithAlphabeticalCharacters*
:   Parameter enum how terminals or pins with alphabetical elements in the designation should be numbered.

*strScheme*
:   Numbering scheme.

*nStartValue*
:   Start value.

*nIncrement*
:   Step width.

*strPrefix*
:   The prefix value that comes before the numbering value. Is only used if scheme is set to "According to online numbering format".

*strSufix*
:   The suffix value that comes after the numbering value. Is only used if scheme is set to "According to online numbering format".

*bOnlyNumberMarkedOnes*
:   I true - Terminals / pins whose designations contain a "?" will be numbered .

*bAlsoNumberedByPLC*
:   If true - terminals / pins controlled by PLCs will also be numbered.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown, if an argument is set to null. |
| **ArgumentException** | Thrown in case of invalid parameters, e.g. the specified functions do not exist or are invalid. |
| **ApplicationException** | Internal interface for numbering could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during numbering. |
| **InvalidScheme** | An error occurrs when used scheme name doesn't exist |
