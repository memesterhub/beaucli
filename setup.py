import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="beaucli",
    version="0.0.dev1",
    author="Hussein Amine",
    author_email="husseinraedamine56@gmail.com",
    description="a tool for making your cli applications more colorful!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/memesterhub/beaucli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
