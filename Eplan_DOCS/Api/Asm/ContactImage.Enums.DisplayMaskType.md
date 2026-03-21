# ContactImage.Enums.DisplayMaskType

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ContactImage+Enums+DisplayMaskType.html

---

Enum containing all possible setting of contact image.

Syntax

**C#**



[Flags()]

public enum ContactImage.Enums.DisplayMaskType : System.Enum

[Flags()]

public enum class ContactImage.Enums.DisplayMaskType : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **MarkQVW** | 8192 | Underline cross-references of NC and change-over contacts. |
| **Rotate180** | 262144 | Rotation: 180 degrees. |
| **Rotate90** | 131072 | Rotation: 90 degrees. |
| **RotateQVW** | 32 | Display cross-references vertically. |
| **ShowACLines** | 1024 |  |
| **ShowAllQVW** | 64 | Display as symbol image. |
| **ShowAsTable** | 2048 | Show in tabular form. |
| **ShowEmbeddedFrom** | 33554432 | Display embedded form. |
| **ShowFirstArticle\_Lower** | 524288 | Display of 1st part: Below. |
| **ShowFirstArticleUpper** | 4 | Display of 1st part: Above. |
| **ShowFirstTypeLower** | 2097152 | Display of 1st part type: Below. |
| **ShowFirstTypeUpper** | 1048576 | Display of 1st part type: Above. |
| **ShowNoLeftProperty** | 16384 | Hide left-hand connection point description. |
| **ShowNoRightProperty** | 32768 | Hide right-hand connection point description. |
| **ShowOnComponent** | 16 | Display on component. |
| **ShowOwnQVW** | 128 | Display own cross-reference. |
| **ShowSecondArticleLower** | 8388608 | Display of 2ndt part: Below. |
| **ShowSecondArticleUpper** | 4194304 | Display of 2nd part: Above. |
| **ShowSecondTypeLower** | 16777216 | Display of 2nd part type: Below. |
| **ShowSecondTypeUpper** | 8 | Display of 2nd part type: Above. |
| **ShowSymbols** | 256 | Show symbols. |
| **ShowVertical** | 2 | Arrange vertically. |
| **ShrinkText** | 65536 | Decrease cross-references and connection point designations. |
| **SwapQVWVariant** | 512 | Show cross-references on the left. |
| **Undefined** | 0 | Undefined state. |
| **UserSettings** | 1 | User-defined settings. |
| **UseVariableTable** | 4096 | Table cross with variable length. |

Remarks

This enum is defined as bit field. This mean that variable which contain data of this type can contain a set of values.

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.DataModel.Graphics.ContactImage.Enums.DisplayMaskType**
