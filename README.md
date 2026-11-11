# 企业质量知识中枢 · Quality Knowledge Hub

统一质量知识目录、受控检索与反馈沉淀的工程仓库。

**当前状态：V1.1 文档基线已导入并完成完整性核对，技术验证尚未开始。**
本仓库尚未实现平台代码，未完成解析器对比、企业接口联调或 G0 验收。

## 从这里开始

- [工程协作规则](AGENTS.md)
- [V1.1 原始文档导航及核对说明](docs/BASELINE_REVIEW.md)
- [Codex 执行入口与路径适配](CODEX_EXECUTION_PROMPT.md)
- [原始 V1.1 项目计划](docs/baselines/v1.1/PROJECT_PLAN.md)
- [V1.0 历史快照](docs/baselines/v1.1/version-history/v1.0-baseline/README.md)
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
  baselines/v1.1/    原始文档：43 份 V1.1 + 31 份 V1.0 历史快照
  sources/           原始 ZIP、独立提示词及逐文件校验清单
scripts/             工程文档检查
.github/             协作模板和自动检查
```

74 份 Markdown 的内容与原始 ZIP 逐字节一致，内部目录完整保留。
独立提示词与包内版本一致；[校验清单](docs/sources/MANIFEST.json)记录原包和逐文件 SHA-256。
`docs-v1.1-baseline` 标签标识此次文档归档，不表示平台或 G0 已通过验收。

本次工作范围为工程文件整理和推送；原始任务书中的 PHASE 00 尚未执行。
后续明确启动该阶段时，按[仓库执行入口](CODEX_EXECUTION_PROMPT.md)读取原文与任务。
路径差异和待细化项见[基线核对说明](docs/BASELINE_REVIEW.md)。

## 本地检查

需要 Python 3，仅使用标准库：

```sh
python3 scripts/check_docs.py
git diff --check
```

该检查验证工程目录、文档链接及原包、提示词、74 份文件的一致性，
不证明知识准确率、权限安全性或接口兼容性。
