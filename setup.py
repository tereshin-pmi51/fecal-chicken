import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    lond_description = f.read()

__version__ = '0.0.1'

REPO_NAME = 'fecal-chicken'
AUTHOR_USER_NAME = 'tereshin-pmi51'
SRC_REPO = 'cnnClassifier'
AUTHOR_EMAIL = 'tereshin-pmi51@bk.ru'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='Our DS project for live-coding on YouTube',
    lond_description=lond_description,
    lond_description_content='text/markdown',
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls={
        'Bug Tracker': f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues'
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    license='MIT'
)