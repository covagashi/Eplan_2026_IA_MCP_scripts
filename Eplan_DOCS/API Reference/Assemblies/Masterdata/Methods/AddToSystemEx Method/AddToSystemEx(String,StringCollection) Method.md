# AddToSystemEx(String,StringCollection) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Masterdata~AddToSystemEx(String,StringCollection).html

---

Copies stored project master data into the system master data pool.

Syntax

**C#**



public Hashtable AddToSystemEx( 

   string strFullLinkFileName,

   StringCollection masterDataFiles

)

public:

Hashtable^ AddToSystemEx( 

   String^ strFullLinkFileName,

   StringCollection^ masterDataFiles

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project from which the data will be copied.

*masterDataFiles*
:   List of project master data files names to be copied. Files to add must exist in project library.

#### Return Value

Hashtable object with collection of errors. Key is a filename (as String) which was passed to `masterDataFiles` and value is a exception object (based on System::Exception). If all elements was processed correctly returned hastable is empty.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | A parameter was set to a null reference. |
| **ArgumentException** | Parameters are invalid, e.g. one (or more) of given file name(s) doesn't exist in project library. |
| **ApplicationException** | Internal interface for master data could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Master data could not be copied to the system master data pool. |

Remarks

Given link to project is used by **ProjectManager::OpenProject(System:** function. Exception provided by OpenProject() function may be also thrown.
