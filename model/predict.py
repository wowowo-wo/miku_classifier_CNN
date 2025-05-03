import torch
from torchvision import transforms
from PIL import Image
from model.architecture import ResNet50

def load_model(path='model/resnet50_miku.pth'):
    state_dict = torch.load(path,map_location=torch.device('cpu'))
    new_state_dict = {}
    for k, v in state_dict.items():
        new_state_dict['model.' + k] = v

    model=ResNet50()
    model.load_state_dict(new_state_dict)
    model.eval()
    return model

def predict(model, image: Image.Image):
    try:
        transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
        ])
        input_tensor = transform(image).unsqueeze(0)

        with torch.no_grad():
            output = model(input_tensor)
            probs = torch.softmax(output, dim=1) 
            pred = torch.argmax(probs, dim=1).item()
            confidence = probs[0, pred].item() 

        return pred, confidence
    
    except Exception as e:
        print(f"Error: {e}")
        return None, None