# ExportSegmentTemplates(Project,String,MultiLangString) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1402.html

---

Exports all segment templates from project to file.

Syntax

**C#**



public bool ExportSegmentTemplates( 

   Project pProject,

   string strFileName,

   MultiLangString mlsDescription

)

public:

bool ExportSegmentTemplates( 

   Project^ pProject,

   String^ strFileName,

   MultiLangString^ mlsDescription

)


#### Parameters

*pProject*
:   Project from which all segment template are exported. Can't be `null`.

*strFileName*
:   Full file name of target file. Can't be `null` or `empty`.

*mlsDescription*
:   Description which is contained in exported file.

#### Return Value

Returns `true` if export is successful.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when parameter `pProject` is a `null` value. |
| [System.ArgumentException](#) | Thrown when `strFileName` of `null` or `empty`. |
