# Quality Knowledge Hub（QKH）V1.1

企业质量统一知识中枢。V1.1 是 V1.0 工程基线的增量修订，保留 V1.0 原始快照，不覆盖历史决策。

## 项目目标
建设统一、受治理、可追溯的企业质量知识基础设施，为 Web、企业微信及后续 AI 小系统提供统一知识服务。知识平台不等于一个更大的 Dify 知识库。

## 已确认事实
- OA 文件当前通过人工下载/导出；没有已确认可用 API。
- 企业微信微盘尚无已开通 API 权限。
- 文件编号与版本规则整体存在，但需抽样核验字段完整性及跨来源一致性。
- Dify 为公司内置私有部署；现有解析/切片返回存在较大错误率，根因尚待基准测试。
- 首期业务范围为质量部门。
- 首期入口为 Web + 企业微信。
- 后续个人小系统、MCP、插件通过统一 API 和身份权限标准接入。

## V1.1 已确认架构决策
1. 知识地图采用三层结构：业务对象地图 + 需求意图地图 + 工具能力地图。
2. 第一期建设完整反馈数据模型与审核闭环；自动提炼候选知识，人工审核/验证/批准后才能发布。
3. 第一期建设统一 API 和身份权限标准；Web、企业微信先落地；MCP、插件按需适配。
4. Dify 保留为私有工作流编排层，不作为唯一文档解析、业务主数据或检索引擎。
5. Docling 为首选解析 PoC，RAGFlow 与现有 Dify 作为对照；最终选择以同一批文件的实测为准。
6. 首期 OA/微盘使用人工接入；不假设接口权限存在。
7. 权威性、生命周期、解析状态、索引状态、知识可信状态必须分开管理。
8. AI 不得自行决定权限、文件权威性、审批状态或正式知识发布。

## 文档导航
- 项目：`PROJECT_PLAN.md`、`ROADMAP.md`
- 架构：`ARCHITECTURE.md`、`KNOWLEDGE_MAP.md`、`INTEGRATION_CONTRACT.md`
- 数据：`DATABASE_SCHEMA.md`、`KNOWLEDGE_MODEL.md`、`KNOWLEDGE_RELATIONS.md`
- 解析：`INGESTION_PIPELINE.md`、`PARSING_RULES.md`
- 治理：`KNOWLEDGE_LIFECYCLE.md`、`KNOWLEDGE_TRUST_LEVELS.md`、`FEEDBACK_TAXONOMY.md`、`KNOWLEDGE_OWNERSHIP.md`、`KNOWLEDGE_REVIEW_POLICY.md`
- 接口：`API_SPEC.md`、`MCP_PLUGIN_STRATEGY.md`
- 安全测试：`SECURITY.md`、`TEST_PLAN.md`
- 工程协作：`AGENTS.md`、`CONTRIBUTING.md`、`CHANGELOG.md`、`ADR/`、`execution/`、`evaluation/`、`records/`
- 历史：`version-history/v1.0-baseline/`

## 版本说明
V1.0：原始工程基线，保留在 `version-history/v1.0-baseline/`。
V1.1：补齐知识模型、三层知识地图、反馈到候选知识的审核闭环、统一接入契约、分期及验收。
