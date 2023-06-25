from setuptools import setup


def read_description():
    with open("README.md") as file:
        return file.read()


setup(
    name="leekbot_cog",
    version="0.0.1",
    description="Tags Extension for Leek",
    long_description=read_description(),
    long_description_content_type="text/markdown",
    author="Lemon",
    author_email="justlemoncl@gmail.com",
    url="https://github.com/LeekByLemon/LeekTags",
    packages=[
        "leek_tags"
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
    ],
    install_requires=[
        "leekbot"
    ],
    python_requires=">=3.8",
    package_data={
        "": [
            "*.json"
        ]
    },
    include_package_data=True
)
