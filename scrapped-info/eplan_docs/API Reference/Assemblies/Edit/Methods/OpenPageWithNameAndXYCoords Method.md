# OpenPageWithNameAndXYCoords Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~OpenPageWithNameAndXYCoords.html

---

Opens the page with the name passed to strPageName and sets the cursor to the position defined by the X and Y coordinates.

Syntax

**C#**



public void OpenPageWithNameAndXYCoords( 

   string strFullLinkFileName,

   string strPageName,

   double nXCoord,

   double nYCoord

)

public:

void OpenPageWithNameAndXYCoords( 

   String^ strFullLinkFileName,

   String^ strPageName,

   double nXCoord,

   double nYCoord

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project.

*strPageName*
:   Name of the page to open.

*nXCoord*
:   X coordinate.

*nYCoord*
:   Y coordinate.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Is thrown in case of invalid parameters. |
| [System.ApplicationException](#) | The graphics editor interface could not be created. |
