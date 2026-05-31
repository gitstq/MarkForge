#!/usr/bin/env python3
"""
MarkForge CLI - Command Line Interface
轻量级Markdown智能转换引擎命令行工具
"""

import argparse
import sys
import json
from pathlib import Path
from typing import Optional

from .converter import MarkForgeConverter, OutputFormat, ConversionOptions


def create_parser() -> argparse.ArgumentParser:
    """Create argument parser"""
    parser = argparse.ArgumentParser(
        prog="markforge",
        description="🔨 MarkForge - Lightweight Markdown Intelligent Conversion Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  markforge input.md output.html              Convert to HTML
  markforge input.md output.pdf --theme dark  Convert to PDF with dark theme
  markforge input.md output.docx              Convert to Word document
  markforge input.md output.pptx              Convert to PowerPoint slides
  markforge ./docs ./output --batch --format html  Batch convert

Supported formats: html, pdf, docx, pptx, txt, rtf
Built-in themes: default, dark, github, notion, solarized
        """
    )
    
    parser.add_argument(
        "input",
        help="Input markdown file or directory (for batch mode)"
    )
    
    parser.add_argument(
        "output",
        help="Output file or directory"
    )
    
    parser.add_argument(
        "-f", "--format",
        choices=["html", "pdf", "docx", "pptx", "txt", "rtf"],
        default="html",
        help="Output format (default: html)"
    )
    
    parser.add_argument(
        "-t", "--theme",
        choices=["default", "dark", "github", "notion", "solarized"],
        default="default",
        help="Theme for HTML/PDF output (default: default)"
    )
    
    parser.add_argument(
        "--title",
        help="Document title (overrides front matter)"
    )
    
    parser.add_argument(
        "--author",
        help="Document author"
    )
    
    parser.add_argument(
        "--no-toc",
        action="store_true",
        help="Disable table of contents"
    )
    
    parser.add_argument(
        "--no-highlight",
        action="store_true",
        help="Disable code syntax highlighting"
    )
    
    parser.add_argument(
        "--batch",
        action="store_true",
        help="Batch convert all .md files in input directory"
    )
    
    parser.add_argument(
        "--css",
        help="Custom CSS file for HTML/PDF output"
    )
    
    parser.add_argument(
        "--template",
        help="Custom template file"
    )
    
    parser.add_argument(
        "--page-size",
        choices=["A4", "A3", "Letter", "Legal"],
        default="A4",
        help="Page size for PDF output (default: A4)"
    )
    
    parser.add_argument(
        "--margin",
        default="20mm",
        help="Page margin for PDF output (default: 20mm)"
    )
    
    parser.add_argument(
        "-v", "--version",
        action="version",
        version="%(prog)s 1.0.0"
    )
    
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output result as JSON"
    )
    
    return parser


def main():
    """Main entry point"""
    parser = create_parser()
    args = parser.parse_args()
    
    # Map format string to enum
    format_map = {
        "html": OutputFormat.HTML,
        "pdf": OutputFormat.PDF,
        "docx": OutputFormat.DOCX,
        "pptx": OutputFormat.PPTX,
        "txt": OutputFormat.TXT,
        "rtf": OutputFormat.RTF
    }
    
    output_format = format_map[args.format]
    
    # Create conversion options
    options = ConversionOptions(
        output_format=output_format,
        theme=args.theme,
        include_toc=not args.no_toc,
        highlight_code=not args.no_highlight,
        title=args.title,
        author=args.author,
        page_size=args.page_size,
        margin=args.margin
    )
    
    # Load custom CSS if provided
    if args.css:
        css_path = Path(args.css)
        if css_path.exists():
            with open(css_path, "r", encoding="utf-8") as f:
                options.custom_css = f.read()
    
    try:
        if args.batch:
            # Batch conversion
            input_dir = Path(args.input)
            output_dir = Path(args.output)
            
            if not input_dir.is_dir():
                print(f"Error: {input_dir} is not a directory", file=sys.stderr)
                sys.exit(1)
            
            output_files = MarkForgeConverter.batch_convert(
                input_dir, output_dir, output_format, options
            )
            
            if args.json:
                result = {
                    "success": True,
                    "files_converted": len(output_files),
                    "output_files": [str(f) for f in output_files]
                }
                print(json.dumps(result, indent=2))
            else:
                print(f"✅ Converted {len(output_files)} files to {output_dir}")
        
        else:
            # Single file conversion
            input_path = Path(args.input)
            output_path = Path(args.output)
            
            if not input_path.exists():
                print(f"Error: File not found: {input_path}", file=sys.stderr)
                sys.exit(1)
            
            converter = MarkForgeConverter(options)
            converter.load_file(input_path)
            
            # Determine output format from extension if not specified
            if output_path.suffix:
                ext_format_map = {
                    ".html": OutputFormat.HTML,
                    ".htm": OutputFormat.HTML,
                    ".pdf": OutputFormat.PDF,
                    ".docx": OutputFormat.DOCX,
                    ".pptx": OutputFormat.PPTX,
                    ".txt": OutputFormat.TXT,
                    ".rtf": OutputFormat.RTF
                }
                detected_format = ext_format_map.get(output_path.suffix.lower())
                if detected_format:
                    output_format = detected_format
            
            result_path = converter.convert_to_file(output_path, output_format)
            
            if args.json:
                result = {
                    "success": True,
                    "input": str(input_path),
                    "output": str(result_path),
                    "format": output_format.value
                }
                print(json.dumps(result, indent=2))
            else:
                print(f"✅ Converted {input_path} → {result_path}")
    
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
