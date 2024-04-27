from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='loggingpython',
    version='1.4.15',
    description='Loggingpython is a Python package that provides a simple and\
 extensible way to integrate logging into your applications. The package\
 starts with a simple logger and can be extended with additional functions to\
 meet the requirements of your application.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='mrmajor.programmer',
    author_email='mrmajork.programmer@gmail.com',
    url='https://github.com/loggingpython-Community/loggingpython',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=['colorama', 'pandas'],
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Logging',
    ],
    include_package_data=True,
    package_data={
        '': ['docs/*'],
    },
)
