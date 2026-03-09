from setuptools import setup, find_packages

setup(
    name="RPYC",
    version="1.0.0",
    author="Gal green",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=["importlib", "flask", "requests", "json"],
)
