# PresPPTDeck — Consulting-grade PPT 生产系统

> **Logic 决定"讲什么" → Content 决定"凭什么" → Visual 决定"怎么讲" → Partner 决定"能不能交付"。**

PresPPTDeck 是一个 **1+4 多 Agent 架构** 的 consulting-grade PPT 生产系统。它不再是"一个超级 Prompt"，而是由一个薄薄的全局宪法 + 四个职责完全不同的 Agent 组成，通过 12 步编排工作流调度。

---

## 系统架构

```
GLOBAL CONSTITUTION（10 条全局规则）
        │
        ├── 01 Logic Architect    讲什么 → Storyline
        ├── 02 Content Strategist 凭什么 → Evidence
        ├── 03 Visual Designer    怎么画 → Layout/Visual
        └── 04 Partner QA         能否交付 → PASS/REWORK
```

---

## 四个 Agent 职责边界（严禁越界）

| Agent | 核心问题 | 唯一职责 | 绝对不做 |
|-------|---------|---------|---------|
| 01 Logic Architect | 该讲什么？ | 模糊需求 → Storyline | 不设计视觉、不补证据 |
| 02 Content Strategist | 凭什么成立？ | 补证据 + 分析 | 不改 Storyline、不排版 |
| 03 Visual Designer | 该怎么画？ | 内容 → 咨询级可编辑页面 | 不改变结论 |
| 04 Partner QA | 能拿给管理层吗？ | 挑错否决 | 不生产内容 |

---

## 目录结构

```
PresPPTDeck/
├── SKILL.md                        # 总调度入口
├── constitution/GLOBAL_CONSTITUTION.md  # 10 条全局规则
├── agents/                         # 4 个独立 Agent
│   ├── 01_LOGIC_ARCHITECT.md
│   ├── 02_CONTENT_STRATEGIST.md
│   ├── 03_VISUAL_DESIGNER.md
│   └── 04_PARTNER_QA.md
├── framework/12STEP_WORKFLOW.md    # 12 步编排工作流
├── patterns/                       # 页面信息结构模式（20+ 种）
├── visual/                         # 视觉规范（颜色/字体/网格/图标/绘图）
├── qa/                             # QA checklist
├── generator/                      # python-pptx 生成器
├── templates/                      # 汇报类型模板
├── examples/                       # 完整案例
└── tests/                          # 测试
```

---

## 编排流程

```
用户输入
  → 01 Logic Architect（故事线）
  → 02 Content Strategist（证据补全）
  → PPT Blueprint
  → ❗ 用户确认（硬门槛）
  → 03 Visual Designer（页面设计）
  → 04 Partner QA（PASS / REWORK）
  → 交付 或 精确回退
```

---

## 快速使用

1. 将 `SKILL.md` 作为调度入口
2. 系统会依次启动 4 个 Agent
3. Logic + Content 输出 PPT Blueprint 后，**等待用户确认**
4. 确认后进入 Visual + QA，最终用 `generator/` 生成 PPTX

```bash
pip install -r requirements.txt
python -m generator.ppt_generator
```

---

## 版本

- **v0.4.0** — 1+4 多 Agent 架构重构（逻辑/内容/视觉/QA 职责分离）
- **v0.3.0** — AI 商业汇报架构师（Content Expansion + Pattern + 视觉评分）
- **v0.2.0** — 12 步方法论 + 生成器
- **v0.1.0** — 初始版本