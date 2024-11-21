import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hvcheck",
    version="0.2",
    author="Aulia Khalqillah",
    author_email="auliakhalqillah.mail@gmail.com",
    description="Program to check reliable and clear peak of H/V curve",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/auliakhalqillah/hvcheck",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
