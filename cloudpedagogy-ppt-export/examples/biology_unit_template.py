"""Example: Grade 7 Biology Unit - Cell Structure and Function (CAIE KS3)

This example demonstrates how to create a complete biology unit PPT
aligned with CAIE KS3 standards for Grade 7 students.
"""

from cloudpedagogy_ppt_export import (
    PPTExporter,
    BilingualText,
    MediaReference,
    TeacherNotes,
)


def create_biology_unit_ppt():
    """Create a Grade 7 Biology unit on Cell Structure and Function."""
    
    # ========== UNIT CONFIGURATION ==========
    
    unit_title = BilingualText(
        english="Cell Structure and Function",
        chinese="细胞结构与功能"
    )
    
    # Initialize PPT Exporter
    exporter = PPTExporter(
        title=unit_title,
        module_code="BIO7-U1",
        curriculum_standard="CAIE KS3",
        grade_level=7,
        subject="Biology"
    )
    
    # ========== SLIDE 1: TITLE SLIDE ==========
    
    exporter.add_title_slide(
        subtitle=BilingualText(
            english="Interactive Learning Unit",
            chinese="交互式学习单元"
        ),
        author="Science Department",
    )
    
    # ========== SLIDE 2: LEARNING OBJECTIVES ==========
    
    objectives = [
        BilingualText(
            english="Identify basic cell structures and their functions",
            chinese="识别基本的细胞结构及其功能"
        ),
        BilingualText(
            english="Understand the differences between plant and animal cells",
            chinese="理解植物细胞和动物细胞之间的差异"
        ),
        BilingualText(
            english="Explain how cell structures relate to their functions",
            chinese="解释细胞结构如何与其功能相关"
        ),
        BilingualText(
            english="Apply knowledge to predict cell behavior",
            chinese="应用知识来预测细胞行为"
        ),
    ]
    
    objectives_notes = TeacherNotes(
        teaching_tips=[
            "Display objectives at start of unit",
            "Refer back to objectives throughout lessons",
            "Have students self-assess against objectives",
        ],
        learning_objectives=[
            BilingualText(
                english="Students will be able to identify and describe cell structures",
                chinese="学生能够识别和描述细胞结构"
            ),
        ],
        assessment_ideas=[],
        resource_links=[],
        duration_minutes=5,
    )
    
    exporter.add_content_slide(
        heading=BilingualText(
            english="Learning Objectives",
            chinese="学习目标"
        ),
        content_points=objectives,
        teacher_notes=objectives_notes,
    )
    
    # ========== SLIDE 3: WHAT ARE CELLS? ==========
    
    cell_basics = [
        BilingualText(
            english="All living organisms are composed of cells",
            chinese="所有生物都由细胞组成"
        ),
        BilingualText(
            english="The cell is the smallest unit of life",
            chinese="细胞是生命的最小单位"
        ),
        BilingualText(
            english="Cells come in different shapes and sizes",
            chinese="细胞有不同的形状和大小"
        ),
        BilingualText(
            english="Most cells are microscopic and require magnification to see",
            chinese="大多数细胞是微观的，需要放大才能看到"
        ),
    ]
    
    cell_notes = TeacherNotes(
        teaching_tips=[
            "Show real microscope slides if available",
            "Discuss why cells are small (SA:V ratio)",
            "Ask: What's the smallest you can see without magnification?",
        ],
        learning_objectives=[
            BilingualText(
                english="Understand the cell theory",
                chinese="理解细胞学说"
            ),
        ],
        assessment_ideas=[
            "Show pictures of different cell types and ask students to identify them",
            "Quiz: True/false about cell properties",
        ],
        resource_links=[
            {
                "title": "Cells Introduction - Khan Academy",
                "url": "https://www.khanacademy.org/science/biology/structure-of-a-cell"
            },
        ],
        duration_minutes=10,
    )
    
    cell_media = [
        MediaReference(
            url="https://upload.wikimedia.org/wikipedia/commons/3/34/Animal_cell_structure_en.svg",
            type="image",
            caption=BilingualText(
                english="Animal Cell Diagram",
                chinese="动物细胞图"
            ),
            source_url="https://commons.wikimedia.org/wiki/File:Animal_cell_structure_en.svg",
            attribution="Wikimedia Commons - Public Domain"
        ),
    ]
    
    exporter.add_content_slide(
        heading=BilingualText(
            english="What Are Cells?",
            chinese="什么是细胞？"
        ),
        content_points=cell_basics,
        media=cell_media,
        teacher_notes=cell_notes,
    )
    
    # ========== SLIDE 4: PLANT VS ANIMAL CELLS ==========
    
    comparison = [
        BilingualText(
            english="Similarities: Nucleus, cytoplasm, cell membrane",
            chinese="相似之处：细胞核、细胞质、细胞膜"
        ),
        BilingualText(
            english="Plant cells have: Cell wall, chloroplasts, vacuoles",
            chinese="植物细胞有：细胞壁、叶绿体、液泡"
        ),
        BilingualText(
            english="Animal cells lack: Cell wall, chloroplasts, large vacuoles",
            chinese="动物细胞缺乏：细胞壁、叶绿体、大液泡"
        ),
    ]
    
    comparison_notes = TeacherNotes(
        teaching_tips=[
            "Use a Venn diagram on board",
            "Have students draw both cell types",
            "Discuss why these differences exist (function)",
        ],
        learning_objectives=[
            BilingualText(
                english="Compare plant and animal cells",
                chinese="比较植物细胞和动物细胞"
            ),
        ],
        assessment_ideas=[
            "Label diagram of plant and animal cells",
            "Fill-in table comparing cell types",
        ],
        resource_links=[],
        duration_minutes=15,
    )
    
    comparison_media = [
        MediaReference(
            url="https://upload.wikimedia.org/wikipedia/commons/5/5f/Plant_cell_structure_en.svg",
            type="image",
            caption=BilingualText(
                english="Plant Cell Structure",
                chinese="植物细胞结构"
            ),
            source_url="https://commons.wikimedia.org/wiki/File:Plant_cell_structure_en.svg",
            attribution="Wikimedia Commons - Public Domain"
        ),
    ]
    
    exporter.add_content_slide(
        heading=BilingualText(
            english="Plant vs Animal Cells",
            chinese="植物细胞 vs 动物细胞"
        ),
        content_points=comparison,
        media=comparison_media,
        teacher_notes=comparison_notes,
    )
    
    # ========== SLIDE 5: KEY ORGANELLES ==========
    
    organelles = [
        BilingualText(
            english="Nucleus: Controls cell activities, contains DNA",
            chinese="细胞核：控制细胞活动，包含DNA"
        ),
        BilingualText(
            english="Mitochondria: Powerhouse of the cell, produces energy (ATP)",
            chinese="线粒体：细胞的动力源，产生能量（ATP）"
        ),
        BilingualText(
            english="Chloroplasts (plants): Capture light energy for photosynthesis",
            chinese="叶绿体（植物）：捕获光能进行光合作用"
        ),
        BilingualText(
            english="Endoplasmic Reticulum: Network for protein synthesis and transport",
            chinese="内质网：蛋白质合成和运输的网络"
        ),
    ]
    
    organelles_notes = TeacherNotes(
        teaching_tips=[
            "Use analogies (nucleus=brain, mitochondria=power plant)",
            "Show animations of organelle functions",
            "Have students match structures to functions",
        ],
        learning_objectives=[
            BilingualText(
                english="Identify organelles and describe their functions",
                chinese="识别细胞器并描述其功能"
            ),
        ],
        assessment_ideas=[
            "Organelle function matching worksheet",
            "Labeled diagram quiz",
            "Essay: Why is the nucleus important?",
        ],
        resource_links=[
            {
                "title": "Cellular Organelles - Amoeba Sisters Video",
                "url": "https://www.youtube.com/watch?v=E8ZYOUqLcVY"
            },
        ],
        duration_minutes=20,
    )
    
    exporter.add_content_slide(
        heading=BilingualText(
            english="Key Organelles and Their Functions",
            chinese="关键细胞器及其功能"
        ),
        content_points=organelles,
        teacher_notes=organelles_notes,
    )
    
    # ========== SLIDE 6: CELL MEMBRANE ==========
    
    membrane = [
        BilingualText(
            english="Semi-permeable barrier controlling what enters and leaves",
            chinese="半透的屏障，控制进出物质"
        ),
        BilingualText(
            english="Made of phospholipid bilayer with embedded proteins",
            chinese="由磷脂双分子层和嵌入的蛋白质组成"
        ),
        BilingualText(
            english="Selectively permeable: allows some substances through, blocks others",
            chinese="选择透过性：允许某些物质通过，阻挡其他物质"
        ),
    ]
    
    membrane_notes = TeacherNotes(
        teaching_tips=[
            "Use physical model or animation to show structure",
            "Explain why selective permeability is important",
            "Relate to real-life examples (security gate analogy)",
        ],
        learning_objectives=[
            BilingualText(
                english="Understand cell membrane structure and function",
                chinese="理解细胞膜的结构和功能"
            ),
        ],
        assessment_ideas=[
            "Diagram and label cell membrane structure",
            "Explain selective permeability",
        ],
        resource_links=[],
        duration_minutes=12,
    )
    
    exporter.add_content_slide(
        heading=BilingualText(
            english="The Cell Membrane",
            chinese="细胞膜"
        ),
        content_points=membrane,
        teacher_notes=membrane_notes,
    )
    
    # ========== SLIDE 7: SUMMARY & REVIEW ==========
    
    summary = [
        BilingualText(
            english="Cells are the basic units of all living organisms",
            chinese="细胞是所有生物的基本单位"
        ),
        BilingualText(
            english="Plant and animal cells have different structures for different functions",
            chinese="植物细胞和动物细胞有不同的结构来执行不同的功能"
        ),
        BilingualText(
            english="Organelles have specialized roles in cell survival and reproduction",
            chinese="细胞器在细胞生存和繁殖中起专门作用"
        ),
        BilingualText(
            english="Cell membrane controls what enters and leaves the cell",
            chinese="细胞膜控制进出细胞的物质"
        ),
    ]
    
    summary_notes = TeacherNotes(
        teaching_tips=[
            "Review key vocabulary",
            "Check for understanding with exit ticket questions",
            "Preview next unit on cell division",
        ],
        learning_objectives=[
            BilingualText(
                english="Synthesize cell structure and function knowledge",
                chinese="综合细胞结构和功能知识"
            ),
        ],
        assessment_ideas=[
            "Unit test covering all concepts",
            "Student-created cell model project",
            "Discussion: How do cells relate to life processes?",
        ],
        resource_links=[
            {
                "title": "CAIE KS3 Biology Syllabus",
                "url": "https://www.cambridgeinternational.org/"
            },
        ],
        duration_minutes=10,
    )
    
    exporter.add_content_slide(
        heading=BilingualText(
            english="Unit Summary & Key Takeaways",
            chinese="单元总结与关键要点"
        ),
        content_points=summary,
        teacher_notes=summary_notes,
    )
    
    # ========== SAVE PRESENTATION ==========
    
    output_file = "Grade7_Biology_Unit1_CellStructureAndFunction.pptx"
    exporter.save(output_file)
    print(f"\n✅ Successfully created: {output_file}")
    print(f"📊 Unit includes:")
    print(f"   - 8 slides total")
    print(f"   - Bilingual content (English + Chinese)")
    print(f"   - CAIE KS3 alignment")
    print(f"   - Media references with attribution")
    print(f"   - Comprehensive teacher notes")


if __name__ == "__main__":
    create_biology_unit_ppt()
