# Create Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedConnection~Create.html

---

Initializes the MergedConnection object to cover the connections passed in the array parameter. If the connections cannot be merged together into one merged connection an exception is thrown. connections, generally, cannot be merged together if they belong to different devices or they are of different categories. To be merged, they have to represent the same connectional part of the device.

Overload List

| Overload | Description |
| --- | --- |
| [Create(Connection[])](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedConnection~Create(Connection[]).html) | Initializes the MergedConnection object to cover the connections passed in the array parameter. If the connections cannot be merged together into one merged connection an exception is thrown. connections, generally, cannot be merged together if they belong to different devices or they are of different categories. To be merged, they have to represent the same connectional part of the device. |
| [Create(Connection)](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedConnection~Create(Connection).html) | Initializes the merged connection to cover the connection passed as parameter and all the other 'mergable' connections from the input connection belongs to. 'Mergable' in this context means, generally, representing the same corresponding connections with different placement types. |
