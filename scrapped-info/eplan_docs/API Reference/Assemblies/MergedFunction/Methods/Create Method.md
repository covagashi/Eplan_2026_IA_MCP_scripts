# Create Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedFunction~Create.html

---

Initializes the MergedFunction object to cover the functions passed in the array parameter. If the functions cannot be merged together into one merged function an exception is thrown. Functions, generally, cannot be merged together if they belong to different devices or they are of different categories. To be merged, they have to represent the same functional part of the device.

Overload List

| Overload | Description |
| --- | --- |
| [Create(IEnumerable<IFunctionBase>)](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedFunction~Create(IEnumerable{IFunctionBase}).html) | Initializes the MergedFunction object to cover the functions passed in the array parameter. If the functions cannot be merged together into one merged function an exception is thrown. Functions, generally, cannot be merged together if they belong to different devices or they are of different categories. To be merged, they have to represent the same functional part of the device. |
| [Create(Function[])](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedFunction~Create(Function[]).html) | Initializes the MergedFunction object to cover the functions passed in the array parameter. If the functions cannot be merged together into one merged function an exception is thrown. Functions, generally, cannot be merged together if they belong to different devices or they are of different categories. To be merged, they have to represent the same functional part of the device. |
| [Create(Function3D)](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedFunction~Create(Function3D).html) | Initializes the merged function to cover the function 3D passed as parameter and all the other 'mergable' functions from the device that the input function 3D belongs to. 'Mergable' in this context means, generally, representing the same functional part of the device. |
| [Create(Function)](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedFunction~Create(Function).html) | Initializes the merged function to cover the function passed as parameter and all the other 'mergable' functions from the device that the input function belongs to. 'Mergable' in this context means, generally, representing the same functional part of the device. |
