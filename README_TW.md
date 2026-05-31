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
  <strong>輕量級 Markdown 智能轉換引擎</strong>
</p>

<p align="center">
  一鍵將 Markdown 轉換為 HTML、PDF、DOCX、PPTX 等多種格式<br>
  零依賴核心 · 多主題支援 · 程式碼高亮 · 批次轉換
</p>

---

## 🎉 專案介紹

**MarkForge** 是一個輕量級、零依賴的 Markdown 智能轉換引擎。它可以幫助你快速將 Markdown 文件轉換為多種格式，包括 HTML、PDF、Word 文件、PowerPoint 簡報等。

### 💡 解決的痛點

- 📄 **格式轉換繁瑣**：手動複製貼上到 Word/PPT 效率低下
- 🎨 **樣式不統一**：不同工具產生的文件風格各異
- 📦 **工具臃腫**：現有工具依賴複雜、體積龐大
- 🔄 **批次處理難**：大量文件轉換需要手動操作

### ✨ 自研差異化亮點

- 🚀 **零依賴核心**：基礎功能無需安裝任何第三方函式庫
- 🎨 **5 種內建主題**：default、dark、github、notion、solarized
- 📊 **智能目錄生成**：自動提取標題生成目錄導航
- 💻 **程式碼高亮支援**：保留程式碼區塊的格式和語言標識
- 📑 **多格式輸出**：HTML、PDF、DOCX、PPTX、TXT、RTF
- ⚡ **批次轉換**：支援整個目錄的批次處理
- 🔧 **高度可自訂**：支援自訂 CSS、模板等

---

## ✨ 核心特性

### 📄 多格式支援

| 格式 | 說明 | 依賴 |
|------|------|------|
| **HTML** | 帶樣式的網頁文件 | 無 |
| **PDF** | 可列印的 PDF 文件 | weasyprint（可選） |
| **DOCX** | Word 文件 | python-docx（可選） |
| **PPTX** | PowerPoint 簡報 | python-pptx（可選） |
| **TXT** | 純文字 | 無 |
| **RTF** | 富文字格式 | 無 |

### 🎨 內建主題

- **default** - 清爽預設主題
- **dark** - 暗色護眼主題
- **github** - GitHub 風格主題
- **notion** - Notion 風格主題
- **solarized** - Solarized 配色主題

### 💻 Markdown 支援

- ✅ 標題（H1-H6）
- ✅ 段落和換行
- ✅ **粗體**、*斜體*、~~刪除線~~
- ✅ 有序/無序列表
- ✅ 程式碼區塊和行內程式碼
- ✅ 引用區塊
- ✅ 表格
- ✅ 連結和圖片
- ✅ 水平分隔線
- ✅ YAML Front Matter

---

## 🚀 快速開始

### 📋 環境要求

- Python 3.8 或更高版本
- pip 套件管理器

### 📦 安裝

```bash
# 基礎安裝（零依賴）
pip install markforge

# 安裝 PDF 支援
pip install markforge[pdf]

# 安裝 Word 支援
pip install markforge[docx]

# 安裝 PowerPoint 支援
pip install markforge[pptx]

# 安裝所有可選依賴
pip install markforge[all]
```

### 🔨 基本使用

```bash
# 轉換為 HTML
markforge input.md output.html

# 轉換為 PDF（暗色主題）
markforge input.md output.pdf --theme dark

# 轉換為 Word 文件
markforge input.md output.docx

# 轉換為 PowerPoint 簡報
markforge input.md output.pptx

# 批次轉換整個目錄
markforge ./docs ./output --batch --format html

# 停用目錄生成
markforge input.md output.html --no-toc

# 使用 JSON 輸出
markforge input.md output.html --json
```

### 🐍 Python API

```python
from markforge import MarkForgeConverter, OutputFormat

# 建立轉換器
converter = MarkForgeConverter()

# 載入 Markdown 檔案
converter.load_file("input.md")

# 轉換為 HTML
html = converter.convert(OutputFormat.HTML)

# 儲存到檔案
converter.convert_to_file("output.html", OutputFormat.HTML)

# 批次轉換
MarkForgeConverter.batch_convert(
    input_dir="./docs",
    output_dir="./output",
    output_format=OutputFormat.HTML
)
```

---

## 📖 詳細使用指南

### 📝 Markdown 格式說明

MarkForge 支援標準 Markdown 語法，同時支援 YAML Front Matter：

```markdown
---
title: 文件標題
author: 作者名稱
date: 2024-01-01
---

# 正文開始

內容...
```

### 🎨 主題自訂

#### 使用內建主題

```bash
markforge input.md output.html --theme github
```

#### 自訂 CSS

```bash
markforge input.md output.html --css custom.css
```

### 📊 PPTX 簡報

使用 `---` 分隔投影片：

```markdown
# 第一張投影片標題

- 要點一
- 要點二
- 要點三

---

# 第二張投影片標題

- 要點一
- 要點二
```

### ⚙️ 命令列參數

| 參數 | 說明 | 預設值 |
|------|------|--------|
| `-f, --format` | 輸出格式 | html |
| `-t, --theme` | 主題名稱 | default |
| `--title` | 文件標題 | 從 Front Matter 讀取 |
| `--author` | 文件作者 | 從 Front Matter 讀取 |
| `--no-toc` | 停用目錄 | false |
| `--no-highlight` | 停用程式碼高亮 | false |
| `--batch` | 批次轉換模式 | false |
| `--css` | 自訂 CSS 檔案 | - |
| `--page-size` | PDF 頁面大小 | A4 |
| `--margin` | PDF 頁面邊距 | 20mm |
| `--json` | JSON 格式輸出 | false |

---

## 💡 設計思路與迭代規劃

### 🧠 設計理念

MarkForge 的設計遵循以下原則：

1. **零依賴優先**：核心功能不依賴任何第三方函式庫
2. **漸進增強**：可選依賴提供更豐富的功能
3. **開箱即用**：合理的預設配置，無需複雜設定
4. **可擴展性**：支援自訂主題、模板和樣式

### 🔮 迭代規劃

#### v1.1.0（計劃中）

- [ ] 更多程式碼高亮主題
- [ ] 數學公式支援（LaTeX）
- [ ] Mermaid 圖表支援
- [ ] 自訂模板系統

#### v1.2.0（計劃中）

- [ ] 即時預覽伺服器
- [ ] GUI 介面
- [ ] 外掛系統
- [ ] 更多輸出格式（EPUB、ODT）

#### v2.0.0（遠期）

- [ ] AI 智能排版優化
- [ ] 多語言文件支援
- [ ] 協作編輯功能

---

## 📦 打包與部署指南

### 🐍 PyPI 發布

```bash
# 安裝構建工具
pip install build twine

# 構建
python -m build

# 上傳到 PyPI
twine upload dist/*
```

### 📦 可執行檔案打包

```bash
# 使用 PyInstaller
pip install pyinstaller

# 打包為單一檔案
pyinstaller --onefile markforge/cli.py --name markforge

# 打包為目錄
pyinstaller markforge/cli.py --name markforge
```

---

## 🤝 貢獻指南

我們歡迎所有形式的貢獻！

### 📝 提交 PR

1. Fork 本儲存庫
2. 建立特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交變更 (`git commit -m 'feat: 新增某個特性'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交 Pull Request

### 🐛 回報問題

請使用 [GitHub Issues](https://github.com/gitstq/MarkForge/issues) 回報問題。

提交 Issue 時請包含：

- 作業系統和 Python 版本
- 重現步驟
- 預期行為和實際行為
- 相關日誌或截圖

### 📋 提交規範

使用 [Conventional Commits](https://www.conventionalcommits.org/) 規範：

- `feat:` 新功能
- `fix:` 修復問題
- `docs:` 文件更新
- `style:` 程式碼格式
- `refactor:` 程式碼重構
- `test:` 測試相關
- `chore:` 構建/工具相關

---

## 📄 開源協議說明

本專案採用 **MIT 協議** 開源。

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
