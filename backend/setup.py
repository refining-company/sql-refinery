from setuptools import setup, find_packages

setup(
    name="refinery sql language server",
    version="0.1-dev",
    package_dir={"": "reflanser"},
    packages=find_packages("src"),
    dependencies=["pygls", "tree-sitter"],  # TODO: add dependencies
    entry_points={
        "console_scripts": [
            "reflanser=reflanser.server",
        ],
    },
)
