async function waitForWebUiUpdate(divToWatch) {
	const promise = new Promise((resolve, reject) => {
		const iframes = divToWatch.querySelectorAll("iframe");
		if (iframes.length > 0) {
			resolve();
			return;
		}
		const mutationConfig = { attributes: true, childList: true, subtree: true };
		const onMutationHappened = (mutationList, observer) => {
			observer.disconnect();
			resolve();
		};
		const observer = new MutationObserver(onMutationHappened);
		observer.observe(divToWatch, mutationConfig);
	});
	return await promise;
}

async function setImageOnInput(imageInput, img) {
	const response = await fetch(img);
	const blob = await response.blob();
	const file = new File([blob], "image.png", { type: "image/png" });
	const dt = new DataTransfer();
	dt.items.add(file);
	const list = dt.files;
	imageInput.files = list;
	const event = new Event("change", {
		"bubbles": true,
		"composed": true
	});
	imageInput.dispatchEvent(event);
}

function sendImageToControlNet(from_tab, to_tab, control_units) {
	let gallery = txt2img_gallery;
	let tabId = "#txt2img_script_container";
	if (from_tab === "img2img") {
		gallery = img2img_gallery;
	}
	if (to_tab === "img2img") {
		tabId = "#img2img_script_container";
	}
	const img = gallery.querySelectorAll("img")[0].src;
	const controlNetDiv = gradioApp().querySelector(tabId).querySelector("#controlnet");
	var iframes = controlNetDiv.querySelectorAll("iframe");
	if (iframes.length == 0) {
		controlNetDiv.querySelector("span.icon").click();
	}
	for (var i = 0; i < control_units.length; i++) {
		control_unit = Number(control_units[i])
		imageInput = controlNetDiv.querySelectorAll("input[type='file']")[0 + control_unit * 2];
		setImageOnInput(imageInput, img);
	}

	// waitForWebUiUpdate(controlNetDiv).then(() => {
	// 	const tabs = controlNetDiv.querySelectorAll("div.tab-nav > button");
	// 	const buttons = controlNetDiv.querySelectorAll("button[aria-label='Clear']");
	// 	for (var i = 0; i < control_units.length; i++) {
	// 		control_unit = Number(control_units[i])
	// 		if(tabs !== null && tabs.length > control_unit) {
	// 			tabs[control_unit].click();
	// 		}
	// 		if(buttons !== null && buttons.length > control_unit) {
	// 			buttons[control_unit].click();
	// 		}
	// 	}
	// }, 1000);
}