# 文档接入、解析与索引流水线 V1.1

## 1. 输入与治理
首期 OA/微盘人工导出或管理员补录。导入前登记来源、文件编号、Owner、密级、候选版本、适用范围。计算 SHA-256，检测重复；权威状态未确认的文件进入隔离区。

## 2. 四类解析策略（正式基线）
### A. 程序文件、质量手册：层级切片
- 识别章、节、条、款、项及自定义编号。
- 保留 parent_id、heading_path、clause_id、页码、跨页连续关系。
- child 条款检索时附带必要父级标题和适用上下文。
- 表格、流程图、附件与所属条款建立关系。
- 不把页眉页脚、修订记录误合并为正文；保留必要修订元数据。

### B. 检验规范、标准：条款结构切片
- 每条要求形成独立结构对象。
- 关联适用产品、规格、材料、工艺、试验条件、样本量、设备、检验频率、判定规则。
- 数值必须保留字段名、运算符、值、单位、上下限、条件和原文定位。
- 关联引用表格、附录和被引用条款。
- 无法确定适用条件时标记 incomplete，不得模型补全。

### C. Excel检验表、参数表：结构化表格解析
- 保留 workbook、sheet、table、header hierarchy、row/column、cell range。
- 处理多层表头、合并单元格、隐藏行列/工作表、公式与缓存值。
- 每个数据值必须关联表头路径、单位、规格/条件和单元格坐标。
- 空白、0、NA、横线的含义不可擅自等同。
- 复杂表格进入人工核验；公式结果和原公式均保留。
- 不允许将单元格数值脱离表头和单位独立向量化。

### D. 普通通知、会议纪要：语义段落切片
- 按标题、议题、段落、时间组织。
- 提取发布部门、发布人、发布日期、执行日期、接收范围、有效期、关联文件。
- 区分讨论意见、建议、会议决议、正式批准要求。
- 记录是否被后续通知替代；未确认的会议意见不得成为正式制度要求。

## 3. 统一处理流程
原件登记 → 哈希/去重 → 权威性确认 → 解析 → 结构化转换 → 人工抽样核验 → 类型化切片 → FTS/vector索引 → 回归测试 → 发布到对应知识域。

## 4. 统一 ParsedDocument 元素
element_id、document_id、version_id、element_type、parent_id、heading_path、clause_id、content、table_id、table_headers、row/column、page_no、sheet_name、cell_range、applicability、source_locator、parser_name/version、content_hash、review_status。

## 5. 解析候选
Docling 首选 PoC；RAGFlow 与现有 Dify 对照。最终以同样本、同金标准的分类型测试结果决定。不能用单一总体平均掩盖 Excel/扫描PDF的失败。

## 6. 发布门槛
解析成功不等于权威有效。正式检索需同时满足：Owner确认、authority_status=CONFIRMED、lifecycle_status=EFFECTIVE、解析核验通过、索引为当前版本、ACL通过。
