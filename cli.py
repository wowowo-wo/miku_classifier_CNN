import sys
import argparse
from model.predict import load_model, predict
from utils.download import download_image
from utils.display import show_image_from_url

def main():
    parser = argparse.ArgumentParser(description='hatsune miku detection CLI')
    parser.add_argument('url', type=str, help='URL of image')
    args = parser.parse_args()

    show_image_from_url(args.url)
    model = load_model()
    image = download_image(args.url)
    pred, conf = predict(model, image)

    if pred is None:
        print("Prediction failed.", file=sys.stderr)
        sys.exit(255)
    elif pred != 0:
        label = "Miku isn't in a picture."
        print(f"{label} (Confidence: {conf:.2f})", file=sys.stderr)
        sys.exit(1)
    else:
        label = "Miku is in a picture!"
        print(f"{label} (Confidence: {conf:.2f})")

if __name__ == '__main__':
    main()
