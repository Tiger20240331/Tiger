# Changelog

## [0.1.0] - 2024-07-13

### Initial Release

#### Added
- Core PPT Export Engine (`PPTExporter` class)
  - Bilingual (English-Chinese) slide support
  - Title slides with customizable subtitles
  - Content slides with bullet points and media
  - Blank slides for custom content
- Bilingual Text Support (`BilingualText` class)
  - English and Chinese text pairing
  - Automatic display on all elements
- Media Reference System (`MediaReference` class)
  - Image, video, and GIF support
  - Caption localization
  - Source attribution tracking
- Teacher Notes (`TeacherNotes` class)
  - Learning objectives
  - Teaching tips and strategies
  - Assessment ideas
  - Resource links
  - Duration tracking
- PPT Builder (`PPTBuilder` class)
  - Convert course configurations to presentations
  - Support for multiple sessions and sections
  - Content extraction and organization
- Biology-Specific Builder (`BiologyUnitPPTBuilder` class)
  - Grade 7 focus
  - CAIE KS3 alignment
  - Pre-configured subject terminology
- Professional Color Scheme
  - Adolescent-friendly design
  - Accessibility-focused colors
  - Easy customization options
- Complete Documentation
  - README.md - Full feature documentation
  - QUICKSTART.md - 5-minute setup guide
  - INSTALLATION.md - Detailed installation steps
  - INTEGRATION.md - CloudPedagogy integration guide
  - CUSTOMIZATION.md - Customization options
  - CHANGELOG.md - This file
- Examples
  - Grade 7 Biology Unit example (7 slides)
  - Cell Structure and Function unit
  - CAIE KS3 aligned content
- Testing & Quality
  - Installation verification script
  - Example test shell script
  - Makefile for common tasks
  - Setup script for distribution

#### Features

- **Bilingual Support**
  - Full English-Chinese parallel text
  - Automatic formatting for both languages
  - Support for simplified Chinese characters

- **Multimedia Integration**
  - Direct URL-based media references
  - Automatic caption generation
  - Source attribution in notes
  - Support for images, videos, and GIFs

- **Teacher Guidance**
  - Comprehensive notes for each slide
  - Learning objectives tracking
  - Teaching tips and strategies
  - Assessment suggestions
  - Resource links and references

- **Curriculum Alignment**
  - CAIE KS3 support
  - Grade 7 focused design
  - Extensible for other standards
  - Subject-specific builders

- **Accessibility**
  - High contrast color scheme
  - Large, readable fonts
  - Clear hierarchy and spacing
  - Screen reader friendly notes

- **Developer Experience**
  - Simple, intuitive API
  - Comprehensive documentation
  - Working examples
  - Easy customization

#### Technical

- Python 3.8+ support
- Dependencies: python-pptx, pyyaml, pydantic
- MIT License
- Modular architecture
- Extensible design

### Known Limitations

- Direct video embedding not supported (URLs only)
- Requires LibreOffice for PDF export
- Limited template customization in v0.1
- English and Chinese only in initial release

### Future Roadmap

#### v0.2.0 (Planned)
- [ ] Additional language support (Spanish, French)
- [ ] More subject-specific builders
- [ ] Template library
- [ ] Advanced multimedia embedding
- [ ] Real-time slide preview
- [ ] CloudPedagogy CLI integration

#### v0.3.0 (Planned)
- [ ] AI-powered content generation
- [ ] Automatic translation engine
- [ ] Interactive quiz slides
- [ ] Student learning analytics integration
- [ ] Export to multiple formats (PDF, HTML, SCORM)

#### v1.0.0 (Vision)
- [ ] Complete feature parity with commercial tools
- [ ] Full internationalization support
- [ ] Advanced accessibility features
- [ ] Enterprise deployment options
- [ ] Collaborative editing support

## Version History

### Pre-Release
- Initial development and testing
- Community feedback integration
- Documentation refinement

---

## How to Update

```bash
# Check current version
pip show cloudpedagogy-ppt-export

# Update to latest
pip install --upgrade cloudpedagogy-ppt-export
```

## Support

- Issues: https://github.com/Tiger20240331/Tiger/issues
- Documentation: See README.md
- Examples: See examples/ folder
