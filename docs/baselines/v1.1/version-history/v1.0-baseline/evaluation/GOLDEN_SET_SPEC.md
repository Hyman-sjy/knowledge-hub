# 黄金测试集规范

每题字段：
- case_id
- question
- user_role / allowed_domains
- intent_expected
- entities_expected
- expected_document_ids
- expected_version_ids
- expected_clause_ids
- expected_answer_points
- must_abstain
- risk_level
- reviewer
- review_date

100题分布：30文件/条款、20跨文件、20适用范围、20无答案/冲突/废止、10权限/对抗。

评分分开统计：检索召回、排序、答案事实、引用定位、拒答、权限。不得将模型自评置信度当准确率。
