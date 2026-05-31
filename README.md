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
  <strong>轻量级 Markdown 智能转换引擎</strong>
</p>

<p align="center">
  一键将 Markdown 转换为 HTML、PDF、DOCX、PPTX 等多种格式<br>
  零依赖核心 · 多主题支持 · 代码高亮 · 批量转换
</p>

---

## 🎉 项目介绍

**MarkForge** 是一个轻量级、零依赖的 Markdown 智能转换引擎。它可以帮助你快速将 Markdown 文档转换为多种格式，包括 HTML、PDF、Word 文档、PowerPoint 演示文稿等。

### 💡 解决的痛点

- 📄 **格式转换繁琐**：手动复制粘贴到 Word/PPT 效率低下
- 🎨 **样式不统一**：不同工具生成的文档风格各异
- 📦 **工具臃肿**：现有工具依赖复杂、体积庞大
- 🔄 **批量处理难**：大量文档转换需要手动操作

### ✨ 自研差异化亮点

- 🚀 **零依赖核心**：基础功能无需安装任何第三方库
- 🎨 **5 种内置主题**：default、dark、github、notion、solarized
- 📊 **智能目录生成**：自动提取标题生成目录导航
- 💻 **代码高亮支持**：保留代码块的格式和语言标识
- 📑 **多格式输出**：HTML、PDF、DOCX、PPTX、TXT、RTF
- ⚡ **批量转换**：支持整个目录的批量处理
- 🔧 **高度可定制**：支持自定义 CSS、模板等

---

## ✨ 核心特性

### 📄 多格式支持

| 格式 | 说明 | 依赖 |
|------|------|------|
| **HTML** | 带样式的网页文档 | 无 |
| **PDF** | 可打印的 PDF 文档 | weasyprint（可选） |
| **DOCX** | Word 文档 | python-docx（可选） |
| **PPTX** | PowerPoint 演示文稿 | python-pptx（可选） |
| **TXT** | 纯文本 | 无 |
| **RTF** | 富文本格式 | 无 |

### 🎨 内置主题

- **default** - 清爽默认主题
- **dark** - 暗色护眼主题
- **github** - GitHub 风格主题
- **notion** - Notion 风格主题
- **solarized** - Solarized 配色主题

### 💻 Markdown 支持

- ✅ 标题（H1-H6）
- ✅ 段落和换行
- ✅ **粗体**、*斜体*、~~删除线~~
- ✅ 有序/无序列表
- ✅ 代码块和行内代码
- ✅ 引用块
- ✅ 表格
- ✅ 链接和图片
- ✅ 水平分隔线
- ✅ YAML Front Matter

---

## 🚀 快速开始

### 📋 环境要求

- Python 3.8 或更高版本
- pip 包管理器

### 📦 安装

```bash
# 基础安装（零依赖）
pip install markforge

# 安装 PDF 支持
pip install markforge[pdf]

# 安装 Word 支持
pip install markforge[docx]

# 安装 PowerPoint 支持
pip install markforge[pptx]

# 安装所有可选依赖
pip install markforge[all]
```

### 🔨 基本使用

```bash
# 转换为 HTML
markforge input.md output.html

# 转换为 PDF（暗色主题）
markforge input.md output.pdf --theme dark

# 转换为 Word 文档
markforge input.md output.docx

# 转换为 PowerPoint 演示文稿
markforge input.md output.pptx

# 批量转换整个目录
markforge ./docs ./output --batch --format html

# 禁用目录生成
markforge input.md output.html --no-toc

# 使用 JSON 输出
markforge input.md output.html --json
```

### 🐍 Python API

```python
from markforge import MarkForgeConverter, OutputFormat

# 创建转换器
converter = MarkForgeConverter()

# 加载 Markdown 文件
converter.load_file("input.md")

# 转换为 HTML
html = converter.convert(OutputFormat.HTML)

# 保存到文件
converter.convert_to_file("output.html", OutputFormat.HTML)

# 批量转换
MarkForgeConverter.batch_convert(
    input_dir="./docs",
    output_dir="./output",
    output_format=OutputFormat.HTML
)
```

---

## 📖 详细使用指南

### 📝 Markdown 格式说明

MarkForge 支持标准 Markdown 语法，同时支持 YAML Front Matter：

```markdown
---
title: 文档标题
author: 作者名称
date: 2024-01-01
---

# 正文开始

内容...
```

### 🎨 主题定制

#### 使用内置主题

```bash
markforge input.md output.html --theme github
```

#### 自定义 CSS

```bash
markforge input.md output.html --css custom.css
```

### 📊 PPTX 演示文稿

使用 `---` 分隔幻灯片：

```markdown
# 第一张幻灯片标题

- 要点一
- 要点二
- 要点三

---

# 第二张幻灯片标题

- 要点一
- 要点二
```

### ⚙️ 命令行参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `-f, --format` | 输出格式 | html |
| `-t, --theme` | 主题名称 | default |
| `--title` | 文档标题 | 从 Front Matter 读取 |
| `--author` | 文档作者 | 从 Front Matter 读取 |
| `--no-toc` | 禁用目录 | false |
| `--no-highlight` | 禁用代码高亮 | false |
| `--batch` | 批量转换模式 | false |
| `--css` | 自定义 CSS 文件 | - |
| `--page-size` | PDF 页面大小 | A4 |
| `--margin` | PDF 页边距 | 20mm |
| `--json` | JSON 格式输出 | false |

---

## 💡 设计思路与迭代规划

### 🧠 设计理念

MarkForge 的设计遵循以下原则：

1. **零依赖优先**：核心功能不依赖任何第三方库
2. **渐进增强**：可选依赖提供更丰富的功能
3. **开箱即用**：合理的默认配置，无需复杂设置
4. **可扩展性**：支持自定义主题、模板和样式

### 🔮 迭代规划

#### v1.1.0（计划中）

- [ ] 更多代码高亮主题
- [ ] 数学公式支持（LaTeX）
- [ ] Mermaid 图表支持
- [ ] 自定义模板系统

#### v1.2.0（计划中）

- [ ] 实时预览服务器
- [ ] GUI 界面
- [ ] 插件系统
- [ ] 更多输出格式（EPUB、ODT）

#### v2.0.0（远期）

- [ ] AI 智能排版优化
- [ ] 多语言文档支持
- [ ] 协作编辑功能

---

## 📦 打包与部署指南

### 🐍 PyPI 发布

```bash
# 安装构建工具
pip install build twine

# 构建
python -m build

# 上传到 PyPI
twine upload dist/*
```

### 📦 可执行文件打包

```bash
# 使用 PyInstaller
pip install pyinstaller

# 打包为单文件
pyinstaller --onefile markforge/cli.py --name markforge

# 打包为目录
pyinstaller markforge/cli.py --name markforge
```

---

## 🤝 贡献指南

我们欢迎所有形式的贡献！

### 📝 提交 PR

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'feat: 添加某个特性'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交 Pull Request

### 🐛 报告问题

请使用 [GitHub Issues](https://github.com/gitstq/MarkForge/issues) 报告问题。

提交 Issue 时请包含：

- 操作系统和 Python 版本
- 复现步骤
- 期望行为和实际行为
- 相关日志或截图

### 📋 提交规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

- `feat:` 新功能
- `fix:` 修复问题
- `docs:` 文档更新
- `style:` 代码格式
- `refactor:` 代码重构
- `test:` 测试相关
- `chore:` 构建/工具相关

---

## 📄 开源协议说明

本项目采用 **MIT 协议** 开源。

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
