# AssignMainFunction Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService~AssignMainFunction.html

---

Converts auxiliary function into main function.

Syntax

**C#**



public bool AssignMainFunction( 

   Function pFunction,

   bool bOverwriteEmptyPropsWithFilledProps,

   bool bOverwriteFilledPropsWithEmptyProps

)

public:

bool AssignMainFunction( 

   Function^ pFunction,

   bool bOverwriteEmptyPropsWithFilledProps,

   bool bOverwriteFilledPropsWithEmptyProps

)


#### Parameters

*pFunction*
:   Function will be assigned the "Main function" property. Can't be `null` or transient.

*bOverwriteEmptyPropsWithFilledProps*
:   If `true` then properties of old main function that contain value are transfered to properties on new main function that contain no value.

*bOverwriteFilledPropsWithEmptyProps*
:   If `true` then properties of old main function that contain no value removes existing properties on new main function.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `pFunction` is `null`. |
| [System.ArgumentException](#) | Thrown when `pFunction` is `invalid`. |

Remarks

Changes an auxiliary function into a main function by assigning the "Main function" property to the auxiliary function. The auxiliary function is changed into a main function. The original main function is then converted to an auxiliary function. Converting function to main function adopts properties from old to new main function based on parameters passed to method.

This method makes no changes to functions which are transient or their category is `Terminal` or `ArticlePlacement`. For such functions it returns `false`.
