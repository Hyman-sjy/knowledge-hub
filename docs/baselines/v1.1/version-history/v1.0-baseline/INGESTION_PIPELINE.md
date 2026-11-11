# 文档接入、解析与索引流水线

## 1. 输入
首期只接受经批准可用于试点的 Word、PDF、Excel；原件通过 OA 人工导出、微盘人工导出/链接登记或管理员补录。不得假设存在自动连接器。

## 2. 流程
1. 导入前登记来源、文件编号、Owner、密级、候选版本。
2. 计算 SHA-256；检测重复文件和疑似同一逻辑文件。
3. 对照权威性台账，未确认文件进入隔离/待确认区。
4. 使用 Docling 解析，保存原始文件引用和解析产物。
5. 转换为统一 `ParsedDocument`：章节、段落、列表、表格、页码、工作表、单元格范围。
6. 运行结构完整性规则和抽样人工核验。
7. 生成知识单元：
   - 层级条款 chunk：条款作为 child，附带父级标题/章节上下文。
   - 表格 chunk：保留表题、完整表头、单位、行列、合并单元格信息；必要时整表保留。
   - 普通通知：按标题/段落切分。
8. 写入 PostgreSQL 结构数据。
9. 建立 FTS/vector 索引。
10. 运行解析/检索回归。
11. Owner 确认权威性后才允许进入正式知识检索。
12. 记录 parser 版本、规则版本、embedding 模型版本、索引时间。

## 3. 解析策略
- 程序文件/手册：基于标题层级、条款编号、段落边界。
- 检验规范/国家标准：条款独立索引，保留适用范围、表格引用和上下文。
- Excel：优先结构化表格解析，保留 sheet、header、row/column、cell range；禁止将数值单元格脱离表头。
- 扫描PDF：OCR后必须对数值、单位、编号做抽样校验；低置信解析进入人工复核。
- 页眉页脚、页码、修订记录需保留或按规则排除，不得误并入正文。
- 任何解析规则变更必须增加回归样本并重建索引版本。

## 4. 候选工具
- Docling：首选 PoC，评估结构化解析和层级切片。
- RAGFlow：对照 PoC，评估 DeepDoc、模板切片、人工检查与检索体验。
- Dify：现有基线；保留编排，不默认作为最终解析唯一来源。
- LlamaIndex：仅在自定义 ingestion orchestration 确有需要时引入，不与自建流水线重复。
- Haystack/OpenSearch：仅在检索基准显示 PostgreSQL FTS + vector 不足时评估。

## 5. 解析产物格式
每个元素必须含：element_id、document_id、version_id、element_type、text/content、heading_path、clause_id、page_no、sheet_name、cell_range、parent_id、source_locator、parser_name/version、content_hash。
