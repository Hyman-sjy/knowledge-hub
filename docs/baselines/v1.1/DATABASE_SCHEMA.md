# 数据模型 — QKH V1.1

## 1. 原则
逻辑文件、版本、来源、结构元素、业务对象、知识候选、审核、验证、发布、权限、查询反馈分离。禁止用单一 status 表达多个生命周期。

## 2. 文件与解析
- documents：逻辑文件主目录。
- document_versions：版本、有效期、生命周期、批准状态、哈希。
- document_sources：来源系统、来源记录ID、原文链接/导入信息、来源权威性。
- document_acl：用户/角色/部门/应用对文档或版本的权限。
- parsed_elements：章节、条款、表格、表格行、单元格范围、通知段落。
- knowledge_chunks：可检索单元，必须关联 version_id、element_id、source_locator。
- parse_jobs / index_jobs：解析和索引任务、版本、工具版本、错误、时间。
- document_relations：文件间引用、替代、附件、相关关系。

## 3. 三层知识地图
- business_objects：对象类型、稳定ID、名称、属性、来源。
- business_object_relations：source_object、relation_type、target_object、valid_from/to、evidence_id、confidence、review_status。
- knowledge_domains：知识域及Owner。
- intent_definitions：意图、schema、澄清策略、版本。
- tool_capabilities：工具能力、输入输出schema、权限scope、风险等级、启用状态。
- route_bindings：intent—domain—tool关联、过滤条件、证据要求、版本。

## 4. 反馈与知识沉淀
- query_sessions：会话。
- query_logs：用户、入口应用、问题、意图、路由、证据快照、回答、模型/Prompt版本、状态。
- feedbacks：反馈类型、原因、原始评论、附件/证据引用、提交者。
- feedback_reviews：审核者、决定、理由、时间、处理记录。
- knowledge_candidates：候选类型、标题、内容、来源反馈/查询/文件、去重键、风险等级、状态。
- candidate_sources：候选与原始反馈、查询、文档/条款的多对多来源关系。
- candidate_relations：候选间重复、支持、反驳、补充关系。
- candidate_validations：验证方法、样本、结果、证据、验证人、时间。
- knowledge_items：审核后发布的知识条目，带类型、适用范围、可信状态、Owner。
- knowledge_item_versions：知识条目版本、内容哈希、生效区间、批准人。
- knowledge_publications：发布记录、目标知识域、索引版本、撤回记录。
- knowledge_reviews：发布/撤回/更新审批记录。

## 5. 身份与治理
- users、roles、user_roles。
- applications：调用方应用登记、类型、Owner、认证方式、允许scope、状态。
- application_credentials：仅存凭证哈希/密钥引用，不存明文。
- audit_logs：操作者、应用、动作、资源、request_id。
- ownership_assignments：知识域/文件/对象Owner及代理人。
- review_policies：按知识类型配置审核和验证要求。

## 6. 状态分离
- authority_status：UNCONFIRMED / CONFIRMED / CONFLICT。
- lifecycle_status：DRAFT / PENDING_APPROVAL / EFFECTIVE / SUPERSEDED / WITHDRAWN。
- parse_status：PENDING / PROCESSING / SUCCEEDED / FAILED / NEEDS_REVIEW。
- index_status：PENDING / INDEXED / STALE / FAILED。
- candidate_status：NEW / DEDUP_PENDING / IN_REVIEW / NEEDS_VALIDATION / APPROVED_FOR_PUBLICATION / REJECTED / PUBLISHED / WITHDRAWN。
- trust_status：CANDIDATE / REVIEWED / VALIDATED / APPROVED / SUPERSEDED / REJECTED；具体适用规则由知识类型决定，不将其当成所有知识的统一线性状态机。
- feedback_status：OPEN / TRIAGED / IN_REVIEW / RESOLVED / REJECTED。

## 7. 关键约束
- AI不得写入权威状态、批准状态或发布状态。
- 候选知识必须可追溯到至少一个来源证据。
- 发布知识必须有Owner、审核记录、适用范围、版本和证据。
- 质量案例的 VALIDATED 与正式制度 APPROVED 分开表达。
- 每个表格数值元素必须关联表头路径、单位、规格/条件和源单元格位置。
- 历史版本保留审计，默认不参与当前要求问答。
- 权限过滤先于模型上下文构建。
