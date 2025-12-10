import cv2
import mediapipe as mp
import numpy as np


def detect_nail_polish(image_path):
    # 初始化手部检测模块
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
        print(f"无法读取图片 {image_path}，请检查图片路径。")
        return False

    # 复制一份原始图像用于绘制标注
    annotated_image = image.copy()

    # 将图片转换为 RGB 格式
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 进行手部检测
    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        # 获取手部关键点
        hand_landmarks = results.multi_hand_landmarks[0]
        h, w, _ = image.shape

        # 定义手指甲相关的关键点索引
        nail_landmark_indices = [
            (4, 3, 2),  # 拇指
            (8, 6, 5),  # 食指
            (12, 10, 9),  # 中指
            (16, 14, 13),  # 无名指
            (20, 18, 17)  # 小指
        ]

        for tip_index, base_index, side_index in nail_landmark_indices:
            # 获取手指甲末端、基部和侧面的关键点坐标
            tip_point = hand_landmarks.landmark[tip_index]
            base_point = hand_landmarks.landmark[base_index]
            side_point = hand_landmarks.landmark[side_index]
            tip_x, tip_y = int(tip_point.x * w), int(tip_point.y * h)
            base_x, base_y = int(base_point.x * w), int(base_point.y * h)
            side_x, side_y = int(side_point.x * w), int(side_point.y * h)

            # 更精确地提取手指甲区域
            dx = abs(side_x - base_x)
            roi_x1 = max(0, min(tip_x, base_x) - dx // 2)
            roi_x2 = min(w, max(tip_x, base_x) + dx // 2)
            roi_y1 = max(0, min(tip_y, base_y))
            roi_y2 = min(h, max(tip_y, base_y))
            nail_area = image[roi_y1:roi_y2, roi_x1:roi_x2]

            if nail_area.size > 0:
                # 提取手部其他区域作为参考（这里简单取手掌部分）
                palm_point = hand_landmarks.landmark[0]
                palm_x, palm_y = int(palm_point.x * w), int(palm_point.y * h)
                palm_area = image[
                            max(0, palm_y - 20):min(h, palm_y + 20),
                            max(0, palm_x - 20):min(w, palm_x + 20)
                            ]

                if palm_area.size > 0:
                    # 计算手指甲区域和手掌区域的颜色直方图
                    nail_hist = cv2.calcHist([nail_area], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
                    palm_hist = cv2.calcHist([palm_area], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
                    nail_hist = cv2.normalize(nail_hist, nail_hist).flatten()
                    palm_hist = cv2.normalize(palm_hist, palm_hist).flatten()

                    # 计算颜色直方图的差异
                    hist_diff = cv2.compareHist(nail_hist, palm_hist, cv2.HISTCMP_CHISQR)

                    # 动态调整阈值
                    image_mean_color = np.mean(image, axis=(0, 1))
                    std_dev = np.std(image, axis=(0, 1))
                    threshold = 50 + np.mean(std_dev) * 0.5

                    # 判断是否有美甲
                    if hist_diff > threshold:
                        # 在标注图像上绘制矩形框标记美甲区域
                        cv2.rectangle(annotated_image, (roi_x1, roi_y1), (roi_x2, roi_y2), (0, 255, 0), 2)
                        hands.close()
                        cv2.imshow('Annotated Image', annotated_image)
                        cv2.waitKey(0)
                        cv2.destroyAllWindows()
                        return True

    hands.close()
    return False


if __name__ == "__main__":
    image_path = "newdatas/n_c_5465.jpg"
    has_nail_polish = detect_nail_polish(image_path)
    if has_nail_polish:
        print("图片中检测到美甲。")
    else:
        print("图片中未检测到美甲。")
    