import os
import sys
import subprocess
from setuptools import setup, find_packages, Command

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

class AutoSetupCommand(Command):
    """Custom command to auto-setup venv, install requirements, and run bot"""
    description = 'Auto-create venv, install requirements, and run bot'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print("=" * 50)
        print("SURJO LIVE TCP BOT - AUTO SETUP")
        print("=" * 50)
        
        # Step 1: Create virtual environment
        print("\n[1/3] Creating virtual environment...")
        if not os.path.exists("venv"):
            subprocess.check_call([sys.executable, "-m", "venv", "venv"])
            print("✓ Virtual environment created")
        else:
            print("✓ Virtual environment already exists")
        
        # Step 2: Install requirements
        print("\n[2/3] Installing requirements...")
        if os.name == 'nt':  # Windows
            pip_path = os.path.join("venv", "Scripts", "pip")
            python_path = os.path.join("venv", "Scripts", "python")
        else:  # Linux/Mac/Termux
            pip_path = os.path.join("venv", "bin", "pip")
            python_path = os.path.join("venv", "bin", "python")
        
        subprocess.check_call([pip_path, "install", "--upgrade", "pip"])
        subprocess.check_call([pip_path, "install", "-r", "requirements.txt"])
        print("✓ Requirements installed")
        
        # Step 3: Run bot
        print("\n[3/3] Starting bot...")
        print("=" * 50)
        print("BOT IS NOW RUNNING...")
        print("=" * 50)
        subprocess.call([python_path, "main.py"])

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
    cmdclass={
        'auto_setup': AutoSetupCommand,
    },
    include_package_data=True,
    zip_safe=False,
)
