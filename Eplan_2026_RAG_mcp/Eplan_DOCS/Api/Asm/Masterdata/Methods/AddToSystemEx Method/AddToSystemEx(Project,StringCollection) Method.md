# AddToSystemEx(Project,StringCollection) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Masterdata~AddToSystemEx(Project,StringCollection).html

---

Extendent function for coping stored project master data into the system master data pool.

Syntax

**C#**



public Hashtable AddToSystemEx( 

   Project oProject,

   StringCollection masterDataFiles

)

public:

Hashtable^ AddToSystemEx( 

   Project^ oProject,

   StringCollection^ masterDataFiles

)


#### Parameters

*oProject*
:   Project from which the data will be copied.

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
|  | This exception might be returned for same item(s) when this item is correct but it cannot be processed because of other conditions. For example it is returned when masterdata database is locked for some items. |
| [Eplan.EplApi.DataModel.OperationCanceledException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OperationCanceledException.html) | This exception might be returned for some item(s) when user cancel operation. In this version canceling operation by API is not available. |
