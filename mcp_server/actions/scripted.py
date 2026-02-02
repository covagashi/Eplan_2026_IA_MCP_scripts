"""
Scripted actions - Uses dynamically generated C# scripts for advanced EPLAN APIs.

These actions access internal EPLAN APIs that aren't available via standard actions:
- MDPartsManagement: Direct parts database access
- Settings: Typed settings (string, bool, int) with direct API
- PathMap: Variable substitution
"""

import os
import json
import time
import uuid
from typing import Optional, List
from ._base import _get_connected_manager

# Directory for generated scripts and results
SCRIPT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts", "generated")
RESULTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts", "results")


def _ensure_dirs():
    """Ensure script and results directories exist."""
    os.makedirs(SCRIPT_DIR, exist_ok=True)
    os.makedirs(RESULTS_DIR, exist_ok=True)


def _execute_script(script_content: str, timeout: float = 30.0) -> dict:
    """
    Execute a C# script in EPLAN and return results.

    Args:
        script_content: The C# script code
        timeout: Max seconds to wait for results

    Returns:
        dict with success status and results/error
    """
    manager, error = _get_connected_manager()
    if error:
        return error

    _ensure_dirs()

    # Generate unique IDs for this execution
    exec_id = str(uuid.uuid4())[:8]
    script_path = os.path.join(SCRIPT_DIR, f"script_{exec_id}.cs")
    result_path = os.path.join(RESULTS_DIR, f"result_{exec_id}.json")

    # Inject result path into script
    script_with_path = script_content.replace("{{RESULT_PATH}}", result_path.replace("\\", "\\\\"))

    try:
        # Write script
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(script_with_path)

        # Register and execute
        reg_result = manager.execute_action(f'RegisterScript /ScriptFile:"{script_path}"')
        if not reg_result.get("success"):
            return {"success": False, "message": f"Failed to register script: {reg_result.get('message')}"}

        exec_result = manager.execute_action(f'ExecuteScript /ScriptFile:"{script_path}"')
        if not exec_result.get("success"):
            return {"success": False, "message": f"Failed to execute script: {exec_result.get('message')}"}

        # Wait for results file
        start_time = time.time()
        while not os.path.exists(result_path):
            if time.time() - start_time > timeout:
                return {"success": False, "message": "Timeout waiting for script results"}
            time.sleep(0.1)

        # Small delay to ensure file is fully written
        time.sleep(0.1)

        # Read results
        with open(result_path, 'r', encoding='utf-8') as f:
            results = json.load(f)

        return {"success": True, "results": results}

    except Exception as e:
        return {"success": False, "message": str(e)}
    finally:
        # Cleanup
        try:
            manager.execute_action(f'UnregisterScript /ScriptFile:"{script_path}"')
        except:
            pass
        try:
            if os.path.exists(script_path):
                os.remove(script_path)
            if os.path.exists(result_path):
                os.remove(result_path)
        except:
            pass


# =============================================================================
# PARTS DATABASE (MDPartsManagement)
# =============================================================================

def parts_db_query(
    filter_property: str = None,
    filter_value: str = None,
    return_properties: List[str] = None,
    limit: int = 100
) -> dict:
    """
    Query parts from the EPLAN parts database.

    Uses MDPartsManagement API for direct database access.

    Args:
        filter_property: Property to filter on (e.g., "ProductSubGroup", "PartNr", "Manufacturer")
        filter_value: Value to match
        return_properties: List of properties to return (default: PartNr, Description1, Manufacturer)
        limit: Maximum number of parts to return

    Returns:
        dict with parts list and count
    """
    if return_properties is None:
        return_properties = ["PartNr", "Description1", "Manufacturer", "ProductGroup", "ProductSubGroup"]

    props_array = ", ".join([f'"{p}"' for p in return_properties])

    filter_code = ""
    if filter_property and filter_value:
        filter_code = f'''
            .Where(p => p.{filter_property}?.ToString()?.Contains("{filter_value}") == true)'''

    script = f'''using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using Eplan.EplApi.MasterData;
using Eplan.EplApi.Scripting;

public class PartsQuery_{uuid.uuid4().hex[:6]}
{{
    [Start]
    public void Run()
    {{
        var results = new Dictionary<string, object>();
        var partsList = new List<Dictionary<string, object>>();

        try
        {{
            var mdParts = new MDPartsManagement();
            using (var db = mdParts.OpenDatabase())
            {{
                var parts = db.Parts{filter_code}
                    .Take({limit})
                    .ToList();

                string[] propsToGet = new string[] {{ {props_array} }};

                foreach (var part in parts)
                {{
                    var partDict = new Dictionary<string, object>();
                    foreach (var propName in propsToGet)
                    {{
                        try
                        {{
                            var prop = part.Properties.GetType().GetProperty(propName);
                            if (prop != null)
                            {{
                                var val = prop.GetValue(part.Properties);
                                partDict[propName] = val?.ToString() ?? "";
                            }}
                        }}
                        catch {{ partDict[propName] = ""; }}
                    }}
                    partsList.Add(partDict);
                }}

                results["success"] = true;
                results["count"] = partsList.Count;
                results["parts"] = partsList;
            }}
        }}
        catch (Exception ex)
        {{
            results["success"] = false;
            results["error"] = ex.Message;
        }}

        string json = Newtonsoft.Json.JsonConvert.SerializeObject(results, Newtonsoft.Json.Formatting.Indented);
        File.WriteAllText(@"{{{{RESULT_PATH}}}}", json);
    }}
}}
'''
    return _execute_script(script)


def parts_db_count(
    filter_property: str = None,
    filter_value: str = None
) -> dict:
    """
    Count parts in the EPLAN parts database.

    Args:
        filter_property: Property to filter on
        filter_value: Value to match

    Returns:
        dict with count
    """
    filter_code = ""
    if filter_property and filter_value:
        filter_code = f'.Where(p => p.{filter_property}?.ToString()?.Contains("{filter_value}") == true)'

    script = f'''using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using Eplan.EplApi.MasterData;
using Eplan.EplApi.Scripting;

public class PartsCount_{uuid.uuid4().hex[:6]}
{{
    [Start]
    public void Run()
    {{
        var results = new Dictionary<string, object>();

        try
        {{
            var mdParts = new MDPartsManagement();
            using (var db = mdParts.OpenDatabase())
            {{
                int count = db.Parts{filter_code}.Count();
                results["success"] = true;
                results["count"] = count;
            }}
        }}
        catch (Exception ex)
        {{
            results["success"] = false;
            results["error"] = ex.Message;
        }}

        string json = Newtonsoft.Json.JsonConvert.SerializeObject(results);
        File.WriteAllText(@"{{{{RESULT_PATH}}}}", json);
    }}
}}
'''
    return _execute_script(script)


def parts_db_get_part(part_number: str) -> dict:
    """
    Get detailed information about a specific part.

    Args:
        part_number: The part number to look up

    Returns:
        dict with part details
    """
    script = f'''using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using Eplan.EplApi.MasterData;
using Eplan.EplApi.Scripting;

public class PartsGet_{uuid.uuid4().hex[:6]}
{{
    [Start]
    public void Run()
    {{
        var results = new Dictionary<string, object>();

        try
        {{
            var mdParts = new MDPartsManagement();
            using (var db = mdParts.OpenDatabase())
            {{
                var part = db.Parts.FirstOrDefault(p => p.PartNr == "{part_number}");

                if (part != null)
                {{
                    var props = part.Properties;
                    var partDict = new Dictionary<string, object>
                    {{
                        ["PartNr"] = props.ARTICLE_PARTNR ?? "",
                        ["Description1"] = props.ARTICLE_DESCR1 ?? "",
                        ["Description2"] = props.ARTICLE_DESCR2 ?? "",
                        ["Description3"] = props.ARTICLE_DESCR3 ?? "",
                        ["Manufacturer"] = props.ARTICLE_MANUFACTURER ?? "",
                        ["Supplier"] = props.ARTICLE_SUPPLIER ?? "",
                        ["OrderNr"] = props.ARTICLE_ORDERNR ?? "",
                        ["ProductGroup"] = part.ProductGroup.ToString(),
                        ["ProductSubGroup"] = part.ProductSubGroup.ToString(),
                        ["ProductTopGroup"] = part.ProductTopGroup.ToString()
                    }};

                    results["success"] = true;
                    results["found"] = true;
                    results["part"] = partDict;
                }}
                else
                {{
                    results["success"] = true;
                    results["found"] = false;
                }}
            }}
        }}
        catch (Exception ex)
        {{
            results["success"] = false;
            results["error"] = ex.Message;
        }}

        string json = Newtonsoft.Json.JsonConvert.SerializeObject(results, Newtonsoft.Json.Formatting.Indented);
        File.WriteAllText(@"{{{{RESULT_PATH}}}}", json);
    }}
}}
'''
    return _execute_script(script)


def parts_db_update(
    part_number: str,
    property_name: str,
    property_value: str
) -> dict:
    """
    Update a property on a part in the database.

    Args:
        part_number: The part number to update
        property_name: Property to update (e.g., "ARTICLE_DESCR1")
        property_value: New value

    Returns:
        dict with success status
    """
    script = f'''using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using Eplan.EplApi.MasterData;
using Eplan.EplApi.Scripting;

public class PartsUpdate_{uuid.uuid4().hex[:6]}
{{
    [Start]
    public void Run()
    {{
        var results = new Dictionary<string, object>();

        try
        {{
            var mdParts = new MDPartsManagement();
            using (var db = mdParts.OpenDatabase())
            {{
                var part = db.Parts.FirstOrDefault(p => p.PartNr == "{part_number}");

                if (part != null)
                {{
                    var prop = part.Properties.GetType().GetProperty("{property_name}");
                    if (prop != null)
                    {{
                        prop.SetValue(part.Properties, "{property_value}");
                        results["success"] = true;
                        results["updated"] = true;
                    }}
                    else
                    {{
                        results["success"] = false;
                        results["error"] = "Property not found: {property_name}";
                    }}
                }}
                else
                {{
                    results["success"] = false;
                    results["error"] = "Part not found: {part_number}";
                }}
            }}
        }}
        catch (Exception ex)
        {{
            results["success"] = false;
            results["error"] = ex.Message;
        }}

        string json = Newtonsoft.Json.JsonConvert.SerializeObject(results);
        File.WriteAllText(@"{{{{RESULT_PATH}}}}", json);
    }}
}}
'''
    return _execute_script(script)


def parts_db_list_product_groups() -> dict:
    """
    List all product groups and subgroups in the parts database.

    Returns:
        dict with product groups
    """
    script = f'''using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using Eplan.EplApi.MasterData;
using Eplan.EplApi.Scripting;

public class PartsGroups_{uuid.uuid4().hex[:6]}
{{
    [Start]
    public void Run()
    {{
        var results = new Dictionary<string, object>();

        try
        {{
            var groups = Enum.GetNames(typeof(MDPartsDatabaseItem.Enums.ProductGroup)).ToList();
            var subGroups = Enum.GetNames(typeof(MDPartsDatabaseItem.Enums.ProductSubGroup)).ToList();
            var topGroups = Enum.GetNames(typeof(MDPartsDatabaseItem.Enums.ProductTopGroup)).ToList();

            results["success"] = true;
            results["productGroups"] = groups;
            results["productSubGroups"] = subGroups;
            results["productTopGroups"] = topGroups;
        }}
        catch (Exception ex)
        {{
            results["success"] = false;
            results["error"] = ex.Message;
        }}

        string json = Newtonsoft.Json.JsonConvert.SerializeObject(results, Newtonsoft.Json.Formatting.Indented);
        File.WriteAllText(@"{{{{RESULT_PATH}}}}", json);
    }}
}}
'''
    return _execute_script(script)


# =============================================================================
# SETTINGS API (Direct typed access)
# =============================================================================

def settings_get_string(setting_path: str, index: int = 0) -> dict:
    """
    Get a string setting from EPLAN.

    Args:
        setting_path: Full setting path (e.g., "USER.TrDMProject.UserData.Longname")
        index: Setting index (default 0)

    Returns:
        dict with setting value
    """
    script = f'''using System;
using System.IO;
using System.Collections.Generic;
using Eplan.EplApi.Base;
using Eplan.EplApi.Scripting;

public class SettingsGetStr_{uuid.uuid4().hex[:6]}
{{
    [Start]
    public void Run()
    {{
        var results = new Dictionary<string, object>();

        try
        {{
            var settings = new Settings();
            string value = settings.GetStringSetting("{setting_path}", {index});
            results["success"] = true;
            results["value"] = value;
            results["type"] = "string";
        }}
        catch (Exception ex)
        {{
            results["success"] = false;
            results["error"] = ex.Message;
        }}

        string json = Newtonsoft.Json.JsonConvert.SerializeObject(results);
        File.WriteAllText(@"{{{{RESULT_PATH}}}}", json);
    }}
}}
'''
    return _execute_script(script)


def settings_set_string(setting_path: str, value: str, index: int = 0) -> dict:
    """
    Set a string setting in EPLAN.

    Args:
        setting_path: Full setting path
        value: Value to set
        index: Setting index (default 0)

    Returns:
        dict with success status
    """
    script = f'''using System;
using System.IO;
using System.Collections.Generic;
using Eplan.EplApi.Base;
using Eplan.EplApi.Scripting;

public class SettingsSetStr_{uuid.uuid4().hex[:6]}
{{
    [Start]
    public void Run()
    {{
        var results = new Dictionary<string, object>();

        try
        {{
            var settings = new Settings();
            settings.SetStringSetting("{setting_path}", "{value}", {index});
            results["success"] = true;
        }}
        catch (Exception ex)
        {{
            results["success"] = false;
            results["error"] = ex.Message;
        }}

        string json = Newtonsoft.Json.JsonConvert.SerializeObject(results);
        File.WriteAllText(@"{{{{RESULT_PATH}}}}", json);
    }}
}}
'''
    return _execute_script(script)


def settings_get_bool(setting_path: str, index: int = 0) -> dict:
    """
    Get a boolean setting from EPLAN.

    Args:
        setting_path: Full setting path
        index: Setting index (default 0)

    Returns:
        dict with setting value
    """
    script = f'''using System;
using System.IO;
using System.Collections.Generic;
using Eplan.EplApi.Base;
using Eplan.EplApi.Scripting;

public class SettingsGetBool_{uuid.uuid4().hex[:6]}
{{
    [Start]
    public void Run()
    {{
        var results = new Dictionary<string, object>();

        try
        {{
            var settings = new Settings();
            bool value = settings.GetBoolSetting("{setting_path}", {index});
            results["success"] = true;
            results["value"] = value;
            results["type"] = "bool";
        }}
        catch (Exception ex)
        {{
            results["success"] = false;
            results["error"] = ex.Message;
        }}

        string json = Newtonsoft.Json.JsonConvert.SerializeObject(results);
        File.WriteAllText(@"{{{{RESULT_PATH}}}}", json);
    }}
}}
'''
    return _execute_script(script)


def settings_set_bool(setting_path: str, value: bool, index: int = 0) -> dict:
    """
    Set a boolean setting in EPLAN.

    Args:
        setting_path: Full setting path
        value: Value to set
        index: Setting index (default 0)

    Returns:
        dict with success status
    """
    value_str = "true" if value else "false"
    script = f'''using System;
using System.IO;
using System.Collections.Generic;
using Eplan.EplApi.Base;
using Eplan.EplApi.Scripting;

public class SettingsSetBool_{uuid.uuid4().hex[:6]}
{{
    [Start]
    public void Run()
    {{
        var results = new Dictionary<string, object>();

        try
        {{
            var settings = new Settings();
            settings.SetBoolSetting("{setting_path}", {value_str}, {index});
            results["success"] = true;
        }}
        catch (Exception ex)
        {{
            results["success"] = false;
            results["error"] = ex.Message;
        }}

        string json = Newtonsoft.Json.JsonConvert.SerializeObject(results);
        File.WriteAllText(@"{{{{RESULT_PATH}}}}", json);
    }}
}}
'''
    return _execute_script(script)


def settings_get_int(setting_path: str, index: int = 0) -> dict:
    """
    Get an integer setting from EPLAN.

    Args:
        setting_path: Full setting path
        index: Setting index (default 0)

    Returns:
        dict with setting value
    """
    script = f'''using System;
using System.IO;
using System.Collections.Generic;
using Eplan.EplApi.Base;
using Eplan.EplApi.Scripting;

public class SettingsGetInt_{uuid.uuid4().hex[:6]}
{{
    [Start]
    public void Run()
    {{
        var results = new Dictionary<string, object>();

        try
        {{
            var settings = new Settings();
            int value = settings.GetNumericSetting("{setting_path}", {index});
            results["success"] = true;
            results["value"] = value;
            results["type"] = "int";
        }}
        catch (Exception ex)
        {{
            results["success"] = false;
            results["error"] = ex.Message;
        }}

        string json = Newtonsoft.Json.JsonConvert.SerializeObject(results);
        File.WriteAllText(@"{{{{RESULT_PATH}}}}", json);
    }}
}}
'''
    return _execute_script(script)


def settings_set_int(setting_path: str, value: int, index: int = 0) -> dict:
    """
    Set an integer setting in EPLAN.

    Args:
        setting_path: Full setting path
        value: Value to set
        index: Setting index (default 0)

    Returns:
        dict with success status
    """
    script = f'''using System;
using System.IO;
using System.Collections.Generic;
using Eplan.EplApi.Base;
using Eplan.EplApi.Scripting;

public class SettingsSetInt_{uuid.uuid4().hex[:6]}
{{
    [Start]
    public void Run()
    {{
        var results = new Dictionary<string, object>();

        try
        {{
            var settings = new Settings();
            settings.SetNumericSetting("{setting_path}", {value}, {index});
            results["success"] = true;
        }}
        catch (Exception ex)
        {{
            results["success"] = false;
            results["error"] = ex.Message;
        }}

        string json = Newtonsoft.Json.JsonConvert.SerializeObject(results);
        File.WriteAllText(@"{{{{RESULT_PATH}}}}", json);
    }}
}}
'''
    return _execute_script(script)


def settings_get_double(setting_path: str, index: int = 0) -> dict:
    """
    Get a double/float setting from EPLAN.

    Args:
        setting_path: Full setting path
        index: Setting index (default 0)

    Returns:
        dict with setting value
    """
    script = f'''using System;
using System.IO;
using System.Collections.Generic;
using Eplan.EplApi.Base;
using Eplan.EplApi.Scripting;

public class SettingsGetDbl_{uuid.uuid4().hex[:6]}
{{
    [Start]
    public void Run()
    {{
        var results = new Dictionary<string, object>();

        try
        {{
            var settings = new Settings();
            double value = settings.GetDoubleSetting("{setting_path}", {index});
            results["success"] = true;
            results["value"] = value;
            results["type"] = "double";
        }}
        catch (Exception ex)
        {{
            results["success"] = false;
            results["error"] = ex.Message;
        }}

        string json = Newtonsoft.Json.JsonConvert.SerializeObject(results);
        File.WriteAllText(@"{{{{RESULT_PATH}}}}", json);
    }}
}}
'''
    return _execute_script(script)


def settings_set_double(setting_path: str, value: float, index: int = 0) -> dict:
    """
    Set a double/float setting in EPLAN.

    Args:
        setting_path: Full setting path
        value: Value to set
        index: Setting index (default 0)

    Returns:
        dict with success status
    """
    script = f'''using System;
using System.IO;
using System.Collections.Generic;
using Eplan.EplApi.Base;
using Eplan.EplApi.Scripting;

public class SettingsSetDbl_{uuid.uuid4().hex[:6]}
{{
    [Start]
    public void Run()
    {{
        var results = new Dictionary<string, object>();

        try
        {{
            var settings = new Settings();
            settings.SetDoubleSetting("{setting_path}", {value}, {index});
            results["success"] = true;
        }}
        catch (Exception ex)
        {{
            results["success"] = false;
            results["error"] = ex.Message;
        }}

        string json = Newtonsoft.Json.JsonConvert.SerializeObject(results);
        File.WriteAllText(@"{{{{RESULT_PATH}}}}", json);
    }}
}}
'''
    return _execute_script(script)


# =============================================================================
# PATH MAP (Variable substitution)
# =============================================================================

def pathmap_substitute(path_with_variables: str) -> dict:
    """
    Substitute EPLAN path variables in a string.

    Args:
        path_with_variables: Path with EPLAN variables (e.g., "$(PROJECTPATH)")

    Common variables:
        $(PROJECTPATH) - Current project path
        $(PROJECTNAME) - Current project name
        $(DOC) - Documents folder
        $(ELOGIN) - Current user login
        $(MD_MACROS) - Macros master data path
        $(MD_PARTS) - Parts master data path

    Returns:
        dict with substituted path
    """
    # Escape the path for C# string
    escaped_path = path_with_variables.replace("\\", "\\\\")

    script = f'''using System;
using System.IO;
using System.Collections.Generic;
using Eplan.EplApi.Base;
using Eplan.EplApi.Scripting;

public class PathMap_{uuid.uuid4().hex[:6]}
{{
    [Start]
    public void Run()
    {{
        var results = new Dictionary<string, object>();

        try
        {{
            string substituted = PathMap.SubstitutePath(@"{escaped_path}");
            results["success"] = true;
            results["original"] = @"{escaped_path}";
            results["substituted"] = substituted;
        }}
        catch (Exception ex)
        {{
            results["success"] = false;
            results["error"] = ex.Message;
        }}

        string json = Newtonsoft.Json.JsonConvert.SerializeObject(results);
        File.WriteAllText(@"{{{{RESULT_PATH}}}}", json);
    }}
}}
'''
    return _execute_script(script)


def pathmap_get_common_paths() -> dict:
    """
    Get all common EPLAN path variables and their current values.

    Returns:
        dict with path variables and values
    """
    script = f'''using System;
using System.IO;
using System.Collections.Generic;
using Eplan.EplApi.Base;
using Eplan.EplApi.Scripting;

public class PathMapAll_{uuid.uuid4().hex[:6]}
{{
    [Start]
    public void Run()
    {{
        var results = new Dictionary<string, object>();
        var paths = new Dictionary<string, string>();

        string[] variables = new string[]
        {{
            "$(PROJECTPATH)",
            "$(PROJECTNAME)",
            "$(DOC)",
            "$(ELOGIN)",
            "$(MD_MACROS)",
            "$(MD_PARTS)",
            "$(MD_SYMBOLS)",
            "$(MD_FORMS)",
            "$(MD_SCHEMES)",
            "$(MD_IMAGES)",
            "$(TEMPPATH)",
            "$(USERSETTINGSPATH)"
        }};

        try
        {{
            foreach (var v in variables)
            {{
                try
                {{
                    paths[v] = PathMap.SubstitutePath(v);
                }}
                catch
                {{
                    paths[v] = "(not available)";
                }}
            }}

            results["success"] = true;
            results["paths"] = paths;
        }}
        catch (Exception ex)
        {{
            results["success"] = false;
            results["error"] = ex.Message;
        }}

        string json = Newtonsoft.Json.JsonConvert.SerializeObject(results, Newtonsoft.Json.Formatting.Indented);
        File.WriteAllText(@"{{{{RESULT_PATH}}}}", json);
    }}
}}
'''
    return _execute_script(script)


# =============================================================================
# CUSTOM SCRIPT EXECUTION
# =============================================================================

def execute_custom_script(script_code: str) -> dict:
    """
    Execute a custom C# script in EPLAN.

    The script should write results to a JSON file at the path specified by
    the {{RESULT_PATH}} placeholder.

    Args:
        script_code: Complete C# script code with {{RESULT_PATH}} placeholder

    Returns:
        dict with script results

    Example script:
        using System;
        using System.IO;
        using System.Collections.Generic;
        using Eplan.EplApi.Scripting;

        public class MyScript
        {
            [Start]
            public void Run()
            {
                var results = new Dictionary<string, object>();
                results["success"] = true;
                results["message"] = "Hello from EPLAN!";

                string json = Newtonsoft.Json.JsonConvert.SerializeObject(results);
                File.WriteAllText(@"{{RESULT_PATH}}", json);
            }
        }
    """
    return _execute_script(script_code)
