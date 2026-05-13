from setuptools import setup, find_packages

setup(
    name="gitblame-iq",
    version="0.1.0",
    description="Turn git history into developer personality profiles",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "gitpython>=3.1.43",
        "radon>=6.0.1",
        "anthropic>=0.28.0",
        "jinja2>=3.1.4",
        "click>=8.1.7",
        "rich>=13.7.1",
    ],
    entry_points={
        "console_scripts": [
            "gitblame-iq=gitblame_iq.cli:main",
        ],
    },
    python_requires=">=3.9",
)