from setuptools import setup

setup(
    name="nodemon-py-simple",
    packages = ['nodemon-py-simple'],
    version="0.0.2",
    license='MIT',
    description="Nodemon like for python, very simple and without dependencies",
    download_url="https://github.com/thomasync/nodemon-py-simple/archive/refs/tags/0.0.2.tar.gz",
    scripts=["nodemon-py-simple/main.py"],
    author="thomasync",
    url="https://github.com/thomasync/nodemon-py-simple",
    keywords="python, nodemon, simple, watch, file, change, execute, command",
)
