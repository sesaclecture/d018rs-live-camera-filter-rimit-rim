import cv2
import numpy as np


class Filters:
    # TODO: Image kernels
    Kernels = {
        "Original": np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=np.float32),
        "Blur": np.array([[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]], dtype=np.float32),
        "Gaussian blur": np.array([[1/16, 2/16, 1/16], [2/16, 4/16, 2/16], [1/16, 2/16, 1/16]], dtype=np.float32),
        "Sharpen": np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32),
        "Sobel (x)": np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32),
        "Sobel (y)": np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float32),
        "Edge detection": np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]], dtype=np.float32),
        "Emboss": np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]], dtype=np.float32)
    }

    def __init__(self, kernels=Kernels):
        self.kernels = kernels
        # TODO: Implement internal variables
        self.filter_names = list(self.kernels.keys())   # 필터 이름 리스트
        self.current_index = 0                         # 현재 선택된 필터 인덱스

    def apply_filter(self, frame, filter_name) -> np.array:
        # TODO: Apply the selected filter kernel to the frame
        if filter_name is None:
            filter_name = self.get_current_filter_name()
        kernel = self.kernels[filter_name]
        return cv2.filter2D(frame, -1, kernel)

    def get_current_filter_name(self) -> str:
        # TODO: Return currently set kernels's name
        return self.filter_names[self.current_index]

    def switch_next_filter(self):
        # TODO: Update currently selected kernel to the next
        self.current_index = (self.current_index + 1) % len(self.filter_names)

    def switch_previous_filter(self):
        # TODO: Update currently selected kernel to the previous
        self.current_index = (self.current_index - 1) % len(self.filter_names)
