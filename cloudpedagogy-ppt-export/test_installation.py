"""Test script to verify installation and dependencies."""

import sys
import subprocess


def test_imports():
    """Test if all required modules can be imported."""
    print("\n" + "="*50)
    print("TESTING IMPORTS")
    print("="*50)
    
    modules = [
        ("pptx", "python-pptx"),
        ("yaml", "pyyaml"),
        ("pydantic", "pydantic"),
    ]
    
    all_ok = True
    for module, package in modules:
        try:
            __import__(module)
            print(f"✅ {package:20} INSTALLED")
        except ImportError:
            print(f"❌ {package:20} MISSING")
            print(f"   Install with: pip install {package}")
            all_ok = False
    
    return all_ok


def test_module_imports():
    """Test PPT export module imports."""
    print("\n" + "="*50)
    print("TESTING MODULE IMPORTS")
    print("="*50)
    
    try:
        from ppt_exporter import (
            PPTExporter,
            BilingualText,
            MediaReference,
            TeacherNotes,
        )
        print("✅ PPTExporter:      OK")
        print("✅ BilingualText:    OK")
        print("✅ MediaReference:   OK")
        print("✅ TeacherNotes:     OK")
        
        from ppt_builder import PPTBuilder, BiologyUnitPPTBuilder
        print("✅ PPTBuilder:       OK")
        print("✅ BiologyUnitPPTBuilder: OK")
        
        return True
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        return False


def test_ppt_creation():
    """Test basic PPT creation."""
    print("\n" + "="*50)
    print("TESTING PPT CREATION")
    print("="*50)
    
    try:
        from ppt_exporter import PPTExporter, BilingualText
        
        print("Creating test presentation...")
        exporter = PPTExporter(
            title=BilingualText(
                english="Installation Test",
                chinese="安装测试"
            ),
            module_code="TEST-01",
        )
        
        exporter.add_title_slide()
        exporter.save("/tmp/test_installation.pptx")
        
        print("✅ Test PPT created: /tmp/test_installation.pptx")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def main():
    """Run all tests."""
    print("\n" + "#"*50)
    print("# CloudPedagogy PPT Export - Installation Test")
    print("#"*50)
    
    results = []
    
    # Test imports
    results.append(("Dependencies", test_imports()))
    
    # Test module imports
    results.append(("Module Imports", test_module_imports()))
    
    # Test PPT creation
    if results[-1][1]:  # Only test if module imports passed
        results.append(("PPT Creation", test_ppt_creation()))
    
    # Summary
    print("\n" + "="*50)
    print("TEST SUMMARY")
    print("="*50)
    
    all_passed = True
    for test_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{test_name:25} {status}")
        all_passed = all_passed and passed
    
    print("="*50)
    
    if all_passed:
        print("\n✅ ALL TESTS PASSED!")
        print("\nYou're ready to use CloudPedagogy PPT Export.")
        print("\nNext steps:")
        print("1. Run example: python examples/biology_unit_template.py")
        print("2. Create your own presentation")
        print("3. Check README.md for documentation")
        return 0
    else:
        print("\n❌ SOME TESTS FAILED")
        print("\nPlease install missing dependencies:")
        print("  pip install -r requirements.txt")
        return 1


if __name__ == "__main__":
    sys.exit(main())
