from setuptools import setup, find_packages

setup(
    name="config-server",
    version="1.0.0",
    author="Girish Mallula",
    author_email="chandramgc@gmail.com",
    description="A Python configuration server project that dynamically fetches configuration from a Git repository.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/chandramgc/config-server",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "Flask",
        "GitPython",
        "pyyaml",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "config-server=main:main",
        ]
    },
)
