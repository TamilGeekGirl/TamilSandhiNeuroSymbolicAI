from setuptools import setup, find_packages

setup(
    name="TamilSandhi",  
    version="0.1.0",     # 0.1.0 for early release
    packages=find_packages(),  
    install_requires=[
        "open-tamil"     # List dependencies here
    ],
    author="XYZ",
    author_email="mymail@example.com",
    description="A Python library to detect and correct Tamil Sandhi errors using rule-based methods.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TamilGeekGirl/TamilSandhiLib",  
    license="MIT",  # Or "Apache-2.0", depending on what you choose
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Tamil",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic"
    ],
    python_requires='>=3.6',
)
