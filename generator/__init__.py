# PresPPTDeck Generator
# PPT生成器模块

from .ppt_generator import PPTGenerator
from .templates import (
    SlideTemplate,
    CoverSlide,
    TOCSlide,
    ContentSlide,
    DataSlide,
    ComparisonSlide,
    EndingSlide,
    DESIGN_STYLES,
)

__all__ = [
    "PPTGenerator",
    "SlideTemplate",
    "CoverSlide",
    "TOCSlide",
    "ContentSlide",
    "DataSlide",
    "ComparisonSlide",
    "EndingSlide",
    "DESIGN_STYLES",
]