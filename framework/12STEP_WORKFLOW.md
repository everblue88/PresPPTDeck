# 12 Step Orchestration Workflow

> **12 Step 不再是"一个超级 Prompt"，而是整个 Agent 系统的编排工作流。**

它定义了 4 个 Agent 如何被调度，以及用户确认闸门的位置。

---

## 编排全景

```
用户输入
   ↓
【01 Logic Architect】        ← Step 1-6（理解 → 问题 → 故事线 → 蓝图）
   ↓
【02 Content Strategist】     ← Step 7（证据补全）
   ↓
【PPT Blueprint】             ← Step 8-9（逐页蓝图 + 数据缺口）
   ↓
❗ USER CONFIRM               ← 用户确认闸门（硬门槛）
   ↓
【03 Visual Designer】        ← Step 10-11（Pattern → Layout → Visual）
   ↓
【PPTX / Deck】
   ↓
【04 Partner QA】             ← Step 12（最终审稿 → PASS / REWORK）
   ↓
   ┌─── PASS ───→ FINAL
   └── REWORK ──→ 精确回退到对应 Agent
```

---

## 12 Step 与 4 Agent 的映射

| Step | 名称 | 归属 Agent | 输出 |
|------|------|-----------|------|
| 1 | 理解需求（最少问询） | 01 Logic | 三个问题的答案 |
| 2 | 定义汇报对象 | 01 Logic | Audience Profile |
| 3 | 定义汇报目的 | 01 Logic | Objective |
| 4 | Governing Question | 01 Logic | 核心问题 |
| 5 | Issue Tree | 01 Logic | MECE 问题分解 |
| 6 | Hypothesis + Storyline | 01 Logic | 假设 + 故事线 |
| 7 | Evidence Mapping | 02 Content | 结论→论据→证据 |
| 8 | 逐页蓝图（内容补全） | 02 Content | Page Blueprint + 证据等级 |
| 9 | 输出 PPT Blueprint | 01 + 02 协同 | 完整内容蓝图 |
| 10 | Pattern Selector + Layout | 03 Visual | 页面结构 + 版式 |
| 11 | Visual Design | 03 Visual | 可视化页面 |
| 12 | Partner QA | 04 QA | PASS / REWORK |

---

## 关键机制

### 1. 用户确认闸门（硬门槛）

- Logic + Content 输出 `PPT Blueprint` 后，**必须**经用户确认。
- 用户确认前，**不得**进入 Visual / 页面生成。
- 用户回复"继续"或给出新指令 = 通过；用户提修改 = 只改受影响分支。

### 2. REWORK 精确回退

QA 的 REWORK 不整体重来，而是精确回退到对应层：

| QA 发现 | 回退目标 |
|---------|---------|
| 逻辑问题（Page 5 结论不能由 Page 4 推出） | 01 Logic Architect |
| 证据问题（"效率提升40%"无证据） | 02 Content Strategist |
| 视觉问题（信息关系对但层级乱） | 03 Visual Designer |

### 3. 循环而非串行

```
Logic → Content → [确认] → Visual → QA
            ↑                              │
            └────────── REWORK ────────────┘
```

## 一句话总结

> **Logic 决定"讲什么"，Content 决定"凭什么"，Visual 决定"怎么讲"，Partner 决定"能不能交付"。**