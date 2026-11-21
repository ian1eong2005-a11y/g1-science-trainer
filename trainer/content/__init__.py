"""Question content registry. Importing the chapter modules registers their templates."""
import importlib

from .base import TEMPLATES, Question, Template

MODULES = ["ch01", "ch01w", "ch02", "ch02w", "ch03", "ch03w", "ch04", "ch04w", "ch05", "ch06", "ch07", "ch08", "ch09", "ch10", "ch11", "nlevel_specimen", "nlevel_past"]
for _m in MODULES:
    try:
        importlib.import_module(f"{__name__}.{_m}")
    except ModuleNotFoundError as e:                   # a chapter not written yet; any other import error is real
        if e.name != f"{__name__}.{_m}":
            raise

__all__ = ["TEMPLATES", "Question", "Template"]
