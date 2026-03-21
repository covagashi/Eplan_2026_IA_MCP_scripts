# XAfActionSetting

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XAfActionSetting.html

---

```
 Sets the value of a setting.

```

| Parameter | Description |
| --- | --- |
| ``` set
 ``` | ``` Name of the setting to set.
 ``` |
| ``` index
 ``` | ``` Optional index of setting. If missing, then 0 is used.
 ``` |
| ``` value
 ``` | ``` New value of setting.
 ``` |

**Remarks**

```
 See also "XAfActionSettingProject" to change project settings.

```

**Example**

```
 XAfActionSetting /set:USER.MacrosLog.Pxf.writeDebugInfo /value:1

```