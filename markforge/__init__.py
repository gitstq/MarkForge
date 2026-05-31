"""
MarkForge - Lightweight Markdown Intelligent Conversion Engine
轻量级Markdown智能转换引擎

A powerful CLI tool for converting Markdown to multiple formats:
- HTML with syntax highlighting
- PDF with custom themes
- DOCX with templates
- PPTX from markdown slides
- And more...

Author: MarkForge Team
License: MIT
Version: 1.0.0
"""

__version__ = "1.0.0"
__author__ = "MarkForge Team"
__description__ = "Lightweight Markdown Intelligent Conversion Engine"

from .converter import MarkForgeConverter
from .cli import main

__all__ = ["MarkForgeConverter", "main"]
