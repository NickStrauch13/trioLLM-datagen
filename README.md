[![CI](https://github.com/NickStrauch13/trioLLM-datagen/actions/workflows/python-ci.yml/badge.svg)](https://github.com/NickStrauch13/trioLLM-datagen/actions/workflows/python-ci.yml)
[![CD](https://github.com/NickStrauch13/trioLLM-datagen/actions/workflows/docker-image.yml/badge.svg)](https://github.com/NickStrauch13/trioLLM-datagen/actions/workflows/docker-image.yml)

# TrioLLM

[--> Demo Video <--](https://youtu.be/tO4LxOXT4b4)

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

## Evaluation

I evaluated the LLM Trio by comparing it against GPT-4o. I generated two distinct datasets—Amazon Product Reviews and Call Center Technician Call Transcripts—using both my LLM Trio and GPT-4o, and then conducted a human evaluation of the resulting datasets. My analysis focused on four key factors: Variance (the diversity of the dataset samples), Detail (the richness of information in each sample), Accuracy (the factual correctness of the data samples), and Realism (how believable and pertinent the samples were to the original topic). I scored each factor on a scale from 1 to 10 for both models and averaged the results. The LLM Trio outperformed GPT-4o in terms of Variance and Detail, scoring 9.5 and 10 respectively, but fell short in Accuracy and Realism, scoring 7.5 and 6.5 respectively. I beleive that the high temperature of the Actor contributed to the increased variance in the genreated samples, while the critic did a great job at highlighting areas where more facts could be inserted. However, the LLM Trio fell behind in accuracy likely due to the higher fequency of facts in the samples along with the weaker LLM's pretraining. Additionally, the GPT-4o responses were more realistic, and I belive this is because the Regenerator has the tendency to overcorrect the Actor's samples, which can lead to less realistic responses. Overall, the LLM Trio using a weaker LLM, Mistral-7b-Instruct, was able to produce high quality data samples that outperformed GPT-4o in some regards.

| Model    | Variance | Detail | Accuracy | Realism |
| -------- | -------- | ------ | -------- | ------- |
| LLM Trio | 9.5      | 10     | 7.5      | 6.5     |
| GPT-4o   | 6        | 7.5    | 9        | 8       |

Latency was a significant challenge in evaluating my LLM Trio synthetic data generator. The architecture required three sequential LLM calls, which created a major bottleneck. Additionally, I was running the LLM locally on an NVIDIA GeForce RTX 3050 Ti with only 4GB of memory. Consequently, the LLM Trio took approximately 283 seconds per data sample on average, while GPT-4o was near instantaneous. Although this latency is a crucial factor to consider, the data generation task does not necessarily require immediate results. It can be run overnight or in the background, mitigating the impact of the longer processing time.

_While generating data samples for this comparison, I noticed that the LLM Trio and GPT-4o both happened to generate a review for a pressure cooker. I included these samples below for a direct comparison:_

GPT-4o:

```
I absolutely love this pressure cooker! It has made meal preparation so much faster and easier. The various preset cooking programs are very convenient, and it handles everything from soups to desserts perfectly. The stainless steel inner pot is durable and easy to clean. I appreciate the safety features, such as the lid locking mechanism and pressure release valve. It’s a versatile appliance that has become a staple in my kitchen. Highly recommend it to anyone looking to save time on cooking.
```

LLM Trio:

```
I've had my Instant Pot Duo Plus for about a month now and I couldn't be happier with my purchase. This 7-in-1 electric pressure cooker has revolutionized my cooking experience, saving me at least 2 hours a week by allowing me to cook rice, beans, and even my morning oatmeal in a fraction of the time it used to take in a traditional crockpot. For instance, a single cycle in the Instant Pot cooks 3 cups of rice or 6 cups of beans, saving me significant time and energy compared to the hours-long process in a crockpot. The saute function is also a game changer, allowing me to brown meats and saute vegetables directly in the pot before pressure cooking, eliminating the need for a separate pan. The interface is intuitive and easy to use, with preset buttons for common cooking tasks such as rice, beans, and soup. I highly recommend this product.
```

## Testing, Linting, and Formatting

- To run the provided tests, execute the following command:

  ```bash
  make test
  ```

  ![Make Image](https://private-user-images.githubusercontent.com/61529274/355606786-f998ca5e-7708-44d3-a4e9-1bcb766420bf.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjI5ODA4NTMsIm5iZiI6MTcyMjk4MDU1MywicGF0aCI6Ii82MTUyOTI3NC8zNTU2MDY3ODYtZjk5OGNhNWUtNzcwOC00NGQzLWE0ZTktMWJjYjc2NjQyMGJmLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA4MDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwODA2VDIxNDIzM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTU3YzkyMGRiMTJjZGE5YTQzNzM3YWMzODJiODViZDQ1MTg3NjhhZWVhYzI1NDg5MjZhZWNmNDRiMjAwM2E0YzEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.qszQYMODmcTpOhgtW4u1X9uG5xhd5uK73iqX0asmx9M)

- To run the linter, execute the following command:

  ```bash
  make lint
  ```

  ![Make Lint](https://private-user-images.githubusercontent.com/61529274/355608683-2ccf55bb-6fae-403e-8a7e-8c89a1c02293.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjI5ODA4NTMsIm5iZiI6MTcyMjk4MDU1MywicGF0aCI6Ii82MTUyOTI3NC8zNTU2MDg2ODMtMmNjZjU1YmItNmZhZS00MDNlLThhN2UtOGM4OWExYzAyMjkzLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA4MDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwODA2VDIxNDIzM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPThkMDY0ZjdiZDg5Y2QzMTMyMjMxNWNkZTdmNTE1ZDc0YjA1ZGYzZGRiOThhOWNlZWRhZTZjZTg4ODZjMmU1ZTImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.6ZmxLaGdf9vSi2MWePzPJqymJrbM11TumQhT-6MugDc)

- To format the code, execute the following command:

  ```bash
  make format
  ```

  ![Make Format](https://private-user-images.githubusercontent.com/61529274/355608740-bfdf6c50-3bc4-4f4d-b226-831430a59fc4.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjI5ODA4NTMsIm5iZiI6MTcyMjk4MDU1MywicGF0aCI6Ii82MTUyOTI3NC8zNTU2MDg3NDAtYmZkZjZjNTAtM2JjNC00ZjRkLWIyMjYtODMxNDMwYTU5ZmM0LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA4MDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwODA2VDIxNDIzM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTljNTMxZjE2ODNkYjJlMGZlMTMwZTk1N2UyYzMyNjI1NThjNjUyOGMyOWZiOWQ0ZTc3Mjc1MGQyMjQzYWU1NTYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.v2ps7WavlW_DX88bPA1gOyPprNHfLNNffmWh5fYtuk8)

## Inspiration

Inspired by [HelixNet](https://huggingface.co/migtissera/HelixNet)
