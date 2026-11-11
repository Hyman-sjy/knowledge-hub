# 知识地图 V1.0

## 目的
知识地图负责把“用户意图”路由到合适的知识域、检索方法和证据要求。它不是权威知识本身，也不承担权限判断。

## 首期意图
| Intent | 描述 | 主检索 | 必要约束 |
|---|---|---|---|
| document_search | 找文件/备案版 | 编号、标题、关键词、目录 | ACL、权威性状态 |
| clause_qa | 查询内部条款/要求 | 精确条款 + BM25 + vector + rerank | 当前有效版本、产品/工艺范围 |
| applicability_check | 文件是否适用 | 结构化元数据 + 条款证据 | 产品、规格、基地、时间；缺项需追问 |
| document_compare | 比较已登记版本 | 版本差异/结构元素比较 | 不生成正式变更批准结论 |

## 路由规则
1. 先认证用户，再做查询。
2. 意图模型只输出受限 JSON：intent、entities、missing_fields、route_reason。
3. 规则校验 intent 是否允许、实体是否完整。
4. 路由服务执行 ACL 和状态过滤。
5. 对精确文件编号，优先走精确索引。
6. 对条款问答，使用混合检索。
7. 对表格数值，优先检索结构化表格单元/行，不依赖普通段落向量。
8. 多个权威来源冲突时返回冲突状态，不由模型择一。
9. 找不到权威证据时拒答，并建议联系 Owner。
10. AI 输出必须引用 evidence_id；服务端验证引用是否属于本次检索结果。

## 配置示例
```yaml
version: 1
routes:
  - intent: document_search
    domain: quality
    methods: [exact_id, title_bm25, metadata]
    evidence: [document_id, version_id, authority_status, source_url]
  - intent: clause_qa
    domain: quality
    methods: [clause_exact, bm25, vector, rerank]
    filters: [acl, authority_confirmed, effective_version, applicability]
    evidence: [doc_code, version, heading_path, clause_id, page, source_locator]
  - intent: applicability_check
    domain: quality
    methods: [metadata_filter, clause_search]
    required_entities: [product_or_process, effective_at]
    missing_action: clarify
  - intent: document_compare
    domain: quality
    methods: [version_diff]
    allowed_status: [CONFIRMED]
    output: [added, removed, changed, uncertain]
```

## 未来知识域
case_library、quality_metrics、audit_evidence、external_standards 等在后续阶段启用，不得在首期伪造已具备能力。
