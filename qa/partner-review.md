# Partner Review — 最终合伙人审稿清单

对应 04 Partner QA 的综合审稿，最终裁决 PASS / REWORK。

## 11 项 Review

| # | Review | 判定 |
|---|--------|------|
| 1 | Executive Test：CEO 看 30 秒能懂？ | PASS / REWORK |
| 2 | Title Test：标题是结论句？（非主题描述） | PASS / FAIL |
| 3 | Storyline Test：Because/Therefore/So What/Now What | PASS / FAIL |
| 4 | MECE Test：互斥且完整 | PASS / REWORK |
| 5 | Evidence Test：每个结论有证据 | PASS / UNSUPPORTED |
| 6 | Fact Test：无虚构数据/案例/ROI | PASS / FAIL |
| 7 | Content Density：不太空不太满 | PASS / REWORK |
| 8 | Visual Test：对齐/层级/一致性/颜色语义 | PASS / REWORK |
| 9 | Diagram Test：图表达关系，非装饰 | PASS / DELETE |
| 10 | Boundary Test：AI/Human 职责边界清晰 | PASS / REWORK |
| 11 | Decision Test：帮助管理层理解/判断/决策/行动 | PASS / FAIL |

## 最终裁决

只能输出：
- **PASS**（可交付）
- **REWORK**（必须指明：修改哪页、改什么、为什么、目标、回退到哪个 Agent）

## REWORK 回退映射

| 问题类型 | 回退 |
|---------|------|
| 逻辑问题 | 01 Logic Architect |
| 证据问题 | 02 Content Strategist |
| 视觉问题 | 03 Visual Designer |