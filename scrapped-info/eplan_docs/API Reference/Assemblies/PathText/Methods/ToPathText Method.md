# ToPathText Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PathText~ToPathText.html

---

Transforms this Text instance into a PathText instance.

Syntax

**C#**



public override PathText ToPathText()

public:

PathText^ ToPathText(); override


#### Return Value

A new PathText instance.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown every time for instances of PathText class. |

Remarks

After calling this method the current Text object becomes invalid (i.e. deleted) This method should not be called on an object that already is a PathText instance, otherwise an ObjectCreationException is thrown.
