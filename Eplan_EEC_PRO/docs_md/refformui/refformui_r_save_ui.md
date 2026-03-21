---
title: "Save Form-UI"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_save_ui.htm"
file: "refformui_r_save_ui"
category: "refformui"
---

# Save Form-UI

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Save Form-UI Each time you enter a Form-UI, the editor changes to the change state (see [Working in the editor area](gui_k_editors_working_on_editor_area.htm)). In order for the changes to affect the model, you must save the Form-UI. To save a Form-UI you can apply the shortcut key [Ctrl] \+ [S], the save icon , or an action. The shortcut key and the save icon are only available in the EEC user interface. If the Form-UI is executed in the Web EEC, you require an action to save it. [To create an action to save a Form-UI:](javascript:void\(0\);)
    1. Call up the popup menu of a library or a unit and select New > Object here.
    2. In the Create new library object wizard, select Object > Action.
    3. Click [Finish].
    4. The action editor opens.
    5. Enter a name for the action (for example, SaveFormUi).
    6. Open the Methods editor page.
    7. Click Add method.
    8. Enter the name run for the method.
    9. In the Language field select Java.
    10. Click Add single argument.
    11. Change the name of the argument to obj.
    12. Add the following program lines to the Code field:
    
        import com.mind8.mechatronic.skill.api.IUtilAPI;
    IUtilAPI.DEFAULT.saveActiveEditor()

    1. Save the action.
[To create a button in the Form-UI to perform the actions:](javascript:void\(0\);)
    1. Open the editor page Form-UI of the respective component.
    2. Change to the Source editor view.
    3. Insert the following program lines at this point to place the button:
    
        <action name="<Path to actions>.SaveFormUi" arguments="this" type="button" text="Save Configuration" />

    1. For <Path to actions>, enter the path to your own action.
    2. Save the Form-UI.
Result:
