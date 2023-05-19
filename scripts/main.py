from modules import extensions
from modules import script_callbacks
import modules.scripts as scripts
import gradio as gr


class Script(scripts.Script):
	def title(self):
		return "SendToControlNet"

	def show(self, is_img2img):
		return scripts.AlwaysVisible

def on_after_component(component, **kwargs):
	executed = False #prevent multiple buttons
	for extension in extensions.active():
		if "controlnet" in extension.name and not executed:
			element = kwargs.get("elem_id")
			executed = True
			if element == "image_buttons_txt2img":
				with gr.Row():
					controlNetButtonTxToTx = gr.Button(value="Send to ControlNet #0", elem_id="sendto_controlnet_button_tx_to_tx")
					controlNetButtonTxToTx.click(fn=None, _js="(i) => {sendImageToControlNet('txt2img', 'txt2img', 0)}")
					controlNetButtonTxToIm = gr.Button(value="Send to img2img ControlNet #0", elem_id="sendto_controlnet_button_tx_to_im")
					controlNetButtonTxToIm.click(fn=None, _js="(i) => {sendImageToControlNet('txt2img', 'img2img', 0)}")
			elif element == "image_buttons_img2img":
				with gr.Row():
					controlNetButtonImToIm = gr.Button(value="Send to ControlNet #0", elem_id="sendto_controlnet_button_im_to_im")
					controlNetButtonImToIm.click(fn=None, _js="(i) => {sendImageToControlNet('img2img', 'img2img', 0)}")
					controlNetButtonImToTx = gr.Button(value="Send to txt2img ControlNet #0", elem_id="sendto_controlnet_button_im_to_tx")
					controlNetButtonImToTx.click(fn=None, _js="(i) => {sendImageToControlNet('img2img', 'txt2img', 0)}")
script_callbacks.on_after_component(on_after_component)
