# XMImportDCArticleDataAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XMImportDCArticleDataAction.html

---

```
 Imports a data configuration file into an existing EPLAN article database.

```

| Parameter | Description |
| --- | --- |
| ``` DATACONFIGURATIONFILE
 ``` | ``` Path of data configuration file.
 ``` |
| ``` PROGRESSTITLE
 ``` | ``` Defines the progress title (optional).
 ``` |
| ``` SHOWIMPORTMESSAGES
 ``` | ``` Determines whether an information dialog is shown (optional).
  0 = "no information dialog (with count of added parts) is shown", 1 = "information dialog is shown" (default value).
  
 ``` |
| ``` IMPORTMODE
 ``` | ``` Determines whether to create new objects or to only update existing ones (optional).
  0 = only create new objects,
  1 = only update objects,
  2 = create new and update objects
  If not entered, objects are updated and if new objects are in the list, a question dialog comes up, if new objects should be created.
  
 ``` |
| ``` IDENTIFYBYNAMEINSTEADOFID
 ``` | ``` Determines whether objects are identified by name instead of ID (optional).
  Possible values: 0 = "objects are identified by ID", 1 = "objects are identified by name instead"
  If not entered, objects are identified by object ID.
 
  These 2 modes are meant for different workflows/use-cases:
  If you export data from the parts management, change them and import them into the same parts database, then identifying the objects by object ID is the right mechanism for identification and it is possible to change the identifying name of the objects (for example the part number).
  If you want to import data from a different data source, for example a file generated from a connection to an ERP system, you usually don't have an object ID of EPLAN. In this case, use the identifying name to import the data.
  If you import by name, you still need to specify part of the object ID in the first column - the type of the object, to define if the data contains for example a part, an address or an accessory list.
  The supported main types are:
  117 = part
  156 = drilling pattern
  157 = connection point pattern
  213 = accessory list
  226 = accessory placement
  135 = address
  The import supports not only main types, but also their subtypes. Since they have no identifying name, but are identified as subobjects of the main object, they have to be defined in the second column in the format "99 (117:99/1)", where the first 99 is the subtype and in brackets is the relation: Containing a main object, the relation and its index.
  So "99 (117:99/1)" means that it is a function template (first 99), and is related to a part (117), where it is the first index in the parts function templates. Sub-objects must follow main objects in the imported file.
  Valid subtypes are:
  For a part:
  99  = function template
  85  = module/assembly position
  224 = drilling patterns
  215 = accessory
  242 = safety related values
  For a drilling pattern:
  158 = cut-out
  For a connection point pattern:
  159 = connection point
  For an accessory list:
  214 = accessory list entry
  For an accessory placement:
  227 = accessory placement entry
  
 ``` |

**Remarks**

```
 This allows the properties of articles to be changed.

 The data configuration file can be created e.g. via the Backstage view "File > Export > Project data > External editing > Properties"

```

**Example**

```
        XMImportDCArticleDataAction /DataConfigurationFile:c:\\EPLAN\\DataCfgFile.edc

```