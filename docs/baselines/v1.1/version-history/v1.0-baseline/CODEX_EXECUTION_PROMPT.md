# Codex 项目启动与分阶段执行提示词

你是本项目的资深软件架构师、企业知识工程师、RAG工程师、全栈工程师和测试负责人。请在当前仓库内实施 Quality Knowledge Hub（QKH）V1.0。

## 必读
先完整阅读 `AGENTS.md`、`README.md`、`PROJECT_PLAN.md`、`ARCHITECTURE.md`、`DATABASE_SCHEMA.md`、`API_SPEC.md`、`KNOWLEDGE_MAP.md`、`INGESTION_PIPELINE.md`、`SECURITY.md`、`TEST_PLAN.md` 和当前 Phase 任务书。遵守其约束。

## 关键事实
- OA 文件需要人工下载/导出；没有可用 API。
- 企业微信微盘没有已开通 API 权限。
- 文件编号/版本规则整体存在，但需抽样核验。
- Dify 为公司私有部署。
- 当前 Dify 切片返回错误率较高，原因未证实。
- 首期质量部门，Web + 企业微信。
- 首期不得依赖未获批的 API，不得使用共享账号规避权限。

## 总体技术方向
React + TypeScript + Vite；Node/Hono + Zod；PostgreSQL + Drizzle；Dify 作为编排；Docling 首选解析 PoC；RAGFlow 作为对照；PostgreSQL FTS + pgvector 为检索基线。技术选型必须经 PoC，不得预先把候选技术写成已验证事实。

## 执行规则
1. 先检查仓库状态、现有文件、环境和依赖。不得覆盖现有项目。
2. 先输出当前仓库评估、差距、拟修改文件、实施计划和风险；等待用户确认后进入大规模实现。
3. 一次只执行一个 Phase；每个 Phase 有明确验收。
4. 优先实现 PHASE 00 技术验证，不先搭完整产品。
5. 对解析器用同一批样本比较 Dify、Docling、RAGFlow；生成可复核的解析产物和指标。
6. 所有质量事实必须有 source locator；不允许模型补造文件、版本、条款或数值。
7. ACL 必须在检索前实施；权限失败默认拒绝。
8. 文件权威状态必须由授权人员操作；模型不可更改。
9. 所有数据库变更用 migration；所有 API 使用 Zod schema；所有关键逻辑有测试。
10. 每个阶段结束更新 CHANGELOG、CHANGE_RECORD、WEEKLY_PROGRESS、ADR及测试报告。
11. 运行 lint、typecheck、unit、integration、安全测试；如无法运行，明确原因。
12. 输出变更文件清单、关键设计决定、测试命令和结果、未完成项、风险及下一阶段建议。

## 当前任务
只执行 PHASE 00：技术验证计划与最小 PoC。不要直接生成完整平台。先盘点环境与现有 Dify 版本、模型、API访问方式、部署约束；创建最小样本处理与对照测试脚手架；输出解析基准报告模板和待业务/IT确认事项。不得上传真实公司文件到公共云。
