# Diagram Rules — 绘图规则

## 铁律：先确定逻辑，再决定表达方式

任何图都必须回答：**它表达了什么关系？**

如果图只是装饰 → DELETE。

## 图表选择决策表

| 信息关系 | 图形 |
|---------|------|
| 趋势 | 折线图 |
| 对比 | 排序条形图 |
| 构成 | 瀑布图 |
| 计划 | 甘特图 |
| 拆解 | Issue Tree |
| 转化 | 漏斗 |
| 关系 | Relationship Diagram |
| 流程 | Process |
| 因果 | Causal Chain |
| 层级 | Pyramid / Layer |
| 能力 | Capability Map |
| 闭环 | Flywheel / Closed Loop |
| 时间 | Timeline |
| 比较 | Before / After |
| 选择 | Decision Matrix |
| 数据 | Chart |

## 形状规范

优先：矩形、轻量圆角矩形、圆、线、箭头。
避免：过度圆角、3D、复杂渐变、无意义装饰。

## 箭头语义

箭头必须表达正确关系：
- 单向箭头 → 依赖 / 流程方向
- 双向箭头 ↔ 交互 / 协作
- 虚线箭头 → 反馈 / 弱关联

## Engineering Information Design

涉及 AI / Agent / IT / Platform / Architecture 时，必须标注：
Module、Boundary、Input、Output、Owner、Evidence、Gate、Feedback。