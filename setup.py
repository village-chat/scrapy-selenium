from setuptools import setup, find_packages

def get_requirements(source):
    """Get the requirements from the given ``source``

    Parameters
    ----------
    source: str
        The filename containing the requirements
    """
    with open(source, 'r') as f:
        requirements = f.readlines()
    # Remove any comments or empty lines
    requirements = [r.strip() for r in requirements if r.strip() and not r.startswith('#')]
    return requirements

setup(
    packages=find_packages(),
    install_requires=get_requirements('requirements/requirements.txt')
)
