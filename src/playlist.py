from datetime import timedelta
import isodate as isodate
from src.channel import youtube


class PlayList:

    def __init__(self, pl_id):
        self.pl_id = pl_id
        self.playlist_videos = youtube.playlistItems().list(playlistId=self.pl_id,
                                                            part='contentDetails,snippet',
                                                            maxResults=50,
                                                            ).execute()

        playlist_info = youtube.playlists().list(part='snippet', id=pl_id).execute()
        self.title = playlist_info['items'][0]['snippet']['title']
        self.url = 'https://www.youtube.com/playlist?list=' + self.pl_id

    @property
    def total_duration(self):
        total_duration = timedelta(hours=0, minutes=0, seconds=0)
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(video_ids)
                                               ).execute()
        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration
        return total_duration

    def show_best_video(self):

        video_dict = {}
        for video in self.playlist_videos['items']:
            video_id = video['contentDetails']['videoId']
            video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                   id=video_id
                                                   ).execute()
            like_count: int = int(video_response['items'][0]['statistics']['likeCount'])
            video_dict[like_count] = video_id
        sorted_videos = sorted(video_dict.items())
        return f'https://youtu.be/{sorted_videos[-1][-1]}'
