"""
MarkForge Tests
"""

import pytest
from pathlib import Path
import tempfile
import os

from markforge.converter import MarkForgeConverter, OutputFormat, ConversionOptions


class TestMarkForgeConverter:
    """Test cases for MarkForgeConverter"""
    
    @pytest.fixture
    def sample_markdown(self):
        """Sample markdown content"""
        return """---
title: Test Document
author: Test Author
---

# Heading 1

This is a paragraph with **bold** and *italic* text.

## Heading 2

Here's a code block:

```python
def hello():
    print("Hello, World!")
```

### Heading 3

- List item 1
- List item 2
- List item 3

> This is a blockquote

| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 2   |

[Link to GitHub](https://github.com)
"""
    
    def test_load_string(self, sample_markdown):
        """Test loading markdown from string"""
        converter = MarkForgeConverter()
        converter.load_string(sample_markdown)
        assert converter._markdown_content
        assert converter._metadata.get("title") == "Test Document"
    
    def test_load_file(self, sample_markdown):
        """Test loading markdown from file"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write(sample_markdown)
            f.flush()
            
            converter = MarkForgeConverter()
            converter.load_file(f.name)
            
            assert converter._markdown_content
            assert converter._metadata.get("author") == "Test Author"
            
            os.unlink(f.name)
    
    def test_to_html(self, sample_markdown):
        """Test HTML conversion"""
        converter = MarkForgeConverter()
        converter.load_string(sample_markdown)
        
        html = converter.convert(OutputFormat.HTML)
        
        assert "<!DOCTYPE html>" in html
        assert "<h1>" in html
        assert "<strong>" in html
        assert "<em>" in html
        assert "<code" in html  # Code blocks use <code class="language-...">
    
    def test_to_html_with_theme(self, sample_markdown):
        """Test HTML conversion with different themes"""
        options = ConversionOptions(theme="dark")
        converter = MarkForgeConverter(options)
        converter.load_string(sample_markdown)
        
        html = converter.convert(OutputFormat.HTML)
        
        assert "#1f2937" in html  # Dark theme background
    
    def test_to_txt(self, sample_markdown):
        """Test plain text conversion"""
        converter = MarkForgeConverter()
        converter.load_string(sample_markdown)
        
        txt = converter.convert(OutputFormat.TXT)
        
        assert "Heading 1" in txt
        assert "**" not in txt  # Formatting removed
        assert "Hello, World!" in txt
    
    def test_to_rtf(self, sample_markdown):
        """Test RTF conversion"""
        converter = MarkForgeConverter()
        converter.load_string(sample_markdown)
        
        rtf = converter.convert(OutputFormat.RTF)
        
        assert r"{\rtf1" in rtf
        assert "Heading 1" in rtf
    
    def test_front_matter_extraction(self):
        """Test front matter extraction"""
        markdown = """---
title: My Title
author: John Doe
date: 2024-01-01
---

# Content
"""
        converter = MarkForgeConverter()
        converter.load_string(markdown)
        
        assert converter._metadata.get("title") == "My Title"
        assert converter._metadata.get("author") == "John Doe"
        assert converter._metadata.get("date") == "2024-01-01"
        assert "# Content" in converter._markdown_content
    
    def test_toc_generation(self, sample_markdown):
        """Test table of contents generation"""
        options = ConversionOptions(include_toc=True)
        converter = MarkForgeConverter(options)
        converter.load_string(sample_markdown)
        
        html = converter.convert(OutputFormat.HTML)
        
        assert "目录" in html or "toc" in html.lower()
    
    def test_no_toc(self, sample_markdown):
        """Test disabling table of contents"""
        options = ConversionOptions(include_toc=False)
        converter = MarkForgeConverter(options)
        converter.load_string(sample_markdown)
        
        html = converter.convert(OutputFormat.HTML)
        
        # Should not have TOC class
        assert 'class="toc"' not in html
    
    def test_convert_to_file(self, sample_markdown):
        """Test converting to file"""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "output.html"
            
            converter = MarkForgeConverter()
            converter.load_string(sample_markdown)
            converter.convert_to_file(output_path, OutputFormat.HTML)
            
            assert output_path.exists()
            
            content = output_path.read_text()
            assert "<!DOCTYPE html>" in content
    
    def test_batch_convert(self):
        """Test batch conversion"""
        with tempfile.TemporaryDirectory() as tmpdir:
            input_dir = Path(tmpdir) / "input"
            output_dir = Path(tmpdir) / "output"
            input_dir.mkdir()
            
            # Create test files
            (input_dir / "test1.md").write_text("# Test 1\n\nContent 1")
            (input_dir / "test2.md").write_text("# Test 2\n\nContent 2")
            
            output_files = MarkForgeConverter.batch_convert(
                input_dir, output_dir, OutputFormat.HTML
            )
            
            assert len(output_files) == 2
            assert all(f.exists() for f in output_files)


class TestConversionOptions:
    """Test cases for ConversionOptions"""
    
    def test_default_options(self):
        """Test default options"""
        options = ConversionOptions()
        
        assert options.output_format == OutputFormat.HTML
        assert options.theme == "default"
        assert options.highlight_code is True
        assert options.include_toc is True
        assert options.page_size == "A4"
    
    def test_custom_options(self):
        """Test custom options"""
        options = ConversionOptions(
            output_format=OutputFormat.PDF,
            theme="dark",
            title="Custom Title",
            author="Custom Author"
        )
        
        assert options.output_format == OutputFormat.PDF
        assert options.theme == "dark"
        assert options.title == "Custom Title"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
