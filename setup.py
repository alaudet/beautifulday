from setuptools import setup

version = "0.3.0"

setup(
    name="beautifulday",
    version=version,
    description="Learning about Webscraping",
    long_description_content_type="text/markdown",
    long_description=open("./README.md", "r").read(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    author="Al Audet",
    author_email="alaudet@linuxnorth.org",
    url="https://www.linuxnorth.org/beautifulday/",
    download_url="https://github.com/alaudet/beautifulday/releases",
    license="MIT License",
    packages=["beautifulday"],
    scripts=["bin/beautifulday"],
    install_requires=["requests", "beautifulsoup4"],
)
