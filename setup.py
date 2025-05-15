from setuptools import setup, find_packages

setup(
    name="mad-libs-game",
    version="1.0.0",
    author="Devin Lawrence",
    author_email="your.email@example.com",  # Replace with your email
    description="A Mad Libs game with basic, mid, and complex versions",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mad-libs-game",  # Replace with your repo URL
    packages=find_packages(),
    install_requires=[
        "Pillow>=10.0.0",
        "requests>=2.28.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    scripts=[
        "Mad_Libs_Devin_Lawrence_Basic.py",
        "Mad_Libs_Devin_Lawrence_mid.py",
        "Mad_Libs_Devin_Lawrence_Complex.py",
    ],
    include_package_data=True,
    package_data={
        "": ["mad_libs.csv"],
    },
)