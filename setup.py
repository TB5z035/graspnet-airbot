from setuptools import setup, find_packages

setup(
    name='graspnet',
    version='0.1',
	description='graspnet',
    author='Hongrui Zhu',
	author_email='',
    packages=find_packages(),
    install_requires=[
        'tensorboard',
        'numpy<=1.22.0',
        'scipy',
        'open3d',
        'Pillow',
        'tqdm',
        'torch',
    ]
)
