# translate

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/translate.html

---

```
Action class for translate functions: translate a project, export missing translation list, and remove languages from a project.

```

| Parameter | Description |
| --- | --- |
| ``` TYPE
 ``` | ``` Type of task to be performed by the action:
 '¢ "TRANSLATEPROJECT": Translate project
 '¢ "TRANSLATEPAGES": Translate given pages
 '¢ "REMOVELANGUAGE": Remove language entry
 '¢ "EXPORTMISSINGTRANSLATIONS": Export missing-word list
 '¢ "IMPORTTOTRANSDB": Import database texts
 '¢ "EXPORTFROMTRANSDB": Export database texts
 '¢ "CORRECT": Corrects translations
 ``` |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction (see also "XEsProjectAction") must be used first, otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` IMPORTFILE
 ``` | ``` Name of the file with texts to import. Only applies to the parameter TYPE equal to "IMPORTTOTRANSDB"
 ``` |
| ``` EXPORTFILE
 ``` | ``` Name of file containing exported missing word list. 
 This parameter is only effective with the TYPE equal to "EXPORTMISSINGTRANSLATIONS" or "EXPORTFROMTRANSDB"
 ``` |
| ``` CONVERTER
 ``` | ``` Name of converter (optional). This name is used as the input and output format.
 Default values:"XTrLanguageDbXmlConverterImpl" 
 (Native format XML) for TYPE equal to "EXPORTFROMTRANSDB", XTrLanguageDbXml2TabConverterImpl for "IMPORTTOTRANSDB" and "EXPORTMISSINGTRANSLATIONS"
 This parameter is only effective with the TYPE equal to "EXPORTMISSINGTRANSLATIONS", "IMPORTTOTRANSDB" or "EXPORTFROMTRANSDB"
 ``` |
| ``` LANGUAGE
 ``` | ``` Translation language, e.g., "fr_FR"
 ``` |
| ``` USEPAGEFILTER
 ``` | ``` Determines if only filtered pages should be used or all project pages (optional). It corresponds to "Active" check box in GUI. 
 These parameters are only effective with the "TRANSLATEPAGES" value of the TYPE parameter.
 Default value: 0 
 ``` |
| ``` PAGFILTERNAME
 ``` | ``` Pages are read from pagefilter with the name pagefiltername.These parameters are only effective with the "TRANSLATEPAGES" value of the TYPE parameter.
 ``` |
| ``` PAGENAME
 ``` | ``` Name of the page to be translated (optional).
 ``` |
| ``` PAGENAMEn
 ``` | ``` Names of the pages to be translated (optional), where n is a number e.g. /PAGENAME1:=AP+ST1/2 /PAGENAME2:=AP+ST1/4 /PAGENAME3:=AP+ST1/7 etc. 
 These parameters are only effective with the "TRANSLATEPAGES" value of the TYPE parameter.
 ``` |
| ``` SELn
 ``` | ``` Identifier of the pages to be translated (optional), where n is a number (e.g. /SEL1:38/4/12/0 (result from StorableObject.ToStringIdentifier())) 
 parameters are only effective with the "TRANSLATEPAGES" value of the TYPE parameter.
 ``` |
| ``` CONVERTTRANSLATEDTEXTS
 ``` | ``` Determines if already translated texts should be also converted. Default value: 0. This parameter is only effective with the TYPE equal to "CORRECT".
 ``` |

**Remarks**

```
The main language of a project cannot be removed from it. 

If several languages are to be removed from the project, they must be entered individually, separated by comma, e.g., /LANGUAGE:en_US,fr_FR,da_DK

```

**Example**

```
Translate project

translate /TYPE:TRANSLATEPROJECT /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk


Import database texts

translate /TYPE:IMPORTTOTRANSDB  /CONVERTER:XTrLanguageDbXmlConverterImpl  /IMPORTFILE:c:\test\TranslationDB_FULL.etd /LANGUAGE:de_DE


Remove translation from project:

translate /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk  /TYPE:REMOVELANGUAGE /LANGUAGE:en_US


Export missing-word list

translate /TYPE:EXPORTMISSINGTRANSLATIONS /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /LANGUAGE:en_US /EXPORTFILE:C:\temp\missingTransFile.txt /CONVERTER:XTrLanguageDbXmlConverterImpl

```