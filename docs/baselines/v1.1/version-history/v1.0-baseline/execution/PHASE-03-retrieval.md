# PHASE 03 — 检索与 Dify 集成（第4周）

## 任务
- 精确文档编号/标题检索。
- PostgreSQL FTS 与 pgvector 检索。
- RRF/重排接口。
- 版本、适用范围、ACL前置过滤。
- 统一证据对象和来源定位。
- 四类意图路由。
- Dify External Knowledge API adapter。
- 无证据/冲突/权限不足拒答。
- 检索日志和回归测试。

## 验收
- Recall@5 达到阶段目标或输出明确差距。
- 当前有效版本策略可测试。
- 越权证据不进入模型上下文。
- Dify响应能携带原文件、版本、条款和位置。
