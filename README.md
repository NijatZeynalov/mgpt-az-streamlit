# Azerbaijani Text Generation with mGPT-XL (Streamlit app)


This project is a Streamlit app that uses the mGPT-XL (1.3B) model to generate Azerbaijani text. Users can input partial text, and the model will complete it with contextually relevant text in Azerbaijani.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Dockerization](#dockerization)
- [License](#license)

---

## Installation

To run the Streamlit app locally, you need to set up a Python environment and install the required dependencies. Follow these steps:

1. **Clone the repository** to your local machine:

   ```bash
   git clone https://github.com/NijatZeynalov/mgpt-az-streamlit.git
   cd mgpt-az-streamlit
   ```
2. **Install the project dependencies:**

   ```python
   pip install -r requirements.txt
   ```

## Usage
Once you have set up the environment, you can run the Streamlit app:

```bash
streamlit run main.py
```

The app will be accessible in your web browser at http://localhost:8501. You can enter partial text in the provided input field and click the "Tamamla" (Complete) button to generate text.


## Dockerization

This project includes a Dockerfile for containerizing the Streamlit app. Follow these steps to build and run the Docker container:

1. Build the Docker image:
   
```bash
docker build --no-cache -t streamlit-az-text .
```

2. Run the Docker container (mapping port 8501 to the host):
   
```bash
docker run -p 8501:8501 streamlit-az-text
```

## Demo

You can see a demo of how the app works below:

![Demo](https://github.com/NijatZeynalov/mgpt-az-streamlit/assets/31247506/745d994e-179f-4680-9c40-abc73f0cf2ce)

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Project Details

I've utilized the impressive mGPT-1.3B model, which is available through the Hugging Face model hub.

- Model: [mGPT-1.3B for Azerbaijani](https://huggingface.co/ai-forever/mGPT-1.3B-azerbaijan)

Using open-source models not only accelerates innovation but also fosters collaboration within the AI community. We're grateful for the contributions of the Hugging Face community and the accessibility of this model, which has enriched our project.

Feel free to explore the model's capabilities and contribute to its ongoing development!

