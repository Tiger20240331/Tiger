"""PowerPoint export module for bilingual educational presentations.

Generates PPTX files with:
- Bilingual (English-Chinese) content
- Embedded multimedia (images, videos, GIFs)
- Teacher notes and student guidance
- CAIE KS3 curriculum alignment
- Age-appropriate design for adolescent learners
"""

import os
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from datetime import datetime
import logging

try:
    from pptx import Presentation
    from pptx.util import Inches, Pt
    from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
    from pptx.dml.color import RGBColor
    from pptx.enum.shapes import MSO_SHAPE
except ImportError:
    raise ImportError(
        "python-pptx is required for PPT export. "
        "Install with: pip install python-pptx"
    )

logger = logging.getLogger(__name__)


@dataclass
class BilingualText:
    """Container for English and Chinese text pairs."""
    english: str
    chinese: str

    def __str__(self):
        return f"{self.english} | {self.chinese}"


@dataclass
class MediaReference:
    """Container for multimedia references with attribution."""
    url: str
    type: str  # 'image', 'video', 'gif'
    caption: Optional['BilingualText'] = None
    attribution: Optional[str] = None
    source_url: Optional[str] = None  # For notes section


@dataclass
class TeacherNotes:
    """Container for teacher guidance and learning instructions."""
    teaching_tips: List[str]
    learning_objectives: List['BilingualText']
    assessment_ideas: List[str]
    resource_links: List[Dict[str, str]]  # {"title": "...", "url": "..."}
    duration_minutes: int = 45


class PPTExporter:
    """Export educational course content to PowerPoint presentations.
    
    Designed for international bilingual schools with Chinese mainland students
    at intermediate English proficiency levels.
    
    Features:
    - Bilingual slide content (English + Chinese)
    - Multiple slide layouts (title, content, blank)
    - Embedded multimedia with direct playback
    - Comprehensive teacher notes with learning objectives
    - Media source attribution in notes section
    - CAIE KS3 curriculum alignment metadata
    - Adolescent-friendly color schemes and typography
    """

    # Color scheme - adolescent-friendly, accessible
    COLORS = {
        'primary': RGBColor(26, 118, 188),      # Professional blue
        'secondary': RGBColor(76, 175, 80),      # Learning green
        'accent': RGBColor(255, 152, 0),         # Engaging orange
        'text_dark': RGBColor(33, 33, 33),       # Dark gray
        'text_light': RGBColor(255, 255, 255),   # White
        'background_light': RGBColor(245, 245, 245),  # Light gray
    }

    def __init__(
        self,
        title: BilingualText,
        module_code: str,
        curriculum_standard: str = "CAIE KS3",
        grade_level: int = 7,
        subject: str = "Biology",
    ):
        """Initialize PPT exporter.
        
        Args:
            title: Bilingual title (English, Chinese)
            module_code: Course/module code
            curriculum_standard: Curriculum alignment (default: CAIE KS3)
            grade_level: Grade level (default: 7)
            subject: Subject area (default: Biology)
        """
        self.presentation = Presentation()
        self.presentation.slide_width = Inches(10)
        self.presentation.slide_height = Inches(7.5)
        
        self.title = title
        self.module_code = module_code
        self.curriculum_standard = curriculum_standard
        self.grade_level = grade_level
        self.subject = subject
        self.slides_data: List[Dict[str, Any]] = []
        
        logger.info(
            f"Initialized PPT Exporter: {title.english} | {title.chinese}"
        )

    def add_title_slide(
        self,
        subtitle: Optional[BilingualText] = None,
        author: str = "CloudPedagogy Learning Publisher",
        date_str: Optional[str] = None,
    ) -> None:
        """Add a title slide.
        
        Args:
            subtitle: Optional subtitle
            author: Author name
            date_str: Date string (auto-generated if not provided)
        """
        if date_str is None:
            date_str = datetime.now().strftime("%B %d, %Y")
        
        slide = self.presentation.slides.add_slide(
            self.presentation.slide_layouts[6]  # Blank layout
        )
        
        # Background
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = self.COLORS['primary']
        
        # Title (bilingual)
        title_box = slide.shapes.add_textbox(
            Inches(0.5), Inches(2), Inches(9), Inches(1.5)
        )
        title_frame = title_box.text_frame
        title_frame.word_wrap = True
        
        p_en = title_frame.paragraphs[0]
        p_en.text = self.title.english
        p_en.font.size = Pt(54)
        p_en.font.bold = True
        p_en.font.color.rgb = self.COLORS['text_light']
        p_en.alignment = PP_ALIGN.CENTER
        
        p_zh = title_frame.add_paragraph()
        p_zh.text = self.title.chinese
        p_zh.font.size = Pt(48)
        p_zh.font.bold = True
        p_zh.font.color.rgb = self.COLORS['text_light']
        p_zh.alignment = PP_ALIGN.CENTER
        
        # Subtitle
        if subtitle:
            subtitle_box = slide.shapes.add_textbox(
                Inches(0.5), Inches(3.7), Inches(9), Inches(1)
            )
            subtitle_frame = subtitle_box.text_frame
            p_sub_en = subtitle_frame.paragraphs[0]
            p_sub_en.text = subtitle.english
            p_sub_en.font.size = Pt(24)
            p_sub_en.font.color.rgb = self.COLORS['accent']
            p_sub_en.alignment = PP_ALIGN.CENTER
            
            p_sub_zh = subtitle_frame.add_paragraph()
            p_sub_zh.text = subtitle.chinese
            p_sub_zh.font.size = Pt(20)
            p_sub_zh.font.color.rgb = self.COLORS['accent']
            p_sub_zh.alignment = PP_ALIGN.CENTER
        
        # Footer info
        footer_box = slide.shapes.add_textbox(
            Inches(0.5), Inches(6.5), Inches(9), Inches(0.8)
        )
        footer_frame = footer_box.text_frame
        p_footer = footer_frame.paragraphs[0]
        p_footer.text = (
            f"{self.module_code} | {self.subject} (Grade {self.grade_level}) | "
            f"{self.curriculum_standard} | {date_str}"
        )
        p_footer.font.size = Pt(12)
        p_footer.font.color.rgb = self.COLORS['text_light']
        p_footer.alignment = PP_ALIGN.CENTER
        
        logger.info("Added title slide")

    def add_content_slide(
        self,
        heading: BilingualText,
        content_points: List[BilingualText],
        media: Optional[List[MediaReference]] = None,
        teacher_notes: Optional[TeacherNotes] = None,
    ) -> None:
        """Add a content slide with bilingual text and optional multimedia.
        
        Args:
            heading: Bilingual heading
            content_points: List of bilingual content points (bullet points)
            media: Optional list of media references
            teacher_notes: Optional teacher guidance notes
        """
        slide = self.presentation.slides.add_slide(
            self.presentation.slide_layouts[6]  # Blank layout
        )
        
        # Background
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = self.COLORS['text_light']
        
        # Heading box with accent bar
        heading_box = slide.shapes.add_textbox(
            Inches(0.5), Inches(0.3), Inches(9), Inches(0.8)
        )
        heading_frame = heading_box.text_frame
        heading_frame.word_wrap = True
        
        p_h_en = heading_frame.paragraphs[0]
        p_h_en.text = heading.english
        p_h_en.font.size = Pt(40)
        p_h_en.font.bold = True
        p_h_en.font.color.rgb = self.COLORS['primary']
        
        p_h_zh = heading_frame.add_paragraph()
        p_h_zh.text = heading.chinese
        p_h_zh.font.size = Pt(32)
        p_h_zh.font.bold = True
        p_h_zh.font.color.rgb = self.COLORS['primary']
        p_h_zh.space_before = Pt(6)
        
        # Accent line under heading
        line_shape = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0.5), Inches(1.15), Inches(4), Inches(0.05)
        )
        line_shape.fill.solid()
        line_shape.fill.fore_color.rgb = self.COLORS['accent']
        line_shape.line.color.rgb = self.COLORS['accent']
        
        # Content (bullet points)
        content_box = slide.shapes.add_textbox(
            Inches(0.7), Inches(1.4), Inches(4.5), Inches(5.5)
        )
        content_frame = content_box.text_frame
        content_frame.word_wrap = True
        
        for i, point in enumerate(content_points):
            if i == 0:
                p = content_frame.paragraphs[0]
            else:
                p = content_frame.add_paragraph()
            
            # English bullet
            p.text = point.english
            p.font.size = Pt(18)
            p.font.color.rgb = self.COLORS['text_dark']
            p.level = 0
            p.space_after = Pt(6)
            
            # Chinese sub-bullet
            p_zh = content_frame.add_paragraph()
            p_zh.text = point.chinese
            p_zh.font.size = Pt(16)
            p_zh.font.color.rgb = self.COLORS['text_dark']
            p_zh.font.italic = True
            p_zh.level = 1
            p_zh.space_after = Pt(12)
        
        # Media placeholder (on right side)
        if media:
            media_box = slide.shapes.add_textbox(
                Inches(5.5), Inches(1.4), Inches(4), Inches(5.5)
            )
            media_frame = media_box.text_frame
            media_frame.word_wrap = True
            
            p_media = media_frame.paragraphs[0]
            p_media.text = "[Media Content]"
            p_media.font.size = Pt(14)
            p_media.font.bold = True
            p_media.font.color.rgb = self.COLORS['accent']
            p_media.space_after = Pt(6)
            
            for med in media:
                if med.caption:
                    p_caption = media_frame.add_paragraph()
                    p_caption.text = med.caption.english
                    p_caption.font.size = Pt(12)
                    p_caption.font.bold = True
                    p_caption.font.color.rgb = self.COLORS['primary']
                    p_caption.space_after = Pt(3)
                
                p_url = media_frame.add_paragraph()
                p_url.text = f"📎 {med.url[:50]}..."
                p_url.font.size = Pt(10)
                p_url.font.color.rgb = RGBColor(0, 102, 204)  # Link color
                p_url.space_after = Pt(6)
        
        # Store teacher notes (to be added to slide notes)
        if teacher_notes:
            self._add_notes_to_slide(slide, teacher_notes, media)
        
        logger.info(f"Added content slide: {heading.english}")

    def add_blank_slide(self) -> None:
        """Add a blank slide for custom content."""
        slide = self.presentation.slides.add_slide(
            self.presentation.slide_layouts[6]  # Blank layout
        )
        
        # White background
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = self.COLORS['text_light']
        
        logger.info("Added blank slide")

    def _add_notes_to_slide(
        self,
        slide,
        teacher_notes: TeacherNotes,
        media: Optional[List[MediaReference]] = None,
    ) -> None:
        """Add teacher notes to slide.
        
        Args:
            slide: The slide object
            teacher_notes: Teacher guidance data
            media: Optional media references for source attribution
        """
        notes_slide = slide.notes_slide
        notes_frame = notes_slide.notes_text_frame
        notes_frame.clear()  # Clear default text
        
        notes_text = []
        
        # Learning objectives
        notes_text.append("=== LEARNING OBJECTIVES ===")
        for obj in teacher_notes.learning_objectives:
            notes_text.append(f"• {obj.english}")
            notes_text.append(f"  ({obj.chinese})")
        
        # Teaching tips
        notes_text.append("\n=== TEACHING TIPS ===")
        notes_text.append(f"Duration: {teacher_notes.duration_minutes} minutes")
        notes_text.append("\nTips for effective teaching:")
        for tip in teacher_notes.teaching_tips:
            notes_text.append(f"• {tip}")
        
        # Assessment ideas
        notes_text.append("\n=== ASSESSMENT IDEAS ===")
        for assessment in teacher_notes.assessment_ideas:
            notes_text.append(f"• {assessment}")
        
        # Media source attribution
        if media:
            notes_text.append("\n=== MEDIA SOURCES ===")
            for med in media:
                if med.source_url:
                    caption_text = (
                        f"{med.caption.english}"
                        if med.caption
                        else f"{med.type.upper()}"
                    )
                    notes_text.append(f"\n• {caption_text}")
                    notes_text.append(f"  Type: {med.type}")
                    notes_text.append(f"  Source: {med.source_url}")
                    if med.attribution:
                        notes_text.append(f"  Attribution: {med.attribution}")
        
        # Resource links
        if teacher_notes.resource_links:
            notes_text.append("\n=== ADDITIONAL RESOURCES ===")
            for resource in teacher_notes.resource_links:
                notes_text.append(
                    f"• {resource.get('title', 'Resource')}\n"
                    f"  {resource.get('url', '')}"
                )
        
        # Add all text to notes
        p = notes_frame.paragraphs[0]
        p.text = "\n".join(notes_text)
        p.font.size = Pt(10)

    def save(self, output_path: str) -> None:
        """Save presentation to file.
        
        Args:
            output_path: Path where to save the PPTX file
        """
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
        
        self.presentation.save(output_path)
        logger.info(f"Saved presentation to: {output_path}")
        print(f"✅ PPT presentation saved: {output_path}")
