# XDLInsertDeviceAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XDLInsertDeviceAction.html

---

```
 Starts interaction for inserting a device.

```

| Parameter | Description |
| --- | --- |
| ``` PartNr
 ``` | ``` Article part number
 ``` |
| ``` PartVariant
 ``` | ``` Variant of the article. 
 ``` |
| ``` ProjectId
 ``` | ``` Project ID
 ``` |
| ``` PropertyIndex
 ``` | ``` Index of the project article, must be reduced to (1-50). If 0, then no project article is set.
 ``` |

**Remarks**

```
 The action can be used only interactively.

Used specialized calling context: DMBaseHandleContext

```

**Example**

```
                XDLInsertDeviceAction /PartNr:MOE.010042 /PartVariant:1 /PropertyIndex:0 /ProjectId:0

```