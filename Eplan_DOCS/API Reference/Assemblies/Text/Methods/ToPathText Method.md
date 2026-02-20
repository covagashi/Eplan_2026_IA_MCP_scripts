# ToPathText Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Text~ToPathText.html

---

Transforms this Text instance into a PathText instance.

Syntax

**C#**



public virtual PathText ToPathText()

public:

virtual PathText^ ToPathText();


#### Return Value

A new PathText instance.

Remarks

After calling this method the current Text object becomes invalid (i.e. deleted) This method should not be called on an object that already is a PathText instance, otherwise an ObjectCreationException is thrown.
