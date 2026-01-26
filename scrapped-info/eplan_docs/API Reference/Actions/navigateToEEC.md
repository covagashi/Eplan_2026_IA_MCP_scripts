# navigateToEEC

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/navigateToEEC.html

---

```
Action class to navigate to an object in the EPLAN Engineering Configuration.

```

| Parameter | Description |
| --- | --- |
| ``` EECOBJECTID
 ``` | ``` Object ID in the EEC to navigate to.
 ``` |

**Remarks**

```
If the object ID is not given or if it is invalid, a "BaseException" is thrown.

```

**Example**

```
navigateToEEC /EECOBJECTID:"?"

```