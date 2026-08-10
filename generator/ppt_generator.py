# PPT生成器核心模块

"""
基于python-pptx的PPT生成器。

支持从YAML/Markdown结构定义生成.pptx文件。
支持5种设计风格、6种页面模板类型。

使用方式：
    from generator import PPTGenerator
    gen = PPTGenerator(style="tech_blue")
    gen.add_cover(title="...", subtitle="...")
    gen.add_toc(items=[...])
    gen.add_content(title="...", points=[...])
    gen.add_data(title="...", metrics=[...])
    gen.add_comparison(title="...", left_points=[...], right_points=[...])
    gen.add_ending(thank_text="感谢聆听")
    gen.save("output.pptx")
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

from .templates import (
    DESIGN_STYLES,
    CoverSlide,
    TOCSlide,
    ContentSlide,
    DataSlide,
    ComparisonSlide,
    EndingSlide,
    RoadmapSlide,
    ProcessSlide,
    TimelineSlide,
    SLIDE_WIDTH,
    SLIDE_HEIGHT,
)


class PPTGenerator:
    """PPT生成器主类"""

    def __init__(self, style: str = "tech_blue", template_path: str = None):
        """
        初始化PPT生成器

        Args:
            style: 设计风格名称
                - "tech_blue": 科技蓝白
                - "finance_gold": 金融黑金
                - "minimal_white": 极简白灰
                - "dark_tech": 深色科技
                - "vibrant_orange": 活力橙红
            template_path: 可选的.pptx模板文件路径
        """
        if style not in DESIGN_STYLES:
            raise ValueError(f"不支持的设计风格: {style}。可选: {list(DESIGN_STYLES.keys())}")

        self.style_name = style
        self.style = DESIGN_STYLES[style]

        # 创建演示文稿
        if template_path and os.path.exists(template_path):
            self.prs = Presentation(template_path)
        else:
            self.prs = Presentation()

        # 设置幻灯片尺寸为16:9
        self.prs.slide_width = SLIDE_WIDTH
        self.prs.slide_height = SLIDE_HEIGHT

        # 初始化页面模板
        self.cover = CoverSlide(self.style)
        self.toc = TOCSlide(self.style)
        self.content = ContentSlide(self.style)
        self.data = DataSlide(self.style)
        self.comparison = ComparisonSlide(self.style)
        self.ending = EndingSlide(self.style)
        self.roadmap = RoadmapSlide(self.style)
        self.process = ProcessSlide(self.style)
        self.timeline = TimelineSlide(self.style)

        # 幻灯片计数
        self.slide_count = 0

    def _add_blank_slide(self):
        """添加空白幻灯片"""
        blank_layout = self.prs.slide_layouts[6]  # 空白布局
        slide = self.prs.slides.add_slide(blank_layout)
        self.slide_count += 1
        return slide

    def add_cover(self, title: str, subtitle: str = "", presenter: str = "",
                  date: str = ""):
        """
        添加封面页

        Args:
            title: PPT标题
            subtitle: 副标题
            presenter: 汇报人
            date: 日期
        """
        slide = self._add_blank_slide()
        self.cover.create(slide, title, subtitle, presenter, date, self.style_name)
        return self

    def add_toc(self, items: list):
        """
        添加目录页

        Args:
            items: 目录项列表
                [{"title": "章节标题", "subtitle": "章节描述", "icon": "📊"}, ...]
        """
        slide = self._add_blank_slide()
        self.toc.create(slide, items, self.style_name)
        return self

    def add_content(self, title: str, subtitle: str = "", points: list = None,
                    visual_type: str = "list"):
        """
        添加内容页

        Args:
            title: 页面标题（有观点！）
            subtitle: 副标题
            points: 内容要点列表
            visual_type: 视觉类型 - "list" | "cards" | "pyramid"
        """
        slide = self._add_blank_slide()
        self.content.create(slide, title, subtitle, points, self.style_name, visual_type)
        return self

    def add_data(self, title: str, metrics: list = None):
        """
        添加数据页

        Args:
            title: 页面标题
            metrics: 指标列表
                [{"label": "指标名", "value": "数值", "trend": "↑15%", "trend_up": True}, ...]
        """
        slide = self._add_blank_slide()
        self.data.create(slide, title, metrics, self.style_name)
        return self

    def add_comparison(self, title: str, left_title: str = "Before",
                       right_title: str = "After", left_points: list = None,
                       right_points: list = None):
        """
        添加对比页

        Args:
            title: 页面标题
            left_title: 左侧标题（如Before）
            right_title: 右侧标题（如After）
            left_points: 左侧要点列表
            right_points: 右侧要点列表
        """
        slide = self._add_blank_slide()
        self.comparison.create(slide, title, left_title, right_title,
                               left_points, right_points, self.style_name)
        return self

    def add_ending(self, thank_text: str = "感谢聆听", summary: str = "",
                   call_to_action: str = "", contact: str = ""):
        """
        添加结尾页

        Args:
            thank_text: 感谢语
            summary: 总结
            call_to_action: 行动号召
            contact: 联系方式
        """
        slide = self._add_blank_slide()
        self.ending.create(slide, thank_text, summary, call_to_action, contact, self.style_name)
        return self

    def add_section_header(self, title: str, section_num: int = None):
        """
        添加章节过渡页

        Args:
            title: 章节标题
            section_num: 章节序号
        """
        slide = self._add_blank_slide()
        is_dark = self.style_name in ("dark_tech", "finance_gold")
        bg_key = "primary" if is_dark else "bg_white"
        self.cover._set_slide_bg(slide, bg_key)

        # 章节序号
        if section_num:
            accent_color = "bright_blue" if self.style_name == "dark_tech" else \
                           "gold" if self.style_name == "finance_gold" else "primary"
            self.cover._add_text_box(
                slide, Inches(0.8), Inches(2.5), Inches(2.0), Inches(1.0),
                f"PART {section_num:02d}", font_size=Pt(18),
                font_color_key=accent_color, bold=True
            )

        # 章节标题
        title_color = "text_white" if is_dark else "text_black"
        self.cover._add_text_box(
            slide, Inches(0.8), Inches(3.2), Inches(11.0), Inches(1.0),
            title, font_size=Pt(36), font_color_key=title_color, bold=True
        )

        return self

    def add_image_placeholder(self, title: str, description: str = ""):
        """
        添加图片占位页（用于后续插入图片）

        Args:
            title: 页面标题
            description: 图片描述
        """
        slide = self._add_blank_slide()
        is_dark = self.style_name in ("dark_tech", "finance_gold")
        bg_key = "primary" if is_dark else "bg_white"
        self.cover._set_slide_bg(slide, bg_key)

        # 标题
        title_color = "text_white" if is_dark else "text_black"
        self.cover._add_text_box(
            slide, Inches(0.8), Inches(0.4), Inches(11.0), Inches(0.8),
            title, font_size=Pt(28), font_color_key=title_color, bold=True
        )

        # 占位框
        placeholder_bg = "card_bg" if is_dark else "light_gray"
        self.cover._add_rect(slide, Inches(1.5), Inches(1.6), Inches(10.3), Inches(5.0),
                             fill_color_key=placeholder_bg)

        if description:
            desc_color = "text_gray" if is_dark else "text_gray"
            self.cover._add_text_box(
                slide, Inches(2.0), Inches(3.5), Inches(9.3), Inches(0.6),
                description, font_size=Pt(14), font_color_key=desc_color,
                alignment=PP_ALIGN.CENTER
            )

        return self

    def add_roadmap(self, title: str, phases: list = None):
        """
        添加路线图页

        Args:
            title: 页面标题
            phases: 阶段列表
                [{"name": "Phase 1", "time": "H1 2026", "goals": ["目标1", "目标2"]}, ...]
        """
        slide = self._add_blank_slide()
        self.roadmap.create(slide, title, phases, self.style_name)
        return self

    def add_process(self, title: str, steps: list = None):
        """
        添加流程图页

        Args:
            title: 页面标题
            steps: 步骤列表
                [{"name": "步骤名", "desc": "说明"}, ...]
        """
        slide = self._add_blank_slide()
        self.process.create(slide, title, steps, self.style_name)
        return self

    def add_timeline(self, title: str, milestones: list = None):
        """
        添加时间轴页

        Args:
            title: 页面标题
            milestones: 里程碑列表
                [{"time": "Q1", "event": "事件名", "desc": "说明"}, ...]
        """
        slide = self._add_blank_slide()
        self.timeline.create(slide, title, milestones, self.style_name)
        return self

    def build_from_story(self, story_data: dict):
        """
        从 Story Architect 输出直接构建完整PPT（V0.3新增）

        Args:
            story_data: Story Architecture 数据
                {
                    "title": "PPT标题",
                    "subtitle": "副标题",
                    "presenter": "汇报人",
                    "date": "日期",
                    "style": "tech_blue",
                    "toc_items": [...],
                    "slides": [
                        {"type": "cover", ...},
                        {"type": "summary", ...},
                        {"type": "dashboard", "title": "...", "metrics": [...]},
                        {"type": "before_after", "title": "...", "left_points": [...], "right_points": [...]},
                        {"type": "comparison", ...},
                        {"type": "roadmap", "title": "...", "phases": [...]},
                        {"type": "process", "title": "...", "steps": [...]},
                        {"type": "timeline", "title": "...", "milestones": [...]},
                        {"type": "content", "title": "...", "points": [...]},
                        {"type": "data", "title": "...", "metrics": [...]},
                        {"type": "ending", ...},
                    ],
                    "ending": {"thank_text": "感谢聆听", "summary": "...", "call_to_action": "..."}
                }
        """
        # 封面
        self.add_cover(
            title=story_data.get("title", ""),
            subtitle=story_data.get("subtitle", ""),
            presenter=story_data.get("presenter", ""),
            date=story_data.get("date", ""),
        )

        # 目录
        toc_items = story_data.get("toc_items", [])
        if toc_items:
            self.add_toc(toc_items)

        # 内容页
        for slide_data in story_data.get("slides", []):
            slide_type = slide_data.get("type", "content")

            if slide_type == "section":
                self.add_section_header(
                    title=slide_data.get("title", ""),
                    section_num=slide_data.get("section_num"),
                )
            elif slide_type == "summary":
                self.add_content(
                    title=slide_data.get("title", ""),
                    subtitle=slide_data.get("subtitle", ""),
                    points=slide_data.get("points", []),
                    visual_type="cards",
                )
            elif slide_type == "content":
                self.add_content(
                    title=slide_data.get("title", ""),
                    subtitle=slide_data.get("subtitle", ""),
                    points=slide_data.get("points", []),
                    visual_type=slide_data.get("visual_type", "list"),
                )
            elif slide_type == "data" or slide_type == "dashboard":
                self.add_data(
                    title=slide_data.get("title", ""),
                    metrics=slide_data.get("metrics", []),
                )
            elif slide_type == "comparison":
                self.add_comparison(
                    title=slide_data.get("title", ""),
                    left_title=slide_data.get("left_title", "Before"),
                    right_title=slide_data.get("right_title", "After"),
                    left_points=slide_data.get("left_points", []),
                    right_points=slide_data.get("right_points", []),
                )
            elif slide_type == "before_after":
                self.add_comparison(
                    title=slide_data.get("title", ""),
                    left_title=slide_data.get("left_title", "Before"),
                    right_title=slide_data.get("right_title", "After"),
                    left_points=slide_data.get("left_points", []),
                    right_points=slide_data.get("right_points", []),
                )
            elif slide_type == "roadmap":
                self.add_roadmap(
                    title=slide_data.get("title", ""),
                    phases=slide_data.get("phases", []),
                )
            elif slide_type == "process":
                self.add_process(
                    title=slide_data.get("title", ""),
                    steps=slide_data.get("steps", []),
                )
            elif slide_type == "timeline":
                self.add_timeline(
                    title=slide_data.get("title", ""),
                    milestones=slide_data.get("milestones", []),
                )
            elif slide_type == "image":
                self.add_image_placeholder(
                    title=slide_data.get("title", ""),
                    description=slide_data.get("description", ""),
                )

        # 结尾
        ending = story_data.get("ending", {})
        self.add_ending(
            thank_text=ending.get("thank_text", "感谢聆听"),
            summary=ending.get("summary", ""),
            call_to_action=ending.get("call_to_action", ""),
            contact=ending.get("contact", ""),
        )

        return self

    def save(self, output_path: str):
        """
        保存PPT文件

        Args:
            output_path: 输出文件路径（.pptx）
        """
        self.prs.save(output_path)
        print(f"PPT已保存至: {output_path}")
        print(f"共 {self.slide_count} 页")

    def build_from_template(self, template_data: dict):
        """
        从模板数据构建完整PPT

        Args:
            template_data: 模板数据字典
                {
                    "title": "PPT标题",
                    "subtitle": "副标题",
                    "presenter": "汇报人",
                    "date": "日期",
                    "style": "tech_blue",
                    "toc_items": [...],
                    "slides": [
                        {"type": "content", "title": "...", "points": [...]},
                        {"type": "data", "title": "...", "metrics": [...]},
                        {"type": "comparison", "title": "...", "left_points": [...], "right_points": [...]},
                        ...
                    ],
                    "ending": {
                        "thank_text": "感谢聆听",
                        "summary": "总结",
                        "call_to_action": "行动号召",
                        "contact": "联系方式"
                    }
                }
        """
        # 封面
        self.add_cover(
            title=template_data.get("title", ""),
            subtitle=template_data.get("subtitle", ""),
            presenter=template_data.get("presenter", ""),
            date=template_data.get("date", ""),
        )

        # 目录
        toc_items = template_data.get("toc_items", [])
        if toc_items:
            self.add_toc(toc_items)

        # 内容页
        for slide_data in template_data.get("slides", []):
            slide_type = slide_data.get("type", "content")

            if slide_type == "section":
                self.add_section_header(
                    title=slide_data.get("title", ""),
                    section_num=slide_data.get("section_num"),
                )

            elif slide_type == "content":
                self.add_content(
                    title=slide_data.get("title", ""),
                    subtitle=slide_data.get("subtitle", ""),
                    points=slide_data.get("points", []),
                    visual_type=slide_data.get("visual_type", "list"),
                )

            elif slide_type == "data":
                self.add_data(
                    title=slide_data.get("title", ""),
                    metrics=slide_data.get("metrics", []),
                )

            elif slide_type == "comparison":
                self.add_comparison(
                    title=slide_data.get("title", ""),
                    left_title=slide_data.get("left_title", "Before"),
                    right_title=slide_data.get("right_title", "After"),
                    left_points=slide_data.get("left_points", []),
                    right_points=slide_data.get("right_points", []),
                )

            elif slide_type == "image":
                self.add_image_placeholder(
                    title=slide_data.get("title", ""),
                    description=slide_data.get("description", ""),
                )

        # 结尾
        ending = template_data.get("ending", {})
        self.add_ending(
            thank_text=ending.get("thank_text", "感谢聆听"),
            summary=ending.get("summary", ""),
            call_to_action=ending.get("call_to_action", ""),
            contact=ending.get("contact", ""),
        )

        return self


# ============================================================
# 便捷函数
# ============================================================

def quick_preview():
    """快速生成预览PPT，验证生成器是否正常工作"""
    gen = PPTGenerator(style="tech_blue")

    gen.add_cover(
        title="这是一个测试PPT",
        subtitle="验证PPT生成器功能",
        presenter="PresPPTDeck",
        date="2025年8月",
    )

    gen.add_toc([
        {"title": "背景与目标", "subtitle": "为什么做这个项目", "icon": "🎯"},
        {"title": "核心策略", "subtitle": "我们的解决方案", "icon": "💡"},
        {"title": "成果展示", "subtitle": "数据驱动的结果", "icon": "📊"},
        {"title": "未来规划", "subtitle": "下一步做什么", "icon": "🚀"},
    ])

    gen.add_content(
        title="我们的核心策略是聚焦用户体验",
        subtitle="通过3个关键举措，在6个月内实现用户满意度大幅提升",
        points=[
            "重构核心交互流程，将操作步骤从5步减少到2步",
            "建立用户反馈闭环，需求响应时间从7天缩短到24小时",
            "引入AI辅助功能，让用户3分钟完成原来30分钟的工作",
        ],
        visual_type="list",
    )

    gen.add_data(
        title="核心指标全面超出预期",
        metrics=[
            {"label": "用户活跃度", "value": "85%", "trend": "↑15%", "trend_up": True},
            {"label": "用户满意度", "value": "4.8", "trend": "↑0.6", "trend_up": True},
            {"label": "处理效率", "value": "3min", "trend": "↓90%", "trend_up": True},
            {"label": "成本降低", "value": "40%", "trend": "↓40%", "trend_up": True},
        ],
    )

    gen.add_comparison(
        title="改造前后的用户体验对比",
        left_title="改造前",
        right_title="改造后",
        left_points=[
            "5步操作才能完成核心任务",
            "用户反馈响应时间7天",
            "数据分析需要手动处理30分钟",
            "NPS评分62分",
        ],
        right_points=[
            "2步操作即可完成核心任务",
            "用户反馈响应时间24小时",
            "AI自动分析，3分钟出报告",
            "NPS评分78分",
        ],
    )

    gen.add_ending(
        thank_text="感谢聆听",
        summary="核心信息：用户体验重构是一个持续的过程，数据证明了我们的方向是正确的",
        call_to_action="欢迎提出宝贵意见",
        contact="联系方式：prespptdeck@example.com",
    )

    gen.save("preview_output.pptx")
    return gen


if __name__ == "__main__":
    quick_preview()