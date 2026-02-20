# Plugs(Project,PlugsSequence,TerminalsPotential,TerminalsPotential,TerminalsPotential,Boolean,String,Int32,Int32) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1441.html

---

Method for renumbering plugs of a project.

Syntax

**C#**



public void Plugs( 

   Project pProject,

   Renumber.Enums.PlugsSequence eSequence,

   Renumber.Enums.TerminalsPotential ePotential_N,

   Renumber.Enums.TerminalsPotential ePotential_PE,

   Renumber.Enums.TerminalsPotential ePotential_SH,

   bool bKeepAlphanumeric,

   string strScheme,

   int nStartValue,

   int nIncrement

)

public:

void Plugs( 

   Project^ pProject,

   Renumber.Enums.PlugsSequence eSequence,

   Renumber.Enums.TerminalsPotential ePotential_N,

   Renumber.Enums.TerminalsPotential ePotential_PE,

   Renumber.Enums.TerminalsPotential ePotential_SH,

   bool bKeepAlphanumeric,

   String^ strScheme,

   int nStartValue,

   int nIncrement

)


#### Parameters

*pProject*
:   Project in which all plugs will be renumbered.

*eSequence*
:   Mode to use for numbering, given by a member of enum PlugSequence.

*ePotential\_N*
:   Parameter to determine, N plugs will be treated during numbering. Use value from enum [Renumber.Enums.TerminalsPotential](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Renumber+Enums+TerminalsPotential.html).

*ePotential\_PE*
:   Parameter to determine, how PE plugs will be treated during numbering. Use value from enum [Renumber.Enums.TerminalsPotential](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Renumber+Enums+TerminalsPotential.html).

*ePotential\_SH*
:   Parameter to determine, how SH plugs will be treated during numbering. Use value from enum [Renumber.Enums.TerminalsPotential](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Renumber+Enums+TerminalsPotential.html).

*bKeepAlphanumeric*
:   Keep alphabetic components of the device number.

*strScheme*
:   Numbering scheme.

*nStartValue*
:   Start value.

*nIncrement*
:   Step width.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown, if an argument is set to null. |
| **ArgumentException** | Thrown in case of invalid parameters, e.g. the specified project does not exist or is invalid. |
| **ApplicationException** | \Internal interface for numbering could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during numbering. |
| **InvalidScheme** | An error occurrs when used scheme name doesn't exist |
