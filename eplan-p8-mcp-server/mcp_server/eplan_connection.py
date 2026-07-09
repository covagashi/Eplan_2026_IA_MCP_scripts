"""
EPLAN Connection Manager
Connection to EPLAN via Remoting API (pythonnet/CLR)

Requirements:
- EPLAN installed
- pip install pythonnet
"""

import sys
import os
import logging
import re
import json
import time
import uuid
from typing import Optional, List

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("EPLAN")

# Select the pythonnet runtime before the first `import clr`.
# EPLAN 2027+ targets .NET 8 (net8.0) and requires coreclr.
# EPLAN 2026 and older are .NET Framework and use the default netfx runtime.
# Detection heuristic: presence of Grpc.Net.Client.dll (a .NET 8-only assembly)
# in the EPLAN Bin signals a .NET 8 build.
def _select_dotnet_runtime() -> None:
    _candidate_bins = [
        rf"C:\Program Files\EPLAN\Platform\{v}\Bin"
        for v in ["2027.0.1", "2027.0.3", "2027.0", "2026.0.3", "2026.0.1", "2026.0",
                  "2025.0.3", "2025.0", "2024.0", "2023.0.3", "2023.0"]
    ]
    runtime = "default"
    for _bin in _candidate_bins:
        if os.path.exists(os.path.join(_bin, "Grpc.Net.Client.dll")):
            runtime = "coreclr"
            break
        if os.path.exists(_bin):
            break  # Found an EPLAN install that is NOT .NET 8 — stop looking
    try:
        from pythonnet import load as _pnet_load
        if runtime == "coreclr":
            _pnet_load("coreclr")
            logger.info("pythonnet: coreclr (.NET 8) runtime selected (EPLAN 2027+)")
        else:
            logger.info("pythonnet: using default runtime (EPLAN 2026 or older)")
    except Exception as _pnet_err:
        logger.warning(f"pythonnet: runtime selection failed ({_pnet_err})")

_select_dotnet_runtime()


class EPLANConnectionManager:
    """Manages the connection to EPLAN via Remote Client API."""

    DEFAULT_PORT = "49152"
    DEFAULT_HOST = "localhost"
    TIMEOUT_SECONDS = 10

    def __init__(self, target_version: str = "2026"):
        self.target_version = target_version
        self.client = None
        self.connected = False
        self.port = self.DEFAULT_PORT
        self.last_error = ""
        self._clr_initialized = self._setup_api()

    def _setup_api(self) -> bool:
        """Load EPLAN DLLs via pythonnet."""
        try:
            import clr

            # Search for EPLAN installation
            # Target version paths first, then fallbacks
            paths = [
                rf"C:\Program Files\EPLAN\Platform\{self.target_version}.0\Bin",
                rf"C:\Program Files\EPLAN\Platform\{self.target_version}.0.3\Bin",
                rf"C:\Program Files\EPLAN\Platform\{self.target_version}.0.1\Bin",
                r"C:\Program Files\EPLAN\Platform\2025.0\Bin",
                r"C:\Program Files\EPLAN\Platform\2025.0.3\Bin",
                r"C:\Program Files\EPLAN\Platform\2024.0\Bin",
                r"C:\Program Files\EPLAN\Platform\2023.0.3\Bin",
                r"C:\Program Files\EPLAN\Platform\2023.0\Bin",
            ]

            eplan_path = None
            for p in paths:
                if os.path.exists(p):
                    eplan_path = p
                    break

            if not eplan_path:
                self.last_error = "EPLAN not found in Program Files"
                logger.error(self.last_error)
                return False

            if eplan_path not in sys.path:
                sys.path.append(eplan_path)

            # Add additional dependency paths
            dep_paths = [
                r"C:\Program Files\EPLAN\Common\IdentityClient",
                os.path.join(os.path.dirname(eplan_path), "Bin"),
            ]
            for dp in dep_paths:
                if os.path.exists(dp) and dp not in sys.path:
                    sys.path.append(dp)

            # Load EPLAN DLLs via LoadFrom so .NET probes the EPLAN Bin directory
            # for dependencies (e.g. Grpc.Core), preventing version conflicts with
            # any system-wide or Python-env assembly of the same name.
            import System.Reflection
            import System

            def _resolve_from_eplan(sender, args):
                asm_name = System.Reflection.AssemblyName(args.Name).Name
                candidate = os.path.join(eplan_path, asm_name + ".dll")
                if os.path.exists(candidate):
                    return System.Reflection.Assembly.LoadFrom(candidate)
                return None

            System.AppDomain.CurrentDomain.AssemblyResolve += _resolve_from_eplan

            for dll in ("Eplan.EplApi.Starteru.dll", "Eplan.EplApi.RemoteClientu.dll", "Eplan.EplApi.Remotingu.dll"):
                dll_path = os.path.join(eplan_path, dll)
                if os.path.exists(dll_path):
                    System.Reflection.Assembly.LoadFrom(dll_path)

            clr.AddReference("Eplan.EplApi.Starteru")
            clr.AddReference("Eplan.EplApi.RemoteClientu")
            clr.AddReference("Eplan.EplApi.Remotingu")

            logger.info(f"EPLAN API loaded from: {eplan_path}")
            return True

        except ImportError:
            self.last_error = "pythonnet not installed. Run: pip install pythonnet"
            logger.error(self.last_error)
            return False
        except Exception as e:
            self.last_error = f"Failed to load EPLAN API: {e}"
            logger.error(self.last_error)
            return False

    def get_active_servers(self) -> list:
        """Get active EPLAN servers on the local machine."""
        if not self._clr_initialized:
            self._clr_initialized = self._setup_api()
        if not self._clr_initialized:
            return []

        try:
            from Eplan.EplApi.RemoteClient import EplanRemoteClient, EplanServerData
            from System.Collections.Generic import List as NetList

            temp = EplanRemoteClient()
            # out parameter in pythonnet
            servers = NetList[EplanServerData]()
            temp.GetActiveEplanServersOnLocalMachine(servers)

            result = []
            for s in servers:
                result.append({
                    "version": str(s.EplanVersion),
                    "variant": str(s.EplanVariant),
                    "port": str(s.ServerPort)
                })
                logger.info(f"Found: EPLAN {s.EplanVersion} on port {s.ServerPort}")

            temp.Dispose()
            return result

        except Exception as e:
            self.last_error = f"Error getting servers: {e}"
            logger.error(self.last_error)
            return []

    def connect(self, host: str = None, port: str = None) -> dict:
        """Connect to an EPLAN instance."""
        if not self._clr_initialized:
            self._clr_initialized = self._setup_api()
        if not self._clr_initialized:
            return {"success": False, "message": self.last_error}

        host = host or self.DEFAULT_HOST

        try:
            from Eplan.EplApi.RemoteClient import EplanRemoteClient
            import System

            # Auto-detect port if not specified
            if not port:
                servers = self.get_active_servers()
                if servers:
                    port = servers[-1]["port"]
                    logger.info(f"Auto-detected port: {port}")
                else:
                    port = self.DEFAULT_PORT

            self.port = port
            logger.info(f"Connecting to {host}:{port}...")

            self.client = EplanRemoteClient()
            timeout = System.TimeSpan.FromSeconds(self.TIMEOUT_SECONDS)
            self.client.Connect(host, port, timeout)

            if self.client.Ping():
                self.connected = True
                logger.info(f"Connected to EPLAN at {host}:{port}")
                return {
                    "success": True,
                    "message": f"Connected to EPLAN at {host}:{port}",
                    "port": port
                }
            else:
                return {"success": False, "message": "Connected but ping failed"}

        except Exception as e:
            self.last_error = f"Connection failed: {e}"
            logger.error(self.last_error)
            self.connected = False
            return {"success": False, "message": self.last_error}

    def ping(self) -> dict:
        """Check if EPLAN is responding."""
        if not self.connected or not self.client:
            return {"alive": False, "message": "Not connected"}

        try:
            alive = self.client.Ping()
            return {
                "alive": alive,
                "message": "EPLAN responding" if alive else "No response"
            }
        except Exception as e:
            self.connected = False
            return {"alive": False, "message": f"Ping failed: {e}"}

    def execute_action(self, action: str, quiet_mode: bool = False) -> dict:
        """
        Execute an EPLAN action.

        Args:
            action: The action string to execute
            quiet_mode: If True, suppresses all EPLAN dialogs during execution using a C# script.
        """
        if not self.connected or not self.client:
            return {"success": False, "message": "Not connected"}

        try:
            # Parse the action name (first word before any space or '/')
            action_name_match = re.match(r'^([^\s/]+)', action)
            action_name = action_name_match.group(1) if action_name_match else action
            action_name_lower = action_name.lower()

            # RegisterScript, ExecuteScript, and UnregisterScript MUST run directly
            # to avoid infinite recursion. Also run directly if quiet_mode is False.
            if action_name_lower in ("registerscript", "executescript", "unregisterscript") or not quiet_mode:
                logger.info(f"Executing directly: {action}")
                self.client.SynchronousMode = True
                self.client.ExecuteAction(action)
                return {"success": True, "message": f"Executed directly: {action}", "action": action}

            # Parse parameters
            params = {}
            matches = re.finditer(r'/([a-zA-Z0-9_]+):(?:("([^"]*)"|([^\s]*)))', action)
            for m in matches:
                key = m.group(1)
                val = m.group(3) if m.group(2).startswith('"') else m.group(4)
                params[key] = val

            # Generate directories
            base_dir = os.path.dirname(os.path.abspath(__file__))
            script_dir = os.path.join(base_dir, "scripts", "generated")
            results_dir = os.path.join(base_dir, "scripts", "results")
            os.makedirs(script_dir, exist_ok=True)
            os.makedirs(results_dir, exist_ok=True)

            exec_id = str(uuid.uuid4())[:8]
            script_path = os.path.join(script_dir, f"exec_action_{exec_id}.cs")
            result_path = os.path.join(results_dir, f"exec_result_{exec_id}.json")

            # C# parameters generation
            acc_parameters_code = ""
            check_keys = ["PROJECT", "PROJECTS", "PAGES", "LAYOUTSPACES", "PropertyValue", "value", "Value", "Result", "Output", "Success", "Count", "Error", "Message"]
            for key, val in params.items():
                escaped_val = val.replace("\\", "\\\\").replace('"', '\\"')
                acc_parameters_code += f'\n                acc.AddParameter("{key}", "{escaped_val}");'
                if key not in check_keys:
                    check_keys.append(key)

            check_keys_code = ", ".join([f'"{k}"' for k in check_keys])
            escaped_result_path = result_path.replace("\\", "\\\\")

            # C# Script Content
            script_content = f"""using System;
using System.IO;
using System.Collections.Generic;
using Eplan.EplApi.ApplicationFramework;
using Eplan.EplApi.Scripting;

public class QuietExecute_{exec_id}
{{
    [Start]
    public void Run()
    {{
        var results = new Dictionary<string, object>();
        try
        {{
            using (var qm = new QuietModeStep(QuietModes.ShowNoDialogs))
            {{
                var acc = new ActionCallingContext();
                {acc_parameters_code}
                
                var cli = new CommandLineInterpreter();
                bool success = cli.Execute("{action_name}", acc);
                results["success"] = success;
                
                var returnParams = new Dictionary<string, string>();
                string[] checkKeys = new string[] {{ {check_keys_code} }};
                foreach (var key in checkKeys)
                {{
                    try
                    {{
                        string val = "";
                        acc.GetParameter(key, ref val);
                        if (!string.IsNullOrEmpty(val))
                        {{
                            returnParams[key] = val;
                        }}
                    }}
                    catch {{}}
                }}
                results["parameters"] = returnParams;
            }}
        }}
        catch (Exception ex)
        {{
            results["success"] = false;
            results["error"] = ex.Message;
        }}
        
        string json = Newtonsoft.Json.JsonConvert.SerializeObject(results);
        File.WriteAllText("{escaped_result_path}", json);
    }}
}}
"""
            # Write script to disk
            with open(script_path, "w", encoding="utf-8") as f:
                f.write(script_content)

            # Register script
            logger.info(f"Wrapping action via script: {action_name} (exec_id={exec_id})")
            reg_result = self.execute_action(f'RegisterScript /ScriptFile:"{script_path}"', quiet_mode=False)
            if not reg_result.get("success"):
                return {"success": False, "message": f"Failed to register execution script: {reg_result.get('message')}"}

            # Execute script
            exec_result = self.execute_action(f'ExecuteScript /ScriptFile:"{script_path}"', quiet_mode=False)
            if not exec_result.get("success"):
                return {"success": False, "message": f"Failed to execute action via script: {exec_result.get('message')}"}

            # Wait for result file
            timeout = 30.0
            start_time = time.time()
            while not os.path.exists(result_path):
                if time.time() - start_time > timeout:
                    return {"success": False, "message": "Timeout waiting for scripted action execution result"}
                time.sleep(0.1)

            # Read results
            time.sleep(0.05) # Small sleep to let OS release file lock
            with open(result_path, "r", encoding="utf-8") as f:
                res_data = json.load(f)

            return res_data

        except Exception as e:
            self.last_error = f"Scripted execution failed: {e}"
            logger.error(self.last_error)
            return {"success": False, "message": self.last_error, "action": action}

        finally:
            # Cleanup temp files
            try:
                if 'script_path' in locals() and os.path.exists(script_path):
                    self.execute_action(f'UnregisterScript /ScriptFile:"{script_path}"', quiet_mode=False)
                    os.remove(script_path)
            except Exception:
                pass
            try:
                if 'result_path' in locals() and os.path.exists(result_path):
                    os.remove(result_path)
            except Exception:
                pass

    def disconnect(self) -> dict:
        """Disconnect from EPLAN."""
        try:
            if self.client:
                self.client.Disconnect()
                self.client.Dispose()
                self.client = None
            self.connected = False
            logger.info("Disconnected")
            return {"success": True, "message": "Disconnected"}
        except Exception as e:
            return {"success": False, "message": f"Disconnect failed: {e}"}

    def get_status(self) -> dict:
        """Get current connection status."""
        return {
            "connected": self.connected,
            "api_loaded": self._clr_initialized,
            "port": self.port if self.connected else None,
            "last_error": self.last_error
        }


# Singleton
_manager: Optional[EPLANConnectionManager] = None


def get_manager(target_version: str = "2026") -> EPLANConnectionManager:
    global _manager
    if _manager is None or not _manager._clr_initialized:
        _manager = EPLANConnectionManager(target_version)
    return _manager
