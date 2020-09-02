import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kspconfig", # Replace with your own username
    version="1.1",
    author="Penta0308",
    author_email="kevin03088@naver.com",
    description="Kerbal Space Program Craft and Cfg Loader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Penta0308/kspconfig-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
