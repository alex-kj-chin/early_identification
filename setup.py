import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="early-identification-alex-kj-chin",
    version="0.0.1",
    author="Aelx Chin",
    author_email="alexanderchin@college.harvard.edu",
    description="A package to identify struggling students based on gradescope data",
    long_description=long_description,
    url="https://github.com/alex-kj-chin/early_identification",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)