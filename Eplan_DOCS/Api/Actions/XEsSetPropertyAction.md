# XEsSetPropertyAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XEsSetPropertyAction.html

---

```
 Gets selected objects and sets the property.

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
When PAGE_LASTMANUMODIFICATIONDATE property is set, then PropertyValue has to be formatted this way:

 long milliseconds = (DateTime.Now.Ticks - new DateTime(1970, 1, 1).Ticks) / TimeSpan.TicksPerSecond;

 context.AddParameter("PropertyValue", milliseconds.ToString());

```

**Example**

```
XEsSetPropertyAction /PropertyId:? /PropertyIndex:0 /PropertyValue:"?"

 or

 XEsSetPropertyAction /PropertyIdentName:? /PropertyIndex:0 /PropertyValue:"?"

```