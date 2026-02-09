# TODO

## Migrate actions to scripts (QuietMode)

Some EPLAN actions may show dialogs that require user interaction (confirmations, file selectors, etc.). Since the Remote Client API (`EplanRemoteClient`) can only send action strings via `ExecuteAction()`, there is no way to suppress these dialogs from the client side.

**Solution:** Migrate these actions to C# scripts that run inside EPLAN's process, where `QuietMode` is available:

```csharp
using Eplan.EplApi.ApplicationFramework;

using (var qm = new QuietModeStep(QuietModes.ShowNoDialogs))
{
    new CommandLineInterpreter().Execute("ActionName", acc);
}
```

The workflow is:
1. Generate a `.cs` script dynamically from Python
2. Register it via `RegisterScript /ScriptFile:"path"`
3. Execute it via `ExecuteScript /ScriptFile:"path"`
4. Read results from a temp file if needed

Scripts have full access to `ActionCallingContext`, `CommandLineInterpreter`, and all `Eplan.EplApi.*` namespaces (ApplicationFramework, Gui, MasterData, etc.) that are not available from the Remote Client.

### Actions to migrate (progressively)

- [ ] Actions that show confirmation dialogs (e.g. delete pages, close project with unsaved changes)
- [ ] Actions that require reading return values via `ActionCallingContext`
- [ ] Export actions that may prompt for overwrite confirmation
- [ ] Any action where silent/unattended execution is needed

