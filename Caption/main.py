from PIL import Image
import requests
import torch
from torchvision import transforms
from torchvision.transforms.functional import InterpolationMode

from models.blip import blip_decoder
from fastapi import FastAPI, File, UploadFile

import os.path
fname = 'models/model_base_capfilt_large.pth'
model_url = fname if os.path.isfile(fname) else\
	 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/models/model_base_capfilt_large.pth'

app = FastAPI()

device = 'cpu'
image_size = 384
print("Loading model...")
# model_url = 'models/model_base_capfilt_large.pth'
# model_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/models/model_base_capfilt_large.pth'
model = blip_decoder(pretrained=model_url, image_size=image_size, vit='base')
model.eval()
model = model.to(device)
print("Model Loaded")


# def load_image_from_url(img, image_size, device):
# 	raw_image = Image.open(requests.get(img, stream=True).raw).convert('RGB')   

# 	w,h = raw_image.size
# 	# display(raw_image.resize((w//5,h//5)))

# 	transform = transforms.Compose([
# 		transforms.Resize((image_size,image_size),interpolation=InterpolationMode.BICUBIC),
# 		transforms.ToTensor(),
# 		transforms.Normalize((0.48145466, 0.4578275, 0.40821073), (0.26862954, 0.26130258, 0.27577711))
# 		])
# 	image = transform(raw_image).unsqueeze(0).to(device)
# 	return image

def load_image(img, image_size, device):
	raw_image = Image.open(img).convert('RGB')   

	w,h = raw_image.size
	# display(raw_image.resize((w//5,h//5)))

	transform = transforms.Compose([
		transforms.Resize((image_size,image_size),interpolation=InterpolationMode.BICUBIC),
		transforms.ToTensor(),
		transforms.Normalize((0.48145466, 0.4578275, 0.40821073), (0.26862954, 0.26130258, 0.27577711))
		])
	image = transform(raw_image).unsqueeze(0).to(device)
	return image

@app.get('/')
def main():
	return {'response': 'ok'}


@app.post('/image_captioning')
def exec_image_captioning(img: UploadFile):
	# img_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg'
	# print(img)
	try:
		contents = img.file
		# image = load_image_from_url(img, image_size, device)
		image = load_image(contents, image_size, device)
		with torch.no_grad():
			# beam search
			caption = model.generate(image, sample=False, num_beams=3, max_length=20, min_length=5) 
			# nucleus sampling
			# caption = model.generate(image, sample=True, top_p=0.9, max_length=20, min_length=5) 
			return {'caption': caption[0]}
	except Exception as e:
		print(e)
		return {'Error': e}


# if __name__ == '__main__':
#     model_url = 'models/model_base_capfilt_large.pth'
#     model = blip_decoder(pretrained=model_url, image_size=image_size, vit='base')
#     model.eval()
#     model = model.to(device)
#     uvicorn.run(app, host='0.0.0.0', port='8080')