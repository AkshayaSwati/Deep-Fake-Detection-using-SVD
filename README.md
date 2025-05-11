# Deep-Fake-Detection-using-SVD (Singular Value Decomposition)

This project demonstrates a simple and effective method for detecting potential deepfake images using matrix decomposition, specifically Singular Value Decomposition (SVD).

By analyzing the singular value spectrum of grayscale face images, we observe that authentic images typically exhibit a smooth spectral decay, whereas deepfakes often show irregular or unstable patterns — helping us identify manipulated content.

🚀 How to Run
1. Clone the Repository
git clone https://github.com/yourusername/deepfake-svd-demo.git
cd deepfake-svd-demo

3. Install Dependencies
pip install -r requirements.txt

4. Run the Script (Command Line)
python src/svd_detector.py

5. Or Use the Jupyter Notebook
jupyter notebook notebooks/demo_svd_face_analysis.ipynb

🔍 How It Works
Convert the input image to grayscale and resize it.

Apply Singular Value Decomposition (SVD) to decompose the image matrix.

Plot the singular values (S) to visualize decay.

Analyze the drop-off ratio between the largest and smallest singular values:

High drop-off → Likely real

Low drop-off → Possible deepfake

📊 Example Output
Singular value plot of a real face:
Singular value plot of a deepfake:

🛠 Tools & Libraries
Python
OpenCV
NumPy
Matplotlib
Jupyter Notebook (optional for demo)

📚 Reference
This method is inspired by research exploring matrix decomposition techniques in deepfake forensics and image complexity analysis.

🧑‍💻 Author
Created by Akshaya Swati R
Conference Presentation – 2025
