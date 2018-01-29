from os.path import join
from setuptools import setup, find_packages


long_description = 'Computed property fields for Django'


def get_version():
    with open(join('computed_property', '__init__.py')) as f:
        for line in f:
            if line.startswith('__version__ ='):
                return line.split('=')[1].strip().strip('"\'')


setup(
    name='django-computed-property',
    version=get_version(),
    description="Computed property model fields for Django",
    long_description=long_description,
    author='Jason Brechin',
    author_email='brechinj@gmail.com',
    url='https://github.com/brechin/django-computed-property/',
    packages=find_packages(exclude=["*.tests", "*.tests.*"]),
    install_requires=['Django>=1.8.2', 'six==1.11.0'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        # 'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Framework :: Django',
    ],
)
