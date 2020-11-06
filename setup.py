from setuptools import setup,find_packages

setup(name='mycode',
      version = '0.1',
      author='Peter Livingston',
      author_email='petston@gmail.com',
      pytho_requires='>2.7',
      packages=find_packages(include=['mycode','mycode.*']),
      py_modules=['mycode'],)
