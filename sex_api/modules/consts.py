import re

# Root URLs

root = "https://sex.com/pins"  # Note, we don't care about the sex.com videos. It's just about the pins at /pins
root_pics = "https://www.sex.com/pics/?sort=popular&sub=all"
root_videos = "https://www.sex.com/videos/?sort=popular&sub=all"
root_gifs = "https://www.sex.com/gifs/?sort=popular&sub=all"

# Cookies:

cookie_accept_cookies = "%7B%22essential%22%3Atrue%2C%22analytics%22%3Atrue%7D"
cookie_locale = "en"
gre_captcha = "09APYnBZU4wfvpTRcU4Gd7r_VzNUmf_cO-MoM3-XsjCF41KmbLVrU7QAv8to6JHEWJqTDJaOYuo_q4NDS1n-zus23qoz8Cst2StxO5bQ"

cookies = {
    "privacy-preferences": cookie_accept_cookies,
    "locale": cookie_locale,
    "_grecaptcha": gre_captcha
}


# Headers
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': "https://www.sex.com/pins"
    }

# Regexes

# Comment
regex_comment_id = re.compile(r"<div class='comment' id='comment_(.*?)'>", re.DOTALL)
regex_comment_user = re.compile(r'class=\'commentUsername\'>(.*?)</a><br />', re.DOTALL)
regex_comment_messages = re.compile(r'<span> (.*?) </span>')
regex_comment_count = re.compile(r'Comments \((.*?)\)')

# Pin
regex_pin_name = re.compile(r'<h1 title="(.*?)" class="line', re.DOTALL)
regex_pin_publish_date = re.compile(r'<div[^>]+class="[^"]*shrink-0 w-px h-2 bg-heavy-tertiary[^"]*"[^>]*></div>\s*</li>\s*<li>([^<]+)</li>')
regex_pin_download_url = re.compile(r'<img\s+(?=.*?\balt\b)(?=.*?\bwidth\b)(?=.*?\bheight\b).*?src="(.*?)".*?>')
regex_pin_download_url_mp4 = re.compile(r'<video[^>]*\sid="video_html5_api"\sclass="vjs-tech"[^>]*\ssrc="([^"]*)"')
regex_detect_video = re.compile(r'To view this video please enable JavaScript, and consider upgrading to a (.*?) browser that')

# Tag
regex_tag_name = re.compile(r'class="tag">(.*?)</a>')

# Search
regex_extract_pins = re.compile(r'a class="image_wrapper" href="(.*?)/"')

# Users
regex_extract_name = re.compile(r'h1>(.*?)</h1>')
regex_description = re.compile(r'<div class="description">(.*?)</div>')
regex_amount_boards = re.compile(r'">(.*?) Boards')
regex_amount_following = re.compile(r'">(.*?) Following')
regex_amount_pins = re.compile(r'/pins/">(.*?) Pins')
regex_amount_repins = re.compile(r'">(.*?) Repins')
regex_amount_likes = re.compile(r'">(.*?) Likes')
regex_get_boards = re.compile(r'<a href="(.*?)/"><strong>')
regex_get_users = re.compile(r'<div class="title"><a href="(.*?)"><i class="fa fa-user">', re.DOTALL)

# Boards
regex_follower_count = re.compile(r'<div class="followerCount">(.*?) followers</div>')
regex_pin_count = re.compile(r'<div class="pinCount">(.*?) pins</div>')

# Other
regex_get_total_pages = re.compile(r'page=(.*?)" class="btn btn-default">')
