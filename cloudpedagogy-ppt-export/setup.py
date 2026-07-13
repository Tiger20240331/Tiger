"""Setup script for CloudPedagogy PPT Export Module."""

from setuptools import setup, find_packages
from pathlib import Path

# Read requirements
requirements = Path("requirements.txt").read_text().strip().split("\n")

setup(
    name="cloudpedagogy-ppt-export",
    version="0.1.0",
    description="PowerPoint export module for CloudPedagogy Learning Publisher with bilingual (English-Chinese) support and CAIE KS3 alignment",
    author="CloudPedagogy Contributors",
    author_email="support@cloudpedagogy.com",
    url="https://github.com/Tiger20240331/Tiger/tree/main/cloudpedagogy-ppt-export",
    license="MIT",
    py_modules=["ppt_exporter", "ppt_builder"],
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Education",
        "Natural Language :: English",
        "Natural Language :: Chinese (Simplified)",
    ],
    keywords="powerpoint pptx education bilingual caie ks3 biology",
    project_urls={
        "Documentation": "https://github.com/Tiger20240331/Tiger/tree/main/cloudpedagogy-ppt-export",
        "Source": "https://github.com/Tiger20240331/Tiger",
        "Tracker": "https://github.com/Tiger20240331/Tiger/issues",
    },
)
