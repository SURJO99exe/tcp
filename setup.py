from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="surjo-live-tcp-bot",
    version="1.0.0",
    author="SURJO LIVE GAMING",
    author_email="contact@surjolive.com",
    description="A powerful TCP bot for Free Fire with advanced features",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SURJO99exe/tcp",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Games/Entertainment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "surjo-live-bot=main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
