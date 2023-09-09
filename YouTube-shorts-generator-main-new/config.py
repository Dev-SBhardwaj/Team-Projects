subreddit = "funny" # exclude 'r/', you can combine multiple subreddits with '+'. Ex: "funny+cars"
database = 'database.txt' # local text database file that ensures no duplicate videos get processed.

# Additional setup information for authenticating with the Reddit API can be found in the Reddit API documentation.
# Check this video: https://youtu.be/NRgfgtzIhBQ?t=50

# Using this config file alone should be able to get you going without further modification.
reddit_login = {
	'client_id': '07c7aYH6NwdHzPTMO8sY_w',
	'client_secret': 'F5Nq5DPjYN0hYB8gjUveZFglDe7BEw',
	'password': '3xdanger',
	'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
	'username': 'No_Natural_2064'
}


youtube = {
	'tags': '',
	'category': 22,  # has to be an int, more about category below
	'status': 'public'  # {public, private, unlisted}
}
# Note that by default, public isn't available unless you go through an audit. Checkout: https://support.google.com/youtube/contact/yt_api_form

video = {
	'dimensions': (1080, 1920),  # (horizontal, vertical) or None (not a string but literal) to upload the original clip as is.
	'blur': False  # blur non-perfect-fit clip
}

# for category: has to be an int, refer to YouTube Data 4 API's documentation, but as of Jan 2022,
# checkout https://techpostplus.com/youtube-video-categories-list-faqs-and-solutions/
