import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-simple-authentication',
    zip_safe=False,
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='',
    long_description=README,
    url='https://github.com/teapow/django-simple-authentication',
    author='Thomas Power',
    author_email='thomaspwr@gmail.com',
    install_requires=[],
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
    test_suite='simple_authentication.run_tests.run',
)
