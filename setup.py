from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="mglib",
    version="1.1.0",
    author="Eugen Ciur",
    author_email="eugen@papermerge.com",
    url="https://github.com/papermerge/mglib",
    description="Common code used across all Papermerge project utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache 2.0 License",
    keywords="common, pacakge, shared, papermerge",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
