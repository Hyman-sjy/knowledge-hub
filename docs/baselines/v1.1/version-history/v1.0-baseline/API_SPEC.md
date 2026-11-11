# API 契约 — QKH V1.0

## 通用约定
- Base path: `/api/v1`
- JSON；时间 ISO-8601 UTC；ID 为 UUID。
- 所有请求必须携带认证上下文；服务端从可信身份令牌解析用户，不接受客户端自报 user_id。
- 每次请求生成/传递 `X-Request-ID`。
- 错误结构：`{ "error": { "code": "...", "message": "...", "request_id": "..." } }`
- 禁止在响应中暴露无权访问的文件是否存在、文件名或内容。

## 员工/应用接口
### POST `/knowledge/search`
请求：`{ "query": "...", "domain": "quality", "filters": { "product": "...", "document_type": "...", "effective_at": "..." }, "top_k": 5 }`
响应：`{ "results": [{ "document_id": "...", "version_id": "...", "title": "...", "doc_code": "...", "version": "...", "authority_status": "...", "lifecycle_status": "...", "heading_path": [], "clause_id": "...", "page": 1, "snippet": "...", "source_url": "...", "retrieval_method": "..." }], "warnings": [] }`
权限过滤必须在召回内容进入生成模型前执行。

### POST `/knowledge/answer-context`
供 Dify 取证据。输入 query、用户授权上下文、domain、filters。输出仅包含已授权且满足版本策略的证据片段、定位元数据及警告。Dify External Knowledge API Adapter 单独适配 Dify 所需协议。

### GET `/documents`
支持分页、状态、类型、Owner、来源筛选；权限过滤由服务端执行。

### GET `/documents/{id}`
返回逻辑文件元数据、版本列表、来源及可见关系。

### GET `/versions/{id}/content`
只返回当前用户有权访问的原文/解析视图；不允许用公开静态链接绕过权限。

### POST `/feedback`
请求：`{ "query_log_id": "...", "type": "WRONG_ANSWER|MISSING_DOC|WRONG_VERSION|WRONG_SCOPE|BAD_CITATION|OTHER", "comment": "..." }`
响应：反馈 ID 与状态。

### POST `/admin/import-jobs`
管理员提交文件及元数据；必须验证角色、文件类型、大小、病毒扫描/安全策略和导入来源。

### POST `/admin/documents/{id}/authority-review`
由授权 Owner 确认/撤销权威性；记录理由、证据、操作者和时间。AI 不可调用此接口。

## Dify External Knowledge Adapter
按当前私有 Dify 版本的官方 External Knowledge API 契约实现 `/retrieval` 适配器。适配器只调用内部受控检索服务；不可绕过 ACL、版本过滤和审计。上线前用当前部署版本实测认证头、请求字段和响应结构。

## 幂等与审计
导入、索引和反馈写入需支持幂等键。所有管理操作写 audit_logs。错误响应不得包含 token、内部路径、数据库信息或未授权资源元数据。
