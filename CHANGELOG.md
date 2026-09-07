# Changelog

## v0.4.0 (2026-09-07)

### 架构级重构：从"单一大 Prompt"到"1+4 多 Agent 系统"

**核心变化：** 旧的 15 条规则大 Prompt 拆解为 1 个全局宪法 + 4 个职责完全不同的 Agent，由 12 步编排工作流调度。

**新增 constitition/：**
- `constitution/GLOBAL_CONSTITUTION.md`：10 条全局规则（薄），所有 Agent 共同遵守

**新增 agents/（4 个独立 Agent，职责严格分离）：**
- `agents/01_LOGIC_ARCHITECT.md`：讲什么 → Storyline（Engagement Manager 角色，不设计视觉）
- `agents/02_CONTENT_STRATEGIST.md`：凭什么 → Evidence（Research Lead 角色，不改 Storyline）
- `agents/03_VISUAL_DESIGNER.md`：怎么画 → Layout/Visual（Presentation Designer 角色，不改变结论）
- `agents/04_PARTNER_QA.md`：能否交付 → PASS/REWORK（Partner 角色，只否决不生产）

**新增 framework/：**
- `framework/12STEP_WORKFLOW.md`：12 步从"超级 Prompt"降级为"编排工作流"

**顶层重构：**
- 重写 `SKILL.md`：从"15条规则大 Prompt"改为"1+4 架构调度入口"
- 新增用户确认闸门（Logic+Content 输出 Blueprint → 用户确认 → 才进入 Visual）
- 新增 REWORK 精确回退机制（逻辑问题→Logic，证据问题→Content，视觉问题→Visual）

**目录重组：**
- `patterns/`：从 design/pattern_library 迁移 + 重命名（summary→executive-summary，flywheel→closed-loop，organization→governance-model）+ 新增 7 个（capability-map/decision-matrix/issue-tree/funnel/layer/operating-model/evidence-chain）
- `visual/`：从 design/style_system + visual_rules 拆分为 5 个（color/typography/grid/icon/diagram-rules）
- `qa/`：从 quality/ 拆分为 4 个 checklist（logic/content/visual/partner-review）

**删除旧目录：**
- 删除 `core/`、`design/`、`quality/`（内容全部迁移）

---

## v0.3.0 (2025-08-07)

### 定位升级：从"AI PPT生成器"到"AI商业汇报架构师"

**核心理念变化：** AI负责理解20%，补全80%。用户只需要提供最核心的信息，其余由AI结合行业经验、案例和最佳实践完成。

**工作流升级：** 4阶段引擎 → 3阶段引擎（THINK → CONFIRM → CREATE）

### ★ Story Approval — 汇报框架确认（V0.3.0 关键节点）

- 新增 `core/story_approval.md`：强制内容确认节点
- 三级信息结构输出：Title（我要讲什么？）+ Subtitle（从什么角度讲？）+ Logic（想让听众记住什么？）
- 3个确认指令：确认/调整/重新生成
- 调整规则：只修改受影响页面，不推翻整个框架
- 硬规则：未经用户确认的 Story Framework，不得直接进入最终 PPT 生成

### 新增核心引擎（core/）
- `core/discovery.md`：3问发现模块
- `core/content_expansion.md`：★ AI主动补全引擎
- `core/story_architect.md`：Executive Story Framework + Slide Type Recognition
- `core/story_approval.md`：★ Story Approval 汇报框架确认

### 新增设计系统（design/）
- `design/style_system.md`：5种设计风格 + 自动匹配
- `design/visual_rules.md`：★ 视觉评分规则
- `design/pattern_library/`：★ 15种版式模式

### 新增质量保障（quality/）
- `quality/presentation_checker.md`：自动质量检查

### 顶层重构
- 重写 `SKILL.md`：THINK → CONFIRM → CREATE 3阶段引擎
- 产品定义：**"From scattered ideas → Structured Story → Professional Deck"**
- 更新 `manifest.yaml`：新增 story_approval capability
- 更新 `README.md`
- 新增最简输入案例 `examples/minimal_input_case.md`

### 删除旧文件
- 删除 `prompts/`（12个文件）、`assets/`、`framework/`

### 核心数据
- 23个新建文件 + 9个修改文件 + 17个删除文件

**新增核心引擎（core/）：**
- `core/discovery.md`：3问发现模块，只采集最少必要信息（对象、目的、想法），其余全部AI推断
- `core/content_expansion.md`：★ 最大差异化 — AI主动补全引擎，6个补全维度（行业背景/市场数据/竞争案例/最佳实践/价值逻辑/风险预判）
- `core/story_architect.md`：Executive Story Framework（6段式）+ Slide Type Recognition（自动页面类型识别）+ Slide Planner（页面规划）

**新增设计系统（design/）：**
- `design/style_system.md`：5种设计风格（从 assets/ 进化），新增自动风格匹配规则
- `design/visual_rules.md`：★ 视觉评分规则 — 覆盖率≥60%、≤4 Bullet 自动转换、Page Score 100分制
- `design/pattern_library/`：★ 15种版式模式（cover/summary/framework/timeline/roadmap/comparison/before_after/dashboard/matrix/pyramid/flywheel/case_card/process/organization/architecture）

**新增质量保障（quality/）：**
- `quality/presentation_checker.md`：自动质量检查，全局评分 + 逐页Page Score + 改进建议

**顶层重构：**
- 重写 `SKILL.md`：从200+行12步流程 → 4阶段引擎驱动（Discover→Expand→Architect→Deliver）
- 更新 `manifest.yaml`：新增 content_expansion、slide_type_recognition、pattern_library、visual_scoring、quality_assurance 等能力
- 重写 `README.md`：突出新定位和新能力
- 新增开场白：从"先告诉我谁看"→"告诉我你的想法，剩下的我来补全"

**删除旧文件：**
- 删除 `prompts/`（12个文件）：内容迁移至 core/
- 删除 `assets/`：内容迁移至 design/
- 删除 `framework/`：内容迁移至 core/

**核心数据：**
- 22个新建文件 + 7个修改文件 + 17个删除文件
- 总新增约3,500行

---

## v0.2.0 (2025-08-05)

### 重大升级：从骨架到生产级AI职场汇报Skill

**方法论深化：**
- 重写 `framework/12step_framework.md`：从99行简略提纲升级为500+行完整方法论，每步包含核心问题、决策树、检查清单、输出模板
- 重写 `assets/design_styles.md`：从3种风格升级为5种完整视觉规范（含HEX配色、字体配对、图标风格、适用场景）
- 重写 `assets/visual_models.md`：从6种模型升级为12种视觉模型（含使用场景、搭配建议、最佳实践）

**Prompt体系扩展：**
- 从5个简略prompt（各3-9行）扩展为12个详细prompt
- 每个prompt包含：角色设定、输入上下文、执行步骤、输出格式、验证标准
- 覆盖四阶段完整流程：业务理解→逻辑构建→视觉设计→制作交付

**SKILL.md重写：**
- 从51行简单角色定义升级为200+行完整Agent定义
- 包含12步完整执行指令、场景自适应规则、输出质量要求

**模板扩展：**
- 3个简略模板（各6行）升级为5个完整页面结构模板
- 新增：方案评审模板、战略规划模板
- 每个模板包含：封面、目录、逐页内容结构、视觉建议、使用提示

**案例扩展：**
- 1个简略案例升级为3个完整12步全流程案例
- 新增：年度述职案例、产品发布案例
- 每个案例展示从用户输入到最终交付的完整过程

**PPT生成器：**
- 从空目录到完整的Python PPT生成器
- `generator/templates.py`：6种页面模板（封面、目录、内容、数据、对比、结尾）
- `generator/ppt_generator.py`：核心生成器，支持链式调用和模板数据构建
- 支持5种设计风格一键切换

**文档更新：**
- 重写 README.md：完整项目说明、快速开始指南、API文档
- 更新 manifest.yaml：版本号、capabilities、workflow
- 更新 requirements.txt：确认依赖完整
- 重写 tests/test_cases.md：结构化测试用例

---

## v0.1.1

- 删除打包文件
- 初始化项目结构

## v0.1.0

- 初始版本
- 12步框架骨架
- 5个基础prompt
- 3个基础模板
- 1个简略案例