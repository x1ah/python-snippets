import re

import requests

from bs4 import BeautifulSoup


class Tumblr:
    def __init__(self, post_id, post_author, proxies=None):
        self.post_id = post_id
        self.post_author = post_author
        self.http = requests.Session()
        if proxies:
            self.http.proxies = proxies

    @classmethod
    def parse_post_url(cls, post_url):
        compail = re.compile('https?://(\w+)\.tumblr.com/post/(\d+)/?.+')
        ret = compail.search(post_url)
        if not ret:
            return None, None
        return ret.groups()

    def get_native_video_url(self):
        return f"https://www.tumblr.com/video/{self.post_author}/{self.post_id}/1000"

    def get_mp4_video_url(self):
        native_url = self.get_native_video_url()
        resp = self.http.get(native_url)
        soup = BeautifulSoup(resp.content, 'html.parser')
        return soup.video.source.get('src', '')
