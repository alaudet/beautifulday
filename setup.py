from setuptools import setup

version = '0.0.3.1'

setup(name='my_weather',
      version=version,
      description='Learning about Webscraping',
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
      author='Al Audet',
      author_email='alaudet@linuxnorth.org',
      url='https://github.com/alaudet/my_weather',
      download_url='https://github.com/alaudet/my_weather/releases',
      license='MIT License',
      packages=['my_weather'],
      scripts=['bin/my_weather'],
      install_requires=['requests', 'beautifulsoup4']
      )
