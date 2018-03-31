import requests

from urllib.parse import urlparse
from bs4 import BeautifulSoup


class Tumblr:
    def __init__(self, post_url, proxies=None):
        self.post_url = post_url
        self.http = requests.Session()
        if proxies:
            self.http.proxies = proxies

    def get_native_video_url(self):
        p = urlparse(self.post_url.strip('/'))
        tumblr_user = p.netloc.split('.')[0]
        post_id = p.path.split('/')[-1]
        return f"https://www.tumblr.com/video/{tumblr_user}/{post_id}/1000"

    def get_mp4_video_url(self):
        native_url = self.get_native_video_url()
        resp = self.http.get(native_url)
        soup = BeautifulSoup(resp.content, 'html.parser')
        return soup.video.source.get('src', '')
