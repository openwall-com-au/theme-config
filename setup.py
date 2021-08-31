import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pelican-theme-config",
    version="0.0.2",
    author="(GalaxyMaster)",
    author_email="galaxy4public+pypi@gmail.com",
    description="A theme configuration plugin for Pelican",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords = 'pelican blog plugin theme',
    url="https://github.com/pelican-plugins/theme-config",
    packages=setuptools.find_packages(),
    install_requires = ['pelican>=4.2.0'],
    license = 'AGPL 3.0',
    classifiers=[
        "Framework :: Pelican :: Plugins",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
