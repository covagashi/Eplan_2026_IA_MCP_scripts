# Label

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Label.html

---

Class used for labeling. The following example shows how to use class Label.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.HEServices.Label**

Syntax

**C#**



public class Label

public ref class Label


Example

The following example shows how to use class Label.

**C#**

```


Label oLabel = new Label();

oLabel.DoLabel(m_oTestProject,

    "",                 // use implicitly last used scheme

    "",                 // don't filter

    "",                 // don't sort

    "en_EN",            // use English language  

    m_oTestProject.ProjectDirectoryPath + "\\LabelledPrj_2.txt", // destination file

    2,                  // Record Repeat = 2

    1);                 // Task Repeat = 1

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Label Constructor](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Label~_ctor.html) | Default constructor |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Label~Dispose().html) | Destructor |
| Public Method | [DoLabel](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Label~DoLabel.html) | Overloaded. do a labeling for a given objects. |


