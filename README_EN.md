<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0.0-blue.svg" alt="Version">
  <img src="https://img.shields.io/badge/Python-3.8+-green.svg" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen.svg" alt="PRs Welcome">
</p>

<p align="center">
  <a href="README.md">简体中文</a> | 
  <a href="README_EN.md">English</a> | 
  <a href="README_TW.md">繁體中文</a>
</p>

<h1 align="center">🔨 MarkForge</h1>

<p align="center">
  <strong>Lightweight Markdown Intelligent Conversion Engine</strong>
</p>

<p align="center">
  Convert Markdown to HTML, PDF, DOCX, PPTX and more with a single command<br>
  Zero Dependencies Core · Multiple Themes · Syntax Highlighting · Batch Conversion
</p>

---

## 🎉 Introduction

**MarkForge** is a lightweight, zero-dependency Markdown intelligent conversion engine. It helps you quickly convert Markdown documents to various formats, including HTML, PDF, Word documents, PowerPoint presentations, and more.

### 💡 Problems We Solve

- 📄 **Tedious Format Conversion**: Manually copying and pasting to Word/PPT is inefficient
- 🎨 **Inconsistent Styling**: Different tools produce documents with varying styles
- 📦 **Bloated Tools**: Existing tools have complex dependencies and large sizes
- 🔄 **Difficult Batch Processing**: Converting large numbers of documents requires manual work

### ✨ Unique Highlights

- 🚀 **Zero-Dependency Core**: Basic functionality requires no third-party libraries
- 🎨 **5 Built-in Themes**: default, dark, github, notion, solarized
- 📊 **Smart TOC Generation**: Automatically extracts headings for navigation
- 💻 **Code Highlighting Support**: Preserves code block formatting and language tags
- 📑 **Multi-Format Output**: HTML, PDF, DOCX, PPTX, TXT, RTF
- ⚡ **Batch Conversion**: Support for processing entire directories
- 🔧 **Highly Customizable**: Support for custom CSS, templates, and more

---

## ✨ Core Features

### 📄 Multi-Format Support

| Format | Description | Dependencies |
|--------|-------------|--------------|
| **HTML** | Styled web documents | None |
| **PDF** | Printable PDF documents | weasyprint (optional) |
| **DOCX** | Word documents | python-docx (optional) |
| **PPTX** | PowerPoint presentations | python-pptx (optional) |
| **TXT** | Plain text | None |
| **RTF** | Rich Text Format | None |

### 🎨 Built-in Themes

- **default** - Clean default theme
- **dark** - Dark mode for eye protection
- **github** - GitHub-style theme
- **notion** - Notion-style theme
- **solarized** - Solarized color scheme

### 💻 Markdown Support

- ✅ Headings (H1-H6)
- ✅ Paragraphs and line breaks
- ✅ **Bold**, *italic*, ~~strikethrough~~
- ✅ Ordered/unordered lists
- ✅ Code blocks and inline code
- ✅ Blockquotes
- ✅ Tables
- ✅ Links and images
- ✅ Horizontal rules
- ✅ YAML Front Matter

---

## 🚀 Quick Start

### 📋 Requirements

- Python 3.8 or higher
- pip package manager

### 📦 Installation

```bash
# Basic installation (zero dependencies)
pip install markforge

# Install PDF support
pip install markforge[pdf]

# Install Word support
pip install markforge[docx]

# Install PowerPoint support
pip install markforge[pptx]

# Install all optional dependencies
pip install markforge[all]
```

### 🔨 Basic Usage

```bash
# Convert to HTML
markforge input.md output.html

# Convert to PDF (dark theme)
markforge input.md output.pdf --theme dark

# Convert to Word document
markforge input.md output.docx

# Convert to PowerPoint presentation
markforge input.md output.pptx

# Batch convert entire directory
markforge ./docs ./output --batch --format html

# Disable table of contents
markforge input.md output.html --no-toc

# JSON output
markforge input.md output.html --json
```

### 🐍 Python API

```python
from markforge import MarkForgeConverter, OutputFormat

# Create converter
converter = MarkForgeConverter()

# Load Markdown file
converter.load_file("input.md")

# Convert to HTML
html = converter.convert(OutputFormat.HTML)

# Save to file
converter.convert_to_file("output.html", OutputFormat.HTML)

# Batch conversion
MarkForgeConverter.batch_convert(
    input_dir="./docs",
    output_dir="./output",
    output_format=OutputFormat.HTML
)
```

---

## 📖 Detailed Usage Guide

### 📝 Markdown Format

MarkForge supports standard Markdown syntax with YAML Front Matter:

```markdown
---
title: Document Title
author: Author Name
date: 2024-01-01
---

# Content Starts Here

Content...
```

### 🎨 Theme Customization

#### Using Built-in Themes

```bash
markforge input.md output.html --theme github
```

#### Custom CSS

```bash
markforge input.md output.html --css custom.css
```

### 📊 PPTX Presentations

Use `---` to separate slides:

```markdown
# First Slide Title

- Point one
- Point two
- Point three

---

# Second Slide Title

- Point one
- Point two
```

### ⚙️ Command Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `-f, --format` | Output format | html |
| `-t, --theme` | Theme name | default |
| `--title` | Document title | Read from Front Matter |
| `--author` | Document author | Read from Front Matter |
| `--no-toc` | Disable TOC | false |
| `--no-highlight` | Disable code highlighting | false |
| `--batch` | Batch conversion mode | false |
| `--css` | Custom CSS file | - |
| `--page-size` | PDF page size | A4 |
| `--margin` | PDF margin | 20mm |
| `--json` | JSON format output | false |

---

## 💡 Design Philosophy & Roadmap

### 🧠 Design Principles

1. **Zero Dependencies First**: Core functionality requires no third-party libraries
2. **Progressive Enhancement**: Optional dependencies provide richer features
3. **Batteries Included**: Reasonable defaults without complex setup
4. **Extensibility**: Support for custom themes, templates, and styles

### 🔮 Roadmap

#### v1.1.0 (Planned)

- [ ] More syntax highlighting themes
- [ ] Math formula support (LaTeX)
- [ ] Mermaid diagram support
- [ ] Custom template system

#### v1.2.0 (Planned)

- [ ] Live preview server
- [ ] GUI interface
- [ ] Plugin system
- [ ] More output formats (EPUB, ODT)

#### v2.0.0 (Future)

- [ ] AI-powered layout optimization
- [ ] Multi-language document support
- [ ] Collaborative editing features

---

## 📦 Packaging & Deployment

### 🐍 PyPI Publishing

```bash
# Install build tools
pip install build twine

# Build
python -m build

# Upload to PyPI
twine upload dist/*
```

### 📦 Executable Packaging

```bash
# Using PyInstaller
pip install pyinstaller

# Package as single file
pyinstaller --onefile markforge/cli.py --name markforge

# Package as directory
pyinstaller markforge/cli.py --name markforge
```

---

## 🤝 Contributing

We welcome all forms of contributions!

### 📝 Submitting PRs

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'feat: add some feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Submit a Pull Request

### 🐛 Reporting Issues

Please use [GitHub Issues](https://github.com/gitstq/MarkForge/issues) to report problems.

When submitting an Issue, please include:

- Operating system and Python version
- Steps to reproduce
- Expected behavior and actual behavior
- Relevant logs or screenshots

### 📋 Commit Convention

Use [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation update
- `style:` Code formatting
- `refactor:` Code refactoring
- `test:` Test related
- `chore:` Build/tool related

---

## 📄 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2024 MarkForge Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

<p align="center">
  Made with ❤️ by MarkForge Team
</p>

<p align="center">
  <a href="https://github.com/gitstq/MarkForge">⭐ Star</a> ·
  <a href="https://github.com/gitstq/MarkForge/issues">🐛 Issues</a> ·
  <a href="https://github.com/gitstq/MarkForge/pulls">🤝 Pull Requests</a>
</p>
