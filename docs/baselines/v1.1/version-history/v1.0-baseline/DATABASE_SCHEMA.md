# 数据模型 — QKH V1.0

## 1. 设计原则
逻辑文件、版本、来源、解析产物、索引、权限和反馈分开建模。状态不可混用。所有业务实体使用 UUID；时间使用 timestamptz；所有写操作记录 actor 与 request_id。

## 2. 核心表
| 表 | 关键字段 | 说明 |
|---|---|---|
| documents | id, doc_code, title, domain_id, type, owner_dept, owner_user_id, authority_status, classification | 逻辑文件 |
| document_versions | id, document_id, version_label, effective_from/to, lifecycle_status, approval_status, file_hash, content_hash, supersedes_version_id | 版本 |
| document_sources | id, version_id, source_system, source_record_id, source_url, imported_at, source_authority, original_filename | 来源副本/链接 |
| document_relations | from_document_id, to_document_id, relation_type, evidence | 引用/关联 |
| document_acl | document_id/version_id, principal_type, principal_id, permission | 文档授权 |
| knowledge_domains | id, code, name, owner, description | 知识域 |
| knowledge_routes | id, intent_code, domain_id, retrieval_profile, constraints, enabled, version | 路由 |
| parse_jobs | id, version_id, parser_name/version, status, error, started_at, finished_at | 解析任务 |
| parsed_elements | id, version_id, element_type, parent_id, heading_path, page_no, sheet_name, cell_range, content, source_locator | 结构元素 |
| knowledge_chunks | id, version_id, element_id, chunk_type, content, metadata, content_hash, index_status | 检索单元 |
| index_jobs | id, version_id, index_name, status, indexed_at, error | 索引任务 |
| users | id, external_subject, display_name, status | 员工映射 |
| roles / user_roles | id, role_code, user_id | 角色 |
| query_sessions | id, user_id, channel, created_at | 会话 |
| query_logs | id, request_id, user_id, query, intent, route, evidence_ids, answer_ref, latency_ms, status | 查询审计 |
| feedbacks | id, query_log_id, type, reason, user_comment, status | 原始反馈 |
| feedback_reviews | id, feedback_id, reviewer_id, decision, resolution, linked_change_id | 审核处理 |
| audit_logs | id, actor_id, action, resource_type, resource_id, request_id, created_at | 操作审计 |

## 3. 状态分离
- authority_status: UNCONFIRMED / CONFIRMED / CONFLICT。
- lifecycle_status: DRAFT / PENDING_APPROVAL / EFFECTIVE / SUPERSEDED / WITHDRAWN。
- parse_status: PENDING / PROCESSING / SUCCEEDED / FAILED / NEEDS_REVIEW。
- index_status: PENDING / INDEXED / STALE / FAILED。
- feedback_status: OPEN / TRIAGED / IN_REVIEW / RESOLVED / REJECTED。

不得用一个 `status` 字段承载上述所有语义。

## 4. 关键约束
- `doc_code` 不保证全局唯一时，使用来源组织/文件类别组合约束，并允许无编号文件。
- 同一逻辑文件可有多个版本；同一版本可有多个来源副本。
- 文件哈希用于重复检测，不作为逻辑身份的唯一依据。
- 一个文档可有多个 Owner/ACL 主体。
- 任何 chunk 必须关联 version_id 与 source_locator。
- 只有 authority_status=CONFIRMED、lifecycle_status=EFFECTIVE、parse_status=SUCCEEDED、index_status=INDEXED 且通过 ACL 的版本，才可作为正式要求类问答证据。
- 保留历史版本以供审计，但默认不参与“当前要求”检索。
- JSONB 仅用于可扩展元数据；核心查询字段必须结构化。
