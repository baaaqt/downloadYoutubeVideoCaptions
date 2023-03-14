from youtube_transcript_api import YouTubeTranscriptApi
import os
import json


def get_captions(file_path: str, save_to: str) -> None:
    with open(file_path, "r") as links:
        '''
        file_path - path to the file with video_id
        file with video_ids must be in format like:
        "{video_id}\n
         {video_id}]\n
         ..."

        save_to - path to the directory where will be saved the captions as json files
        '''

        while True:
            video_id = links.readline().replace('\n', '')
            if not video_id:
                break
            try:
                captions = (YouTubeTranscriptApi.get_transcript(video_id))
            except:
                print(video_id, "- can't get captions")
                continue
            with open(save_to + f"/{video_id}.json", "w") as file:
                for caption in captions:
                    print(json.dumps(caption), file=file)

get_captions("links.txt", "captions")