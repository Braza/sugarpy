from setuptools import setup, find_packages

setup(
    name='sugarpy',
    version='0.1.0.dev1',
    packages=find_packages(exclude=['tests*', 'sample*']),
    license='MIT',
    description='SugarCube v2 interpreter and processor',
    long_description=open('README.md').read(),
    install_requires=['antlr4-python3-runtime'],
    url='https://github.com/Braza/sugarpy',
    author='Sergey Yakovlev',
    author_email='https://github.com/Braza/sugarpy',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        ],
    keywords='sugarcube twine twee'
)
