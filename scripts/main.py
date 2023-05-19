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
	for extension in extensions.active():
		if "controlnet" in extension.name:
			currentElement = kwargs.get("elem_id")
			if currentElement == "extras_tab" and tabId in ["img2img_gallery", "txt2img_gallery"]:
				with gr.Column():
					with gr.Row():
						if tabId == "txt2img_gallery":
							#controlNetUnitTx = gr.Dropdown([str(i) for i in range(controlNetMaxUnits)], label="Send to ControlNet Unit #", value="0", interactive=True, visible=(controlNetMaxUnits > 1))
							controlNetUnitTx = 1
							controlNetButtonTxToTx = gr.Button(value="Send to ControlNet", elem_id="sendto_controlnet_button_tx_to_tx")
							controlNetButtonTxToTx.click(None, controlNetUnitTx, None, _js="(i) => {sendImageToControlNet('txt2img', 'txt2img', i)}")
							controlNetButtonTxToIm = gr.Button(value="Send to img2img ControlNet", elem_id="sendto_controlnet_button_tx_to_im")
							controlNetButtonTxToIm.click(None, controlNetUnitTx, None, _js="(i) => {sendImageToControlNet('txt2img', 'img2img', i)}")
						elif tabId == "img2img_gallery":
							#controlNetUnitIm = gr.Dropdown([str(i) for i in range(controlNetMaxUnits)], label="Send to ControlNet Unit #", value="0", interactive=True, visible=(controlNetMaxUnits > 1))
							controlNetUnitIm = 1
							controlNetButtonImToIm = gr.Button(value="Send to ControlNet", elem_id="sendto_controlnet_button_im_to_im")
							controlNetButtonImToIm.click(None, controlNetUnitIm, None, _js="(i) => {sendImageToControlNet('img2img', 'img2img', i)}")
							controlNetButtonImToTx = gr.Button(value="Send to txt2img ControlNet", elem_id="sendto_controlnet_button_im_to_tx")
							controlNetButtonImToTx.click(None, controlNetUnitIm, None, _js="(i) => {sendImageToControlNet('img2img', 'txt2img', i)}")
				tabId = ""
			elif currentElement in ["img2img_gallery", "txt2img_gallery"]:
				tabId = currentElement
tabId = ""
script_callbacks.on_after_component(on_after_component)
