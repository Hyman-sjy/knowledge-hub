# 企业质量知识中枢 · Quality Knowledge Hub

统一质量知识目录、受控检索与反馈沉淀的工程仓库。

**当前状态：工程骨架已建立，V1.1 原始文档包及执行提示词待导入。**
本仓库尚未实现平台代码，未完成解析器对比、企业接口联调或 G0 验收。

## 从这里开始

- [工程协作规则](AGENTS.md)
- [已确认决策及来源](docs/PROJECT_CONTEXT.md)
- [原始资料接收清单](docs/SOURCE_INTAKE.md)
- [PHASE 00 技术验证任务](docs/PHASE_00.md)
- [任务看板](docs/TASKS.md)
- [验证记录模板](docs/templates/VALIDATION_RECORD.md)
- [技术决策模板](docs/templates/ADR_TEMPLATE.md)
- [G0 验收报告模板](docs/templates/G0_REPORT.md)
- [协作与提交方式](CONTRIBUTING.md)
- [变更记录](CHANGELOG.md)

## 工程目录

```text
docs/                当前上下文、任务、资料接收清单
  templates/         决策、验证与验收模板
  baselines/         原始工程文档包导入位置（待接收）
scripts/             工程文档检查
.github/             协作模板和自动检查
```

收到原始压缩包后，保持其目录和内容原样导入 `docs/baselines/v1.1/`，
记录文件清单与 SHA-256，核对其中 V1.0 历史文件及执行提示词。
核对完整后再创建 `docs-v1.1-baseline` 标签；当前骨架不使用该标签。

## 本地检查

需要 Python 3，仅使用标准库：

```sh
python3 scripts/check_docs.py
git diff --check
```

该检查只验证工程目录和本地 Markdown 链接，不证明知识准确率、权限安全性或接口兼容性。
