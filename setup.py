import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "IPYNBRenderer"
AUTHOR_USER_NAME = 'rewatevijaykumar'
SRC_REPO = 'IPYNBRenderer'
AUTHOR_EMAIL = 'rewatevijaykumar@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="a small python package",
    long_description=long_description,
    long_desciption_content='text/markdown',
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls={
        'BugTracker': f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues'
    },
    package_dir={'':'src'},
    packages=setuptools.find_packages(where='src'),
}
