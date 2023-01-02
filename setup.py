from setuptools import find_packages, setup

long_description = ""
with open("README.md") as ifp:
    long_description = ifp.read()

setup(
    name="semantics",
    version="0.0.1",
    packages=find_packages(),
    package_data={"semantics": ["py.typed"]},
    install_requires=[
        "openai"
    ],
    extras_require={
        "dev": ["black", "isort", "mypy", "wheel"],
        "distribute": ["setuptools", "twine", "wheel"],
    },
    description="Tools to extract semantics from data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="zomglings",
    author_email="neeraj@moonstream.to",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.6",
    url="https://github.com/zomglings/semantics",
    entry_points={"console_scripts": ["semantics=semantics.cli:main"]},
    include_package_data=True,
)
