# ADR-003：检索引擎选择

- 状态：Proposed
- 首选基线：PostgreSQL FTS + pgvector + 精确字段检索 + RRF/重排。
- 备选：OpenSearch hybrid retrieval；Dify 内置检索作为对照。
- 不首期引入多个向量库。
- 评价：Recall@5、MRR/nDCG、过滤准确性、延迟、运维成本、中文专业词召回。
- 只有当 PostgreSQL 基线未达目标且 OpenSearch 对照明显改善时，才引入 OpenSearch。
