import os 
from youtube_transcript_api import YouTubeTranscriptApi
import re
import requests
from pytube import Playlist

def text_link(path_text,name="raw_data"):
    if not os.path.exists(f"./{name}/"):
      os.makedirs(f"./{name}/")
    with open(path_text, "r") as f:
        content = f.readlines()
    count = 0
    for url in content:
        count = count+1
        url = url.replace("/n","")
        try: 
   

            pattern = r'v=([a-zA-Z0-9_-]+)'

            match = re.search(pattern, url)

            if match:
                extracted_string = match.group(1)
            else:
                print("No match found")

            transcript = YouTubeTranscriptApi.get_transcript(extracted_string)

            exclude_keywords = ["[Music]", "[Applause]"]

            filtered_transcript = ' '.join(entry['text'] for entry in transcript if all(keyword not in entry['text'] for keyword in exclude_keywords))

            url_punct = "http://bark.phon.ioc.ee/punctuator"

            data = {"text": filtered_transcript}

            response = requests.post(url_punct, data=data)

            if response.status_code == 200:
              file_name = f"./{name}/{name}_{count}.txt"
              if not os.path.exists(file_name):
                with open(file_name, "w", encoding='utf-8') as f:
                  output = f.write(str(response.text))
                  print(f"{file_name} is created with data.")
                      
              else:
                count += 1
                    
            else:
                print("Error:", response.status_code)

        except:
            pass

def url_grab(url,name="raw_data"):
    if not os.path.exists(f"./{name}/"):
      os.makedirs(f"./{name}/")

        
   
    url = url.replace("/n","")
    try: 
   

      pattern = r'v=([a-zA-Z0-9_-]+)'

      match = re.search(pattern, url)

      if match:
        extracted_string = match.group(1)
      else:
        print("No match found")

      transcript = YouTubeTranscriptApi.get_transcript(extracted_string)

      exclude_keywords = ["[Music]", "[Applause]"]

      filtered_transcript = ' '.join(entry['text'] for entry in transcript if all(keyword not in entry['text'] for keyword in exclude_keywords))

      url_punct = "http://bark.phon.ioc.ee/punctuator"

      data = {"text": filtered_transcript}
      response = requests.post(url_punct, data=data)
      
      if response.status_code == 200:
        while True:
          file_name = f"./{name}/{name}.txt"
          if not os.path.exists(file_name):
              with open(file_name, "w", encoding='utf-8') as f:
                output = f.write(str(response.text))
                break
          else:
            cmd = input("File name is already in exist. Do you want to replace the file (y/n): ")
            if cmd == "y":
              with open(file_name, "w", encoding='utf-8') as f:
                output = f.write(str(response.text))
                break
            else:
              break
          
                    
      else:
        print("Error:", response.status_code)

    except Exception as e:
      print("Some error occured plz check the url that you provided is validate.")
      print(e)

def playlist_grab(playlist_url, name="raw_data"):
    try:
        playlist = Playlist(playlist_url)
        playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

        video_links = [f"{url}" for url in playlist.video_urls]

        if not os.path.exists(f"./{name}/"):
            os.makedirs(f"./{name}/")
        content = video_links
        count = 0
        for url in content:
            count += 1
            url = url.replace("/n", "")
            try:
                pattern = r'v=([a-zA-Z0-9_-]+)'
                match = re.search(pattern, url)

                if match:
                    extracted_string = match.group(1)
                else:
                    print("No match found")

                transcript = YouTubeTranscriptApi.get_transcript(extracted_string)

                exclude_keywords = ["[Music]", "[Applause]"]

                filtered_transcript = ' '.join(entry['text'] for entry in transcript if all(keyword not in entry['text'] for keyword in exclude_keywords))

                url_punct = "http://bark.phon.ioc.ee/punctuator"

                data = {"text": filtered_transcript}

                response = requests.post(url_punct, data=data)
                if response.status_code == 200:
                  file_name = f"./{name}/{name}_{count}.txt"
                  if not os.path.exists(file_name):
                    with open(file_name, "w", encoding='utf-8') as f:
                      output = f.write(str(response.text))
                      print(f"{file_name} is created with data.")
                      
                  else:
                    count += 1
                else:
                  print("Error:", response.status_code)

            except Exception as e:
                print(e)
    except Exception as e:
        print("Error:", e)
from pytube import Playlist

def play2text(playlist_url):
    try:
        playlist = Playlist(playlist_url)
        playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

        video_links = [f"https://www.youtube.com{url}" for url in playlist.video_urls]

        if video_links:
            print("\nVideo Links in the Playlist:")
            with open("links.txt", "a") as f:
                for idx, link in enumerate(video_links, start=1):
                    f.write(link + "\n")
        else:
            print("No video links found in the playlist.")
    except Exception as e:
        print("Error:", e)





