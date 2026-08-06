# PresPPTDeck — AI职场汇报顾问

> **通过12个标准步骤，让AI从"PPT制作工具"升级为"职场汇报顾问"。**

---

## 核心理念

> **先思考，再表达；先逻辑，再设计；先说服，再美化。**

PresPPTDeck 不是一个简单的PPT模板库，而是一套**完整的职场汇报方法论**。它帮助用户完成从业务理解、逻辑构建、视觉设计到最终交付的全流程闭环。

---

## 项目结构

```
PresPPTDeck/
├── SKILL.md                          # AI Agent 顶层定义（核心入口）
├── README.md                         # 项目说明（本文件）
├── manifest.yaml                     # 技能元数据
├── CHANGELOG.md                      # 版本变更记录
├── requirements.txt                  # Python依赖
│
├── framework/                        # 方法论框架
│   └── 12step_framework.md          # 12步完整方法论详解
│
├── prompts/                          # 12步Prompt体系
│   ├── 01_audience.md               # Step 1: 明确汇报对象
│   ├── 02_purpose.md                # Step 2: 明确汇报目的
│   ├── 03_key_concern.md            # Step 3: 确认核心关注点
│   ├── 04_storyline.md              # Step 4: 建立故事线
│   ├── 05_slide_architecture.md     # Step 5: 拆解分页结构
│   ├── 06_design_style.md           # Step 6: 确定设计风格
│   ├── 07_visual_model.md           # Step 7: 选择视觉模型
│   ├── 08_markdown_review.md        # Step 8: Markdown逻辑复核
│   ├── 09_output_format.md          # Step 9: 确认输出形式
│   ├── 10_resources.md              # Step 10: 搜集素材资源
│   ├── 11_production.md             # Step 11: 生成最终PPT
│   └── 12_coaching.md               # Step 12: 汇报演练优化
│
├── assets/                           # 资源库
│   ├── design_styles.md             # 5种完整设计风格（含配色/字体/图标）
│   └── visual_models.md             # 12种视觉模型（含使用场景和搭配）
│
├── templates/                        # 页面结构模板
│   ├── annual_review.md             # 年度述职模板
│   ├── product_strategy.md          # 产品策略模板
│   ├── project_report.md            # 项目汇报模板
│   ├── proposal.md                  # 方案评审模板
│   └── strategic_planning.md        # 战略规划模板
│
├── examples/                         # 完整案例
│   ├── ai_finance_case.md           # AI金融转型案例
│   ├── annual_review_case.md        # 年度述职案例
│   └── product_launch_case.md       # 产品发布案例
│
├── generator/                        # PPT生成器
│   ├── __init__.py                   # 模块入口
│   ├── ppt_generator.py             # 核心生成器
│   └── templates.py                 # 页面布局模板
│
└── tests/                            # 测试
    └── test_cases.md                # 测试用例
```

---

## 12步工作流

```
第一阶段：业务理解（Discover）
  ① 明确汇报对象 → 谁看？
  ② 明确汇报目的 → 为什么做？
  ③ 确认核心关注点 → 听众最关心什么？

第二阶段：逻辑构建（Framework）
  ④ 建立故事线 → WHY→WHAT→HOW→RESULT→NEXT
  ⑤ 拆解分页结构 → 一页一观点

第三阶段：视觉设计（Visualization）
  ⑥ 确定设计风格 → 配色+字体+图标
  ⑦ 选择视觉模型 → 每页用什么图形
  ⑧ Markdown逻辑复核 → 制作前最后检查

第四阶段：制作交付（Delivery）
  ⑨ 确认输出形式 → PPTX/HTML/PDF/图片
  ⑩ 搜集素材资源 → 图片+图标+数据+案例
  ⑪ 生成最终PPT → 完整内容+设计
  ⑫ 汇报演练优化 → 演讲稿+Q&A准备
```

---

## 快速开始

### 1. 使用 SKILL.md 作为 AI 指令

将 `SKILL.md` 的内容作为 system prompt 提供给 AI 助手（如 Claude），AI 将自动按照12步方法论引导你完成PPT制作。

### 2. 使用 Python 生成器

```bash
# 安装依赖
pip install -r requirements.txt

# 快速预览（生成测试PPT）
python -m generator.ppt_generator

# 编程方式使用
python -c "
from generator import PPTGenerator

gen = PPTGenerator(style='tech_blue')
gen.add_cover(title='我的汇报', subtitle='副标题')
gen.add_content(title='核心观点', points=['要点1', '要点2', '要点3'])
gen.add_ending(thank_text='感谢聆听')
gen.save('my_ppt.pptx')
"
```

### 3. 使用模板数据构建

```python
from generator import PPTGenerator

template_data = {
    "title": "Q2业务汇报",
    "subtitle": "AI驱动的业务增长",
    "presenter": "张三",
    "style": "tech_blue",
    "toc_items": [
        {"title": "背景", "subtitle": "为什么做"},
        {"title": "策略", "subtitle": "怎么做"},
        {"title": "成果", "subtitle": "效果如何"},
    ],
    "slides": [
        {"type": "content", "title": "核心策略", "points": ["策略1", "策略2", "策略3"]},
        {"type": "data", "title": "核心指标", "metrics": [
            {"label": "用户增长", "value": "+35%", "trend": "↑35%", "trend_up": True}
        ]},
    ],
    "ending": {"thank_text": "感谢聆听", "summary": "核心信息总结"}
}

gen = PPTGenerator(style="tech_blue")
gen.build_from_template(template_data)
gen.save("output.pptx")
```

---

## 5种设计风格

| 风格 | 主色 | 适合场景 |
|------|------|---------|
| 科技蓝白 | #1A73E8 | AI、技术、数字化 |
| 金融黑金 | #1A1A2E + #D4AF37 | 投资、战略、高端汇报 |
| 极简白灰 | #FFFFFF + #1A1A1A | 产品、管理汇报 |
| 深色科技 | #0F172A + #38BDF8 | AI产品发布、技术峰会 |
| 活力橙红 | #FF6B35 | 产品发布、营销方案 |

---

## 5种汇报模板

| 模板 | 页数 | 适用场景 |
|------|------|---------|
| 年度述职 | 12页 | 年中/年度述职、晋升答辩 |
| 产品策略 | 12页 | 产品定位、产品规划 |
| 项目汇报 | 12页 | 项目阶段汇报、结项报告 |
| 方案评审 | 11页 | 技术/产品方案评审 |
| 战略规划 | 13页 | 年度/季度战略规划 |

---

## 版本

- **v0.2.0** — 全面升级：完整12步方法论、12个详细Prompt、5种设计风格、12种视觉模型、5个完整模板、3个完整案例、Python PPT生成器

---

## 适用场景

- 年度/季度述职报告
- 项目阶段汇报和结项报告
- 产品策略和方案评审
- 战略规划汇报
- 投资人路演
- 产品发布会
- 任何需要正式汇报的职场场景