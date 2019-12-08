import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jsn",
    version="0.0.2",
    author="Alex Dixon",
    author_email="alexandercdixon@gmail.com",
    description="A relaxed, user-friendly json-like data format with comments, includes, inheritance and syntactic sugar.. extending json and json5.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/polymonster/jsn",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)