import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="winregmgr",
    version="0.0.4",
    author="Egor Wexler",
    author_email="egor.wexler@icloud.com",
    description="Context manager for Windows Registry manipulations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LuckyKarter/winregmgr",
    project_urls={
        "Bug Tracker": "https://github.com/LuckyKarter/winregmgr/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)