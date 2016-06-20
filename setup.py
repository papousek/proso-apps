from setuptools import setup, find_packages
import proso.release
import os

VERSION = proso.release.VERSION

setup(
    name='proso-apps',
    version=VERSION,
    description='General library for applications in PROSO projects',
    author='Adaptive Learning Group',
    author_email='al@fi.muni.cz',
    namespace_packages = ['proso', 'proso.django'],
    include_package_data = True,
    packages=[
        'proso',
        'proso.django',
        'proso.models',
        'proso_ab',
        'proso_ab.migrations',
        'proso_common',
        'proso_common.management',
        'proso_common.management.commands',
        'proso_common.migrations',
        'proso_configab',
        'proso_configab.management',
        'proso_configab.management.commands',
        'proso_configab.migrations',
        'proso_feedback',
        'proso_feedback.migrations',
        'proso_models',
        'proso_models.management',
        'proso_models.management.commands',
        'proso_models.migrations',
        'proso_user',
        'proso_user.management',
        'proso_user.management.commands',
        'proso_user.migrations',
        'proso_flashcards',
        'proso_flashcards.management',
        'proso_flashcards.management.commands',
        'proso_flashcards.migrations',
        'proso_tasks',
        'proso_tasks.management',
        'proso_tasks.management.commands',
        'proso_tasks.migrations',
        'proso_concepts',
        'proso_concepts.management',
        'proso_concepts.management.commands',
        'proso_concepts.migrations',
    ],
    setup_requires=[
        'Sphinx>=1.3',
        'sphinxcontrib-napoleon>=0.5.0',
    ],
    install_requires=[
        'Django==1.9.1',
        'Markdown==2.6.5',
        'Pillow==2.6.0',
        'PyYAML==3.11',
        'clint==0.5.1',
        'django-debug-toolbar==1.4',
        'django-flatblocks==0.9.2',
        'django-ipware==1.1.3',
        'django-lazysignup==1.0.2',
        'flake8==2.5.1',
        'ipython==4.0.3',
        'jsonfield==1.0.3',
        'jsonschema==2.5.1',
        'mock==1.3.0',
        'pandas==0.17.1',
        'psycopg2==2.6.1',
        'python-social-auth==0.2.14',
        'seaborn==0.7.0',
        'ua-parser==0.6.1',
        'user-agents==1.0.1',
    ],
    license='MIT',
)
