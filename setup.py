from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="privacy-policy-parser",
    version="1.5.2",
    author="Applied Science Research Institute",
    author_email="research@appresearch.org",
    description="Automated tool for parsing and analyzing privacy policies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/appresearch/privacy-policy-parser",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "beautifulsoup4>=4.9.0",
        "requests>=2.25.0",
        "lxml>=4.6.0",
    ],
    entry_points={
        "console_scripts": [
            "privacy-policy-parser=privacy_policy_parser.cli:main",
        ],
    },
)


