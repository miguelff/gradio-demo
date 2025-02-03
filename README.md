# Gradio Image Classification Demo

This project demonstrates a simple image classification application using a pre-trained ResNet-18 model from the `torchvision` library. The application is built with Gradio, which provides an easy-to-use web interface for machine learning models.

## Features

- Upload an image and get a prediction of its class using a ResNet-18 model.
- The model is pre-trained on the ImageNet dataset, providing predictions with human-readable class labels.

## Requirements

- Anaconda or Miniconda
- Python 3.8

## Setup

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create the Conda environment**:

   Use the provided `environment.yml` file to create the environment:

   ```bash
   conda env create -f environment.yml
   ```

3. **Activate the environment**:

   ```bash
   conda activate gradio-demo
   ```

## Running the Demo

1. **Run the Gradio demo**:

   Use the provided bash script to start the demo:

   ```bash
   ./run_gradio_demo.sh
   ```

   Alternatively, you can run the Python script directly:

   ```bash
   python gradio_demo.py
   ```

2. **Access the Gradio interface**:

   Once the script is running, open your web browser and go to the URL provided in the terminal (usually `http://localhost:7860`).

3. **Upload an image**:

   Use the Gradio interface to upload an image and receive a prediction of its class.

## Notes

- The class labels are fetched from a public GitHub repository and mapped to the model's output indices for human-readable predictions.
- Ensure you have an active internet connection to download the class labels when running the demo for the first time.

## Troubleshooting

- If you encounter a `CondaValueError` about an existing environment, you can remove it with:

  ```bash
  conda env remove -n gradio-demo
  ```

- If you see an `AttributeError` related to Gradio, ensure you have the latest version installed by updating your environment:

  ```bash
  conda env update -f environment.yml
  ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
