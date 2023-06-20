from modules import extensions
from modules import script_callbacks
import modules.scripts as scripts
from modules.shared import opts
import gradio as gr


class Script(scripts.Script):
	def title(self):
		return "SendToControlNet"

	def show(self, is_img2img):
		return scripts.AlwaysVisible

def on_after_component(component, **kwargs):
	global tabId
	controlNetMaxUnits = getattr(opts, 'control_net_max_models_num', 0)
	items = []
	for i in range(0, controlNetMaxUnits):
		items.append(str(i))
	for extension in extensions.active():
		if "controlnet" in extension.name:
			currentElement = kwargs.get("elem_id")
			if currentElement == "extras_tab" and tabId in ["img2img_gallery", "txt2img_gallery"]:
				with gr.Row():
					with gr.Column():
						if tabId == "txt2img_gallery":
							with gr.Row():
								controlNetDropdownTxToTx = gr.Dropdown(choices=items, value=items[0:1], multiselect=True, label="ControlNet Unit t2i", elem_id="sendto_controlnet_dropdown_tx_to_tx")
								controlNetButtonTxToTx = gr.Button(value="Send to ControlNet", elem_id="sendto_controlnet_button_tx_to_tx")
								controlNetButtonTxToTx.click(fn=None, inputs=[controlNetDropdownTxToTx], _js="(i) => {sendImageToControlNet('txt2img', 'txt2img', i)}")
							with gr.Row():
								gr.Dropdown(choices=items, value=items[0:1], multiselect=True, label="ControlNet Unit i2i", elem_id="sendto_controlnet_dropdown_tx_to_im")
								controlNetButtonTxToIm = gr.Button(value="Send to img2img ControlNet", elem_id="sendto_controlnet_button_tx_to_im")
								controlNetButtonTxToIm.click(fn=None, _js="(i) => {sendImageToControlNet('txt2img', 'img2img', 0)}")
						elif tabId == "img2img_gallery":
							with gr.Row():
								gr.Dropdown(choices=items, value=items[0:1], multiselect=True, label="ControlNet Unit t2i", elem_id="sendto_controlnet_dropdown_im_to_im")
								controlNetButtonImToIm = gr.Button(value="Send to ControlNet", elem_id="sendto_controlnet_button_im_to_im")
								controlNetButtonImToIm.click(fn=None, _js="(i) => {sendImageToControlNet('img2img', 'img2img', 0)}")
							with gr.Row():
								gr.Dropdown(choices=items, value=items[0:1], multiselect=True, label="ControlNet Unit i2i", elem_id="sendto_controlnet_dropdown_im_to_tx")
								controlNetButtonImToTx = gr.Button(value="Send to txt2img ControlNet", elem_id="sendto_controlnet_button_im_to_tx")
								controlNetButtonImToTx.click(fn=None, _js="(i) => {sendImageToControlNet('img2img', 'txt2img', 0)}")
					tabId = ""
			elif currentElement in ["img2img_gallery", "txt2img_gallery"]:
				tabId = currentElement
tabId = ""
script_callbacks.on_after_component(on_after_component)
