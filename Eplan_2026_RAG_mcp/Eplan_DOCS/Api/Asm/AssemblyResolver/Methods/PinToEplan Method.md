# PinToEplan Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Starteru~Eplan.EplApi.Starter.AssemblyResolver~PinToEplan.html

---

Pin an offline application to an EPLAN application. When the EPLAN product variant bin path is known, an Offline Application using the EPLAN API DLL can be pinned to this version. This means all referenced EPLAN API DLLs will be loaded. Note: For already loaded linked DLLs the AssemblyResolve event is not fired.

Syntax

**C#**



public void PinToEplan()

public:

void PinToEplan();


Example

This code is in a separate EXE or DLL. It's not allowed to link directly some EPLAN DLLs from the EPLAN product variant bin path. (This causes an error at start when the DLLs are not available.) Separate all EPLAN references in another DLL and link to this. The "EplanAppStarter" class can be defined in this DLL and contains your code.

**C#**

```
// Use the finder to find the correct EPLAN version if not yet known

EplanFinder finder = new EplanFinder();

string binPath = finder.SelectEplanVersion();

// Now use the AssemblyResolver to let the program know where all EPLAN assemblies can be found.

AssemblyResolver resolver = new AssemblyResolver();

resolver.SetEplanBinPath(binPath);

// Pin to EPLAN does the actual preparation. All referenced EPLAN assemblies are loaded from the EPLAN product variant bin path.

resolver.PinToEplan();

// Now the next (referenced) DLL can be used. All EPLAN references of this DLL are known now.

EplanAppStarter app = new EplanAppStarter();

app.startEplan(binPath);

//In the other DLL, EplanAppStarter is implemented:

    public class EplanAppStarter

    {

        public void startEplan(string strVariant, string binPath)

        {

           Eplan.EplApi.System.EplApplication app = new Eplan.EplApi.System.EplApplication();

            app.EplanBinFolder = binPath;

            app.Init("");

        }

    }
```
