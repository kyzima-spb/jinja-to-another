import os

from setuptools import setup


def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


readme = read_file('README.rst')


setup(
    name='jinja-to-another',
    use_scm_version={
        'relative_to': __file__,
        'local_scheme': lambda version: '',
    },
    description='Converts Jinja2 templates to the syntax of other template engines.',
    keywords='jinja templating html django',
    long_description=readme,
    url='https://github.com/kyzima-spb/jinja-to-another',
    license='MIT',
    author='Kirill Vercetti',
    author_email='office@kyzima-spb.com',
    py_modules=['jinja_to_another'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'jinja2another=jinja_to_another.cli:cli',
        ],
    },
    setup_requires=['setuptools_scm'],
    install_requires=[
        'jinja2',
        'Click>=7.1,<8',
        'colorama',
    ],
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
