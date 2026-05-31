---
title: MarkForge 示例文档
author: MarkForge Team
date: 2024-01-01
---

# 🎉 MarkForge 示例文档

这是一个展示 MarkForge 转换能力的示例文档。

## ✨ 功能特性

MarkForge 支持以下功能：

- **多种输出格式**：HTML、PDF、DOCX、PPTX、TXT、RTF
- **多种主题**：default、dark、github、notion、solarized
- **代码高亮**：支持多种编程语言
- **目录生成**：自动生成文档目录
- **批量转换**：支持批量转换多个文件

## 📝 文本格式

这是一段普通文本，包含 **粗体**、*斜体*、`代码` 等格式。

还可以包含 ~~删除线~~ 和 [链接](https://github.com)。

## 💻 代码示例

### Python 示例

```python
def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# 使用示例
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")
```

### JavaScript 示例

```javascript
// 异步获取数据
async function fetchData(url) {
    const response = await fetch(url);
    const data = await response.json();
    return data;
}

// 使用示例
fetchData('https://api.example.com/data')
    .then(data => console.log(data))
    .catch(error => console.error(error));
```

## 📊 表格示例

| 功能 | 支持格式 | 说明 |
|------|----------|------|
| HTML | ✅ | 完整支持，包含样式 |
| PDF | ✅ | 需要 weasyprint |
| DOCX | ✅ | 需要 python-docx |
| PPTX | ✅ | 需要 python-pptx |
| TXT | ✅ | 纯文本输出 |
| RTF | ✅ | 富文本格式 |

## 💡 引用示例

> "简洁是智慧的灵魂。"
> 
> — 威廉·莎士比亚

> MarkForge 是一个轻量级的 Markdown 转换工具，专注于简单、高效、美观的文档转换体验。

## 📋 列表示例

### 无序列表

- 第一项
- 第二项
  - 嵌套项 A
  - 嵌套项 B
- 第三项

### 有序列表

1. 步骤一：安装 MarkForge
2. 步骤二：编写 Markdown 文档
3. 步骤三：运行转换命令
4. 步骤四：查看输出结果

## 🔗 链接和图片

访问 [GitHub](https://github.com) 了解更多。

![示例图片](https://via.placeholder.com/600x300?text=MarkForge+Example)

---

## 📌 分隔线

上面的内容是文档的前半部分。

下面的内容是文档的后半部分。

---

## 🎯 总结

MarkForge 提供了一个简单而强大的方式来转换 Markdown 文档。无论你需要生成网页、PDF 还是演示文稿，MarkForge 都能帮你轻松完成。

### 快速开始

```bash
# 安装
pip install markforge

# 转换为 HTML
markforge input.md output.html

# 转换为 PDF
markforge input.md output.pdf --theme dark

# 批量转换
markforge ./docs ./output --batch --format html
```

感谢使用 MarkForge！ 🎉
