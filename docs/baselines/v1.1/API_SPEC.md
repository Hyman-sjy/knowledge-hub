# API 契约 — QKH V1.1

## 通用
Base `/api/v1`；JSON；认证身份由可信令牌解析，不接受客户端自报 user_id；每次请求有 request_id；所有敏感读取和管理写入审计。错误不泄露无权资源是否存在。

## 知识服务
- `POST /knowledge/search`：按用户权限搜索，返回文档/版本/条款/页码/表格定位。
- `POST /knowledge/answer-context`：Dify External Knowledge Adapter 使用；仅返回已授权、版本合规证据。
- `POST /knowledge/applicability-check`：基于产品/规格/工艺/时间条件查询适用性；条件缺失返回 clarification_required。
- `POST /knowledge/compare-versions`：只比较已登记版本，输出新增/删除/修改/不确定片段；不是审批结论。
- `GET /knowledge/map`：返回调用方授权可见的地图配置。

## 文件管理
- `GET /documents`、`GET /documents/{id}`、`GET /versions/{id}`。
- `GET /versions/{id}/content`：授权后返回解析视图/原文入口。
- `POST /admin/import-jobs`：受控人工导入。
- `POST /admin/documents/{id}/authority-review`：仅授权Owner操作，记录依据。
- `POST /admin/versions/{id}/lifecycle-transition`：仅授权角色操作；首期不提供自动审批。

## 反馈与候选知识
- `POST /feedback`：`WRONG_ANSWER|MISSING_DOC|WRONG_VERSION|WRONG_SCOPE|BAD_CITATION|MISSING_CONTEXT|SUGGESTION|OTHER`。
- `GET /admin/feedback`：审核队列。
- `POST /admin/feedback/{id}/triage`：分类、分派、合并重复。
- `POST /admin/candidates/extract`：从指定反馈/查询快照提炼候选；只生成草稿，不发布。
- `GET /admin/candidates`、`GET /admin/candidates/{id}`。
- `POST /admin/candidates/{id}/review`：`ACCEPT_FOR_VALIDATION|REQUEST_CHANGES|REJECT`。
- `POST /admin/candidates/{id}/validation`：记录方法、结果、证据、验证人。
- `POST /admin/candidates/{id}/approve-publication`：授权知识Owner批准。
- `POST /admin/knowledge-items/{id}/publish`：批准后发布；写入版本和审计。
- `POST /admin/knowledge-items/{id}/withdraw`：撤回并使索引失效。

## 应用接入
- `POST /admin/applications`：登记调用应用、Owner、scope、身份方式。
- `GET /applications/me`：当前应用身份和可用scope。
- `POST /applications/token`：仅按公司认可的服务身份流程签发/交换令牌；不得自创绕过SSO的凭证机制。

## MCP/插件
首期不开发完整MCP/插件。未来适配器只能包装上述API，沿用相同身份、scope、审计、速率限制和证据结构，不允许直连数据库或绕过ACL。

## 安全
ACL在检索前过滤；模型输出引用由服务端校验；知识候选提炼工具与发布工具权限分离；Dify调用不能丢失终端用户可信身份。若无法安全传递身份，不得开放受限知识域。
