
## Tube-Data: YouTube Video Transcript Extractor

Tube-Data is a Python script designed for extracting and cleaning YouTube video transcripts for preprocessing in machine learning. This versatile tool streamlines the process of acquiring high-quality text data from YouTube videos, making it ideal for various natural language processing tasks, sentiment analysis, speech recognition, and more.

## Features

- Extracts video transcripts from YouTube videos.
- Cleans transcripts by removing unwanted elements like music and applause.
- Saves cleaned transcripts into separate text files.
- Supports individual video URLs, batch processing from a list of URLs, and entire playlists.
- Streamlines the dataset collection process for machine learning applications.

## Installation

You can install the required dependencies using `pip`:

```bash
pip install tubelearns
```

## Usage

### Extract Transcripts from a List of Video URLs

```python
from tubelearns import text_link

# Provide a path to a text file containing YouTube video URLs.
text_link('path_to_file.txt', name='output_folder_name')
```

### Extract Transcript from a Single Video URL

```python
from tubelearns import url_grab

# Provide a single YouTube video URL.
url_grab('video_url', name='output_folder_name')
```

### Extract Transcripts from a YouTube Playlist

```python
from tubelearns import playlist_grab

# Provide the URL of a YouTube playlist.
playlist_grab('playlist_url', name='output_folder_name')
```

### Convert Playlist Video Links to Text File

```python
from tubelearns import play2text

# Provide the URL of a YouTube playlist.
play2text('playlist_url')
```

## Development Status

This project is currently in the planning stage.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributions

Contributions are welcome! Please feel free to open issues or submit pull requests.

## Contact

For any inquiries or feedback, please contact [KabilPreethamK](mailto:kabilpreethamk@gmail.com).

