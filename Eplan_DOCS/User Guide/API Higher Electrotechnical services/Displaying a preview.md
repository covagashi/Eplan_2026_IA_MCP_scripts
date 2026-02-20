# Displaying a preview

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/HE_Display.html

---

The  Eplan.EplApi.HEServices  namespace provides the  DrawingService  class that contains functionality for outputting objects (WindowMacros,  SymbolVariants,  Placements,  or  Pages) on a window or control.

Displaying the preview takes two steps:

The first step is to create a so-called display list using the  CreateDisplayList  function. This actually processes the data into a list of graphical primitives that can be drawn. Depending on what kind of data you want to show, this function will take some time. For example, if you want to create a preview of a macro,  CreateDisplayList  loads the macro file, analyzes it and creates the items to display. You need to call this function just once for a given preview.

The second step actually shows the preview (the created display list) on a window. It takes a  System.Windows.Forms.PaintEventArgs  object as parameter, which is provided by any control in the  Paint callback.

The  DrawingService  class also provides the possibility to influence the appearance of the preview in many ways, such as zooming and changing the background color.

The following example creates a preview of a macro. The first code snippet shows the creation of the display list:

**C#**
```csharp
Eplan.EplApi.HEServices.DrawingService oDs = new DrawingService();

// ...

if(oDs == null)

{

    oDs = new Eplan.EplApi.HEServices.DrawingService();

}

if (!(gProject == null))

{

    try

    {

   oDs.DrawConnections = true;

   oDs.MacroPreview = true;

   oDs.CreateDisplayList(strObj, "", 0, gProject);

    }

    catch (System.Exception ex)

    {

        new Decider().Decide(EnumDecisionType.eOkDecision, "Can't create display list: \r\n" + ex.Message, "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

    }

    // Raise the Paint event

    oForm.Picture1.Invalidate();

}

   oDs = New Eplan.EplApi.HEServices.DrawingService

   Try

      oDs.DrawConnections = True

      oDs.MacroPreview = True

      oDs.CreateDisplayList(strObj, "", 0, gProject)

   oForm.Picture1.Invalidate()
```

 The next piece of source code shows drawing the display list in the  Paint  method of a picture box:

**C#**
```csharp
private void Picture1_Paint(object sender, System.Windows.Forms.PaintEventArgs e)

{

 if (!(m_DS == null)) {

   try {

     m_DS.DrawDisplayList(e);

   } catch (System.Exception ex) {

     new Decider().Decide(EnumDecisionType.eOkDecision, "Can't draw display list:" + "\r\n" + ex.Message, "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

   }

 }

}

        Try

            m_DS.DrawDisplayList(e)
```

### 

### Setting image size and the viewport

To draw more complex images, it may be necessary to set the resolution and a viewport of the drawn image.

A viewport is a polygon that represents a part of a page that will be rendered:

This can be done using the  SetViewport  method. The coordinates should be passed in the graphical coordinate system.

If the given dimensions are not proportional to the drawing area, they are automatically adjusted to keep the aspect ratio:

**C#**

```


 m_Ds.SetViewport(10.0, 200.0, 300.0, 20.0);

```

In case of 3D drawings, it is also necessary to set the image size, otherwise its quality may be worse than in the Eplan GED:

**C#**

```


 m_Ds.SetWindow(0, 600, 1200, 0);

```