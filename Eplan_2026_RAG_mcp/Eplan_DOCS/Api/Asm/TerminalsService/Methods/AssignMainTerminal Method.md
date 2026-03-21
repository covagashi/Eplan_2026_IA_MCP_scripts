# AssignMainTerminal Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.TerminalsService~AssignMainTerminal.html

---

Converts auxiliary terminal into main terminal.

Syntax

**C#**



public bool AssignMainTerminal( 

   Terminal pTerminal,

   bool bOverwriteEmptyPropsWithFilledProps,

   bool bOverwriteFilledPropsWithEmptyProps

)

public:

bool AssignMainTerminal( 

   Terminal^ pTerminal,

   bool bOverwriteEmptyPropsWithFilledProps,

   bool bOverwriteFilledPropsWithEmptyProps

)


#### Parameters

*pTerminal*
:   Terminal function will be assigned the "Main terminal" property. Can't be `null` or transient.

*bOverwriteEmptyPropsWithFilledProps*
:   If `true` then properties of old main terminal that contain value are transfered to properties on new main terminal that contain no value.

*bOverwriteFilledPropsWithEmptyProps*
:   If `true` then properties of old main terminal that contain no value removes existing properties on new main terminal.

#### Return Value

`true` if operation succeeded i.e. terminal is now main terminal, `false` otherwise

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `pTerminal` is `null`. |
| [System.ArgumentException](#) | Thrown when `pTerminal` is `invalid`. |

Remarks

Changes an auxiliary terminal into a main terminal by assigning the "main terminal" property to the auxiliary terminal. The auxiliary terminal is changed into a main terminal. The original main terminal is then converted to an auxiliary terminal. Converting terminal to main terminal adopts properties from old to new main terminal based on parameters passed to method. Appropriate for terminals, that have multiple representation types. Changes the main terminal property from one representation type to another. Does not change the main terminal property from one level to another for multilevel terminals.

This method makes no changes to functions which are transient or their category is not `Terminal`. For such functions it returns `false`.
