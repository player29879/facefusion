from typing import Literal, Dict, Any
import gradio

Component = gradio.File or gradio.Image or gradio.Video or gradio.Slider
ComponentName = Literal\
[
	'source_file',
	'target_file',
	'preview_frame_slider',
	'face_recognition_dropdown',
	'reference_face_position_gallery',
	'reference_face_distance_slider',
	'face_analyser_direction_dropdown',
	'face_analyser_age_dropdown',
	'face_analyser_gender_dropdown',
	'frame_processors_checkbox_group'
]
Update = Dict[Any, Any]
