# backup

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/backup.html

---

```
Action class for backup functions. Backs up a project and master data (forms, symbols, ...) to disk

```

| Parameter | Description |
| --- | --- |
| ``` TYPE
 ``` | ``` Type of task to be performed.
 '¢ "PROJECT": Backing up the entire project. 
 '¢ "MASTERDATA": Backing up the master data.
 ``` |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional). 
 If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` ARCHIVENAME
 ``` | ``` Archive name.
 Name of the file where the backed up data is to be saved (without path information).
 ``` |
| ``` DESTINATIONPATH
 ``` | ``` Target directory
 ``` |
| ``` COMMENT
 ``` | ``` Remark on backup (optional).
 The remark is written as a string to the corresponding property of the backed up project.
 Default = corresponding property is not set.
 ``` |
| ``` AUTOCOPYREFDATA
 ``` | ``` Specifies whether external files that are referenced by the project 
 are copied to the project's directory (the "\DOC" and "\Images" subdirectories) before the backup.
 (optional, 0 = No, 1 = Yes).
 Default = 0
 Valid only if TYPE parameter equals "PROJECT".
 Images and documents included in project are always backup-ed.
 ``` |
| ``` INCLEXTDOCS
 ``` | ``` Specifies whether documents are to be included in the backup (optional, 0 = No, 1= Yes).
 Default = 0
 ``` |
| ``` INCLIMAGES
 ``` | ``` Specifies whether image files are to be included in the backup (optional, 0 = No, 1=Yes).
 Default = 0
 ``` |
| ``` BACKUPMETHOD
 ``` | ```  Type of backup. 
 '¢ "BACKUP": Project is backed up 
 '¢ "SOURCEOUT": Project is filed off 
 '¢ "ARCHIVE": Project is archived.
 ``` |
| ``` MDTYPE
 ``` | ``` Type of master data to be backed up.
 '¢ "SYMBOLS",
 '¢ "MACROS",
 '¢ "FORMS",
 '¢ "ARTICLES",
 '¢ "LANGUAGES",
 '¢ "STANDARDSHEET",
 '¢ "STATIONDATA"
 ``` |
| ``` SOURCEPATH
 ``` | ``` Source directory, only applies to backup of master data.
 ``` |
| ``` FILENAME
 ``` | ``` Name of the file to be backed up.
 '¢ The file name can be entered with or without the complete path.
 '¢ The file extension must be specified.
 '¢ A file extension with a wildcard is also possible (for example: /FILENAME:*.fn1, /FILENAME:*.*, /FILENAME:*sh)
 This only applies to the backup of master data.
 ``` |

**Remarks**

```
Archive names of the form <some name>.nnn (n = a digit 0 - 9) are forbidden, because an archive name of this form (with a three-digit-extension) is automatically created when the backup file is split into several parts. 

When an error occurs during a data backup operation, a "BaseException" is thrown.

```

**Example**

```
Backup project:

backup /TYPE:PROJECT /DESTINATIONPATH:U:\temp /ARCHIVENAME:EPLAN_Sample_Project.zw1 /AUTOCOPYREFDATA:0

backup /TYPE:PROJECT /DESTINATIONPATH:U:\temp /ARCHIVENAME:EPLAN_Sample_Project.zw1 /COMMENT:Hello /AUTOCOPYREFDATA:1 /INCLIMAGES:0 /INCLEXTDOCS:1

backup /TYPE:PROJECT /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /DESTINATIONPATH:U:\temp /ARCHIVENAME:EPLAN_Sample_Project.zw1 /COMMENT:Hello /BACKUPMETHOD:BACKUP 


Backup master data:

Backup plot frame with full path:

backup /TYPE:MASTERDATA /FILENAME:C:\PlotFrames\EPLAN\ESS_A3DP.fn1 /SOURCEPATH:C:\PlotFrames\EPLAN /DESTINATIONPATH:U:\temp /ARCHIVENAME:my_MasterData /COMMENT:"Hello world" /MDTYPE:STANDARDSHEET

Backup plot frame without full path:

backup /TYPE:MASTERDATA /FILENAME:ESS_A3DP.fn1 /SOURCEPATH:C:\PlotFrames\EPLAN /DESTINATIONPATH:U:\temp /ARCHIVENAME:my_MasterData /COMMENT:"Hello world" /MDTYPE:STANDARDSHEET

Backup all plot frames (*.fn1):

backup /TYPE:MASTERDATA /FILENAME:*.fn1 /SOURCEPATH:C:\PlotFrames\EPLAN /DESTINATIONPATH:U:\temp /ARCHIVENAME:my_MasterData /COMMENT:"Hello world" /MDTYPE:STANDARDSHEET

Backup all files (*.*) in specified source directory:

backup /TYPE:MASTERDATA /FILENAME:*.* /SOURCEPATH:C:\PlotFrames\EPLAN /DESTINATIONPATH:U:\temp /ARCHIVENAME:my_MasterData /COMMENT:"Hello world" /MDTYPE:STANDARDSHEET

Backup all files (*.*) in specified source directory whose file extensions include 'sh':

backup /TYPE:MASTERDATA /FILENAME:*sh /SOURCEPATH:C:\PlotFrames\EPLAN /DESTINATIONPATH:U:\temp /ARCHIVENAME:my_MasterData /COMMENT:"Hello world" /MDTYPE:STANDARDSHEET

```