# CreateDevice(String,String,Page,PointD) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService~CreateDevice(String,String,Page,PointD).html

---

Creates a new device in the project and inserts it on a page. If the article has a macro specified, the macro is inserted onto the specified page.

Syntax

**C#**



public Function[] CreateDevice( 

   string strPartNummer,

   string strPartVariant,

   Page pPage,

   PointD ptInsert

)

public:

array<Function^>^ CreateDevice( 

   String^ strPartNummer,

   String^ strPartVariant,

   Page^ pPage,

   PointD ptInsert

)


#### Parameters

*strPartNummer*
:   The article's part number.

*strPartVariant*
:   The article's variant. If not existing variant is specified, the first available variant is selected.

*pPage*
:   A page to insert the article's macro on.

*ptInsert*
:   Insertion point of the macro.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Is thrown in case of invalid arguments. |
| **ArgumentNullException** | Is thrown, if some of the arguments are NULL. |
| **ApplicationException** | A necessary internal interface for creating devices could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | If an error occurred while creating a device. |

Remarks

This Method does not return 3D objects, even when they are created. To get the 3D objects use other overloaded method instead. Warning: Inserted functions are not numerated by this method. When a device is created by a function templates, only the main function (or terminal) is placed on the page, the rest is added to the project as unplaced function. In this case, the page needs to be refreshed (e.g. by using Edit.RedrawGed) to make the result visible.
