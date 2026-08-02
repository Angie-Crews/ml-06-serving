"""Tests for the serving module."""

import importlib
from pathlib import Path
import sys


def test_serve_case_import_does_not_require_model_artifact(monkeypatch) -> None:
    """Importing the serving module should not fail before a model artifact exists."""
    monkeypatch.setattr(Path, "exists", lambda self: False)
    sys.modules.pop("mlstudio.serve_case", None)

    module = importlib.import_module("mlstudio.serve_case")

    assert module.app is not None
