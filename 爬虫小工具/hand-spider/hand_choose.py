import cv2
import mediapipe as mp
import os
import time
import shutil


def detect_hand_in_image(image_path):
    """
    检测单张图片中是否存在一只手

    :param image_path: 图片的路径
    :return: 若检测到一只手返回 True，否则返回 False
    """
    # 初始化手部检测模块，设置检测置信度和跟踪置信度
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=1,
        min_detection_confidence=0.4,
        min_tracking_confidence=0.4
    )

    # 读取图片
    image = cv2.imread(image_path)
    if image is None:
        return False

    # 将图片转换为RGB格式
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 进行手部检测
    results = hands.process(image_rgb)

    # 判断是否检测到一只手
    has_one_hand = results.multi_hand_landmarks and len(results.multi_hand_landmarks) == 1

    # 释放资源
    hands.close()
    return has_one_hand


def check_images_in_folder(folder_path, output_folder, start_index, sleep_time=0.2):
    hand_detected_count = 0
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            if detect_hand_in_image(image_path):
                file_ext = os.path.splitext(filename)[1]
                new_filename = f"n_c_{start_index}{file_ext}"
                shutil.copy2(image_path, os.path.join(output_folder, new_filename))
                start_index += 1
                hand_detected_count += 1
            time.sleep(sleep_time)
    return hand_detected_count, start_index


if __name__ == "__main__":
    total_count = 0
    output_folder = "newdatas"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    current_index = 1
    for i in range(1, 6):
        folder_path = f"downloaded_images{i}"
        if os.path.exists(folder_path):
            count, current_index = check_images_in_folder(folder_path, output_folder, current_index)
            total_count += count

    print(f"新文件夹写入了 {total_count} 张图片。")