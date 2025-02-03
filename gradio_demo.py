import gradio as gr
import torch
from torchvision import models, transforms
from torchvision.models import ResNet18_Weights
from PIL import Image
import json
import requests

# Load a pre-trained ResNet model using the new 'weights' parameter
weights = ResNet18_Weights.DEFAULT
model = models.resnet18(weights=weights)
model.eval()

# Define the image transformation
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=weights.transforms().mean, std=weights.transforms().std),
])

# Load ImageNet class labels
LABELS_URL = "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json"
response = requests.get(LABELS_URL)
class_labels = response.json()

# Define a function to process the image and make a prediction
def predict(image):
    image = transform(image).unsqueeze(0)  # Add batch dimension
    with torch.no_grad():
        outputs = model(image)
    _, predicted = torch.max(outputs, 1)
    class_index = predicted.item()
    class_name = class_labels[class_index]
    return f"Predicted class: {class_name}"

# Create a Gradio interface
iface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=gr.Textbox(),
    title="Image Classification with ResNet",
    description="Upload an image to get a prediction from a pre-trained ResNet model."
)

# Launch the interface
if __name__ == "__main__":
    iface.launch() 