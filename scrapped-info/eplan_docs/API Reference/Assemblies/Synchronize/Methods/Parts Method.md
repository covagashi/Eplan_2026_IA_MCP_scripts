# Parts Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~Parts.html

---

Synchronizes the parts in the project to the parts master database. Updates parts database. This method corresponds with the EPLAN functionality in the ribbon "Master data \> Parts \> Synchronize". Additionally the user can specify, whether parts, which are already existing in the parts database, should be modified.

Overload List

| Overload | Description |
| --- | --- |
| [Parts(Project,StoreMode,Boolean)](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~Parts(Project,StoreMode,Boolean).html) | Synchronizes the parts in the project to the parts master database. Updates parts database. This method corresponds with the EPLAN functionality in the ribbon "Master data \> Parts \> Synchronize". Additionally the user can specify, whether parts, which are already existing in the parts database, should be modified. |
| [Parts(Project,StoreMode)](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~Parts(Project,StoreMode).html) | Synchronizes the parts in the project to the parts master database. Updates parts database. Parts in the project are not changed. This method corresponds with the EPLAN functionality in the ribbon "Master data \> Parts \> Synchronize". Additionally the user can specify, whether parts, which are already existing in the parts database, should be modified. |
| [Parts(Project)](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~Parts(Project).html) | Synchronizes the parts in the project to the parts master database. Updates parts database. When there is a reference to a part in a project, and the part is not in the project, then after invoking oSynchronize.Parts(oProject), this part becomes stored in the project (Project.Articles increases by 1), in other case parts in the project are not changed. This method corresponds with the EPLAN. functionality in the ribbon "Master data \> Parts \> Synchronize". |
| [Parts(String)](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~Parts(String).html) | Synchronizes the parts in the project to the parts master database. Updates parts database. When there is a reference to a part in a project, and the part is not in the project, then after invoking oSynchronize.Parts(oProject), this part becomes stored in the project (Project.Articles increases by 1), in other case parts in the project are not changed. This method corresponds with the EPLAN functionality in the ribbon "Master data \> Parts \> Synchronize". |
