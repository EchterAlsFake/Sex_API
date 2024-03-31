from setuptools import setup, find_packages

setup(
    name="Sex_API",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "requests", "lxml", "bs4", "eaf_base_api"
    ],
    entry_points={
        'console_scripts': [
            # If you want to create any executable scripts
        ],
    },
    author="Johannes Habel",
    author_email="EchterAlsFake@proton.me",
    description="A Python API for the Porn Site Sex.com/pins",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license="LGPLv3",
    url="https://github.com/EchterAlsFake/Sex_API",
    classifiers=[
        # Classifiers help users find your project on PyPI
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Programming Language :: Python",
    ],
)