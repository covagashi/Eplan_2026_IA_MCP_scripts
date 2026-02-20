# XEsSetProjectPropertyAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XEsSetProjectPropertyAction.html

---

```
 Sets a special property of a current project.

```

| Parameter | Description |
| --- | --- |
| ``` PropertyId
 ``` | ``` Identifier name or number of the property to be set. Values are defined in class "Eplan::EplApi::DataModel::Properties" (input parameter, mandatory)
 ``` |
| ``` PropertyIdentName
 ``` | ``` Identifier name of the user defined property to be set (input parameter, mandatory)
 ``` |
| ``` PropertyIndex
 ``` | ``` If the property has indices, the index; mostly 0 (input parameter, mandatory)
 ``` |
| ``` PropertyValue
 ``` | ``` New value of the property (input parameter, mandatory)
 ``` |

**Remarks**

```
Only project properties can be set.

 When PAGE_LASTMANUMODIFICATIONDATE property is set, then PropertyValue has to be formatted this way:

 long milliseconds = (DateTime.Now.Ticks - new DateTime(1970, 1, 1).Ticks) / TimeSpan.TicksPerSecond;

 context.AddParameter("PropertyValue", milliseconds.ToString());

 The action returns true if the execution was completed.

 Please use "SysMessagesCollection" to read error messages which are generated for example if a property does not exist.

```

**Example**

```
XEsSetProjectPropertyAction /PropertyId:? /PropertyIndex:0 /PropertyValue:"?"

 or

 XEsSetProjectPropertyAction /PropertyIdentName:? /PropertyIndex:0 /PropertyValue:"?"

```