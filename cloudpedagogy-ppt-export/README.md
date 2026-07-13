# CloudPedagogy PPT Export Module

## Overview

A Python module for generating PowerPoint presentations from educational course content with comprehensive support for:

- **Bilingual Content**: English and Chinese (Simplified)
- **Curriculum Alignment**: CAIE KS3 (easily configurable for other standards)
- **Embedded Multimedia**: Images, GIFs, and videos with direct playback
- **Teacher Guidance**: Comprehensive notes with learning objectives and teaching tips
- **Age-Appropriate Design**: Optimized for Grade 7 learners (adolescent design principles)
- **Source Attribution**: All media sources linked in notes for academic integrity

## Installation

### Requirements

- Python 3.8+
- `python-pptx` library

### Setup

```bash
pip install python-pptx
```

## Quick Start

### Basic Example

```python
from cloudpedagogy_ppt_export import PPTExporter, BilingualText, TeacherNotes

# Create bilingual title
title = BilingualText(
    english="Cell Structure and Function",
    chinese="细胞结构与功能"
)

# Initialize exporter
exporter = PPTExporter(
    title=title,
    module_code="BIO7-U1",
    curriculum_standard="CAIE KS3",
    grade_level=7,
    subject="Biology"
)

# Add title slide
exporter.add_title_slide(
    subtitle=BilingualText(
        english="Interactive Learning Unit",
        chinese="交互式学习单元"
    )
)

# Add content slide
from cloudpedagogy_ppt_export import MediaReference

content_points = [
    BilingualText(
        english="All living organisms are made of cells",
        chinese="所有生物都由细胞组成"
    ),
    BilingualText(
        english="Cells contain specialized structures (organelles)",
        chinese="细胞包含专门的结构（细胞器）"
    ),
]

teacher_notes = TeacherNotes(
    teaching_tips=[
        "Use the cell model to show structure",
        "Have students identify organelles in diagram",
    ],
    learning_objectives=[
        BilingualText(
            english="Identify basic cell structures",
            chinese="识别基本的细胞结构"
        ),
    ],
    assessment_ideas=[
        "Label cell diagram worksheet",
        "Verbal quiz on organelle functions",
    ],
    resource_links=[
        {"title": "Cell Structure Video", "url": "https://example.com/cell-video"},
    ],
    duration_minutes=45,
)

media = [
    MediaReference(
        url="https://example.com/cell-diagram.png",
        type="image",
        caption=BilingualText(
            english="Animal Cell Structure",
            chinese="动物细胞结构"
        ),
        source_url="https://commons.wikimedia.org/wiki/File:Cell_structure.svg",
        attribution="Wikimedia Commons"
    ),
]

exporter.add_content_slide(
    heading=BilingualText(
        english="Cell Structure Basics",
        chinese="细胞结构基础"
    ),
    content_points=content_points,
    media=media,
    teacher_notes=teacher_notes,
)

# Save presentation
exporter.save("biology_unit_1.pptx")
```

## Features

### 1. Bilingual Support

Every text element supports English and Chinese:

```python
from cloudpedagogy_ppt_export import BilingualText

title = BilingualText(
    english="Photosynthesis",
    chinese="光合作用"
)
```

### 2. Multimedia Integration

Embed media with proper attribution:

```python
from cloudpedagogy_ppt_export import MediaReference

media = MediaReference(
    url="https://example.com/video.mp4",
    type="video",  # 'image', 'video', or 'gif'
    caption=BilingualText(
        english="Photosynthesis Process",
        chinese="光合作用过程"
    ),
    source_url="https://example.com/source",
    attribution="Educational Video Creator"
)
```

### 3. Teacher Notes

Comprehensive guidance for educators:

```python
from cloudpedagogy_ppt_export import TeacherNotes

notes = TeacherNotes(
    teaching_tips=[
        "Start with real-world examples",
        "Use interactive demonstrations",
    ],
    learning_objectives=[
        BilingualText(
            english="Understand photosynthesis equation",
            chinese="理解光合作用方程式"
        ),
    ],
    assessment_ideas=[
        "Quiz on factors affecting photosynthesis",
        "Lab report on light intensity effects",
    ],
    resource_links=[
        {
            "title": "BBC Bitesize: Photosynthesis",
            "url": "https://www.bbc.co.uk/bitesize/..."
        },
    ],
    duration_minutes=50,
)
```

### 4. CAIE KS3 Alignment

The module is pre-configured for CAIE KS3 curriculum:

- Grade 7 learner-focused design
- Appropriate vocabulary and complexity
- Learning objectives aligned with KS3 standards
- Assessment methods suitable for this level

## Slide Types

### Title Slide

```python
exporter.add_title_slide(
    subtitle=BilingualText(
        english="Unit 1: Introduction",
        chinese="单元1：介绍"
    ),
    author="Your Name",
    date_str="2024-07-13",
)
```

### Content Slide

```python
exporter.add_content_slide(
    heading=BilingualText(
        english="Key Concepts",
        chinese="关键概念"
    ),
    content_points=[
        BilingualText(english="Point 1", chinese="要点1"),
        BilingualText(english="Point 2", chinese="要点2"),
    ],
    media=media_list,
    teacher_notes=notes,
)
```

### Blank Slide

```python
exporter.add_blank_slide()
```

## Color Scheme

Optimized for adolescent learners and accessibility:

- **Primary Blue** (26, 118, 188): Professional, calming
- **Secondary Green** (76, 175, 80): Learning, growth
- **Accent Orange** (255, 152, 0): Engagement, attention
- **Dark Gray** (33, 33, 33): Text readability
- **Light Gray** (245, 245, 245): Background, reduces eye strain

## Media Source Attribution

All media sources are automatically documented in the Notes section for each slide:

```
=== MEDIA SOURCES ===

• Cell Diagram (Labeled)
  Type: image
  Source: https://commons.wikimedia.org/wiki/File:Cell_structure.svg
  Attribution: Wikimedia Commons
```

## For Teachers

Teacher notes include:

- **Learning Objectives**: Clear goals for each slide
- **Teaching Tips**: Practical strategies and timing
- **Assessment Ideas**: Formative and summative assessments
- **Resource Links**: Additional materials and references
- **Media Attribution**: Sources for all embedded content

## For Students

Design considerations for Chinese mainland students with intermediate English:

- **Bilingual text** on every slide (English + Chinese)
- **Large, readable fonts** (18pt+ for body text)
- **Visual aids** with clear captions
- **Age-appropriate color scheme** and layout
- **Embedded videos** playable directly in PowerPoint

## Example: Grade 7 Biology Unit

See `examples/biology_unit_template.py` for a complete Grade 7 Biology unit aligned with CAIE KS3.

## Integration with CloudPedagogy

This module is designed to integrate with the CloudPedagogy Learning Publisher:

1. **From YAML Config**: Convert course YAML to PPT structure
2. **From QMD Files**: Extract content from Quarto markdown
3. **To PPTX Output**: Generate PowerPoint with all features

```bash
# Coming soon:
coursegen export_ppt config/biology_unit.yml --output biology_unit.pptx
```

## License

MIT License - See LICENSE file for details

## Contributing

Contributions welcome! Please ensure:

- Code follows PEP 8 style guide
- Bilingual support (English + Chinese) for all text
- Proper documentation and comments
- Tests for new features

## Support

For issues, feature requests, or questions:

- GitHub Issues: (Link to repository)
- Documentation: See `/docs/` folder
- Examples: See `/examples/` folder
