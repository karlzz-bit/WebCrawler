import requests
import json
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
cookies={
    'bd_ticket_guard_client_web_domain':'2',
    'passport_assist_user':'CkFNQ41LJ6iflmYS8ozcksJW6eYq-l6mAV1y7BjALoOiUYHXWZs9D2XZt6ahRG_XSK2V7AXPPTveE3MnhFBhTmjSpxpKCjxhHC2ftkVyp13C7oY722iIR7s0XFt1DaX1t9kfLJn5-CyDfB6IMsDB8Ga3ckWetsjcfvN7FHKelEM6tI4Q3MvIDRiJr9ZUIAEiAQNYaKw1',
    'n_mh':'hsMsIWkbJIm3gPXI830gZpXV512ohr551eogFhRSows',
    'sso_uid_tt':'2d48b2ad1d4190c47f7220a135f3c32d',
    'sso_uid_tt_ss':'2d48b2ad1d4190c47f7220a135f3c32d',
    'toutiao_sso_user':'da82f480711c3b8dc43b1423522776ae',
    'toutiao_sso_user_ss':'da82f480711c3b8dc43b1423522776ae',
    'LOGIN_STATUS':'1',  '_bd_ticket_crypt_cookie':'8ddcfbc4bd5e640a8a35a04637982ebf',
    'store-region':'cn-sd',
    'store-region-src':'uid',
    'my_rd':'2',
    'ttwid':'1%7CwcXCzQQwVqABkOIClhaoetB-D1SpNwG263R2V6KMLH0%7C1707727490%7C41d2ac49f50d3ee063cfcb80663aa0a2ee16d4a5b2fb3567ae8cb0c3ed82db4f',
    'live_use_vvc':'%22false%22',
    'dy_swidth':'2048',
    'dy_sheight':'1152',
    'xgplayer_device_id':'25143490980',
    'xgplayer_user_id':'292957142818',
    'uid_tt':'119b8e9bb47d573152ec33b0f45c92e5',
    'uid_tt_ss':'119b8e9bb47d573152ec33b0f45c92e5',
    'sid_tt':'cbd7ef25e611f8c886c5b40e4dd028a1',
    'sessionid':'cbd7ef25e611f8c886c5b40e4dd028a1',
    'sessionid_ss':'cbd7ef25e611f8c886c5b40e4dd028a1',
    '__live_version__':'%221.1.1.9068%22',
    's_v_web_id':'verify_lu9sd8jm_773a53bd_46d2_95cd_77fe_74656d2827f1',
    'SEARCH_RESULT_LIST_TYPE':'%22single%22',
    'download_guide':'%223%2F20240405%2F0%22',
    'passport_csrf_token':'8bf80be9a3b05b99b40514ba9573734e',
    'passport_csrf_token_default':'8bf80be9a3b05b99b40514ba9573734e',
    'sid_ucp_sso_v1':'1.0.0-KGFhMzg5ZjYzZDY3NjFiNjQ3ODAwNjVhY2I0NzMzYzViMDU3YjZiZTcKHwj-qYDx1YzyARD5qPywBhjvMSAMMNPG14oGOAZA9AcaAmxmIiBkYTgyZjQ4MDcxMWMzYjhkYzQzYjE0MjM1MjI3NzZhZQ',
    'ssid_ucp_sso_v1':'1.0.0-KGFhMzg5ZjYzZDY3NjFiNjQ3ODAwNjVhY2I0NzMzYzViMDU3YjZiZTcKHwj-qYDx1YzyARD5qPywBhjvMSAMMNPG14oGOAZA9AcaAmxmIiBkYTgyZjQ4MDcxMWMzYjhkYzQzYjE0MjM1MjI3NzZhZQ',
    'sid_guard':'cbd7ef25e611f8c886c5b40e4dd028a1%7C1713312889%7C5184000%7CSun%2C+16-Jun-2024+00%3A14%3A49+GMT',
    'sid_ucp_v1':'1.0.0-KGU5NTI4YjE4ODE5MDdmOWViMTQ2M2RkYWUyYmQ5M2ViMjJjZGI0MDQKGwj-qYDx1YzyARD5qPywBhjvMSAMOAZA9AdIBBoCbGYiIGNiZDdlZjI1ZTYxMWY4Yzg4NmM1YjQwZTRkZDAyOGEx',
    'ssid_ucp_v1':'1.0.0-KGU5NTI4YjE4ODE5MDdmOWViMTQ2M2RkYWUyYmQ5M2ViMjJjZGI0MDQKGwj-qYDx1YzyARD5qPywBhjvMSAMOAZA9AdIBBoCbGYiIGNiZDdlZjI1ZTYxMWY4Yzg4NmM1YjQwZTRkZDAyOGEx',
    'publish_badge_show_info':'%220%2C0%2C0%2C1713356531724%22',
    'EnhanceDownloadGuide':'%220_0_2_1713431282_0_0%22',
    'pwa2':'%220%7C0%7C3%7C0%22',
    'device_web_cpu_core':'12',
    'device_web_memory_size':'8',
    'architecture':'amd64',
    'csrf_session_id':'865d981b06959877ca662065c548fcda',
    'strategyABtestKey':'%221713838841.37%22',
    '__ac_nonce':'06627237b00a8ca2ff48f',
    '__ac_signature':'_02B4Z6wo00f01YfSp7wAAIDDCfqNFrYTgoGH8qMAAAfUWmpVEzWtmZRINMOZfE4Y8GuA-3trxNIUpZk6dmhnL27bYlUGv7arEOYHTvrvLUmsLATcb-kci7GuVV12edZVXq5N2I4RYvFho4GI72',
    'xg_device_score':'7.6933497129581925',
    'stream_player_status_params':'%22%7B%5C%22is_auto_play%5C%22%3A1%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22',
    'FOLLOW_NUMBER_YELLOW_POINT_INFO':'%22MS4wLjABAAAAqH_tG9K_TCM2xgS7FTFTOEfUBcPi0nURieiDfVtGRZ_xRy31azd-6FeraqDcsNJb%2F1713888000000%2F0%2F0%2F1713842601602%22',
    'odin_tt':'c50fb31ea9f4cb092e2d81d8394a1017aa9b7d0a936d3b3d172749b367498bfe1e42f0e0156424fc694e92eb291f69e4',
    'volume_info':'%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A1%7D',
    'IsDouyinActive':'true',
    'stream_recommend_feed_params':'%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A2048%2C%5C%22screen_height%5C%22%3A1152%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A12%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A1.45%2C%5C%22effective_type%5C%22%3A%5C%223g%5C%22%2C%5C%22round_trip_time%5C%22%3A300%7D%22',
    'msToken':'8EDb1I8NP4s4Ft5tsgKXYxt7SPJZiCy1DrTR48uAZHQ0JFe0abAehNwtNQFtTyaEQ-e3EgpG1rujzR_u7yVuxI93AOH9ckrANHpQ3gV7h8LseMFzQ4-PXfs=',
    'home_can_add_dy_2_desktop':'%221%22',
    'bd_ticket_guard_client_data':'eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCS3JJT1BzRU42c09xMGJsUHJqNXhGbzRaa005TlBNOFltT3llMnFJUWxONW96SEJMbnRmMzlmenQ3SHRHMVJJdy9QZ25wb2JEQ21CL25vTWRXN1NwTG89IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D',
    'passport_fe_beating_status':'true',
    'FOLLOW_LIVE_POINT_INFO':'%22MS4wLjABAAAAqH_tG9K_TCM2xgS7FTFTOEfUBcPi0nURieiDfVtGRZ_xRy31azd-6FeraqDcsNJb%2F1713888000000%2F0%2F1713842055634%2F0%22'
}
response = requests.get(
    'https://www.douyin.com/aweme/v1/web/im/spotlight/relation/?device_platform=webapp&aid=6383&channel=channel_pc_web&count=100&max_time=1713842064978&min_time=0&with_fstatus=1&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=2048&screen_height=1152&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=123.0.0.0&browser_online=true&engine_name=Blink&engine_version=123.0.0.0&os_name=Windows&os_version=10&cpu_core_num=12&device_memory=8&platform=PC&downlink=1.45&effective_type=3g&round_trip_time=300&webid=7332114273298597388&msToken=ltk17kJ80GutW4aD5HCOKLOcBaTwbTO9FEoZbelC8zH0indbSIAxnicNXIUVMUN0IGonpvR9IZ3UoHCXXVhxGP21x65pGI1Cbyx_FEidzxKzzVvcuiMNc54%3D&a_bogus=DJWhQfzhDigk6fyD5RnLfY3q6AF3YBck0trEMD2f1VvbAg39HMTV9exEqcwvu0mjLG%2FlIemjy4haYpcBrQQH0Hw3H8vO%2F2C2mgU0t-P2soDbRZ8eeg8knGJi-kT1FeeB5vd3EQvswJKcFbSp09or-7avOfPCYrtswyG7GflNv9smif%3D%3D',
    cookies=cookies,
    headers=headers
)
page=response.content.decode('utf-8')
print(page)