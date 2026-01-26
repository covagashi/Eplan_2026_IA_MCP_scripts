# SetProjectLanguage

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/SetProjectLanguage.html

---

```
 Sets project languages for read-write and read-only projects.

```

| Parameter | Description |
| --- | --- |
| ``` PROJECTNAME
 ``` | ``` Full project name. The project has to be open.
 ``` |
| ``` DISPLAY
 ``` | ``` Displayed language ID(s) (e.g. "de_DE" for German).
  If more than one displayed language is specified, the values are separated by ";".
 ``` |
| ``` VARIABLE
 ``` | ``` Variable project language. Can be set via language ID (e.g. "de_DE" for German)
  or displayed language index (e.g. "03_03" for the "Displayed language 3").
  The last described method only works for the first 5 displayed languages (so for this method "05_05" is the maximum value).
 ``` |
| ``` SOURCE
 ``` | ``` Source language
 ``` |

**Remarks**

```
  The action does not translate the strings, it just changes the display settings.

```

**Example**

```
SetProjectLanguage /DISPLAY:en_US;de_DE /VARIABLE:en_US

 Set the project language to the "Displayed language 4" (which is set to French):

   SetProjectLanguage /DISPLAY:en_US;de_DE;pl_PL;fr_FR /VARIABLE:04_04

```