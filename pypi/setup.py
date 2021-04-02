import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jsn",
    version="1.2.2",
    author="Alex Dixon",
    author_email="alexandercdixon@gmail.com",
    description="A relaxed, user-friendly json-like data format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/polymonster/jsn",
    packages=setuptools.find_packages(),
    python_requires='>=2.6',
    classifiers=[
    	'Programming Language :: Python :: 2',
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
