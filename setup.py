from setuptools import setup

readme = open('README.rst').read()
history = open('CHANGELOG.md').read()

# Loading the version with ``from facepy import __version__`` will
# cause setuptools to attempt to import dependencies that we have no
# guarantee exist on the system yet, so we'll have to use ``execfile`` to
# import the file that contains the version specifically.

setup(
    name='aiofacepy',
    version='0.0.1',  # flake8: noqa
    description='Asyncio based facepy port',
    long_description=readme + '\n\n' + history,
    author='Davide Setti',
    author_email='davide.setti@gmail.com',
    url='http://github.com/vad/aiofacepy',
    packages=['facepy'],
    install_requires=['aiohttp >=0.20', 'six >= 1.6'],
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    zip_safe=False
)
