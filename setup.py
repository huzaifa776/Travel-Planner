from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="TRAVEL Planner",
    version="0.1",
    author="Huzaifa",
    packages=find_packages(),
    install_requires = requirements,
)