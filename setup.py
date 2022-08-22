from setuptools import setup, find_packages

setup(
    name='pykawos',
    version='0.0.2',
    description='Python KMA AWS and ASOS',
    author='ParkJooHyeon',
    author_email='www.jrr.kr@gmail.com',
    url='https://gitlab.com/dogbull/pykawos',
    install_requires=[
        'pandas',
        'python-dateutil',
    ],
    packages=find_packages(exclude=['docs', 'tests*']),
    keywords=['kma', 'asos', 'aws'],
    python_requires='>=3',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)
