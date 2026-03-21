# XEsGetPagePropertyAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XEsGetPagePropertyAction.html

---

```
 Gets a special property of first selected page.

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
 ``` | ``` Returned value of the property (output parameter, mandatory)
 ``` |

**Example**

```
XEsGetPagePropertyAction /PropertyId:? /PropertyIndex:0 /PropertyValue:"?"

 or

 XEsGetPagePropertyAction /PropertyIdentName:? /PropertyIndex:0 /PropertyValue:"?"

```