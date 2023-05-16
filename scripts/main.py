from modules import extensions
import modules.scripts as scripts
import gradio as gr


class Script(scripts.Script):
	def __init__(self) -> None:
		super().__init__()

	def title(self):
		return "SendToControlNet"

	def show(self, is_img2img):
		return scripts.AlwaysVisible

	def ui(self, is_img2img):
		for extension in extensions.active():
			if "controlnet" in extension.name:
				controlNetButtonTxToTx = gr.Button(value="Send to ControlNet #0 (txt2img -> txt2img)", elem_id="sendto_controlnet_button_tx_to_tx")
				controlNetButtonTxToTx.click(fn=None, _js="(i) => {sendImageToControlNet('txt2img', 'txt2img', 0)}")
				controlNetButtonImToIm = gr.Button(value="Send to ControlNet #0 (img2img -> img2img)", elem_id="sendto_controlnet_button_im_to_im")
				controlNetButtonImToIm.click(fn=None, _js="(i) => {sendImageToControlNet('img2img', 'img2img', 0)}")
				controlNetButtonTxToIm = gr.Button(value="Send to ControlNet #0 (txt2img -> img2img)", elem_id="sendto_controlnet_button_tx_to_im")
				controlNetButtonTxToIm.click(fn=None, _js="(i) => {sendImageToControlNet('txt2img', 'img2img', 0)}")
				controlNetButtonImToTx = gr.Button(value="Send to ControlNet #0 (img2img -> txt2img)", elem_id="sendto_controlnet_button_im_to_tx")
				controlNetButtonImToTx.click(fn=None, _js="(i) => {sendImageToControlNet('img2img', 'txt2img', 0)}")
				return [controlNetButtonTxToTx, controlNetButtonImToIm, controlNetButtonTxToIm, controlNetButtonImToTx]
