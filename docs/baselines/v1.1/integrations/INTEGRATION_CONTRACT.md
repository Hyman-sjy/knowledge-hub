# 统一接入契约

## 原则
所有 Web、企业微信、个人AI小系统、未来MCP/插件统一调用 Knowledge API；不得直连 PostgreSQL、Dify内部知识库或文件存储。

## 每个调用方登记
application_id、name、owner、environment、auth_method、allowed_scopes、rate_limit、status、created_at。

## 身份
用户交互请求传递可信终端用户身份；后台任务使用独立服务身份。应用身份不能冒充用户身份。服务端进行 scope + user ACL 双重授权。

## 统一响应证据
evidence_id、document_id、version_id、doc_code、title、clause_id、heading_path、page/sheet/cell、authority/lifecycle status、source locator、snippet。

## 入口路线
首期 Web + 企业微信；未来 MCP/插件只做 API adapter，复用同一授权、审计、限流和证据结构。
