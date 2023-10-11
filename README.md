
## TubeLearns: YouTube Video Transcript Extractor

TubeLearns is a Python script designed for extracting and cleaning YouTube video transcripts for preprocessing in machine learning. This versatile tool streamlines the process of acquiring high-quality text data from YouTube videos, making it ideal for various natural language processing tasks, sentiment analysis, speech recognition, and more.

## Features

- Extracts video transcripts from YouTube videos.
- Saves cleaned transcripts into separate text files.
- Supports individual video URLs, batch processing from a list of URLs, and entire playlists.
- Streamlines the dataset collection process for machine learning applications.
- New Feature: Tokenization and Punctuation Removal for text preprocessing and cleaning.

## Installation

You can install TubeLearns using pip:

```bash
pip install tubelearns
```

## Usage

### Playlist Grabbing

```python
from tubelearns import Acquisition

# Initialize the Acquisition class
model = Acquisition()

# Grab transcripts from a YouTube playlist
playlist_url = 'https://www.youtube.com/your_playlist_url'
model.playlist_grab(playlist_url, name="raw_data")
```

### Extract Video Links from Playlist

```python
# Extract video links from a YouTube playlist
playlist_url = 'https://www.youtube.com/your_playlist_url'
model.play2text(playlist_url)
```

### Tokenization and Cleaning

```python
from tubelearns.tokenizers import Tokenization, Cleaning

# Initialize the Tokenization class
tokenizer = Tokenization()
cleaner = Cleaning()

# Tokenize text data
text_data = "Your input text here."
tokenized_data = tokenizer.tokenize_raw(text_data)
cleaned_data = cleaner.punct_raw(tokenized_data)
```

Refer to the [TubeLearns documentation](https://github.com/KabilPreethamK/tubelearns/blob/main/Documentation.md) for detailed usage instructions and examples.

## Contributing

If you'd like to contribute to TubeLearns or report issues, please check out the [GitHub repository](https://github.com/KabilPreethamK/tubelearns).

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api)
- [PyTube](https://github.com/pytube/pytube)
- [spaCy](https://spacy.io/)
- [num2words](https://github.com/savoirfairelinux/num2words)

---


Enjoy using TubeLearns! If you have any questions or encounter issues, please don't hesitate to [get in touch](mailto:tubelearnsofficial@gmail.com).
```
