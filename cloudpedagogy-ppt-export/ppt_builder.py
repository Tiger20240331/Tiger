"""PPT Builder - Converts course configuration to PowerPoint presentations.

Bridges CloudPedagogy course structure (YAML config + Quarto content)
to PowerPoint output with bilingual support and embedded multimedia.
"""

import os
import logging
import json
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass

from .ppt_exporter import PPTExporter, BilingualText, MediaReference, TeacherNotes

logger = logging.getLogger(__name__)


class PPTBuilder:
    """Convert course content to PowerPoint presentations.
    
    Workflow:
    1. Parse YAML course configuration
    2. Extract content from QMD (Quarto Markdown) files
    3. Map bilingual content (English-Chinese)
    4. Identify embedded media references
    5. Build PowerPoint with teacher notes
    """

    def __init__(
        self,
        course_dir: str,
        config: Dict[str, Any],
        output_dir: str = "output",
    ):
        """Initialize PPT builder.
        
        Args:
            course_dir: Directory containing course scaffold
            config: Parsed YAML configuration
            output_dir: Output directory for PPTX files
        """
        self.course_dir = Path(course_dir)
        self.config = config
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Initialized PPTBuilder for {course_dir}")

    def build_from_config(
        self,
        module_config: Dict[str, Any],
        target_session: Optional[str] = None,
    ) -> str:
        """Build PowerPoint from module configuration.
        
        Args:
            module_config: Module configuration (from YAML)
            target_session: Specific session to build (or all if None)
            
        Returns:
            Path to generated PPTX file
        """
        module_id = module_config.get("id", "course")
        module_code = module_config.get("code", "Unknown")
        module_title = module_config.get("title", "Educational Module")
        
        # Create bilingual title
        title_en = module_title
        title_zh = module_config.get("title_zh", module_title)
        title = BilingualText(english=title_en, chinese=title_zh)
        
        # Initialize exporter
        exporter = PPTExporter(
            title=title,
            module_code=module_code,
            curriculum_standard=module_config.get(
                "curriculum_standard", "CAIE KS3"
            ),
            grade_level=module_config.get("grade_level", 7),
            subject=module_config.get("subject", "Biology"),
        )
        
        # Add title slide
        subtitle = BilingualText(
            english="Interactive Learning Unit",
            chinese="交互式学习单元"
        )
        exporter.add_title_slide(subtitle=subtitle)
        
        logger.info(f"Building PPT for module: {module_id}")
        
        # Build slides from sessions/sections
        sessions = module_config.get("sessions", [])
        for session in sessions:
            if target_session and session.get("id") != target_session:
                continue
            self._add_session_slides(exporter, session)
        
        # Save
        output_file = self.output_dir / f"{module_id}.pptx"
        exporter.save(str(output_file))
        
        return str(output_file)

    def _add_session_slides(
        self,
        exporter: PPTExporter,
        session: Dict[str, Any],
    ) -> None:
        """Add slides for a session.
        
        Args:
            exporter: PPTExporter instance
            session: Session configuration
        """
        session_title = session.get("title", "Session")
        session_title_zh = session.get("title_zh", session_title)
        
        sections = session.get("sections", [])
        for section in sections:
            self._add_section_slides(exporter, section)

    def _add_section_slides(
        self,
        exporter: PPTExporter,
        section: Dict[str, Any],
    ) -> None:
        """Add slides for a section.
        
        Args:
            exporter: PPTExporter instance
            section: Section configuration
        """
        section_title = section.get("title", "Section")
        section_title_zh = section.get("title_zh", section_title)
        
        heading = BilingualText(
            english=section_title,
            chinese=section_title_zh
        )
        
        # Add section divider slide
        exporter.add_blank_slide()

    @staticmethod
    def extract_bilingual_content(
        english_text: str,
        chinese_text: Optional[str] = None,
    ) -> BilingualText:
        """Extract or pair bilingual content.
        
        Args:
            english_text: English content
            chinese_text: Chinese translation (optional)
            
        Returns:
            BilingualText object
        """
        return BilingualText(
            english=english_text,
            chinese=chinese_text or english_text,
        )


class BiologyUnitPPTBuilder(PPTBuilder):
    """Specialized builder for Grade 7 Biology units aligned with CAIE KS3."""
    
    def __init__(
        self,
        course_dir: str,
        output_dir: str = "output",
    ):
        """Initialize Biology-specific builder.
        
        Args:
            course_dir: Directory containing course scaffold
            output_dir: Output directory for PPTX files
        """
        config = {
            "subject": "Biology",
            "grade_level": 7,
            "curriculum_standard": "CAIE KS3",
        }
        super().__init__(course_dir, config, output_dir)
