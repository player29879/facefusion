from typing import Optional
from functools import lru_cache
import cv2

from facefusion.typing import Frame


def get_video_frame(video_path : str, frame_number : int = 0) -> Optional[Frame]:
	if video_path:
		capture = cv2.VideoCapture(video_path)
		if capture.isOpened():
			frame_total = capture.get(cv2.CAP_PROP_FRAME_COUNT)
			capture.set(cv2.CAP_PROP_POS_FRAMES, min(frame_total, frame_number - 1))
			has_frame, frame = capture.read()
			capture.release()
			if has_frame:
				return frame
	return None


def detect_fps(video_path : str) -> Optional[float]:
	if video_path:
		capture = cv2.VideoCapture(video_path)
		if capture.isOpened():
			return capture.get(cv2.CAP_PROP_FPS)
	return None


def count_video_frame_total(video_path : str) -> int:
	if video_path:
		capture = cv2.VideoCapture(video_path)
		if capture.isOpened():
			video_frame_total = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
			capture.release()
			return video_frame_total
	return 0


def normalize_frame_color(frame : Frame) -> Frame:
	return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


def resize_frame_dimension(frame : Frame, max_height : int) -> Frame:
	height, width = frame.shape[:2]
	if height > max_height:
		scale = max_height / height
		max_width = int(width * scale)
		frame = cv2.resize(frame, (max_width, max_height))
	return frame


@lru_cache(maxsize = 128)
def read_static_image(image_path : str) -> Optional[Frame]:
	return read_image(image_path)


def read_image(image_path : str) -> Optional[Frame]:
	if image_path:
		return cv2.imread(image_path)
	return None


def write_image(image_path : str, frame : Frame) -> bool:
	if image_path:
		return cv2.imwrite(image_path, frame)
	return False
