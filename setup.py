from setuptools import setup, find_packages

setup(
    name='ai-sdk',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'openai',
        # Otras dependencias como HuggingFace, requests, etc.
    ],
)
