import cv2
import mediapipe as mp
import numpy as np
import os
import shutil


def detect_nail_polish(hand_area, roi):
    """
    检测指甲是否有美甲
    :param hand_area: 手部整体区域
    :param roi: 指甲区域
    :return: 是否有美甲
    """
    # 计算手部整体颜色均值
    hand_mean_color = cv2.mean(hand_area)[0:3]
    # 计算指甲区域颜色均值
    nail_mean_color = cv2.mean(roi)[0:3]
    # 计算颜色差异
    color_diff = np.linalg.norm(np.array(hand_mean_color) - np.array(nail_mean_color))
    # 设置一个阈值来判断是否有美甲
    threshold = 30
    return color_diff > threshold


def check_nail_image(image_path, max_num_hands=2, min_detection_confidence=0.4, white_threshold=0.3):
    # 初始化MediaPipe手部检测模型
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=max_num_hands,
        min_detection_confidence=min_detection_confidence
    )
    mp_drawing = mp.solutions.drawing_utils

    # 读取图像
    try:
        image = cv2.imread(image_path)
        if image is None:
            print("无法读取图像，请检查图像路径。")
            return False
    except Exception as e:
        print(f"读取图像时出现错误: {e}")
        return False

    # 转换图像颜色空间
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 进行手部检测
    try:
        results = hands.process(image)
    except Exception as e:
        print(f"手部检测时出现错误: {e}")
        return False

    # 将图像颜色空间转换回BGR
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    nail_polish_count = 0  # 用于统计有美甲的指甲数量

    if results.multi_hand_landmarks:
        hand_count = len(results.multi_hand_landmarks)
        if hand_count > max_num_hands:
            print("手过多")
            return False
        for hand_landmarks in results.multi_hand_landmarks:
            # 绘制手部关键点和连接线
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            # 获取手部整体区域
            hand_points = []
            for landmark in hand_landmarks.landmark:
                x, y = int(landmark.x * image.shape[1]), int(landmark.y * image.shape[0])
                hand_points.append((x, y))
            hand_points = np.array(hand_points, dtype=np.int32)
            mask = np.zeros(image.shape[:2], dtype=np.uint8)
            cv2.fillPoly(mask, [hand_points], 255)
            hand_area = cv2.bitwise_and(image, image, mask=mask)

            # 获取手指甲区域
            finger_tip_ids = [mp_hands.HandLandmark.THUMB_TIP, mp_hands.HandLandmark.INDEX_FINGER_TIP,
                              mp_hands.HandLandmark.MIDDLE_FINGER_TIP, mp_hands.HandLandmark.RING_FINGER_TIP,
                              mp_hands.HandLandmark.PINKY_TIP]
            for tip_id in finger_tip_ids:
                tip = hand_landmarks.landmark[tip_id]
                x, y = int(tip.x * image.shape[1]), int(tip.y * image.shape[0])
                # 定义一个稍大的矩形区域作为手指甲区域
                roi = image[max(0, y - 20):min(image.shape[0], y + 20), max(0, x - 20):min(image.shape[1], x + 20)]
                if roi.size > 0:
                    # 转换为灰度图
                    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
                    # 二值化处理
                    _, binary_roi = cv2.threshold(gray_roi, 200, 255, cv2.THRESH_BINARY)
                    # 计算白色区域占比
                    white_ratio = np.sum(binary_roi == 255) / binary_roi.size
                    if white_ratio < white_threshold:  # 如果白色区域占比小于阈值，忽略白色区域
                        if detect_nail_polish(hand_area, roi):
                            nail_polish_count += 1
    else:
        print("未检测到手部。")
        return False

    if nail_polish_count <= 1 and results.multi_hand_landmarks:
        print("合格的手指甲图片")
        return True
    elif nail_polish_count > 0:
        print(f"检测到 {nail_polish_count} 个有美甲的指甲。")
        return False


if __name__ == "__main__":
    folder_path = 'downloaded_images1'  # 请替换为实际的文件夹路径
    output_folder = 'true_imgs1'

    # 创建输出文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i in range(1, 1001):
        image_name = f'c_{i}'
        image_extensions = ['.jpg', '.jpeg', '.png']
        found = False
        for ext in image_extensions:
            image_path = os.path.join(folder_path, image_name + ext)
            if os.path.exists(image_path):
                is_valid = check_nail_image(image_path)
                if is_valid:
                    new_name = f't_{image_name}{ext}'
                    new_path = os.path.join(output_folder, new_name)
                    shutil.move(image_path, new_path)
                    print(f"已将 {image_name}{ext} 移动到 {new_path}")
                found = True
                break
        if not found:
            print(f"未找到 {image_name} 的图片")