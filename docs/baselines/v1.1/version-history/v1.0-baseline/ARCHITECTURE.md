# 系统架构 — QKH V1.0

## 1. 架构原则
- 统一知识服务，分布式 AI 应用消费。
- PostgreSQL 是业务主数据；原件仍以来源系统/受控文件存储为准。
- Dify 是工作流编排和模型调用层，不是唯一文档主库、解析器或检索引擎。
- 解析、索引、权威状态、权限、AI生成解耦。
- 人工导入优先，连接器后续扩展。
- 证据优先，无法确认则拒答/升级。

## 2. 逻辑架构
1. 入口：React Web、企业微信 H5。
2. API：Hono + Zod，统一身份、权限、文档、检索、反馈接口。
3. 知识治理：Document Registry、版本、来源、Owner、状态、ACL。
4. Ingestion：文件接收 → Docling 解析 → 质量结构化转换 → chunk → 索引。
5. Retrieval：精确编号/条款查询 + PostgreSQL FTS + pgvector；候选重排；权限与版本过滤。
6. Orchestration：Dify Chatflow/Workflow，通过 External Knowledge API 获取受控证据。
7. 评测：黄金集、解析金标准、检索指标、答案引用指标、安全回归。
8. 审计：查询、访问、导入、审核、索引版本和配置变更记录。

## 3. 推荐技术
- Frontend: React + TypeScript + Vite。
- Backend: Node.js + Hono + Zod。
- DB: PostgreSQL + Drizzle；首轮评测 pgvector 可用性，不预先引入独立向量集群。
- Parser: Docling PoC；对照 RAGFlow 与现有 Dify。
- Retrieval: 精确检索 + PostgreSQL FTS + vector + RRF/重排；OpenSearch 仅在评测证明必要时引入。
- Orchestration: 公司私有 Dify。
- Enterprise entry: 企业微信自建应用/H5；需管理员授权和用户身份映射。
- MCP: 后续包装 API，不作为首期员工身份入口。

## 4. 数据流
文件原件 → 导入登记 → 文件哈希 → 解析产物 → 章节/表格结构 → 质量知识元素 → 索引 → 检索 → ACL/版本过滤 → Dify回答 → 引用/反馈。

## 5. 失败策略
- OA/微盘不可连接：管理员人工导出、登记来源与链接。
- 解析失败：进入人工复核，不索引为正式知识。
- 权威版本冲突：状态为 CONFLICT，阻止确定性问答。
- 索引延迟：返回明确状态，不把旧索引伪装为最新。
- Dify不可用：可提供精确文件目录检索；AI问答提示服务不可用。
- 权限服务不可用：默认拒绝访问（fail closed）。

## 6. 部署建议
优先部署在公司现有私有环境。开发、测试、生产环境隔离；密钥通过环境变量/密钥管理；数据库迁移可回滚；文件原件不因索引重建而删除。
