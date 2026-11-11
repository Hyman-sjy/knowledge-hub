# 知识关系模型

## 首期关系
Document CONTAINS Clause/Table；Clause APPLIES_TO Product/Specification/Process；Clause DEFINES InspectionItem/Metric；Document REFERENCES Document/Standard；Feedback ABOUT Query/Document/Answer；Candidate DERIVED_FROM Feedback/Query/Document；Candidate SUPPORTS/CONTRADICTS Candidate；KnowledgeItem VALIDATED_BY Evidence。

## 后续关系
Case INVOLVES Defect/Product/Batch/Equipment；Case ROOT_CAUSE_HYPOTHESIS FailureMode；Case VALIDATED_BY Experiment；Improvement APPLIES_TO Process；Case SUPERSEDES/CONTRADICTS prior case。

## 关系证据
每条关系需记录来源、有效时间、创建者、审核状态、置信说明。首期用关系表，不建设复杂图数据库。
