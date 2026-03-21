# XEsGetPropertyAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XEsGetPropertyAction.html

---

```
 Gets selected objects and gets the property.

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
XEsGetPropertyAction /PropertyId:? /PropertyIndex:0 

 or

 XEsGetPropertyAction /PropertyIdentName:? /PropertyIndex:0 

```