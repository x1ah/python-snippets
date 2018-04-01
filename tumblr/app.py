import re

from flask import Flask, render_template, request

from tumblr import Tumblr


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def parse():
    url, err = '', ''

    if request.method == 'GET':
        return render_template('index.html', url=url, err=err)

    url = request.form.get('url', '').strip()
    compail = re.compile('https?://(\w+)\.tumblr.com/post/(\d+)/?.+')
    ret = compail.search(url)
    if not ret:
        err = "地址错误"

    try:
        post_author, post_id = ret.groups()
        ret = Tumblr(post_id, post_author)
        url = ret.get_mp4_video_url()
    except Exception as e:
        url, err = '', str(e)

    return render_template('index.html', url=url, err=err)


if __name__ == "__main__":
    app.run()
