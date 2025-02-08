from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="regex-ease",
    version="0.1.1",
    description="A simple regex library to make your life easy :)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Siddesh Shewde",
    author_email="siddesh.shewde@gmail.com",
    url="https://github.com/Collaborative-Open-Source-Projects",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.6",
)
