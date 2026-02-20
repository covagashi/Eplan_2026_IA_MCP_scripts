# Accessing selected objects

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/HE_Selectionset.html

---

The advantage of an add-in is that it is called from within the context of a running Eplan version and can access the currently selected objects. This can be achieved by using the SelectionSet class. The class provides a number of methods for retrieving a list of items currently selected by the user.

You can either get the project the user is currently working on using the  SelectionSet::GetCurrentProject  method, or you can get the currently selected page(s) using the  SelectionSet::GetSelectedPages  method. Depending on whether the graphical editor or the page overview dialog currently has the focus, one or more pages can be selected.

Most importantly, you can get any set of objects selected from any focused (non-modal) dialog through the  SelectionSet.Selection  property. The objects are returned by the function as an array of StorableObjects. You can loop over the array and determine the types (and any other information) about the objects.

The following example shows how to access the selection.

**C#**
```csharp
SelectionSet selectionSet = new SelectionSet();

StorableObject[] storableObjects = selectionSet.Selection;

if (storableObjects.Length == 0)

{

    Console.WriteLine("No current selection!");

}

else

{

    foreach(StorableObject so in storableObjects)

    {

        if(so is Function)

           Console.WriteLine(" StorableObject is a function: " + ((Function) so).Name);

        else

            Console.WriteLine(" StorableObject: " + so.ToString());

    }

}

   Console.WriteLine("No current selection!")

Else

   For Each so In  storableObjects

         Console.WriteLine((" StorableObject is a function: " + CType(so, Function).Name))

      Else

         Console.WriteLine((" StorableObject: " + so.ToString()))

   Next so
```