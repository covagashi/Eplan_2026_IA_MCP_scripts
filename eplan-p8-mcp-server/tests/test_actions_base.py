import pytest
from mcp_server.actions._base import _build_action

def test_build_action_basic():
    """Test building action string with no parameters."""
    assert _build_action("TestAction") == "TestAction"

def test_build_action_params():
    """Test building action string with multiple string parameters."""
    # Note: dict order is preserved in Python 3.7+
    result = _build_action("TestAction", Param1="Value1", Param2="Value2")
    assert result == "TestAction /Param1:Value1 /Param2:Value2"

def test_build_action_boolean():
    """Test boolean parameter conversion (True -> 1, False -> 0)."""
    result = _build_action("TestAction", BoolTrue=True, BoolFalse=False)
    assert result == "TestAction /BoolTrue:1 /BoolFalse:0"

def test_build_action_skip_empty():
    """Test that None and empty strings are skipped."""
    result = _build_action("TestAction", Empty="", Null=None, Valid="OK")
    assert result == "TestAction /Valid:OK"

def test_build_action_quoting():
    """Test that strings with spaces are quoted, but not if already quoted."""
    assert _build_action("TestAction", Space="Value with space") == 'TestAction /Space:"Value with space"'
    assert _build_action("TestAction", AlreadyQuoted='"Already Quoted"') == 'TestAction /AlreadyQuoted:"Already Quoted"'

def test_build_action_integer():
    """Test handling of integer parameters."""
    assert _build_action("TestAction", Num=123) == "TestAction /Num:123"
