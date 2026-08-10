# Pattern Library — 版式模式库

> 15种PPT页面表达模式。不是选择"模板"，而是选择"表达方式"。

---

## 模式索引

### 叙事类

| 模式 | 用途 | 何时使用 |
|------|------|---------|
| [cover](cover.md) | 封面 | 任何PPT的第1页 |
| [summary](summary.md) | 执行摘要 | 需要1页讲清楚整个故事 |
| [ending](cover.md) | 结尾 | 任何PPT的最后1页 |

### 框架类

| 模式 | 用途 | 何时使用 |
|------|------|---------|
| [framework](framework.md) | 框架模型 | 表达战略框架、体系结构 |
| [pyramid](pyramid.md) | 金字塔 | 层级关系、优先级排序 |
| [matrix](matrix.md) | 矩阵/四象限 | 多维度分析、定位 |
| [flywheel](flywheel.md) | 飞轮 | 增长逻辑、正向循环 |

### 流程类

| 模式 | 用途 | 何时使用 |
|------|------|---------|
| [process](process.md) | 流程图 | 步骤、流程、操作链路 |
| [timeline](timeline.md) | 时间轴 | 时间节点、里程碑 |
| [roadmap](roadmap.md) | 路线图 | 规划、分阶段目标 |

### 数据类

| 模式 | 用途 | 何时使用 |
|------|------|---------|
| [dashboard](dashboard.md) | 数据仪表盘 | 核心指标展示 |
| [comparison](comparison.md) | 方案对比 | 多个方案/选项对比 |
| [before_after](before_after.md) | 改造前后 | 对比变化、效果展示 |

### 展示类

| 模式 | 用途 | 何时使用 |
|------|------|---------|
| [case_card](case_card.md) | 案例卡片 | 客户案例、成功案例 |
| [organization](organization.md) | 组织架构 | 团队结构、角色分工 |
| [architecture](architecture.md) | 技术架构 | 系统架构、技术方案 |

---

## 选择指南

### 按内容类型选择

```
内容 = 战略/体系    → framework / pyramid
内容 = 流程/步骤    → process
内容 = 时间/规划    → timeline / roadmap
内容 = 数据/指标    → dashboard
内容 = 对比/变化    → comparison / before_after
内容 = 案例/证据    → case_card
内容 = 团队/分工    → organization
内容 = 技术/系统    → architecture
内容 = 增长/循环    → flywheel
内容 = 分析/定位    → matrix
```

### 按汇报类型选择

| 汇报类型 | 高频使用的Pattern |
|---------|------------------|
| 年度述职 | dashboard, before_after, timeline, case_card |
| 项目汇报 | process, dashboard, comparison, roadmap |
| 方案评审 | comparison, matrix, architecture, dashboard |
| 战略规划 | framework, pyramid, flywheel, roadmap |
| 产品发布 | before_after, dashboard, case_card, timeline |
| 投资人路演 | dashboard, flywheel, matrix, comparison |

---

## 每个 Pattern 文件的结构

```
# Pattern名称

## 适用场景
## 结构图示（ASCII art）
## 布局参数（位置、大小）
## 内容模板
## 变体
## 使用示例
## 视觉评分要点
```