# Codex 仓库执行入口

这是仓库路径适配说明，不是对原始提示词的改写。
原始文件完整保留在 [V1.1 执行提示词](docs/baselines/v1.1/CODEX_EXECUTION_PROMPT.md)，
用户提供的[独立提示词](docs/sources/CODEX_EXECUTION_PROMPT.md)与其逐字节一致。

## 当前范围

本次授权为工程文件整理并推送 GitHub。原始提示词中的“当前唯一任务：PHASE 00”
是未来开发任务书，不会自动触发本次开发或企业接口联调。
归档和完整性检查完成不构成 G0 验收通过。

## 后续明确启动 PHASE 00 时

先读根目录 [AGENTS.md](AGENTS.md)、[README.md](README.md)及[基线核对说明](docs/BASELINE_REVIEW.md)，
再按原始提示词读取实际路径：

1. [原始规则](docs/baselines/v1.1/AGENTS.md)、[项目计划](docs/baselines/v1.1/PROJECT_PLAN.md)、[架构](docs/baselines/v1.1/ARCHITECTURE.md)。
2. [数据模型](docs/baselines/v1.1/DATABASE_SCHEMA.md)、[知识地图](docs/baselines/v1.1/KNOWLEDGE_MAP.md)、[解析流水线](docs/baselines/v1.1/INGESTION_PIPELINE.md)。
3. [解析细则](docs/baselines/v1.1/knowledge/PARSING_RULES.md)、[知识生命周期](docs/baselines/v1.1/knowledge/KNOWLEDGE_LIFECYCLE.md)、[可信等级](docs/baselines/v1.1/knowledge/KNOWLEDGE_TRUST_LEVELS.md)。
4. [API](docs/baselines/v1.1/API_SPEC.md)、[接入契约](docs/baselines/v1.1/integrations/INTEGRATION_CONTRACT.md)、[安全](docs/baselines/v1.1/SECURITY.md)、[测试](docs/baselines/v1.1/TEST_PLAN.md)。
5. [PHASE 00 任务](docs/baselines/v1.1/execution/PHASE-00-technical-spike.md)、[准备清单](docs/PHASE_00.md)、[解析基准](docs/baselines/v1.1/evaluation/PARSER_BENCHMARK.md)、[黄金集](docs/baselines/v1.1/evaluation/GOLDEN_SET_SPEC.md)。

检查仓库和环境，给出评估、差距、影响文件、实施步骤与验收条件；
先做评测准备和 PoC，不生成完整平台。真实样本或企业条件缺失时明确记录“未执行”。
阶段记录及后续修订放在基线目录外，用 Git、ADR 和任务看板关联；
不得直接修改 `docs/baselines/v1.1/` 内的原始归档和历史文件。
