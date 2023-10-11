from setuptools import setup, find_packages
import codecs
import os
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.1.6'
DESCRIPTION = 'Python script for extracting,cleaning and tokenization YouTube video transcripts for Pre-Processing in machine learning.'
LONG_DESCRIPTION = "Tube-Data (Version 1.1.6) is a versatile Python script designed for machine learning professionals and researchers. It automates the extraction of YouTube video transcripts while intelligently cleaning them of extraneous elements like music and applause. This latest version introduces advanced text preprocessing, including tokenization and punctuation removal, making data preparation more efficient. Tube-Data also now supports individual video URLs, batch processing, and entire playlists, streamlining dataset collection. Whether you're working on natural language processing, sentiment analysis, or speech recognition, Tube-Data accelerates research and model development, simplifying your workflow and boosting efficiency."

# Setting up
setup(
    name="tubelearns",
    version=VERSION,
    author="KabilPreethamK",
    author_email="<kabilpreethamk@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['youtube-transcript-api', 'requests', 'pytube','regex','num2words','spacy'],
    keywords=['python', 'video', 'transcript', 'raw data', 'cleaning', 'machine learning','pre-processing'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
]
)