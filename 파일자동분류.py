import os
import shutil

# 다운로드 폴더 경로
download_folder = r'C:\Users\nd981\Downloads'

# 분류할 폴더 경로
images_folder = os.path.join(download_folder, 'images')
data_folder = os.path.join(download_folder, 'data')
docs_folder = os.path.join(download_folder, 'docs')
archive_folder = os.path.join(download_folder, 'archive')

# 폴더 생성
os.makedirs(images_folder, exist_ok=True)
os.makedirs(data_folder, exist_ok=True)
os.makedirs(docs_folder, exist_ok=True)
os.makedirs(archive_folder, exist_ok=True)

# 파일 이동 함수
def move_files(src_folder, file_extensions, dest_folder):
    for file_name in os.listdir(src_folder):
        if any(file_name.lower().endswith(ext) for ext in file_extensions):
            src_path = os.path.join(src_folder, file_name)
            dest_path = os.path.join(dest_folder, file_name)
            shutil.move(src_path, dest_path)
            print(f'Moved: {src_path} -> {dest_path}')

# 파일 확장자별 이동
move_files(download_folder, ['.jpg', '.jpeg'], images_folder)
move_files(download_folder, ['.csv', '.xlsx'], data_folder)
move_files(download_folder, ['.txt', '.doc', '.pdf'], docs_folder)
move_files(download_folder, ['.zip'], archive_folder)
