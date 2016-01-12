
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='realprice',
    version='0.0.0',
    description='real estate price viewer',
    long_description='''A program that uses a web crawler to gather data
        from real estate websites, and then displays that
        to the user''',
    url='https://github.com/pycollabproject/realprice',
    author='pycollabproject',
    license='Apache2.0',
    classifiers=[
        'Development Status :: 0 - pre-development',
        'Intended Audience :: Homebuyers',
        'Topic :: Reference :: Real estate',
        'License :: Apache 2.0',
        'Programming Language :: Python :: 3.x',
    ]
)
