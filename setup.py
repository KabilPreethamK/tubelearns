from setuptools import setup, find_packages
import codecs
import os
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.1.1'
DESCRIPTION = 'Python script for extracting and cleaning YouTube video transcripts for Pre-Processing in machine learning.'
LONG_DESCRIPTION = "This Python script serves as a powerful tool for machine learning practitioners and researchers engaged in the crucial stages of data preprocessing and dataset collection. Specifically designed for YouTube content, it automates the extraction of video transcripts, while intelligently cleaning them of extraneous elements like music and applause. The cleaned textual content is then efficiently saved into separate text files. By leveraging the youtube_transcript_api, pytube, and requests libraries, it streamlines the often time-consuming process of acquiring and refining textual data from YouTube videos. Whether you're working on natural language processing tasks, sentiment analysis, speech recognition, or any other machine learning application that requires high-quality text data, this script becomes an invaluable asset in your toolkit. It empowers you to effortlessly gather and preprocess diverse datasets from YouTube, ultimately accelerating your research and model development. Simplify your workflow, enhance your efficiency, and supercharge your machine learning endeavors with this versatile script.."

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
    install_requires=['youtube-transcript-api', 'requests', 'pytube','regex'],
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