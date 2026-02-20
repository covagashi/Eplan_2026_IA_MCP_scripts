# ImportData(Project,String,String,String,Boolean,PlanningSegment,Boolean,Boolean,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1405.html

---

Imports lists with pre-planning data that were created in external applications.

Syntax

**C#**



public bool ImportData( 

   Project pProject,

   string strFileName,

   string strScheme,

   string strAdditionalParameter,

   bool bSkipHeader,

   PlanningSegment pSegmentPlanning,

   bool bIgnoreErrors,

   bool bOverwrite,

   bool bUpdateOnly

)

public:

bool ImportData( 

   Project^ pProject,

   String^ strFileName,

   String^ strScheme,

   String^ strAdditionalParameter,

   bool bSkipHeader,

   PlanningSegment^ pSegmentPlanning,

   bool bIgnoreErrors,

   bool bOverwrite,

   bool bUpdateOnly

)


#### Parameters

*pProject*
:   Project to which file will be imported. Can't be `null`.

*strFileName*
:   Full file name of source file. Can't be `null` or `empty`.

*strScheme*
:   Name of the scheme that defines the assignment of the external data fields to the EPLAN properties. Can't be `null` or `empty`.

*strAdditionalParameter*
:   Additional parameter used by import routine.

*bSkipHeader*
:   If `true` then column names from the data table are output in the `External field` Used only for import from excel file.

*pSegmentPlanning*
:   Object below which the imported data are to be inserted. If `null` then data are inserted under project.

*bIgnoreErrors*
:   If `true` the import will not be aborted because of errors and messages that occur.

*bOverwrite*
:   If `true` then existing planning objects will be overwritten with the data from the planning objects of the same name from the import file. If `false` then existing planning objects remain unchanged.

*bUpdateOnly*
:   If `true` then only data of existing structure segments and planning objects will be updated.

#### Return Value

Returns `true` if import is successful.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Null was set to `pProject` parameter. |
| [System.ArgumentException](#) | Thrown when `strFileName` or `strScheme`of `null` or `empty`. |

Remarks

Import can be done from excel or text file. If import is done from excel file then additional parameter is interpreted as name of table or data area contained in the data source. In case when import is done from text file then additional parameter is treated to determine the separator that is used in the text file in order to separate the columns.
