# Pattern Library — 页面信息结构模式库

> 不是选择"模板"，而是选择"信息结构表达方式"。
> 规则：**Content → Structure → Pattern → Layout**，先确定逻辑，再决定表达方式。

---

## 模式索引

### 叙事类
| 模式 | 用途 |
|------|------|
| [cover](cover.md) | 封面 |
| [executive-summary](executive-summary.md) | 执行摘要 |

### 框架与拆解类
| 模式 | 用途 |
|------|------|
| [framework](framework.md) | 框架模型 / 战略框架 |
| [pyramid](pyramid.md) | 金字塔 / 层级 |
| [layer](layer.md) | 分层模型 / 技术架构层级 |
| [issue-tree](issue-tree.md) | 问题树 / 根因拆解 |
| [capability-map](capability-map.md) | 能力地图 |

### 流程与时间类
| 模式 | 用途 |
|------|------|
| [process](process.md) | 流程图 |
| [timeline](timeline.md) | 时间轴 |
| [roadmap](roadmap.md) | 路线图 |
| [funnel](funnel.md) | 漏斗 / 转化 |

### 对比与选择类
| 模式 | 用途 |
|------|------|
| [comparison](comparison.md) | 方案对比 |
| [before_after](before_after.md) | 改造前后 |
| [matrix](matrix.md) | 矩阵 / 四象限 |
| [decision-matrix](decision-matrix.md) | 决策矩阵 / 多方案比选 |

### 数据与证据类
| 模式 | 用途 |
|------|------|
| [dashboard](dashboard.md) | KPI 仪表盘 |
| [evidence-chain](evidence-chain.md) | 证据链 / 论证闭环 |

### 组织与运营类
| 模式 | 用途 |
|------|------|
| [governance-model](governance-model.md) | 组织架构 / 治理模型 |
| [operating-model](operating-model.md) | 运营模型 |
| [architecture](architecture.md) | 技术架构 |
| [closed-loop](closed-loop.md) | 飞轮 / 闭环 |
| [case_card](case_card.md) | 案例卡片 |

---

## 选择指南

### 按内容关系选择

```
内容 = 战略/体系    → framework / pyramid / layer
内容 = 问题拆解     → issue-tree / hypothesis-tree
内容 = 能力建设     → capability-map
内容 = 流程/步骤    → process
内容 = 时间/规划    → timeline / roadmap
内容 = 转化/流失    → funnel
内容 = 对比/变化    → comparison / before_after
内容 = 多方案选择   → decision-matrix / matrix
内容 = 数据/指标    → dashboard
内容 = 论证闭环     → evidence-chain
内容 = 团队/分工    → governance-model / operating-model
内容 = 技术/系统    → architecture / layer
内容 = 增长/循环    → closed-loop
```

### 按汇报类型选择

| 汇报类型 | 高频 Pattern |
|---------|-------------|
| 年度述职 | dashboard, before_after, timeline, case_card |
| 项目汇报 | process, dashboard, comparison, roadmap |
| 方案评审 | comparison, decision-matrix, architecture, dashboard |
| 战略规划 | framework, pyramid, closed-loop, roadmap |
| 产品发布 | before_after, dashboard, case_card, timeline |
| 投资人路演 | dashboard, closed-loop, matrix, comparison |