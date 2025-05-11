import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def load_and_preprocess(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Could not load image: {image_path}")
    img = cv2.resize(img, (128, 128))
    return img

def perform_svd(img):
    U, S, VT = np.linalg.svd(img, full_matrices=False)
    return U, S, VT

def analyze_spectrum(S):
    drop_ratio = S[0] / S[-1]
    if drop_ratio < 100:
        verdict = "⚠️ Potential deepfake detected"
    else:
        verdict = "✅ Likely authentic"
    return drop_ratio, verdict

def plot_spectrum(S, title, save_path=None):
    plt.figure(figsize=(8, 4))
    plt.plot(S, 'bo-', linewidth=2)
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Singular Value Magnitude")
    plt.grid(True)
    if save_path:
        plt.savefig(save_path)
    plt.show()

def main():
    # Change the file name here as needed
    image_file = 'images/real_face.jpg'  # or 'images/deepfake_face.jpg'
    img = load_and_preprocess(image_file)
    U, S, VT = perform_svd(img)
    drop_ratio, verdict = analyze_spectrum(S)

    print(f"Image: {image_file}")
    print(f"Drop Ratio: {drop_ratio:.2f}")
    print(f"Verdict: {verdict}")

    # Optional: Save the plot to output folder
    os.makedirs("output", exist_ok=True)
    save_path = f"output/singular_values_plot_{os.path.basename(image_file).split('.')[0]}.png"
    plot_spectrum(S, f"Singular Values Spectrum: {os.path.basename(image_file)}", save_path)

if __name__ == "__main__":
    main()

