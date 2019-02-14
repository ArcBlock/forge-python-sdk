import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

data_files = [('config', ['forge/config/forge_default.toml'])]

setuptools.setup(
    name="forge-python-sdk",
    version="0.2.4",
    author="Riley Shu",
    author_email="riley@arcblock.io",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArcBlock/forge-python-sdk",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={
            'config': ['forge/config/forge_default.toml'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'grpcio',
        'grpcio-tools',
        'toml',
        'deepmerge',
    ],
)
