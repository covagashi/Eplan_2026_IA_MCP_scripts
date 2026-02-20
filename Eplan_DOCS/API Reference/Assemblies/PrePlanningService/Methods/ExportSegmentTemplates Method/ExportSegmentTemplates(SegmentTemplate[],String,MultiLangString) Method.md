# ExportSegmentTemplates(SegmentTemplate[],String,MultiLangString) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1403.html

---

Exports segment templates to file.

Syntax

**C#**



public bool ExportSegmentTemplates( 

   SegmentTemplate[] arrTemplates,

   string strFileName,

   MultiLangString mlsDescription

)

public:

bool ExportSegmentTemplates( 

   array<SegmentTemplate^>^ arrTemplates,

   String^ strFileName,

   MultiLangString^ mlsDescription

)


#### Parameters

*arrTemplates*
:   Array of segment template to export. Can't be `null`.

*strFileName*
:   Full file name of target file. Can't be `null` or `empty`.

*mlsDescription*
:   Description which is contained in exported file.

#### Return Value

Returns `true` if export is successful.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when parameter `arrTemplates` is a `null` value. |
| [System.ArgumentException](#) | Thrown when `strFileName` of `null` or `empty`. |
