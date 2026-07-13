"""CloudPedagogy PPT Export Module

PowerPoint generation for educational content with:
- Bilingual (English-Chinese) support
- CAIE KS3 curriculum alignment
- Embedded multimedia (images, videos, GIFs)
- Teacher notes and student guidance
- Age-appropriate design for adolescent learners

Version: 0.1.0
"""

__version__ = "0.1.0"
__author__ = "CloudPedagogy Contributors"

from .ppt_exporter import PPTExporter, BilingualText, MediaReference, TeacherNotes
from .ppt_builder import PPTBuilder

__all__ = [
    "PPTExporter",
    "BilingualText",
    "MediaReference",
    "TeacherNotes",
    "PPTBuilder",
]
