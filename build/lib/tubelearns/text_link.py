import os 
from youtube_transcript_api import YouTubeTranscriptApi
import re
import requests
from pytube import Playlist


def text_link(path_text,name="raw_data"):
    exclude_keywords  = [
                    "[Music]",
                    "[Applause]",
                    "[Laughter]",
                    "[Singing]",
                    "[Background Noise]",
                    "[Indistinct]",
                    "[Cough]",
                    "[Phone Ringing]",
                    "[Phone Buzzing]",
                    "[Birds Chirping]",
                    "[Traffic Noise]",
                    "[Water Flowing]",
                    "[Wind Blowing]",
                    "[Explosion]",
                    "[Gunshots]",
                    "[Sirens Wailing]",
                    "[Dog Barking]",
                    "[Bell Ringing]"
                ]
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