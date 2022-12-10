import setuptools

setuptools.setup(
    name="nodemon-py-simple",
    packages=setuptools.find_packages(),
    version="0.0.5",
    license='MIT',
    description="Nodemon like for python, very simple and without dependencies",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    download_url="https://github.com/thomasync/nodemon-py-simple/archive/refs/tags/0.0.5.tar.gz",
    author="thomasync",
    url="https://github.com/thomasync/nodemon-py-simple",
    keywords="python, nodemon, simple, watch, file, change, execute, command",
    entry_points={
        "console_scripts": ["nodemon-py-simple=nodemon_py_simple.main:main"]
    }
)
