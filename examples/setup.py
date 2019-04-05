import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="forge-event-chain",
    version="0.18.9",
    author="Riley Shu",
    author_email="riley@arcblock.io",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArcBlock/forge-python-sdk",
    packages=setuptools.find_packages(
                exclude=('kvstore', 'quick_test', 'examples'),
    ),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'Flask==0.12.4',
        'Flask-AppBuilder==1.10.0',
        'Flask-Babel==0.11.1',
        'Flask-Caching==1.4.0',
        'Flask-Compress==1.4.0',
        'Flask-Login==0.2.11',
        'Flask-Migrate==2.2.1',
        'Flask-OpenID==1.2.5',
        'flask-qrcode',
        'Flask-Script==2.0.6',
        'Flask-Session==0.3.1',
        'Flask-SQLAlchemy==2.1',
        'Flask-Testing==0.7.1',
        'Flask-WTF==0.14.2',
        'flask-googlemaps',
        'forge-python-sdk==0.18.9',
        'requests',
        'click==6.7',
    ],
)
