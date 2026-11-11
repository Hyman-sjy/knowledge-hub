# V1.1 基线导航与核对说明

日期：2026-11-11。范围：工程文档接收、保留、核对及路径适配。
74 份 Markdown 完整归档：43 份 V1.1、31 份 V1.0 历史快照。
独立提示词与包内一致；见[接收记录](SOURCE_INTAKE.md)及[逐文件清单](sources/MANIFEST.json)。

## 主文档

| 内容 | 原始文件 |
| --- | --- |
| 入口与版本 | [README](baselines/v1.1/README.md)、[VERSION](baselines/v1.1/VERSION.md) |
| 计划与五期路线 | [PROJECT_PLAN](baselines/v1.1/PROJECT_PLAN.md)、[ROADMAP](baselines/v1.1/ROADMAP.md) |
| 架构与数据 | [ARCHITECTURE](baselines/v1.1/ARCHITECTURE.md)、[DATABASE_SCHEMA](baselines/v1.1/DATABASE_SCHEMA.md) |
| 地图与解析 | [KNOWLEDGE_MAP](baselines/v1.1/KNOWLEDGE_MAP.md)、[INGESTION_PIPELINE](baselines/v1.1/INGESTION_PIPELINE.md) |
| 接口、安全及测试 | [API_SPEC](baselines/v1.1/API_SPEC.md)、[SECURITY](baselines/v1.1/SECURITY.md)、[TEST_PLAN](baselines/v1.1/TEST_PLAN.md) |
| 规则与提示词 | [AGENTS](baselines/v1.1/AGENTS.md)、[CONTRIBUTING](baselines/v1.1/CONTRIBUTING.md)、[原始提示词](baselines/v1.1/CODEX_EXECUTION_PROMPT.md) |
| 历史记录 | [V1.0 入口](baselines/v1.1/version-history/v1.0-baseline/README.md)、[V1.0 决策](baselines/v1.1/version-history/v1.0-baseline/records/DECISION_LOG.md) |

## 原文简写路径适配

原始 README 导航中下列文件名省略了子目录，提示词及 AGENTS 也有部分同类简写。
原文保持不变，通过下表解析实际位置。

| 原文文件名 | 实际文件 |
| --- | --- |
| INTEGRATION_CONTRACT.md | [integrations/INTEGRATION_CONTRACT.md](baselines/v1.1/integrations/INTEGRATION_CONTRACT.md) |
| MCP_PLUGIN_STRATEGY.md | [integrations/MCP_PLUGIN_STRATEGY.md](baselines/v1.1/integrations/MCP_PLUGIN_STRATEGY.md) |
| KNOWLEDGE_MODEL.md | [knowledge/KNOWLEDGE_MODEL.md](baselines/v1.1/knowledge/KNOWLEDGE_MODEL.md) |
| KNOWLEDGE_RELATIONS.md | [knowledge/KNOWLEDGE_RELATIONS.md](baselines/v1.1/knowledge/KNOWLEDGE_RELATIONS.md) |
| PARSING_RULES.md | [knowledge/PARSING_RULES.md](baselines/v1.1/knowledge/PARSING_RULES.md) |
| KNOWLEDGE_LIFECYCLE.md | [knowledge/KNOWLEDGE_LIFECYCLE.md](baselines/v1.1/knowledge/KNOWLEDGE_LIFECYCLE.md) |
| KNOWLEDGE_TRUST_LEVELS.md | [knowledge/KNOWLEDGE_TRUST_LEVELS.md](baselines/v1.1/knowledge/KNOWLEDGE_TRUST_LEVELS.md) |
| FEEDBACK_TAXONOMY.md | [knowledge/FEEDBACK_TAXONOMY.md](baselines/v1.1/knowledge/FEEDBACK_TAXONOMY.md) |
| KNOWLEDGE_OWNERSHIP.md | [governance/KNOWLEDGE_OWNERSHIP.md](baselines/v1.1/governance/KNOWLEDGE_OWNERSHIP.md) |
| KNOWLEDGE_REVIEW_POLICY.md | [governance/KNOWLEDGE_REVIEW_POLICY.md](baselines/v1.1/governance/KNOWLEDGE_REVIEW_POLICY.md) |
| INGESTION_PIPELINE.md（解析细则中的引用） | [INGESTION_PIPELINE.md](baselines/v1.1/INGESTION_PIPELINE.md) |

## 阶段与评测

- [PHASE 00 技术验证](baselines/v1.1/execution/PHASE-00-technical-spike.md)。
- [PHASE 01 基础架构](baselines/v1.1/execution/PHASE-01-foundation.md)。
- [PHASE 02 文件解析](baselines/v1.1/execution/PHASE-02-ingestion.md)。
- [PHASE 03 检索与 Dify](baselines/v1.1/execution/PHASE-03-retrieval.md)。
- [PHASE 04 Web 与知识闭环](baselines/v1.1/execution/PHASE-04-web.md)。
- [PHASE 05 企业微信](baselines/v1.1/execution/PHASE-05-wecom.md)。
- [PHASE 06 验收试点](baselines/v1.1/execution/PHASE-06-acceptance.md)。
- [解析基准](baselines/v1.1/evaluation/PARSER_BENCHMARK.md)、[黄金集](baselines/v1.1/evaluation/GOLDEN_SET_SPEC.md)。

P0～P4 为五期业务路线，PHASE 00～06 为首期开发任务，二者不是同一套编号。

## 治理及记录

- [文件变更后续路线](baselines/v1.1/governance/DOCUMENT_CHANGE_WORKFLOW.md)。
- [ADR-001 架构](baselines/v1.1/ADR/ADR-001-architecture.md)、[ADR-002 解析](baselines/v1.1/ADR/ADR-002-document-parser.md)、[ADR-003 检索](baselines/v1.1/ADR/ADR-003-retrieval-engine.md)、[ADR-004 权限](baselines/v1.1/ADR/ADR-004-permission-model.md)：均保留 Proposed。
- [原始决策](baselines/v1.1/records/DECISION_LOG.md)、[风险](baselines/v1.1/records/RISK_REGISTER.md)、[变更](baselines/v1.1/records/CHANGE_RECORD.md)、[周进度模板](baselines/v1.1/records/WEEKLY_PROGRESS.md)、[原始 Changelog](baselines/v1.1/CHANGELOG.md)。
- [本次归档变更](../CHANGELOG.md)和[任务记录](TASKS.md)位于基线外，不改写原始记录。

## 差异与待细化项

1. 提示词要求进入 PHASE 00；当前授权为整理并推送工程文件。本次不开发 PoC 或平台，后续见[执行入口](../CODEX_EXECUTION_PROMPT.md)。
2. 原文“编号及版本规则整体存在”同时要求抽样核验；包内未附企业规则实物，不表示真实字段已核验。
3. Dify 作为编排层是已确认方向，技术实现 ADR 仍为 Proposed。Docling 首选 PoC 不是生产选型结论。
4. 八周及资源配置为排期假设。样本、负责人、权限、身份和企业环境仍需确认。
5. 数据模型是逻辑表与关键字段清单，API 是端点和规则清单。完整 schema、索引约束、迁移、请求响应、错误码及状态迁移测试仍待后续细化，不把归档完成视为开发已就绪。
6. 解析金标准与验收目标尚无真实结果。正式运行前仍需冻结指标分母、边界及门槛。
7. 原始协作规范要求 main 保留可运行且已验证版本；当前 main 为已验证完整性的文档基线，没有可运行产品。未来代码按功能分支与 PR 协作。

## 验证范围

`python3 scripts/check_docs.py` 检查工程链接，并核对原 ZIP、独立提示词和全部 74 个文件的字节数、SHA-256 与逐字节一致性。
原始文档中的简写文件名以本页映射补充导航，原始正文不改动。
本次无平台代码及企业环境，应用 lint、typecheck、unit、integration、安全联调和 G0 均未执行。
