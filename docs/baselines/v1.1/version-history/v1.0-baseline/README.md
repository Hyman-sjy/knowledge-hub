# Quality Knowledge Hub（QKH）V1.0

企业质量统一知识中枢。第一期范围：质量部门；入口：Web 管理/查询端 + 企业微信 H5；来源：OA 人工导出、企业微信微盘人工导出/登记、人工补录。当前无 OA API、无微盘 API 权限。

## 目标
建立统一质量文件主目录、权威性确认、版本治理、结构化解析、证据检索、统一 API、反馈审核和评测体系。Dify 私有部署保留为工作流编排层，不再作为唯一解析/切片/检索引擎。

## 当前冻结决策
- 首选文档解析 PoC：Docling + 质量领域自定义结构化切片。
- 对照方案：现有 Dify 与 RAGFlow。
- 检索先做 PostgreSQL 全文检索 + pgvector 候选；是否引入 OpenSearch 由基准测试决定。
- Dify 通过 External Knowledge API 调用外部知识服务。
- 首期采用人工文件接入；不假设 OA/微盘 API 已可用。
- 文件权威性由指定业务责任人确认，AI 不得自行认定。
- 无法确认权威版本、适用范围或权限时，拒绝给出确定性制度结论。

## 文档导航
- `PROJECT_PLAN.md`：范围、时间、Gate、交付。
- `ARCHITECTURE.md`：系统架构。
- `DATABASE_SCHEMA.md`：数据模型。
- `API_SPEC.md`：接口契约。
- `KNOWLEDGE_MAP.md`：意图和路由。
- `INGESTION_PIPELINE.md`：解析、切片、索引。
- `SECURITY.md`：权限与安全边界。
- `TEST_PLAN.md`：测试与验收。
- `ADR/`：架构决策记录。
- `execution/`：Codex 分阶段任务书。
- `evaluation/`：黄金集和解析对比。
- `records/`：决策、风险、变更、周报。

## 状态
规划基线 V1.0。技术实现尚未开始；所有候选技术必须在公司私有环境中通过 PoC。
