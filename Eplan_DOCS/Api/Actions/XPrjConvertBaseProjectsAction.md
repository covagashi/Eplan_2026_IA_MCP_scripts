# XPrjConvertBaseProjectsAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XPrjConvertBaseProjectsAction.html

---

```
 This action converts one ore more old basic projects (*.ept and *.epb files) to new basic projects (*.zw9).

 All basic projects in a folder are upgraded (recursively).

```

| Parameter | Description |
| --- | --- |
| ``` ProjectTemplate
 ``` | ``` Full *.ept or *.epb file name of the old basic project to be converted.
 ``` |
| ``` Folder
 ``` | ``` All basic projects in this folder and its subfolders are converted to *.zw9.
 ``` |
| ``` FileTypes
 ``` | ``` *.*: All old basic project formats (such as *.ept and *.epb) are converted.
 ``` |

**Remarks**

```
 Handle Folder:

 All *.ept and *.epb files are converted.

 See also chapter "Basic Projects instead of Project Templates" in the "News 2022" section of the EPLAN Platform Help.

```

**Example**

```
   Conversion of individual project templates:

                XPrjConvertBaseProjectsAction /ProjectTemplate:$(MD_TEMPLATES)\IEC_tpl001.ept

                XPrjConvertBaseProjectsAction /ProjectTemplate:$(MD_TEMPLATES)\GES_SBP.epb

   Conversion of all project templates in a directory:

                XPrjConvertBaseProjectsAction /Folder:$(MD_TEMPLATES)

   Conversion of specific file types in a directory:

                XPrjConvertBaseProjectsAction /Folder:$(MD_TEMPLATES) /FileTypes:*.ept

```