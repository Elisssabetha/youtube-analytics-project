from src.channel import youtube


class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        try:
            video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                   id=video_id
                                                   ).execute()
            self.title = video_response['items'][0]['snippet']['title']
            self.url_video = 'https://youtu.be/' + video_id
            self.view_qty = video_response['items'][0]['statistics']['viewCount']
            self.like_count = video_response['items'][0]['statistics']['likeCount']
        except (IndexError, KeyError):
            self.title = None
            self.url_video = None
            self.view_qty = None
            self.like_count = None

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, pl_id):
        super().__init__(video_id)
        self.pl_id = pl_id

    def __str__(self):
        return self.title
