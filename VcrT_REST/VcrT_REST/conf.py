
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

admin_title = 'VcrT_REST'
admin_header = 'VcrT_REST'

cache_key = 'vcrt_rest'
cache_time = 60*3

success_code = 2000
warning_code = 3000
error_code = 5000

img_upload_path = os.path.join(BASE_DIR, 'media', 'kuukann_img')
face_upload_path = os.path.join(BASE_DIR, 'media', 'face')

url_header = 'http://127.0.0.1:8000/'
kuukann_url = url_header + 'api/kuukann/'

anonymous = 'Anonymous'