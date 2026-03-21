# AddToProjectEx(Project,StringCollection) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Masterdata~AddToProjectEx(Project,StringCollection).html

---

Method for storing system master data in the project.

Syntax

**C#**



public Hashtable AddToProjectEx( 

   Project oProject,

   StringCollection masterDataFiles

)

public:

Hashtable^ AddToProjectEx( 

   Project^ oProject,

   StringCollection^ masterDataFiles

)


#### Parameters

*oProject*
:   Project into which the master data will be copied.

*masterDataFiles*
:   List of master data files names to be added to the project. Files have to be placed in special paths of EPLAN P8 and no paths can be used, only file names. These paths are depended on files types which are recognized only by file name extension. For example forms files, with \file name extention '.f25', have to be placed in directory pointed by [Eplan.EplApi.DataModel.PathInfo.Forms](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PathInfo~Forms.html) (also [Eplan.EplApi.Base.PathMap](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PathMap.html) can be used with `$(MD_FORMS)`.

#### Return Value

Hashtable object with collection of errors. Key is a filename (as String) which was passed to `masterDataFiles` and value is a exception object (based on System::Exception). If all elements was processed correctly returned hastable is empty.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | A parameter was set to a null reference. |
| **ArgumentException** | \Parameters are invalid, e.g. the set project does not exist or is invalid. |
| **ApplicationException** | \Internal interface for master data could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Master data could not be stored in the project. |
