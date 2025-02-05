import requests

class MetaClient:
    def __init__(self, page_id, access_token):
        self.page_id = page_id
        self.access_token = access_token

    def post_message_Facebook(self, message):
        url = f"https://graph.facebook.com/{self.page_id}/feed"
        payload = {
            "message": message,
            "access_token": self.access_token,
        }
        response = requests.post(url, data=payload)
        return response

    def post_image_Facebook(self, image_path, message):
        url = f"https://graph.facebook.com/{self.page_id}/photos"
        payload = {
            "message": message,
            "access_token": self.access_token,
        }
        files = {
            "source": open(image_path, "rb"),
        }
        response = requests.post(url, data=payload, files=files)
        return response

    def post_video_Facebook(self, video_path, message):
        url = f"https://graph.facebook.com/{self.page_id}/videos"
        payload = {
            "description": message,
            "access_token": self.access_token,
        }
        files = {
            "source": open(video_path, "rb"),
        }
        response = requests.post(url, data=payload, files=files)
        return response

    def post_link_Facebook(self, link, message):
        url = f"https://graph.facebook.com/{self.page_id}/feed"
        payload = {
            "link": link,
            "message": message,
            "access_token": self.access_token,
        }
        response = requests.post(url, data=payload)
        return response

    def post_Instagram_picture(self, image_path, message):
        url = f"https://graph.facebook.com/{self.page_id}/media"
        payload = {
            "caption": message,
            "access_token": self.access_token,
        }
        files = {
            "image": open(image_path, "rb"),
        }
        response = requests.post(url, data=payload, files=files)
        return response

    def post_Instagram_video(self, video_path, message):
        url = f"https://graph.facebook.com/{self.page_id}/media"
        payload = {
            "caption": message,
            "access_token": self.access_token,
        }
        files = {
            "video": open(video_path, "rb"),
        }
        response = requests.post(url, data=payload, files=files)
        return response