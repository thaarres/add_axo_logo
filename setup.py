from setuptools import setup, find_packages

setup(
    name='add_axo_logo',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
    ],
    include_package_data=True,
    package_data={
        '': ['*.png'],
        'add_axo_logo': ['*.png'],
    },
    license='MIT',
    description='A package to add the AXO a logo to a corner of a Matplotlib plot.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Thea Aarrestad',
    author_email='thaarres@cern.ch',
    url='https://github.com/thaarres/add_axo_logo',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)