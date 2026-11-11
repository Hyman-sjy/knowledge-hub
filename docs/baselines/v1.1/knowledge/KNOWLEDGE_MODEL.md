# 知识模型 V1.1

## 1. 知识对象类型
- 权威文件知识：制度、程序、标准、SOP、检验规范。
- 结构化要求知识：条款、检验项目、指标、数值、单位、适用条件。
- 经验知识：案例、改善措施、验证方法、反例。
- 方法知识：8D、SPC、FMEA、APQP等经审核的方法资料。
- 组织流程知识：职责、流程、审批路径、通知记录。
- 候选知识：来自反馈/查询/文件抽取，尚未批准发布。

## 2. 统一知识条目字段
knowledge_item_id、type、title、content/structured_payload、domain、applicability、source_refs、trust_status、owner、review_policy、version、valid_from/to、status、created_by、approved_by。

## 3. 原则
文件是权威证据载体；业务对象是知识关系入口；候选知识不是正式知识。结构化数值必须有单位、条件和原文位置。AI总结不能替代原文。
