# PresPPTDeck — AI商业汇报架构师

> **From scattered ideas → Structured Story → Professional Deck**
>
> 先帮你把故事想清楚，再帮你把故事讲漂亮。

PresPPTDeck 是一个 AI 商业汇报架构师。它不再需要你填写完整需求，而是基于你的一句话想法，自动补全行业背景、市场数据、竞争案例和商业价值，构建完整的商业故事，**并在生成 PPT 之前和你确认框架**，确保 AI 理解正确后再进入视觉设计。

---

## 核心理念

```
THINK  → 帮用户想清楚（Discovery + Expansion + Architect）
CONFIRM → 和用户确认讲什么（Story Approval）★
CREATE → 帮用户表达出来（Pattern + Visual + Generator + Quality）
```

**一句话：** 先共同确认"讲什么"，再由 AI 决定"怎么讲、怎么画、怎么做成 PPT"。

---

## 项目结构

```
PresPPTDeck/
├── SKILL.md                          # AI Agent 顶层定义
├── core/                             # 核心引擎
│   ├── discovery.md                  # 3问发现模块
│   ├── content_expansion.md          # AI主动补全引擎（★ 核心差异化）
│   ├── story_architect.md            # Executive Story Framework
│   └── story_approval.md             # ★ Story Approval 汇报框架确认
├── design/                           # 设计系统
│   ├── style_system.md               # 5种设计风格
│   ├── visual_rules.md               # 视觉评分规则
│   └── pattern_library/              # 15种版式模式
├── quality/                          # 质量保障
│   └── presentation_checker.md
├── generator/                        # PPT生成器
├── templates/                        # 5种汇报模板
├── examples/                         # 完整案例
└── tests/                            # 测试用例
```

---

## 3阶段工作流

### THINK — 帮用户想清楚

1. **Discovery**：只问3个问题（对象/目的/想法）
2. **Content Expansion**：AI主动补全行业背景、数据、案例、价值 ★
3. **Story Architect**：6段式商业故事 + 页面规划 + 模式推荐

### CONFIRM — 和用户确认讲什么 ★

4. **Story Approval**：输出三级信息结构（标题+副标题+核心逻辑），用户确认后再进入设计

### CREATE — 帮用户表达出来

5. **Pattern Selector**：自动选择最佳视觉模式
6. **Visual Designer**：设计风格 + 视觉规则检查
7. **PPT Generator**：生成 PPTX/HTML/Markdown
8. **Quality Checker**：Page Score 自动评分

---

## 快速开始

### 1. 使用 SKILL.md 作为 AI 指令

将 `SKILL.md` 作为 system prompt 提供给 AI 助手。

### 2. 使用 Python 生成器

```bash
pip install -r requirements.txt
python -m generator.ppt_generator
```

---

## 版本

- **v0.3.0** — AI商业汇报架构师：THINK→CONFIRM→CREATE 3阶段引擎，Story Approval 强制节点
- **v0.2.0** — 完整12步方法论、PPT生成器
- **v0.1.0** — 初始版本