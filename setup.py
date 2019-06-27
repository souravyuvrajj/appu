from setuptools import setup, find_packages

setup(
      # mandatory
      name="appu",
      # mandatory
      version="0.1",
      # mandatory
      author_email="souravyuvrajj@gmail.com",
      packages=['appu'],
      package_data={},
      install_requires=['click', 'tabulate', 'requests'],
      entry_points={
        'console_scripts': ['appu = appu.appu:main']
      }
)
