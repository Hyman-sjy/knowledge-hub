# ADR-002：文档解析器选择

- 状态：Proposed（Docling 为首选 PoC，不是已批准生产选型）
- 候选：A 现有 Dify；B Docling + 自定义结构切片；C RAGFlow。
- 评价：DOCX标题层级、PDF版面/条款、XLSX表格、扫描OCR、原文定位、错误率、人工修复成本、部署依赖和许可。
- 决策规则：用同一批文档、同一金标准比较；不得凭 GitHub Star 或 Demo 决定。
- 生产选择需业务 Owner、技术 Owner共同批准。
