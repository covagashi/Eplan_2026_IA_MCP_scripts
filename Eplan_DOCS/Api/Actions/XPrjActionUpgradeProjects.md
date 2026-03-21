# XPrjActionUpgradeProjects

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XPrjActionUpgradeProjects.html

---

```
 This action upgrades one ore more projects to the actual database scheme version.

```

| Parameter | Description |
| --- | --- |
| ``` Project
 ``` | ``` Full project link file name
 ``` |
| ``` Folder
 ``` | ``` All projects in the folder and its subfolders are upgraded.
 ``` |
| ``` Archive
 ``` | ``` true: ZW1 projects are also upgraded and packed afterwards.
 ``` |
| ``` BaseProject
 ``` | ``` true: ZW9 and ZX1 projects are also upgraded and packed afterwards.
 ``` |
| ``` UpgradeWriteProtectedProjects
 ``` | ``` true: ReadOnly projects are also upgraded (*.elr and *.elt, *.els, elx).
 ``` |
| ``` UpgradeXMLProjects
 ``` | ``` true: Projects / basic projects in XML format are also upgraded (*.ept and *.epj, *.zx2).
 ``` |
| ``` FileTypes
 ``` | ``` *.*: All projects (such as *.elk, *.ell, *.elp, *.elr, *.elt, *.els, *.elx, *.zw1, *.zw9, *.zx1, *.ept, *.epj, *.zx2).
 ``` |
| ``` PackOriginalProject
 ``` | ``` true: The original projects will be packed into a 7zip file after upgrade (default = true).
 ``` |
| ``` UpdateConnections
 ``` | ``` true: The connections in the project will be updated (default = false). Note: If the DoDataModelUpgrades parameter is false, this value will be ignored.
 ``` |
| ``` NoBackup
 ``` | ``` true: No backup of the old version is created (default = false).
 ``` |
| ``` IgnoreUpgradeBackups
 ``` | ``` true: Backup projects will be ignored when converting a complete folder (default = false). Backup projects have a naming like [NAME]_V[Version]_[Backuptime].
 ``` |
| ``` DoDataModelUpgrades
 ``` | ``` true: Also data model corrections will be done (default = true). Note: If this parameter is set to false, the UpdateConnections parameter will be ignored.
 ``` |
| ``` FileDescription
 ``` | ``` 0: Default, will add new data backup description at the end.
                 1: Data backup description will not change.
       2: Replace data backup description with new one.
  
 ``` |

**Remarks**

```
 The action does nothing when no upgrade is needed. (Except for XML formats).

 Several input formats are provided: a project in ZW1 format is upgraded and packed to ZW1 again.

 All projects in a folder are upgraded (recursively).

 A backup of every project is done before changing.

 Basic projects are only upgraded when a major version change is done. For minor changes the basic project will stay unchanged.

 Each project found produces a system message with the upgrade result.

 Handle Folder:

 All *.elk, *.ell and *.elp are upgraded.

 When the FileTypes parameter is set, the following parameters are ignored: Archive, BaseProject, UpgradeWriteProtectedProjects.

```

**Example**

```
                XPrjActionUpgradeProjects /Project:$(MD_PROJECTS)\EPLAN_Sample_Project.elk

```