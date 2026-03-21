# SetFile Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Image~SetFile.html

---

Sets the reference to bitmap file. If the image file is not yet located in the project folder, it will be copied there, if the second parameter is set to true.

Syntax

**C#**



public bool SetFile( 

   string fileName,

   bool copyToProject,

   bool overWrite

)

public:

bool SetFile( 

   String^ fileName,

   bool copyToProject,

   bool overWrite

)


#### Parameters

*fileName*
:   Full image file name.

*copyToProject*
:   Boolean value. If set to true, the image will be copied into the project directory.

*overWrite*
:   Boolean value. If set to true, an already existing image with the same name will be overwritten

#### Return Value

true: if the image was successfully copied.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the file cannot be set. |
| [System.ArgumentNullException](#) | Thrown when `fileName` is `null`. |
