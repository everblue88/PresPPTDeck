# PresPPTDeck V0.3 测试用例

> 验证 AI商业汇报架构师 的核心能力。

---

## 测试用例 1：极简输入测试（★ V0.3 核心差异化）

### 输入
```
用户：帮我做一个AI赋能金融产研的汇报，给老板看。
```

### 期望行为
1. AI 只问3个问题（对象、目的、核心输入），不追问更多细节
2. AI 自动推断：行业=金融科技、时间=15分钟、风格=金融黑金
3. AI 自动补全：行业背景、市场数据、竞争案例、价值逻辑
4. 所有补全内容标注 `[行业参考]` / `[AI建议]` / `[需验证]`
5. 用户确认方向后，AI构建6段式故事 + 10页分页规划
6. 每页推荐 Pattern（基于 Slide Type Recognition）

### 验证点
- [ ] 是否只问了3个问题？
- [ ] 是否自动补全了行业背景？
- [ ] 是否标注了AI补全的内容？
- [ ] 是否生成了6段式故事线？
- [ ] 是否推荐了匹配的Pattern？

---

## 测试用例 2：Content Expansion 引擎测试

### 输入
```
用户输入：今年做了APP，想汇报成果
```

### 期望补充内容
- [ ] 行业背景：移动互联网/金融科技行业趋势
- [ ] 竞争案例：同行业APP案例
- [ ] 价值逻辑：APP对业务的价值（获客/服务/付费）
- [ ] 风险预判：用户增长、留存、变现等常见挑战

### 验证点
- [ ] 是否补充了行业背景？
- [ ] 是否补充了价值逻辑？
- [ ] 是否标注了补充内容的来源？

---

## 测试用例 3：视觉规则测试

### 场景A：文字堆叠检测
输入：一页有5个连续Bullet的文字列表
期望：AI自动转换为图标卡片或其他视觉形式

### 场景B：覆盖率检测
输入：一页只有标题+2行文字（覆盖率<40%）
期望：AI返回 Content Expansion 补全

### 场景C：Page Score评分
输入：任意一页PPT
期望：AI输出100分制的Page Score（结构30+视觉30+密度20+统一20）

### 验证点
- [ ] 超过4个Bullet是否自动转换？
- [ ] 覆盖率<60%是否触发补全？
- [ ] 是否输出了Page Score？

---

## 测试用例 4：Pattern 自动选择测试

### 输入
| 内容 | 期望Pattern |
|------|-----------|
| "AI赋能流程" | before_after |
| "三大战略方向" | framework |
| "年度规划" | roadmap |
| "核心数据" | dashboard |
| "方案对比" | comparison |
| "技术架构" | architecture |
| "增长逻辑" | flywheel |

### 验证点
- [ ] 是否自动识别了页面类型？
- [ ] 是否推荐了匹配的Pattern？

---

## 测试用例 5：生成器扩展测试

### 输入
```python
from generator import PPTGenerator

gen = PPTGenerator(style='tech_blue')
gen.add_roadmap(title='路线图', phases=[
    {'name': 'Phase 1', 'time': 'H1', 'goals': ['目标1', '目标2']},
])
gen.add_process(title='流程', steps=[
    {'name': '步骤1', 'desc': '说明'},
])
gen.add_timeline(title='时间轴', milestones=[
    {'time': 'Q1', 'event': '事件', 'desc': '说明'},
])
gen.save('test.pptx')
```

### 验证点
- [ ] RoadmapSlide 是否正常生成？
- [ ] ProcessSlide 是否正常生成？
- [ ] TimelineSlide 是否正常生成？
- [ ] 新增的 build_from_story() 是否正常工作？

---

## 测试用例 6：质量检查器测试

### 输入
一份完整的11页PPT（Story Architecture）

### 期望输出
```
【PresPPTDeck 质量报告】
- 全局评分：故事完整性 + 内容质量 + 视觉一致性
- 逐页评分：每页Page Score
- 改进建议：具体问题和改进方案
- 判定：通过 / 需优化 / 需重新设计
```

### 验证点
- [ ] 是否输出了全局评分？
- [ ] 是否逐页给出了Page Score？
- [ ] 是否有具体的改进建议？

---

## 回归测试清单

每次发布前必须验证：

- [ ] SKILL.md 使用4阶段引擎流程
- [ ] core/ 3个文件都是完整文档
- [ ] design/ 包含 style_system + visual_rules + 15 patterns + index
- [ ] quality/ 包含完整检查器
- [ ] 生成器支持所有页面类型（cover/content/data/comparison/ending/roadmap/process/timeline）
- [ ] `python -m generator.ppt_generator` 能成功生成预览PPT
- [ ] manifest.yaml 版本号为 0.3.0
- [ ] 旧目录（prompts/assets/framework）已删除