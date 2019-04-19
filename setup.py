from setuptools import setup

version = '0.0.1'

setup(name='***appname***',
      version=version,
      description='***desc***',
      long_description=open("./README.md", "r").read(),
      classifiers=[
          "Development Status :: 1 - Planning",
          "Environment :: Console",
          "Intended Audience :: End Users/Desktop",
          "Natural Language :: English",
          "Operating System :: POSIX :: Linux",
          "Programming Language :: Python :: 3",
          "Topic :: Multimedia :: Graphics :: Graphics Conversion",
          "License :: OSI Approved :: MIT License",
          ],
      author='Al Audet',
      author_email='alaudet@linuxnorth.org',
      url='https://www.linuxnorth.org/***?***/',
      download_url='https://github.com/alaudet/***/releases',
      license='MIT License',
      packages=['***'],
      scripts=['bin/***'],
      install_requires=['***']
      )
