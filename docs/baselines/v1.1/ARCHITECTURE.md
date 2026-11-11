# 系统架构 — QKH V1.1

## 1. 架构原则
- 统一知识服务，不让每个 AI 小系统维护孤立知识库。
- PostgreSQL 是业务主数据和关系数据；原始文件保留在获批来源或受控存储。
- Dify 是工作流/模型编排层，不是唯一解析、切片、权限或业务数据层。
- 解析、索引、检索、权威性、权限、反馈审核解耦。
- 业务对象地图 + 需求意图地图 + 工具能力地图。
- 反馈可以自动提炼候选，但发布必须经专业审核和授权批准。
- 默认拒绝；无证据、版本冲突、权限不明时不得确定性回答。

## 2. 分层架构
1. 入口：Web 管理/查询、企业微信 H5；后续个人系统、MCP、插件。
2. 接入与身份：应用注册、用户身份映射、角色/部门/文档ACL、请求审计。
3. API：Hono + Zod；文档、检索、知识关系、反馈、候选审核接口。
4. 知识治理：文件主目录、版本、来源、权威性、生命周期、Owner。
5. Ingestion：文件接收 → Docling/RAGFlow/Dify解析对比 → 统一结构元素 → 类型化切片 → 索引。
6. Knowledge Model：业务对象、条款、指标、产品、工艺、缺陷、部门、案例、关系。
7. Retrieval：精确检索 + PostgreSQL FTS + pgvector；ACL/版本/适用性过滤；RRF/重排。
8. Orchestration：Dify 工作流调用外部知识服务，组织答案与引用。
9. Learning Loop：反馈 → 分类 → 候选提炼 → 去重/关联 → 专业审核 → 验证 → 批准 → 发布。
10. Evaluation & Audit：黄金集、解析金标准、日志、审计、质量监控。

## 3. 技术建议
React + TypeScript + Vite；Node/Hono + Zod；PostgreSQL + Drizzle；Docling 首选 PoC；RAGFlow 和 Dify 作对照；Dify 私有部署继续使用；MCP/插件先定义适配契约，不在首期开发完整生态。

## 4. 三层知识地图
- 业务对象：Document、Version、Clause、Product、Specification、Process、InspectionItem、Defect、Department、Role、Case、QualityMethod。
- 需求意图：search、explain、compare、applicability_check、guide、analyze、draft、submit_feedback、change_request、notify（后续意图先登记，不代表首期实现）。
- 工具能力：document_search、clause_retrieval、table_lookup、version_compare、case_search、quality_data_query、feedback_submit、workflow_submit、notification_send。
每个路由定义允许的工具、输入字段、权限要求、证据要求、失败策略和版本。

## 5. 统一检索链
身份认证 → 应用/用户授权 → 意图识别 → 实体抽取 → 规则校验 → ACL过滤 → 权威/生命周期/适用性过滤 → 精确/FTS/vector检索 → rerank → 证据快照 → Dify生成 → 服务端引用校验 → 返回和反馈。

## 6. 反馈与知识提炼链
查询/AI输出/引用快照 → 用户反馈 → 分类和去重 → 候选知识提炼 → 关联业务对象与来源 → 专业Owner审核 → 必要验证 → 授权批准 → 发布到对应知识域 → 建立版本与审计记录。
模型不得直接发布或改变权威状态。

## 7. 失败策略
来源冲突、权限服务不可用、权威性不明、索引过期、解析低置信、证据不足时，分别返回明确状态；权限故障 fail closed；解析失败进入人工复核；历史版本默认不参与现行要求问答。
