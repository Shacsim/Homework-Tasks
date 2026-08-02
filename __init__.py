"""Homework tasks package."""

try:
    from .Task1 import Mashina
except ImportError:  # Fallback for direct script execution
    from Task1 import Mashina

__all__ = ["Mashina"]
