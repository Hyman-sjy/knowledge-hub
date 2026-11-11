# PHASE 01 — 工程骨架与主数据（第2周）

## 任务
- 初始化 pnpm workspace（若团队确认采用 pnpm）。
- 建立 React/Vite、Hono API、Drizzle、PostgreSQL。
- 配置 strict TypeScript、ESLint、Prettier、Vitest。
- 建立数据库迁移和种子数据。
- 实现 users/roles、documents/versions/sources、ACL、audit。
- 建立导入任务状态机。
- 实现健康检查、请求ID、统一错误结构。
- 编写 API/OpenAPI 契约。

## 验收
- 空环境可按文档启动。
- migration 可重复执行/有回滚策略。
- 单元测试覆盖版本状态、权限默认拒绝。
- 无密钥进入仓库。
