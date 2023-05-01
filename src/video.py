from src.channel import youtube


class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
        self.name_video = video_response['items'][0]['snippet']['title']
        self.url_video = 'https://youtu.be/' + video_id
        self.view_qty = video_response['items'][0]['statistics']['viewCount']
        self.like_qty = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.name_video


class PLVideo(Video):
    def __init__(self, video_id, pl_id):
        super().__init__(video_id)
        self.pl_id = pl_id

    def __str__(self):
        return self.name_video
