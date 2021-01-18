from setuptools import setup, find_packages

setup(
    name='rubberducky',
    version='0.1.0',    
    description='A rubber ducky app for terminal',
    url='https://github.com/kgiann78/rubberducky',
    author='Konstantinos Giannousis',
    author_email='kgiann78@gmail.com',
    license='BSD 2-clause',
    packages=['rubberducky', 'rubberducky.core'],
    include_package_data=True,
    install_requires=['search-engine-parser',
                      'aiohttp==3.6.2', 
                      'simple_chalk==0.1.0',
                      'textblob==0.15.0',
                      'nltk==3.2.5',                    
                      ],
    entry_points={'console_scripts': [
        'rubberducky=rubberducky.__main__:runner'
    ]},
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    package_data={
        '': ['*.*'],
        'requirements': ['*.*'],
    },
)
