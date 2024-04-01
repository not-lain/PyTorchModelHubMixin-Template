import pathlib
from setuptools import find_packages, setup

with open('requirements.txt',"r",encoding="utf-8") as f:
    required = f.read().splitlines()

setup(
    name="PyTorchModelHubMixin_template",
    version="0.0.1",
    description="a template for the PyTorchModelHubMixin",
    long_description=pathlib.Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    Homepage="https://github.com/not-lain/PyTorchModelHubMixin-template",
    url="https://github.com/not-lain/PyTorchModelHubMixin-template",
    Issues="https://github.com/not-lain/PyTorchModelHubMixin-template/issues",
    authors=[{"name": "hafedh hichri", "email": "hhichri60@gmail.com"}],
    author_email="hhichri60@gmail.com",
    license="Apache 2.0 License",
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    classifiers=["Topic :: Utilities", "Programming Language :: Python :: 3.9"],
    # install_requires=["setuptools", "wheel", "torch","huggingface_hub=>"],
    install_requires=required,
)
