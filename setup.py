from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="breakout-game",
    version="1.0.0",
    author="MRESKY",
    author_email="",
    description="A classic Breakout arcade game built with Python and Pygame",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MRESKY/6-Python_Game_Breakout_game",
    project_urls={
        "Bug Tracker": "https://github.com/MRESKY/6-Python_Game_Breakout_game/issues",
        "Documentation": "https://github.com/MRESKY/6-Python_Game_Breakout_game#readme",
        "Source Code": "https://github.com/MRESKY/6-Python_Game_Breakout_game",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Games/Entertainment :: Arcade",
        "Topic :: Software Development :: Libraries :: pygame",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.812",
        ],
    },
    entry_points={
        "console_scripts": [
            "breakout-game=main:main",
        ],
    },
    keywords=[
        "game", "pygame", "breakout", "arcade", "python", 
        "entertainment", "classic-games", "retro-games"
    ],
    include_package_data=True,
    zip_safe=False,
)