# MCP 与插件接入策略

## 首期
不开发完整 MCP Server 或插件市场；只稳定 REST API、应用登记、scope、身份映射、审计和错误结构。

## 后续 MCP
将 search_knowledge、resolve_document、check_applicability、submit_feedback 等能力包装为工具；工具按用户/应用授权；输出结构化证据；不暴露任意SQL、文件系统或管理操作。

## 插件
按具体宿主平台能力开发适配器；插件仅调用统一API；不复制知识索引和权限规则。

## 安全
服务端令牌校验、最小scope、审计、速率限制、用户身份委托；身份无法可信传递时不开放受限知识。
