# XAfActionSettingProject

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XAfActionSettingProject.html

---

```
 Sets the value of a project setting.

```

| Parameter | Description |
| --- | --- |
| ``` Project
 ``` | ``` Full name of the target project. When empty, the currently selected project is used.
 ``` |
| ``` set
 ``` | ``` Name of the project setting to set.
 ``` |
| ``` index
 ``` | ``` Optional index of setting. If missing, then 0 is used.
 ``` |
| ``` value
 ``` | ``` New value of setting.
 ``` |

**Remarks**

```
 See also "XAfActionSetting" to change other than project settings.

```

**Example**

```
 XAfActionSettingProject /set:EsCrossReference.ContactImage.MotorSwitchDisplayBitMask /value:1

```