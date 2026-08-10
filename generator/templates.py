# PPT页面布局模板

"""
每种页面类型对应一个类，封装了该页面的布局逻辑和样式参数。
所有尺寸单位为英寸（Inches），符合python-pptx的坐标系统。
"""

from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR


# ============================================================
# 设计风格配色方案
# ============================================================

DESIGN_STYLES = {
    "tech_blue": {
        "name": "科技蓝白",
        "primary": "1A73E8",
        "primary_dark": "0D47A1",
        "primary_light": "E8F0FE",
        "secondary": "4285F4",
        "accent": "FF6D00",
        "accent_green": "0F9D58",
        "accent_red": "DB4437",
        "bg_white": "FFFFFF",
        "bg_gray": "F8F9FA",
        "text_black": "202124",
        "text_gray": "5F6368",
        "divider": "DADCE0",
        "title_font": "思源黑体",
        "body_font": "思源黑体",
    },
    "finance_gold": {
        "name": "金融黑金",
        "primary": "1A1A2E",
        "primary_light": "2D2D44",
        "gold": "D4AF37",
        "gold_light": "F5E6CC",
        "gold_dark": "B8960F",
        "secondary": "4A4A6A",
        "accent_red": "C62828",
        "accent_green": "2E7D32",
        "bg_white": "FAFAFA",
        "bg_gray": "F0F0F0",
        "text_white": "FFFFFF",
        "text_black": "1A1A1A",
        "text_gray": "757575",
        "divider": "E0E0E0",
        "title_font": "思源宋体",
        "body_font": "思源黑体",
    },
    "minimal_white": {
        "name": "极简白灰",
        "primary": "FFFFFF",
        "primary_dark": "1A1A1A",
        "dark_gray": "333333",
        "mid_gray": "666666",
        "light_gray": "F5F5F5",
        "light_gray_border": "E0E0E0",
        "accent_blue": "2563EB",
        "accent_green": "16A34A",
        "accent_red": "DC2626",
        "title_font": "思源黑体",
        "body_font": "思源黑体",
    },
    "dark_tech": {
        "name": "深色科技",
        "primary": "0F172A",
        "card_bg": "1E293B",
        "card_border": "334155",
        "bright_blue": "38BDF8",
        "blue_light": "BAE6FD",
        "blue_dark": "0284C7",
        "purple": "818CF8",
        "green": "10B981",
        "orange": "F59E0B",
        "red": "EF4444",
        "text_white": "F1F5F9",
        "text_gray": "94A3B8",
        "text_dark_gray": "64748B",
        "title_font": "思源黑体",
        "body_font": "思源黑体",
    },
    "vibrant_orange": {
        "name": "活力橙红",
        "primary": "FF6B35",
        "primary_dark": "E5552A",
        "primary_light": "FFF0EB",
        "secondary": "2C3E50",
        "secondary_light": "F8F9FA",
        "blue": "0047AB",
        "green": "27AE60",
        "yellow": "F2C94C",
        "red": "EB5757",
        "text_black": "1A1A1A",
        "text_gray": "7F8C8D",
        "title_font": "思源黑体",
        "body_font": "思源黑体",
    },
}


def hex_to_rgb(hex_color: str) -> RGBColor:
    """将HEX颜色码转换为RGBColor"""
    hex_color = hex_color.lstrip("#")
    return RGBColor(
        int(hex_color[0:2], 16),
        int(hex_color[2:4], 16),
        int(hex_color[4:6], 16),
    )


# ============================================================
# 幻灯片尺寸常量
# ============================================================

SLIDE_WIDTH = Inches(13.333)  # 16:9
SLIDE_HEIGHT = Inches(7.5)

# 边距
MARGIN_LEFT = Inches(0.8)
MARGIN_RIGHT = Inches(0.8)
MARGIN_TOP = Inches(0.6)
MARGIN_BOTTOM = Inches(0.6)

# 内容区域
CONTENT_WIDTH = SLIDE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT
CONTENT_HEIGHT = SLIDE_HEIGHT - MARGIN_TOP - MARGIN_BOTTOM


# ============================================================
# 页面模板基类
# ============================================================

class SlideTemplate:
    """页面模板基类"""

    def __init__(self, style: dict):
        self.style = style

    def _color(self, key: str) -> RGBColor:
        """获取配色方案中的颜色"""
        return hex_to_rgb(self.style.get(key, "000000"))

    def _set_slide_bg(self, slide, color_key: str):
        """设置幻灯片背景色"""
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = self._color(color_key)

    def _add_text_box(self, slide, left, top, width, height, text, font_size=Pt(14),
                      font_color_key="text_black", bold=False, alignment=PP_ALIGN.LEFT,
                      font_name_key="body_font"):
        """添加文本框"""
        from pptx.util import Inches
        txBox = slide.shapes.add_textbox(left, top, width, height)
        tf = txBox.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = text
        p.font.size = font_size
        p.font.color.rgb = self._color(font_color_key)
        p.font.bold = bold
        p.font.name = self.style.get(font_name_key, "思源黑体")
        p.alignment = alignment
        return tf

    def _add_rect(self, slide, left, top, width, height, fill_color_key="primary",
                  border_color_key=None):
        """添加矩形"""
        from pptx.enum.shapes import MSO_SHAPE
        shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = self._color(fill_color_key)
        if border_color_key:
            shape.line.color.rgb = self._color(border_color_key)
        else:
            shape.line.fill.background()
        return shape


# ============================================================
# 封面页模板
# ============================================================

class CoverSlide(SlideTemplate):
    """封面页"""

    def create(self, slide, title: str, subtitle: str = "", presenter: str = "",
               date: str = "", style_name: str = "tech_blue"):
        """创建封面页"""
        is_dark = style_name in ("dark_tech", "finance_gold")

        # 背景
        bg_key = "primary" if is_dark else "bg_white"
        self._set_slide_bg(slide, bg_key)

        # 顶部装饰线
        accent_color = "bright_blue" if style_name == "dark_tech" else \
                       "gold" if style_name == "finance_gold" else \
                       "accent" if style_name == "vibrant_orange" else "primary"
        self._add_rect(slide, Inches(0), Inches(0), SLIDE_WIDTH, Inches(0.06),
                       fill_color_key=accent_color)

        # 标题
        title_color = "text_white" if is_dark else "text_black"
        title_font = self.style.get("title_font", "思源黑体")
        self._add_text_box(
            slide, Inches(1.5), Inches(2.0), Inches(10.3), Inches(1.5),
            title, font_size=Pt(40), font_color_key=title_color, bold=True,
            alignment=PP_ALIGN.CENTER, font_name_key="title_font"
        )

        # 副标题
        if subtitle:
            subtitle_color = "text_gray" if is_dark else "text_gray"
            self._add_text_box(
                slide, Inches(2.0), Inches(3.6), Inches(9.3), Inches(0.8),
                subtitle, font_size=Pt(18), font_color_key=subtitle_color,
                alignment=PP_ALIGN.CENTER
            )

        # 分隔线
        divider_color = accent_color
        self._add_rect(slide, Inches(5.5), Inches(4.6), Inches(2.3), Inches(0.03),
                       fill_color_key=divider_color)

        # 汇报人和日期
        info_text = ""
        if presenter:
            info_text += presenter
        if date:
            if info_text:
                info_text += "  |  "
            info_text += date

        if info_text:
            info_color = "text_gray" if is_dark else "text_gray"
            self._add_text_box(
                slide, Inches(2.0), Inches(5.0), Inches(9.3), Inches(0.6),
                info_text, font_size=Pt(14), font_color_key=info_color,
                alignment=PP_ALIGN.CENTER
            )


# ============================================================
# 目录页模板
# ============================================================

class TOCSlide(SlideTemplate):
    """目录页"""

    def create(self, slide, items: list, style_name: str = "tech_blue"):
        """
        创建目录页
        items: [{"title": "章节标题", "subtitle": "章节描述", "icon": "📊"}, ...]
        """
        is_dark = style_name in ("dark_tech", "finance_gold")
        bg_key = "primary" if is_dark else "bg_white"
        self._set_slide_bg(slide, bg_key)

        # 标题
        title_color = "text_white" if is_dark else "text_black"
        self._add_text_box(
            slide, MARGIN_LEFT, Inches(0.5), Inches(5.0), Inches(0.8),
            "目录", font_size=Pt(28), font_color_key=title_color, bold=True
        )

        # 目录项
        num_items = len(items)
        card_width = (CONTENT_WIDTH - Inches(0.3 * (num_items - 1))) / num_items
        card_height = Inches(4.5)

        for i, item in enumerate(items):
            left = MARGIN_LEFT + (card_width + Inches(0.3)) * i
            top = Inches(1.6)

            # 卡片背景
            card_bg = "card_bg" if is_dark else "light_gray"
            self._add_rect(slide, left, top, card_width, card_height,
                           fill_color_key=card_bg)

            # 序号
            accent_color = "bright_blue" if style_name == "dark_tech" else \
                           "gold" if style_name == "finance_gold" else "primary"
            num_color = "text_white" if is_dark else "text_black"
            self._add_text_box(
                slide, left + Inches(0.3), top + Inches(0.3), Inches(0.8), Inches(0.6),
                f"0{i + 1}", font_size=Pt(36), font_color_key=accent_color, bold=True
            )

            # 图标（如果有）
            if item.get("icon"):
                self._add_text_box(
                    slide, left + Inches(0.3), top + Inches(1.0), Inches(1.0), Inches(1.0),
                    item["icon"], font_size=Pt(32), alignment=PP_ALIGN.CENTER
                )

            # 章节标题
            title_color_key = "text_white" if is_dark else "text_black"
            self._add_text_box(
                slide, left + Inches(0.3), top + Inches(2.0), card_width - Inches(0.6), Inches(0.8),
                item["title"], font_size=Pt(18), font_color_key=title_color_key, bold=True
            )

            # 章节描述
            if item.get("subtitle"):
                desc_color = "text_gray" if is_dark else "text_gray"
                self._add_text_box(
                    slide, left + Inches(0.3), top + Inches(2.8), card_width - Inches(0.6), Inches(1.2),
                    item["subtitle"], font_size=Pt(12), font_color_key=desc_color
                )


# ============================================================
# 内容页模板
# ============================================================

class ContentSlide(SlideTemplate):
    """内容页：标题 + 要点列表"""

    def create(self, slide, title: str, subtitle: str = "", points: list = None,
               style_name: str = "tech_blue", visual_type: str = "list"):
        """
        创建内容页
        points: ["要点1", "要点2", "要点3"]
        visual_type: "list" | "cards" | "pyramid"
        """
        is_dark = style_name in ("dark_tech", "finance_gold")
        bg_key = "primary" if is_dark else "bg_white"
        self._set_slide_bg(slide, bg_key)

        # 顶部装饰线
        accent_color = "bright_blue" if style_name == "dark_tech" else \
                       "gold" if style_name == "finance_gold" else "primary"
        self._add_rect(slide, Inches(0), Inches(0), SLIDE_WIDTH, Inches(0.04),
                       fill_color_key=accent_color)

        # 页面标题
        title_color = "text_white" if is_dark else "text_black"
        self._add_text_box(
            slide, MARGIN_LEFT, Inches(0.4), CONTENT_WIDTH, Inches(0.8),
            title, font_size=Pt(28), font_color_key=title_color, bold=True
        )

        # 副标题
        if subtitle:
            subtitle_color = "text_gray" if is_dark else "text_gray"
            self._add_text_box(
                slide, MARGIN_LEFT, Inches(1.1), CONTENT_WIDTH, Inches(0.5),
                subtitle, font_size=Pt(14), font_color_key=subtitle_color
            )

        if points:
            if visual_type == "cards":
                self._render_cards(slide, points, is_dark, style_name)
            else:
                self._render_list(slide, points, is_dark)

    def _render_list(self, slide, points: list, is_dark: bool):
        """渲染要点列表"""
        text_color = "text_white" if is_dark else "text_black"
        sub_color = "text_gray" if is_dark else "text_gray"

        for i, point in enumerate(points):
            y = Inches(2.0) + Inches(0.7) * i

            # 序号圆点
            accent_color = "bright_blue" if is_dark else "primary"
            self._add_rect(slide, MARGIN_LEFT, y + Inches(0.1), Inches(0.15), Inches(0.15),
                           fill_color_key=accent_color)

            self._add_text_box(
                slide, MARGIN_LEFT + Inches(0.4), y, CONTENT_WIDTH - Inches(0.4), Inches(0.5),
                point, font_size=Pt(16), font_color_key=text_color
            )

    def _render_cards(self, slide, points: list, is_dark: bool, style_name: str):
        """渲染卡片式布局"""
        num_cards = len(points)
        card_width = (CONTENT_WIDTH - Inches(0.3 * (num_cards - 1))) / num_cards
        card_height = Inches(3.5)

        for i, point in enumerate(points):
            left = MARGIN_LEFT + (card_width + Inches(0.3)) * i
            top = Inches(2.0)

            # 卡片背景
            card_bg = "card_bg" if is_dark else "light_gray"
            self._add_rect(slide, left, top, card_width, card_height,
                           fill_color_key=card_bg)

            # 卡片内容
            text_color = "text_white" if is_dark else "text_black"
            self._add_text_box(
                slide, left + Inches(0.3), top + Inches(0.3), card_width - Inches(0.6), card_height - Inches(0.6),
                point, font_size=Pt(14), font_color_key=text_color
            )


# ============================================================
# 数据页模板
# ============================================================

class DataSlide(SlideTemplate):
    """数据页：指标卡 + 图表占位"""

    def create(self, slide, title: str, metrics: list = None,
               style_name: str = "tech_blue"):
        """
        创建数据页
        metrics: [{"label": "用户数", "value": "5,230", "trend": "↑15%", "trend_up": True}, ...]
        """
        is_dark = style_name in ("dark_tech", "finance_gold")
        bg_key = "primary" if is_dark else "bg_white"
        self._set_slide_bg(slide, bg_key)

        # 顶部装饰线
        accent_color = "bright_blue" if style_name == "dark_tech" else \
                       "gold" if style_name == "finance_gold" else "primary"
        self._add_rect(slide, Inches(0), Inches(0), SLIDE_WIDTH, Inches(0.04),
                       fill_color_key=accent_color)

        # 标题
        title_color = "text_white" if is_dark else "text_black"
        self._add_text_box(
            slide, MARGIN_LEFT, Inches(0.4), CONTENT_WIDTH, Inches(0.8),
            title, font_size=Pt(28), font_color_key=title_color, bold=True
        )

        if metrics:
            self._render_metrics(slide, metrics, is_dark, style_name)

    def _render_metrics(self, slide, metrics: list, is_dark: bool, style_name: str):
        """渲染指标卡"""
        num_metrics = len(metrics)
        card_width = (CONTENT_WIDTH - Inches(0.3 * (num_metrics - 1))) / num_metrics
        card_height = Inches(2.5)

        for i, metric in enumerate(metrics):
            left = MARGIN_LEFT + (card_width + Inches(0.3)) * i
            top = Inches(2.0)

            # 卡片背景
            card_bg = "card_bg" if is_dark else "light_gray"
            self._add_rect(slide, left, top, card_width, card_height,
                           fill_color_key=card_bg)

            # 指标标签
            label_color = "text_gray" if is_dark else "text_gray"
            self._add_text_box(
                slide, left + Inches(0.3), top + Inches(0.3), card_width - Inches(0.6), Inches(0.4),
                metric["label"], font_size=Pt(12), font_color_key=label_color
            )

            # 指标数值
            value_color = "text_white" if is_dark else "text_black"
            self._add_text_box(
                slide, left + Inches(0.3), top + Inches(0.8), card_width - Inches(0.6), Inches(0.8),
                metric["value"], font_size=Pt(36), font_color_key=value_color, bold=True
            )

            # 趋势
            if metric.get("trend"):
                trend_up = metric.get("trend_up", True)
                trend_color = "green" if trend_up else "red"
                self._add_text_box(
                    slide, left + Inches(0.3), top + Inches(1.8), card_width - Inches(0.6), Inches(0.4),
                    metric["trend"], font_size=Pt(14), font_color_key=trend_color, bold=True
                )


# ============================================================
# 对比页模板
# ============================================================

class ComparisonSlide(SlideTemplate):
    """对比页：Before/After 或 方案对比"""

    def create(self, slide, title: str, left_title: str = "Before",
               right_title: str = "After", left_points: list = None,
               right_points: list = None, style_name: str = "tech_blue"):
        """
        创建对比页
        """
        is_dark = style_name in ("dark_tech", "finance_gold")
        bg_key = "primary" if is_dark else "bg_white"
        self._set_slide_bg(slide, bg_key)

        # 顶部装饰线
        accent_color = "bright_blue" if style_name == "dark_tech" else \
                       "gold" if style_name == "finance_gold" else "primary"
        self._add_rect(slide, Inches(0), Inches(0), SLIDE_WIDTH, Inches(0.04),
                       fill_color_key=accent_color)

        # 标题
        title_color = "text_white" if is_dark else "text_black"
        self._add_text_box(
            slide, MARGIN_LEFT, Inches(0.4), CONTENT_WIDTH, Inches(0.8),
            title, font_size=Pt(28), font_color_key=title_color, bold=True
        )

        # 左右对比
        half_width = (CONTENT_WIDTH - Inches(0.5)) / 2
        card_height = Inches(5.0)

        # Before 卡片
        before_left = MARGIN_LEFT
        before_top = Inches(1.6)
        before_bg = "card_bg" if is_dark else "light_gray"
        self._add_rect(slide, before_left, before_top, half_width, card_height,
                       fill_color_key=before_bg)

        # Before 标签
        before_label_color = "red" if is_dark else "accent_red"
        self._add_text_box(
            slide, before_left + Inches(0.3), before_top + Inches(0.3), half_width - Inches(0.6), Inches(0.5),
            left_title, font_size=Pt(20), font_color_key=before_label_color, bold=True
        )

        # Before 内容
        if left_points:
            before_text = "\n".join([f"• {p}" for p in left_points])
            text_color = "text_white" if is_dark else "text_black"
            self._add_text_box(
                slide, before_left + Inches(0.3), before_top + Inches(1.0), half_width - Inches(0.6), Inches(3.5),
                before_text, font_size=Pt(14), font_color_key=text_color
            )

        # After 卡片
        after_left = MARGIN_LEFT + half_width + Inches(0.5)
        after_top = Inches(1.6)
        after_bg = "card_bg" if is_dark else "light_gray"
        self._add_rect(slide, after_left, after_top, half_width, card_height,
                       fill_color_key=after_bg)

        # After 标签
        after_label_color = "green" if is_dark else "accent_green"
        self._add_text_box(
            slide, after_left + Inches(0.3), after_top + Inches(0.3), half_width - Inches(0.6), Inches(0.5),
            right_title, font_size=Pt(20), font_color_key=after_label_color, bold=True
        )

        # After 内容
        if right_points:
            after_text = "\n".join([f"• {p}" for p in right_points])
            text_color = "text_white" if is_dark else "text_black"
            self._add_text_box(
                slide, after_left + Inches(0.3), after_top + Inches(1.0), half_width - Inches(0.6), Inches(3.5),
                after_text, font_size=Pt(14), font_color_key=text_color
            )

        # 中间箭头
        arrow_color = "green" if is_dark else "accent_green"
        self._add_text_box(
            slide, MARGIN_LEFT + half_width + Inches(0.05), Inches(3.5), Inches(0.4), Inches(0.5),
            "→", font_size=Pt(24), font_color_key=arrow_color, bold=True,
            alignment=PP_ALIGN.CENTER
        )


# ============================================================
# 结尾页模板
# ============================================================

class EndingSlide(SlideTemplate):
    """结尾页：感谢 + 总结 + 行动号召"""

    def create(self, slide, thank_text: str = "感谢聆听", summary: str = "",
               call_to_action: str = "", contact: str = "", style_name: str = "tech_blue"):
        """
        创建结尾页
        """
        is_dark = style_name in ("dark_tech", "finance_gold")
        bg_key = "primary" if is_dark else "bg_white"
        self._set_slide_bg(slide, bg_key)

        # 感谢文字
        title_color = "text_white" if is_dark else "text_black"
        accent_color = "bright_blue" if style_name == "dark_tech" else \
                       "gold" if style_name == "finance_gold" else "primary"

        self._add_text_box(
            slide, Inches(1.5), Inches(2.0), Inches(10.3), Inches(1.0),
            thank_text, font_size=Pt(40), font_color_key=title_color, bold=True,
            alignment=PP_ALIGN.CENTER
        )

        # 分隔线
        self._add_rect(slide, Inches(5.5), Inches(3.2), Inches(2.3), Inches(0.03),
                       fill_color_key=accent_color)

        # 总结
        if summary:
            summary_color = "text_gray" if is_dark else "mid_gray"
            self._add_text_box(
                slide, Inches(2.0), Inches(3.6), Inches(9.3), Inches(0.8),
                summary, font_size=Pt(16), font_color_key=summary_color,
                alignment=PP_ALIGN.CENTER
            )

        # 行动号召
        if call_to_action:
            self._add_text_box(
                slide, Inches(2.0), Inches(4.5), Inches(9.3), Inches(0.6),
                call_to_action, font_size=Pt(18), font_color_key=accent_color, bold=True,
                alignment=PP_ALIGN.CENTER
            )

        # 联系方式
        if contact:
            contact_color = "text_gray" if is_dark else "text_gray"
            self._add_text_box(
                slide, Inches(2.0), Inches(5.5), Inches(9.3), Inches(0.6),
                contact, font_size=Pt(14), font_color_key=contact_color,
                alignment=PP_ALIGN.CENTER
            )


# ============================================================
# V0.3 新增：Roadmap、Process、Timeline 页面模板
# ============================================================

class RoadmapSlide(SlideTemplate):
    """路线图页：分阶段规划"""

    def create(self, slide, title: str, phases: list = None,
               style_name: str = "tech_blue"):
        """
        phases: [{"name": "Phase 1", "time": "H1 2026", "goals": ["目标1", "目标2"]}, ...]
        """
        is_dark = style_name in ("dark_tech", "finance_gold")
        bg_key = "primary" if is_dark else "bg_white"
        self._set_slide_bg(slide, bg_key)

        accent_color = "bright_blue" if style_name == "dark_tech" else \
                       "gold" if style_name == "finance_gold" else "primary"
        self._add_rect(slide, Inches(0), Inches(0), SLIDE_WIDTH, Inches(0.04),
                       fill_color_key=accent_color)

        title_color = "text_white" if is_dark else "text_black"
        self._add_text_box(
            slide, MARGIN_LEFT, Inches(0.4), CONTENT_WIDTH, Inches(0.8),
            title, font_size=Pt(28), font_color_key=title_color, bold=True
        )

        if not phases:
            return

        num_phases = len(phases)
        phase_height = Inches(1.6)
        total_height = phase_height * num_phases + Inches(0.3) * (num_phases - 1)
        start_y = Inches(2.2)

        for i, phase in enumerate(phases):
            y = start_y + (phase_height + Inches(0.3)) * i
            card_bg = "card_bg" if is_dark else "light_gray"
            self._add_rect(slide, MARGIN_LEFT, y, CONTENT_WIDTH, phase_height,
                           fill_color_key=card_bg)

            # 阶段编号和时间
            self._add_text_box(
                slide, MARGIN_LEFT + Inches(0.3), y + Inches(0.15), Inches(2.5), Inches(0.4),
                f"{phase['name']}  |  {phase['time']}",
                font_size=Pt(14), font_color_key=accent_color, bold=True
            )

            # 目标
            goals_text = "\n".join([f"• {g}" for g in phase.get("goals", [])])
            text_color = "text_white" if is_dark else "text_black"
            self._add_text_box(
                slide, MARGIN_LEFT + Inches(0.3), y + Inches(0.6),
                CONTENT_WIDTH - Inches(0.6), Inches(0.8),
                goals_text, font_size=Pt(13), font_color_key=text_color
            )

            # 箭头（除最后一个）
            if i < num_phases - 1:
                arrow_y = y + phase_height
                self._add_text_box(
                    slide, MARGIN_LEFT + Inches(0.5), arrow_y, Inches(0.5), Inches(0.3),
                    "↓", font_size=Pt(18), font_color_key=accent_color, bold=True,
                    alignment=PP_ALIGN.CENTER
                )


class ProcessSlide(SlideTemplate):
    """流程图页：步骤/流程展示"""

    def create(self, slide, title: str, steps: list = None,
               style_name: str = "tech_blue"):
        """
        steps: [{"name": "步骤名", "desc": "说明"}, ...]
        """
        is_dark = style_name in ("dark_tech", "finance_gold")
        bg_key = "primary" if is_dark else "bg_white"
        self._set_slide_bg(slide, bg_key)

        accent_color = "bright_blue" if style_name == "dark_tech" else \
                       "gold" if style_name == "finance_gold" else "primary"
        self._add_rect(slide, Inches(0), Inches(0), SLIDE_WIDTH, Inches(0.04),
                       fill_color_key=accent_color)

        title_color = "text_white" if is_dark else "text_black"
        self._add_text_box(
            slide, MARGIN_LEFT, Inches(0.4), CONTENT_WIDTH, Inches(0.8),
            title, font_size=Pt(28), font_color_key=title_color, bold=True
        )

        if not steps:
            return

        num_steps = len(steps)
        step_width = Inches(2.0)
        arrow_width = Inches(0.5)
        total_width = step_width * num_steps + arrow_width * (num_steps - 1)
        start_x = (SLIDE_WIDTH - total_width) / 2
        top = Inches(2.5)

        for i, step in enumerate(steps):
            x = start_x + (step_width + arrow_width) * i

            # 步骤框
            card_bg = "card_bg" if is_dark else "light_gray"
            self._add_rect(slide, x, top, step_width, Inches(1.5),
                           fill_color_key=card_bg)

            # 步骤序号
            self._add_text_box(
                slide, x + Inches(0.15), top + Inches(0.1), Inches(0.5), Inches(0.4),
                f"0{i + 1}", font_size=Pt(20), font_color_key=accent_color, bold=True
            )

            # 步骤名称
            text_color = "text_white" if is_dark else "text_black"
            self._add_text_box(
                slide, x + Inches(0.15), top + Inches(0.5), step_width - Inches(0.3), Inches(0.4),
                step["name"], font_size=Pt(14), font_color_key=text_color, bold=True
            )

            # 步骤说明
            if step.get("desc"):
                desc_color = "text_gray" if is_dark else "text_gray"
                self._add_text_box(
                    slide, x + Inches(0.15), top + Inches(0.9), step_width - Inches(0.3), Inches(0.5),
                    step["desc"], font_size=Pt(11), font_color_key=desc_color
                )

            # 箭头
            if i < num_steps - 1:
                arrow_x = x + step_width
                self._add_text_box(
                    slide, arrow_x, top + Inches(0.45), arrow_width, Inches(0.4),
                    "→", font_size=Pt(20), font_color_key=accent_color, bold=True,
                    alignment=PP_ALIGN.CENTER
                )


class TimelineSlide(SlideTemplate):
    """时间轴页：里程碑展示"""

    def create(self, slide, title: str, milestones: list = None,
               style_name: str = "tech_blue"):
        """
        milestones: [{"time": "Q1", "event": "事件名", "desc": "说明"}, ...]
        """
        is_dark = style_name in ("dark_tech", "finance_gold")
        bg_key = "primary" if is_dark else "bg_white"
        self._set_slide_bg(slide, bg_key)

        accent_color = "bright_blue" if style_name == "dark_tech" else \
                       "gold" if style_name == "finance_gold" else "primary"
        self._add_rect(slide, Inches(0), Inches(0), SLIDE_WIDTH, Inches(0.04),
                       fill_color_key=accent_color)

        title_color = "text_white" if is_dark else "text_black"
        self._add_text_box(
            slide, MARGIN_LEFT, Inches(0.4), CONTENT_WIDTH, Inches(0.8),
            title, font_size=Pt(28), font_color_key=title_color, bold=True
        )

        if not milestones:
            return

        # 时间轴线
        line_y = Inches(4.0)
        line_color = "card_bg" if is_dark else "divider"
        self._add_rect(slide, MARGIN_LEFT, line_y, CONTENT_WIDTH, Inches(0.03),
                       fill_color_key=line_color)

        num_milestones = len(milestones)
        spacing = CONTENT_WIDTH / (num_milestones - 1) if num_milestones > 1 else Inches(0)

        for i, ms in enumerate(milestones):
            x = MARGIN_LEFT + spacing * i if num_milestones > 1 else MARGIN_LEFT + CONTENT_WIDTH / 2

            # 节点圆点
            dot_size = Inches(0.2)
            try:
                from pptx.enum.shapes import MSO_SHAPE
                shape = slide.shapes.add_shape(
                    MSO_SHAPE.OVAL,
                    x - dot_size / 2, line_y - dot_size / 2,
                    dot_size, dot_size
                )
                shape.fill.solid()
                shape.fill.fore_color.rgb = self._color(accent_color)
                shape.line.fill.background()
            except Exception:
                pass

            # 时间
            self._add_text_box(
                slide, x - Inches(0.6), line_y - Inches(0.7), Inches(1.2), Inches(0.4),
                ms["time"], font_size=Pt(14), font_color_key=accent_color, bold=True,
                alignment=PP_ALIGN.CENTER
            )

            # 事件
            text_color = "text_white" if is_dark else "text_black"
            self._add_text_box(
                slide, x - Inches(0.8), line_y - Inches(0.35), Inches(1.6), Inches(0.4),
                ms["event"], font_size=Pt(13), font_color_key=text_color, bold=True,
                alignment=PP_ALIGN.CENTER
            )

            # 说明
            if ms.get("desc"):
                desc_color = "text_gray" if is_dark else "text_gray"
                self._add_text_box(
                    slide, x - Inches(0.7), line_y + Inches(0.3), Inches(1.4), Inches(0.6),
                    ms["desc"], font_size=Pt(11), font_color_key=desc_color,
                    alignment=PP_ALIGN.CENTER
                )