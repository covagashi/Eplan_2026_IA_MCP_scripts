# XCMRemoveUnnecessaryNDPsAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XCMRemoveUnnecessaryNDPsAction.html

---

```
 Removes unnecessary net definition points of active project.

```

| Parameter | Description |
| --- | --- |
| ``` Quiet
 ``` | ``` Suppresses message dialog if true.
 ``` |

**Remarks**

```
 Removes unnecessary net definition points of active project, i.e. net definition points that contain connections

 equal to the connections that would be in the net without using net based wiring but using target based wiring.

 If necessary, connection definition points are placed on the connections of the net so that connection properties don't get lost.

```

**Example**

```
 XCMRemoveUnnecessaryNDPsAction /Quiet:true

```