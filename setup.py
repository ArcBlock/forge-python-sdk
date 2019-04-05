import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="forge-python-sdk",
    version="0.18.9",
    author="Riley Shu",
    author_email="riley@arcblock.io",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArcBlock/forge-python-sdk",
    packages=setuptools.find_packages(exclude=('examples',)),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'base58',
        'grpcio',
        'grpcio-tools',
        'toml',
        'deepmerge',
        'pysha3',
        'ed25519',
    ],
)
