from setuptools import setup, find_packages
setup(
    name='django-stickynotes',
    version=__import__('stickynotes').get_version(limit=3),
    description='A Django application to handles messages for users that are deleted only when the user click the close link.',
    author='Guillaume Esquevin',
    author_email='guillaume.esquevin@platypus-creation.com',
    url='https://github.com/platypus-creation/django-stickynotes',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools']
)
