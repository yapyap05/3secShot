import os
import time
from datetime import datetime
import pyautogui

# =========================
# 기본 저장 경로 설정
# =========================

home_dir = os.path.expanduser("~")
downloads_dir = os.path.join(home_dir, "Downloads")
base_save_dir = os.path.join(downloads_dir, "screenshot")

# =========================
# 날짜 폴더 생성
# 예:
# screenshot/2026-05-27/
# =========================

today = datetime.now().strftime("%Y-%m-%d")
save_dir = os.path.join(base_save_dir, today)
# 폴더 없으면 생성
os.makedirs(save_dir, exist_ok=True)

# =========================
# 캡처 시작
# =========================

print("3초 후 전체 화면을 캡처합니다...")
time.sleep(3)

# 전체 화면 캡처
screenshot = pyautogui.screenshot()

# =========================
# 파일명 생성
# 예:
# screenshot_20260527_153012.png
# =========================

now = datetime.now().strftime("%Y%m%d_%H%M%S")
file_name = f"screenshot_{now}.png"
save_path = os.path.join(save_dir, file_name)

# =========================
# 이미지 저장
# =========================

screenshot.save(save_path)
print("저장 완료")
print(save_path)
# pyinstaller --onefile --icon=icon.ico screenshot.py