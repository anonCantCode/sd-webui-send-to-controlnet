from modules import extensions
import modules.scripts as scripts
import gradio as gr


class Script(scripts.Script):
	def title(self):
		return "SendToControlNet"

	def show(self, is_img2img):
		return scripts.AlwaysVisible

def on_after_component(component, **kwargs):
	for extension in extensions.active():
		if "controlnet" in extension.name:
			element = kwargs.get("elem_id")
			if element == "txt2img_gallery":
				with gr.Column():
					controlNetButtonTxToTx = gr.Button(value="Send to ControlNet #0", elem_id="sendto_controlnet_button_tx_to_tx")
					controlNetButtonTxToTx.click(fn=None, _js="(i) => {sendImageToControlNet('txt2img', 'txt2img', 0)}")
					controlNetButtonTxToIm = gr.Button(value="Send to img2img ControlNet #0", elem_id="sendto_controlnet_button_tx_to_im")
					controlNetButtonTxToIm.click(fn=None, _js="(i) => {sendImageToControlNet('txt2img', 'img2img', 0)}")
			elif element == "img2img_gallery":
				with gr.Column():
					controlNetButtonImToIm = gr.Button(value="Send to ControlNet #0", elem_id="sendto_controlnet_button_im_to_im")
					controlNetButtonImToIm.click(fn=None, _js="(i) => {sendImageToControlNet('img2img', 'img2img', 0)}")
					controlNetButtonImToTx = gr.Button(value="Send to txt2img ControlNet #0", elem_id="sendto_controlnet_button_im_to_tx")
					controlNetButtonImToTx.click(fn=None, _js="(i) => {sendImageToControlNet('img2img', 'txt2img', 0)}")
script_callbacks.on_after_component(on_after_component)
