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
from typing import Optional, List

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("EPLAN")


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
            paths = [
                r"C:\Program Files\EPLAN\Platform\2023.0.3\Bin",
                r"C:\Program Files\EPLAN\Platform\2.9.4\Bin",
                rf"C:\Program Files\EPLAN\Platform\{self.target_version}.0\Bin",
                rf"C:\Program Files\EPLAN\Platform\{self.target_version}.0.3\Bin",
                r"C:\Program Files\EPLAN\Platform\2026.0\Bin",
                r"C:\Program Files\EPLAN\Platform\2025.0\Bin",
                r"C:\Program Files\EPLAN\Platform\2024.0\Bin",
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

    def execute_action(self, action: str) -> dict:
        """Execute an EPLAN action."""
        if not self.connected or not self.client:
            return {"success": False, "message": "Not connected"}

        try:
            logger.info(f"Executing: {action}")
            self.client.SynchronousMode = True
            self.client.ExecuteAction(action)
            return {"success": True, "message": f"Executed: {action}", "action": action}
        except Exception as e:
            self.last_error = f"Execution failed: {e}"
            logger.error(self.last_error)
            return {"success": False, "message": self.last_error, "action": action}

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
    if _manager is None:
        _manager = EPLANConnectionManager(target_version)
    return _manager
