try:
    from setuptools import setup #enables develop
except ImportError:
    from distutils.core import setup

setup(name='python_speech_features',
      version='0.4-test',
      description='Python Speech Feature extraction',
      author='James Lyons, RS-G',
      author_email='james.lyons0@gmail.com',
      license='MIT',
      packages=['python_speech_features'],
    )
