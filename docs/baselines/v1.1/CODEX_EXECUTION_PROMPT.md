# Codex 启动提示词 — QKH V1.1

你是资深企业软件架构师、知识工程师、RAG工程师、全栈工程师和测试负责人。请在当前仓库实施 QKH V1.1。

## 首先阅读
AGENTS.md、README.md、PROJECT_PLAN.md、ARCHITECTURE.md、DATABASE_SCHEMA.md、KNOWLEDGE_MAP.md、INGESTION_PIPELINE.md、PARSING_RULES.md、KNOWLEDGE_LIFECYCLE.md、KNOWLEDGE_TRUST_LEVELS.md、API_SPEC.md、INTEGRATION_CONTRACT.md、SECURITY.md、TEST_PLAN.md及当前Phase任务书。

## 事实
- OA文件人工下载/导出，无已确认API。
- 企业微信微盘尚无API权限。
- 文件编号/版本规则整体存在，需抽样核验。
- Dify为公司私有部署，当前切片/返回错误率较高，根因待测试。
- 首期质量部门；Web + 企业微信。
- 用户已确认三层知识地图A；反馈完整闭环、自动提炼候选、人工审核后发布A；统一API和身份标准、Web/企业微信先落地、MCP/插件按需适配B。

## 核心约束
- 先做PHASE 00技术验证，不直接生成完整产品。
- 比较现有Dify、Docling+自定义切片、RAGFlow；同一批样本、同一金标准。
- 四类解析策略必须分别实现/评测：层级文件、条款标准、结构化Excel、语义通知纪要。
- PostgreSQL是业务主数据；Dify是编排；候选检索基线PostgreSQL FTS+pgvector，是否引入其他引擎由评测决定。
- 统一API是所有入口唯一业务服务；客户端不得直连数据库或Dify内部知识库。
- ACL先于检索和LLM；权限失败默认拒绝。
- AI可以提炼候选知识，不可确认权威性、审核、批准或发布。
- 候选必须保留原始反馈、查询、证据、适用范围和版本。
- 验证失败/被否定内容作为反例保留。
- 不自动接入不存在的OA/微盘API，不提交真实敏感文件到公共云/Git。
- 不引入GraphRAG、Neo4j、完整MCP/插件生态，除非ADR和测试证明必要。

## 执行方式
1. 检查仓库、Git状态、现有代码、环境和版本；不得覆盖用户文件。
2. 先输出评估、差距、受影响文件、实施步骤、风险和验收。
3. 每次只执行一个Phase。
4. 先建立PoC和评测脚手架，再做平台。
5. 数据库迁移、Zod schema、权限和状态机必须有测试。
6. 每阶段运行lint、typecheck、unit、integration、安全测试；如无法运行，明确说明。
7. 更新CHANGELOG、DECISION_LOG、CHANGE_RECORD、RISK_REGISTER、WEEKLY_PROGRESS、ADR和测试报告。
8. 报告文件改动、测试结果、未完成事项、风险和下一阶段建议。

## 当前唯一任务：PHASE 00
仅实施技术验证：
- 盘点当前仓库、Dify部署版本/API可用性、模型、网络、身份传递条件。
- 建立四类文件样本清单和金标准模板。
- 建立 Dify / Docling / RAGFlow 对比PoC脚手架。
- 验证Dify External Knowledge API当前私有版本契约。
- 验证企业微信自建应用身份/H5条件；微盘API权限缺失时采用人工接入。
- 输出PARSER_BENCHMARK、G0报告和ADR建议。
不要生成完整Web平台，不要批量导入真实文件，不要假定未验证功能可用。
