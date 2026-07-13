# Customization Guide

## Overview

This guide explains how to customize the PPT Export Module for your specific needs.

## 1. Color Schemes

### Use Built-in Scheme

The module comes with a professional, accessible color scheme optimized for adolescent learners:

```python
PPTExporter.COLORS = {
    'primary': RGBColor(26, 118, 188),      # Professional blue
    'secondary': RGBColor(76, 175, 80),      # Learning green
    'accent': RGBColor(255, 152, 0),         # Engaging orange
    'text_dark': RGBColor(33, 33, 33),       # Dark gray
    'text_light': RGBColor(255, 255, 255),   # White
    'background_light': RGBColor(245, 245, 245),  # Light gray
}
```

### Create Custom Scheme

```python
from pptx.dml.color import RGBColor

# Define custom colors
custom_colors = {
    'primary': RGBColor(0, 102, 204),       # Deep blue
    'secondary': RGBColor(255, 87, 34),     # Deep orange
    'accent': RGBColor(76, 175, 80),        # Green
    'text_dark': RGBColor(25, 25, 25),      # Almost black
    'text_light': RGBColor(255, 255, 255),  # White
    'background_light': RGBColor(250, 250, 250),  # Near white
}

# Apply custom colors
from ppt_exporter import PPTExporter
PPTExporter.COLORS = custom_colors
```

### Color Schemes for Different Contexts

#### School/Academic

```python
academic_colors = {
    'primary': RGBColor(0, 51, 102),         # Navy blue
    'secondary': RGBColor(153, 153, 153),    # Gray
    'accent': RGBColor(204, 0, 0),           # Red
    'text_dark': RGBColor(0, 0, 0),          # Black
    'text_light': RGBColor(255, 255, 255),   # White
    'background_light': RGBColor(245, 245, 245),
}
```

#### Corporate/Professional

```python
corporate_colors = {
    'primary': RGBColor(0, 51, 102),         # Corporate blue
    'secondary': RGBColor(0, 102, 204),      # Light blue
    'accent': RGBColor(255, 128, 0),         # Orange
    'text_dark': RGBColor(51, 51, 51),       # Dark gray
    'text_light': RGBColor(255, 255, 255),   # White
    'background_light': RGBColor(240, 240, 240),
}
```

#### Colorblind-Friendly

```python
colorblind_colors = {
    'primary': RGBColor(0, 114, 188),        # Blue
    'secondary': RGBColor(213, 94, 0),       # Red-orange
    'accent': RGBColor(204, 121, 167),       # Purple
    'text_dark': RGBColor(0, 0, 0),          # Black
    'text_light': RGBColor(255, 255, 255),   # White
    'background_light': RGBColor(242, 242, 242),
}
```

## 2. Typography Customization

### Modify Font Sizes

Edit `ppt_exporter.py` to change default font sizes:

```python
# In add_title_slide()
p_en.font.size = Pt(54)  # Change title size

# In add_content_slide()
p.font.size = Pt(18)  # Change body text size
```

### Supported Languages

The module currently uses these fonts for optimal rendering:

```python
# English: Default sans-serif (Arial, Calibri)
# Chinese: Use SimSun or Microsoft YaHei for Windows
#          Use STHeiti or Hiragino Sans for Mac
#          Use WenQuanYi for Linux
```

### Custom Font Support

```python
# Modify ppt_exporter.py
p.font.name = "YourCustomFont"  # Change font family
p.font.size = Pt(16)             # Change size
p.font.bold = True               # Bold
p.font.italic = True             # Italic
p.font.color.rgb = RGBColor(0, 0, 0)  # Color
```

## 3. Layout Customization

### Change Slide Dimensions

```python
from pptx.util import Inches

# In PPTExporter.__init__()
self.presentation.slide_width = Inches(10)      # Standard 16:9
self.presentation.slide_height = Inches(7.5)

# For 4:3 format:
self.presentation.slide_width = Inches(10)
self.presentation.slide_height = Inches(7.5)

# For widescreen (16:10):
self.presentation.slide_width = Inches(10)
self.presentation.slide_height = Inches(6.25)
```

### Adjust Spacing

```python
# Modify margins and spacing in add_content_slide()
heading_box = slide.shapes.add_textbox(
    Inches(0.5),    # Left margin
    Inches(0.3),    # Top margin
    Inches(9),      # Width
    Inches(0.8)     # Height
)
```

## 4. Subject-Specific Customization

### Create Subject Builder

```python
# File: ppt_builder_chemistry.py
from ppt_builder import PPTBuilder
from ppt_exporter import PPTExporter, BilingualText

class ChemistryUnitPPTBuilder(PPTBuilder):
    """Specialized builder for Chemistry units."""
    
    def __init__(self, course_dir: str, output_dir: str = "output"):
        config = {
            "subject": "Chemistry",
            "grade_level": 7,
            "curriculum_standard": "CAIE KS3",
        }
        super().__init__(course_dir, config, output_dir)
    
    def build_from_config(self, module_config: dict) -> str:
        """Override to add chemistry-specific logic."""
        exporter = PPTExporter(
            title=BilingualText(
                english=module_config.get('title'),
                chinese=module_config.get('title_zh')
            ),
            module_code=module_config.get('code'),
            subject="Chemistry",
        )
        
        # Add chemistry-specific content
        # ...
        
        output_file = self.output_dir / f"{module_config['id']}.pptx"
        exporter.save(str(output_file))
        return str(output_file)
```

### Create Grade-Level Variants

```python
class Grade6BiologyBuilder(BiologyUnitPPTBuilder):
    """For Grade 6 (younger learners)."""
    
    def __init__(self, course_dir: str, output_dir: str = "output"):
        super().__init__(course_dir, output_dir)
        self.grade_level = 6
        # Adjust vocabulary, concepts, etc.

class Grade8BiologyBuilder(BiologyUnitPPTBuilder):
    """For Grade 8 (more advanced)."""
    
    def __init__(self, course_dir: str, output_dir: str = "output"):
        super().__init__(course_dir, output_dir)
        self.grade_level = 8
        # Add more complex concepts
```

## 5. Content Customization

### Add Custom Slide Layouts

```python
def add_two_column_slide(
    self,
    heading: BilingualText,
    left_content: List[BilingualText],
    right_content: List[BilingualText],
    teacher_notes: Optional[TeacherNotes] = None,
) -> None:
    """Add a two-column layout slide."""
    slide = self.presentation.slides.add_slide(
        self.presentation.slide_layouts[6]
    )
    
    # Left column
    left_box = slide.shapes.add_textbox(
        Inches(0.5), Inches(1.4), Inches(4.5), Inches(5.5)
    )
    # ... add left content ...
    
    # Right column
    right_box = slide.shapes.add_textbox(
        Inches(5.2), Inches(1.4), Inches(4.5), Inches(5.5)
    )
    # ... add right content ...
```

### Add Comparison Slides

```python
def add_comparison_slide(
    self,
    heading: BilingualText,
    left_label: BilingualText,
    right_label: BilingualText,
    left_points: List[BilingualText],
    right_points: List[BilingualText],
    teacher_notes: Optional[TeacherNotes] = None,
) -> None:
    """Add a comparison/contrast slide."""
    # Implementation using two columns with labels
    pass
```

## 6. Media Customization

### Configure Media Display

```python
# Modify how media is displayed
media_box = slide.shapes.add_textbox(
    Inches(5.5),    # Position
    Inches(1.4),    # Position
    Inches(4),      # Width
    Inches(5.5)     # Height
)

# Add thumbnails instead of URLs
for med in media:
    # Download and embed thumbnail
    # or show QR code linking to media
    pass
```

## 7. Assessment & Interaction

### Add Quiz Slides

```python
def add_quiz_slide(
    self,
    question: BilingualText,
    options: List[BilingualText],
    teacher_notes: Optional[TeacherNotes] = None,
) -> None:
    """Add a quiz/question slide."""
    slide = self.presentation.slides.add_slide(
        self.presentation.slide_layouts[6]
    )
    # Format as multiple choice question
    pass
```

## 8. Localization

### Support Additional Languages

```python
@dataclass
class MultilingualText:
    """Support for multiple languages."""
    english: str
    chinese: str
    spanish: Optional[str] = None
    french: Optional[str] = None
    
    def get(self, language: str) -> str:
        return getattr(self, language, self.english)
```

## 9. Templates

### Create Reusable Templates

```python
# templates/biology_template.py
from ppt_exporter import PPTExporter, BilingualText

class BiologyTemplate(PPTExporter):
    """Template for Biology units."""
    
    def __init__(self, title: BilingualText):
        super().__init__(
            title=title,
            curriculum_standard="CAIE KS3",
            subject="Biology",
            grade_level=7,
        )
    
    def add_anatomy_slide(self, system_name: BilingualText, organs: List):
        """Pre-formatted slide for anatomical systems."""
        # Specialized formatting for anatomy
        pass
```

## 10. Export Options

### Different Output Formats

```python
def export_to_pdf(self, output_path: str) -> None:
    """Export to PDF (requires LibreOffice)."""
    import subprocess
    subprocess.run([
        "libreoffice", "--headless", "--convert-to", "pdf",
        self.pptx_path, "--outdir", os.path.dirname(output_path)
    ])

def export_to_html(self, output_path: str) -> None:
    """Export to HTML for web viewing."""
    # Convert PPTX to HTML
    pass
```

## Examples

See `examples/` folder for:
- `biology_unit_template.py` - Grade 7 Biology
- Upcoming: Chemistry, Physics, Math examples

## Best Practices

1. **Color**: Use consistent color schemes across all slides
2. **Typography**: Limit to 2-3 fonts per presentation
3. **Layout**: Maintain consistent margins and spacing
4. **Content**: Keep text concise, use bullets
5. **Media**: Optimize image sizes, test video links
6. **Notes**: Always include comprehensive teacher notes
7. **Accessibility**: Ensure adequate contrast ratios
8. **Testing**: Preview on target audience devices

## Troubleshooting

If customizations don't work:
1. Check python-pptx documentation
2. Review examples for reference implementation
3. Test with minimal changes first
4. Enable logging for debugging
