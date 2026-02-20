# UpdateDevice(StorableObject) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService~UpdateDevice(StorableObject).html

---

Updates a given device or a connection with data from the referenced article(s). This method can not be used for wire inside cable, but only for whole cable or single connection.

Syntax

**C#**



public bool UpdateDevice( 

   StorableObject oObject

)

public:

bool UpdateDevice( 

   StorableObject^ oObject

)


#### Parameters

*oObject*
:   Main function of the device or a connection.

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

Example

**C#**

```
//create main cable

Cable oCable = new Cable();

oCable.Create(page, cableSymbolVariant);

oCable.Properties.FUNC_CABLETYPE = "Unknown type";

oCable.Location = new PointD(60.00, 70.00);

//structure part of cable name can't be empty

oCable.Name = "=EB3+ET1-W1";

//add part to cable

ArticleReference oArticleReference = oCable.AddArticleReference(partName);

//update the cable with properties from new part

new DeviceService().UpdateDevice(oCable);

//oCable.Properties.FUNC_CABLETYPE == 'ZB3200'

```
