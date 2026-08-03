"""Tests for the crews serving module."""

import importlib
from pathlib import Path
import sys


def test_serve_crews_import_does_not_require_model_artifact(monkeypatch) -> None:
    """Importing the module should not fail before the model file exists."""
    monkeypatch.setattr(Path, "exists", lambda self: False)
    sys.modules.pop("mlstudio.serve_crews", None)

    module = importlib.import_module("mlstudio.serve_crews")

    assert module.app is not None


def test_health_reports_expected_fields(monkeypatch) -> None:
    """Health endpoint helper should expose status and model metadata."""
    module = importlib.import_module("mlstudio.serve_crews")
    monkeypatch.setattr(Path, "exists", lambda self: True)

    result = module.health()

    assert result["status"] == "ok"
    assert result["model_path"] == str(module.MODEL_PATH)
    assert result["model_exists"] is True
    assert result["model_loaded"] is False
