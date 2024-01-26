import requests
import random
import string
import time
def get_random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    ]
    return random.choice(user_agents)
def get_random_device_id():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
def get_random_ip_address():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))
def simulate_views(stream_id, num_views):
    for i in range(num_views):
        url = f"https://api16-core-c-useast1a.tiktokv.com/aweme/v1/play/?video_id={stream_id}&line=0&file_type=mp4&data_size=0&data_rate=0&live_stream=1&ac=WIFI&device_id={get_random_device_id()}&iid=0&os_version=11.4&app_name=musical_ly&version_code=16.4.0&device_type=iPhone10,4&is_play_url=1&resolution=1080*1920&is_support_h265=1&source=PackSourceEnum_LIVE_STREAMING&ab_version=16.4.0.1&channel=App%20Store&mcc_mnc="
        headers = {
            "User-Agent": get_random_user_agent(),
            "X-Real-IP": get_random_ip_address(),

        }
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            print(f"View {i+1} of {num_views} simulated successfully.")
            time.sleep(1)
        except requests.exceptions.HTTPError as e:
            print(f"Error simulating view: {e}")
            time.sleep(1)
stream_id = "your_live_stream_id_here"
num_views = 100
simulate_views(stream_id, num_views)
