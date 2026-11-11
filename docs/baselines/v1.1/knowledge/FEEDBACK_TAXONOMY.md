# 反馈分类与知识候选规则

## 用户反馈类型
WRONG_ANSWER、MISSING_DOC、WRONG_VERSION、WRONG_SCOPE、BAD_CITATION、MISSING_CONTEXT、SUGGESTION、OTHER。

## 专业处理决定
ACCEPT、MODIFY、REJECT、PENDING_VALIDATION、VALIDATION_SUCCESS、VALIDATION_FAILURE。质量案件可记录采纳/修改/否定/待验证/验证成功/验证失败，保留原因和证据。

## 候选提炼类型
NEW_RULE_CANDIDATE、FAQ_CANDIDATE、PROCESS_TIP、CASE_CANDIDATE、COUNTEREXAMPLE、DOCUMENT_GAP、ROUTING_FIX。

## 去重
使用文本相似度 + 业务对象/来源/适用范围规则生成合并建议；不自动删除原反馈；合并后每条来源仍可追溯。

## 发布
候选提炼仅生成草稿；审核者判断专业性；需要验证的先验证；知识Owner批准后发布。拒绝候选也保留理由。
