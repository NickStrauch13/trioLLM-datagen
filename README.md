[![CI](https://github.com/NickStrauch13/trioLLM-datagen/actions/workflows/python-ci.yml/badge.svg)](https://github.com/NickStrauch13/trioLLM-datagen/actions/workflows/python-ci.yml)
[![CD](https://github.com/NickStrauch13/trioLLM-datagen/actions/workflows/docker-image.yml/badge.svg)](https://github.com/NickStrauch13/trioLLM-datagen/actions/workflows/docker-image.yml)

# TrioLLM

## Project Overview

TrioLLM is a synthetic data generator composed of three LLMs: an Actor, a Critic, and a Regenerator. The purpose of this project is to provide a time-efficient alternative to manually creating or collecting datasets by automating the data generation process using language models.

## Project Purpose

The goal of TrioLLM is to streamline the creation of synthetic datasets, which can be particularly useful in scenarios where collecting real data is challenging or time-consuming. Generating synthetic data using a single LLM can result in highly repetitive and generic datasets. This naive approach often lacks variety and fails to protect against hallucinations or straying from the original topic. By leveraging the capabilities of multiple language models in a structured pipeline, TrioLLM greatly increases the likelihood that the generated data is both diverse and high-quality.

### Components

- **Actor:** Generates the first version of the data sample. The Actor's temperature is set high to encourage variety in the generated samples.
- **Critic:** Evaluates the Actor's output and provides constructive criticism. The Critic has a lower temperature to minimize factual inaccuracies and off-topic remarks.
- **Regenerator:** Takes the original input, the Actor's generated sample, and the Critic's critique to produce an improved final data sample. The Regenerator also has a lower temperature to ensure quality and relevance.

![TrioLLM Diagram](https://private-user-images.githubusercontent.com/61529274/355290122-5f738891-bb05-4cbb-a024-ad95bd05ab13.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjI5MTEzNDYsIm5iZiI6MTcyMjkxMTA0NiwicGF0aCI6Ii82MTUyOTI3NC8zNTUyOTAxMjItNWY3Mzg4OTEtYmIwNS00Y2JiLWEwMjQtYWQ5NWJkMDVhYjEzLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA4MDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwODA2VDAyMjQwNlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPThlMTgwMDhkZjVlZmJlOThhYWI1YTQ2OWJiOTUxN2Y3YmMzZmZkNzVjMjkwYmYxYjMwODdjZWU0Njk4ZGM3MTUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.XAnBu6tE4YzDnKZkTKbzRJquyNPZ1mMaFuLtGgS1n6Q)

### Workflow

1. The Actor generates the initial data sample.
2. The Critic evaluates the sample and provides feedback.
3. The Regenerator improves the sample based on the Critic's feedback.
4. Steps 1-3 are repeated N times to generate a synthetic dataset.
5. The final dataset is outputted to a CSV file.

### Model Selection

Mistral 7B Instruct was chosen for this project due to its balance of performance and resource efficiency. Specifically, this model offers several advantages:

- High Performance: Mistral 7B Instruct is designed to deliver robust performance for a wide range of natural language processing tasks, including text generation and critique, which are essential for the TrioLLM system.
- Instruction Following: The instruct variant of the model is fine-tuned to follow user instructions accurately, making it well-suited for the structured pipeline of the Actor, Critic, and Regenerator components in TrioLLM.
- Resource Efficiency: While providing high performance, Mistral 7B is not as resource-intensive as larger models, making it feasible to run on local hardware without requiring extensive computational resources.

### Why Run Models Locally?

- Data Privacy: By processing all data locally, we ensure that sensitive information remains secure and is not exposed to external servers or cloud environments. This is particularly important for data generation tasks involving proprietary or sensitive data.
- Cost Efficiency: Avoiding cloud-based model inference can lead to substantial cost savings, especially when dealing with large volumes of data or requiring frequent model interactions.
- Customization and Control: Running models locally provides greater control over the entire pipeline, allowing for easy customization, troubleshooting, and optimization without depending on third-party services or infrastructure.

### Flask Application

A Flask app is provided for user interaction. Users can specify:

- The number of samples to generate
- Few-shot examples (if any)
- The dataset topic

The models run locally using Llamafile and must operate sequentially, which introduces significant latency. However, this method offers a significant advantage in terms of automating the dataset creation process.

## Repository Structure

```
├── .devcontainer/
|  ├── devcontainer.json
|  └── Dockerfile
|
├── .github/
│ └── workflows/
|   ├── ci.yml
│   └── cd.yml
│
├── src/
│   ├── backend/
│   │   ├── actor.py
│   │   ├── critic.py
│   │   ├── regenerator.py
|   |   ├── base_model.py
|   |   ├── llm_trio.py
|   |   ├── prompts.py
|   |   └── requirements.txt
│   ├── webapp/
│   │   ├── static/
│   │   ├── templates/
│   │   ├── app.py
│   │   └── requirements.txt
│
├── tests/
│   ├── test_app.py
│   ├── test_models.py
│   └── test_prompts.py
|
├── .dockerignore
├── .gitignore
├── Dockerfile
├── Makefile
├── .gitignore
├── requirements.txt
└── README.md
```

## Getting Started

To get started with TrioLLM, follow these steps:

1. **Download the Mistral-7B-Instruct Llamafile**

   Download the Llamafile [here](https://huggingface.co/Mozilla/Mistral-7B-Instruct-v0.2-llamafile/resolve/main/mistral-7b-instruct-v0.2.Q4_0.llamafile?download=true)

   For more information on Llamafile, visit the [Llamafile repository](https://github.com/Mozilla-Ocho/llamafile)

2. **LLamafile setup**

   For macOS or Linux, you must grant permission for your computer to execute this new file.

   ```bash
   chmod +x mistral-7b-instruct-v0.2.Q4_0.llamafile
   ```

   For Windows, add `.exe` to the end of the file name.

3. **Run the Llamafile**

   ```bash
   ./mistral-7b-instruct-v0.2.Q4_0.llamafile
   ```

   A Llamafile chat interface will open in a browser window, but you can ignore this.

4. **Clone the TrioLLM repository:**

   ```bash
   git clone git@github.com:NickStrauch13/trioLLM-datagen.git
   ```

5. **Create and activate a Python virtual environment:**

   ```bash
   python -m venv venv
   ```

   ```bash
   source venv/bin/activate
   ```

   or

   ```bash
   ./venv/Scripts/activate
   ```

6. **Install dependencies:**

   ```bash
   make install
   ```

   or

   ```bash
   pip install -r requirements.txt
   ```

7. **Run the Flask app:**

   ```bash
   python run.py
   ```

8. **Interact with the app:**
   Open your web browser and navigate to `http://127.0.0.1:5000/` to interact with the TrioLLM interface.

## Usage

1. Specify the number of samples you want to generate.
2. Provide any few-shot examples to guide the data generation process.
3. Define the dataset topic.
4. Click "Generate" and wait for the process to complete.
5. Download the generated dataset in CSV format.

![Webapp](https://private-user-images.githubusercontent.com/61529274/355601985-f79f56e3-b2ba-4ce6-a22f-909ae1db21fa.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjI5Nzg1NDEsIm5iZiI6MTcyMjk3ODI0MSwicGF0aCI6Ii82MTUyOTI3NC8zNTU2MDE5ODUtZjc5ZjU2ZTMtYjJiYS00Y2U2LWEyMmYtOTA5YWUxZGIyMWZhLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA4MDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwODA2VDIxMDQwMVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTI2YWE5OGJiNGMwM2E5NzIxMzM1Y2NmNmMyNzUwYTczN2ViNWViMjYyYzE5YWFkZTI4YmY3ZmE0ZjY0MmU3MGYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.WaaV3C0md-oO5ZUUIG-NWKr_MGElj9-1opx_M-iYNyA)

## Testing, Linting, and Formatting

- To run the provided tests, execute the following command:

  ```bash
  make test
  ```

- To run the linter, execute the following command:

  ```bash
  make lint
  ```

- To format the code, execute the following command:

  ```bash
  make format
  ```

## Inspiration

Inspired by [HelixNet](https://huggingface.co/migtissera/HelixNet)
