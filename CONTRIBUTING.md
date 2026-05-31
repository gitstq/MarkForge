# Contributing to MarkForge

感谢你有兴趣为 MarkForge 做贡献！🎉

## 🤝 如何贡献

### 报告问题

如果你发现了 bug 或有功能建议，请：

1. 检查 [Issues](https://github.com/gitstq/MarkForge/issues) 中是否已有相关问题
2. 如果没有，创建新的 Issue，包含：
   - 清晰的标题
   - 问题描述
   - 复现步骤（如果是 bug）
   - 期望行为
   - 实际行为
   - 环境信息（OS、Python 版本等）

### 提交代码

1. **Fork 仓库**
   ```bash
   git clone https://github.com/your-username/MarkForge.git
   cd MarkForge
   ```

2. **创建分支**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **进行更改**
   - 遵循代码风格
   - 添加必要的测试
   - 更新相关文档

4. **提交更改**
   ```bash
   git add .
   git commit -m "feat: your feature description"
   ```

5. **推送分支**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **创建 Pull Request**

## 📝 提交信息规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 格式：

- `feat:` 新功能
- `fix:` Bug 修复
- `docs:` 文档更新
- `style:` 代码格式（不影响功能）
- `refactor:` 代码重构
- `test:` 测试相关
- `chore:` 构建/工具相关

示例：
```
feat: 添加 LaTeX 数学公式支持
fix: 修复表格解析时的空格问题
docs: 更新安装说明
```

## 🧪 运行测试

```bash
# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest

# 运行测试并查看覆盖率
pytest --cov=markforge
```

## 📚 代码风格

- 使用 [Black](https://github.com/psf/black) 格式化代码
- 使用 [flake8](https://flake8.pycqa.org/) 检查代码质量

```bash
# 格式化代码
black markforge tests

# 检查代码质量
flake8 markforge tests
```

## ❓ 有问题？

如果你有任何问题，可以：

- 在 [Discussions](https://github.com/gitstq/MarkForge/discussions) 中提问
- 发送邮件至 markforge@example.com

再次感谢你的贡献！🙏
