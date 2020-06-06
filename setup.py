#!/usr/bin/env python

from subprocess import check_call

from setuptools import setup, find_packages, Command

from app import __version__, __appname__, __description__

cmdclass = {}


class bdist_app(Command):
    """Custom command to build the application. """

    description = 'Build the application'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        check_call(['./venv/bin/pyinstaller', '-y', 'app.spec'])


cmdclass['bdist_app'] = bdist_app

setup(name=__appname__,
      version=__version__,
      packages=find_packages(),
      description=__description__,
      author='Namuan',
      author_email='info@deskriders.dev',
      license='MIT',
      url='https://deskriders.dev',
      entry_points={
          'gui_scripts': ['app=app.__main__:__main__.py'],
      },
      cmdclass=cmdclass)
