# IEplAddInShadowCopy

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAddInShadowCopy.html

---

Provides a mechanism for framework to pass information about original location of the add-in assembly.

Syntax

**C#**



public interface IEplAddInShadowCopy

public interface class IEplAddInShadowCopy


Remarks

To use this functionality the interface needs to be implemented by class which also implements the IEplAddIn interface. Framework calls the OnBeforeInit method before [IEplAddIn.OnInit](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAddIn~OnInit.html). The argument for this method is an full path of loaded assembly.

Example

**C#**

```
/// <summary>

///  That is an example for using IEplAddInShadowCopy in EPLAN Add-in.  

/// </summary>

public class AddInModule: IEplAddIn, IEplAddInShadowCopy

{

    /// <summary>

    /// This function is called once the Add-ins through the Framework in the registering.

    /// </summary>

    /// <param name="bLoadOnStart"> True:  The Add-in is loaded in the future in system start and the function <seealso cref="OnInit"/> is called. </param>

    /// <returns></returns>

    public bool OnRegister(ref System.Boolean bLoadOnStart)

    {

        bLoadOnStart = true;

        return true;

    }

    /// <summary>

    /// This function will remove from called once the Add-ins through the Framework in that the system. 

    /// </summary>

    /// <returns></returns>

    public bool OnUnregister()

    {

        return true;

    }

    /// <summary>

    /// Called by the framework before <see cref="Eplan::EplApi::ApplicationFramework::IEplAddIn.OnInit" text="OnInit"/> and passes the

    /// location from which add-in assembly has been registered.

    /// </summary>

    public void OnBeforeInit(string strOriginalAssemblyPath)

    {

        m_strOriginalAssemblyPath = strOriginalAssemblyPath;

    }

    public String GetOriginalAssemblyPath()

    {

        return m_strOriginalAssemblyPath;

    }

    /// <summary>

    /// This function is called in system start if the Add-in is supposed to be loaded in system start.<seealso cref="OnRegister"/> 

    /// </summary>

    public bool OnInit()

    {

        return true;

    }

    /// <summary>

    /// This function is called of the Framework if the Framework has initializes already its waiter specialties and the Add-in can modify this surface.  

    /// Only is called if the Add-in is loaded also in system system start.  

    /// </summary>

    public bool OnInitGui()

    {

        return true;

    }

    /// <summary>

    ///This function is called through the Framework in Programmedne if the Add-in was loaded in system start. <seealso cref="OnRegister"/>   

    /// </summary>

    public bool OnExit()

    {

        return true;

    }

    private String m_strOriginalAssemblyPath;

}

```

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [OnBeforeInit](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAddInShadowCopy~OnBeforeInit.html) | Called by the framework before [IEplAddIn.OnInit](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAddIn~OnInit.html) and passes the location from which add-in assembly has been registered. |


