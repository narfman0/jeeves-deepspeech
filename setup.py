from setuptools import setup, find_packages
from jasper_deepspeech import __version__ as version


setup(
    name="jasper-deepspeech",
    version=version,
    description=('DeepSpeech STT plugin for Jasper'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='jasper-deepspeech',
    author='Jon Robison',
    author_email='narfman0@gmail.com',
    license='LICENSE',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'deepspeech',
        # 'jasper', # pretty sure jasper is not on pypi yet :|
    ],
    test_suite='tests/test_jasper_deepspeech',
)
