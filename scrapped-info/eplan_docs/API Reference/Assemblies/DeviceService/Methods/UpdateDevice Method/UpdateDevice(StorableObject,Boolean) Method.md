# UpdateDevice(StorableObject,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService~UpdateDevice(StorableObject,Boolean).html

---

Updates a given device or a connection with data from the referenced article(s). This method can not be used for wire inside cable, but only for whole cable or single connection.

Syntax

**C#**



public bool UpdateDevice( 

   StorableObject oObject,

   bool bKeepSwappedConnPoint

)

public:

bool UpdateDevice( 

   StorableObject^ oObject,

   bool bKeepSwappedConnPoint

)


#### Parameters

*oObject*
:   Main function of the device or a connection.

*bKeepSwappedConnPoint*
:   KeepSwappedConnPointInformation. This parameter specifies Swapped ConnPointInformation (2;1 instead of 1;2) will be kept, but only if all ConnPoint-Designations will match as a set.

#### Return Value

FALSE, if the object given as parameter doesn't have any article references.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | NULL was passed as a parameter. |
| **ArgumentException** | Invalid object passed as a parameter. |
| **ApplicationException** | The internal interface could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred while performing the action. Please refer to the exception message. |

Remarks

Component-specific data will be transfered from article to main-function, function template-data from article will be transfered to all functions of device, modules will be transfered to functions of device, when article is a module and main-function is a blackbox or plcbox, the referenced articles will be stored to project (if they were not before). Please be aware that not all values are overwritten by default with the ones from a part. In case of empty values, they don't overwritte existing ones. This behavior is similar to 'Conflict' dialog from GUI.
