# Create(InstallationSpace,String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Cabinet~Create(InstallationSpace,String,String).html

---

Creates the Cabinet object on an InstallationSpace.

Syntax

**C#**



public void Create( 

   InstallationSpace oInstallationSpace,

   string strArticleNr,

   string strVariant

)

public:

void Create( 

   InstallationSpace^ oInstallationSpace,

   String^ strArticleNr,

   String^ strVariant

)


#### Parameters

*oInstallationSpace*
:   InstalltionSpace where this object will be placed. Can't be null.

*strArticleNr*
:   Part number of article used to create this object. Can't be null or have zero length.

*strVariant*
:   Part variant of article.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [System.ArgumentException](#) | Thrown if `strArticleNr` has zero length. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the Cabinet cannot be created. |

Remarks

Sets initial transformation to identity matrix. If strArticleVariant is null or empty, variant "1" is used.
