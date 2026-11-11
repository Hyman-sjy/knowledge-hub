# 知识地图 V1.1 — 三层模型

## 1. 目的
将业务对象、用户意图和系统工具能力分离。知识地图是路由和关系配置，不是知识内容本身，也不能替代权限引擎。

## 2. 第一层：业务对象地图
首期对象：
- Document / DocumentVersion / DocumentSource
- Clause / Section / Table / TableRow / Metric
- Product / ProductSpecification
- Process / Operation / InspectionItem
- Department / Role / Responsibility
- KnowledgeCandidate / Feedback / Review

后续对象：
- Defect / FailureMode / QualityCase / 8D / CAPA
- Batch / MaterialLot / Equipment / ProductionLine
- Experiment / ValidationEvidence / Supplier

关系示例：
- 文件版本 CONTAINS 条款
- 条款 APPLIES_TO 产品/规格/工艺
- 条款 DEFINES 检验项目/指标
- 文件 REFERENCES 文件/外部标准
- 案例 INVOLVES 缺陷/产品/批次
- 案例 VALIDATED_BY 试验/证据
- 知识候选 DERIVED_FROM 反馈/查询/文件

## 3. 第二层：需求意图地图
| 意图 | 含义 | 首期状态 |
|---|---|---|
| document_search | 查找文件 | 实现 |
| clause_qa | 查询条款要求 | 实现 |
| applicability_check | 判断适用范围 | 实现 |
| document_compare | 比较登记版本 | 限定实现 |
| explain_method | 解释质量方法 | 仅限已有审核资料 |
| submit_feedback | 提交纠错/补充 | 实现 |
| knowledge_candidate_review | 审核候选知识 | 管理端实现 |
| change_request | 发起文件变更 | 后续 |
| case_search | 查找质量案例 | 后续 |
| quality_data_query | 查询QMS/MES | 后续 |
| notify | 通知/阅读确认 | 后续 |

## 4. 第三层：工具能力地图
每个工具配置：tool_code、description、input_schema、output_schema、required_scope、allowed_roles、evidence_policy、timeout、failure_policy、enabled、version。
首期工具：document_search、clause_retrieval、table_lookup、applicability_check、version_compare（限定）、feedback_submit、candidate_extract（生成候选，不发布）、candidate_review（仅授权人员）。

## 5. 路由原则
- 先身份与权限，再检索；模型不授予权限。
- 意图模型只返回受限结构化 JSON。
- 规则层验证实体、必填条件和允许工具。
- 精确编号走精确索引；数值/表格问题走结构化表格查询；条款问题走条款+混合检索。
- 路由失败、意图不确定时澄清，不盲目调用多个工具。
- 结果必须包含来源、版本、定位、权威状态。
- 模型输出的引用必须由服务端校验。
- 候选知识提炼与正式知识发布是两个不同权限动作。

## 6. 路由配置示例
```yaml
version: 1
routes:
  - intent: document_search
    tools: [document_search]
    evidence: [document_id, version_id, source]
  - intent: clause_qa
    tools: [clause_retrieval, table_lookup]
    filters: [acl, authority_confirmed, effective_version, applicability]
    evidence: [doc_code, version, clause_id, heading_path, page]
  - intent: applicability_check
    tools: [applicability_check, clause_retrieval]
    required_entities: [product_or_process, effective_at]
    missing_action: clarify
  - intent: document_compare
    tools: [version_compare]
    allowed_scope: registered_confirmed_versions
  - intent: submit_feedback
    tools: [feedback_submit]
  - intent: knowledge_candidate_review
    tools: [candidate_review]
    required_role: knowledge_reviewer
```
