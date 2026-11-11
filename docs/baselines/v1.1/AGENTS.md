# AGENTS.md — QKH V1.1 项目执行规则

## 必读
README、PROJECT_PLAN、ARCHITECTURE、DATABASE_SCHEMA、KNOWLEDGE_MAP、INGESTION_PIPELINE、PARSING_RULES、KNOWLEDGE_LIFECYCLE、KNOWLEDGE_TRUST_LEVELS、API_SPEC、SECURITY、TEST_PLAN及当前Phase。

## 强制规则
- 先检查仓库状态和现有文件，不覆盖已有资料；V1.0快照只读。
- 每个阶段先计划、列影响文件和验收，再实施。
- 所有状态和知识关系必须有明确schema、来源和测试。
- AI可提炼候选，不可决定权威性、权限、审批或正式发布。
- 正式知识发布必须有授权Owner、审核记录和可追溯证据。
- 质量案例区分假设、采纳、待验证、验证成功、验证失败；失败/反例不得删除。
- 四种文件解析策略分别实现和评测；不能用通用固定长度切片替代。
- 表格数值必须保留表头、单位、规格/条件和源位置。
- ACL在检索前执行；权限服务异常默认拒绝。
- 统一API是所有入口的唯一业务调用层；客户端不得直连数据库/Dify知识库。
- MCP/插件首期只保留契约，不擅自扩大实现范围。
- 不提交真实敏感质量文件、员工数据、密钥到Git。
- 每个Phase更新CHANGELOG、决策、风险、进度、ADR和测试报告。
- 不声称未执行测试通过；输出命令、结果和限制。
