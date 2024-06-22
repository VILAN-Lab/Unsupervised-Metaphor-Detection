# Can ChatGPT's Performance be Improved on Verb Metaphors Detection Tasks? Bootstrapping and Combining Tacit Knowledge (ACL2024)

This repository contains the code for the paper "Can ChatGPT's Performance be Improved on Verb Metaphors Detection Tasks? Bootstrapping and Combining Tacit Knowledge" presented at ACL 2024.

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Usage](#usage)
- [Datasets](#datasets)
- [Contributing](#contributing)

## Introduction

In this project, we investigate approaches to improve the performance of ChatGPT in detecting verb metaphors. By bootstrapping and combining tacit knowledge, we aim to enhance the model's understanding and detection capabilities.

## Setup

### Prerequisites

Ensure you have Python 3.8 or higher installed.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/VILAN-Lab/Unsupervised-Metaphor-Detection.git
   cd Unsupervised-Metaphor-Detection
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### OpenAI API Key

To use the OpenAI API, you need an API key. You can get your API key from [OpenAI](https://platform.openai.com/account/api-keys).

Once you have your API key, manually input it into the `new_Tools.py` file. Open `new_Tools.py` and add your API key as shown below:

```python
# Enter the API of your OpenAI account here
api_key = ""
```

## Usage

### Preparing the Data

Ensure that the `datas` directory contains the verb list and samples mapped with themes. This includes the files:

- `datas/TroFi_sent_svo_oxford_topic_k_basic.csv`
- `datas/TroFi_verb_lists_oxford_topic.csv`

### Running the Model

To evaluate the performance of metaphor detection using the Oxford theme on the TroFi dataset, run the following Python function:

```python
TroFi_judge_by_oxford_topic_k(1, 2, "datas/TroFi_sent_svo_oxford_topic_k_basic.csv", "datas/TroFi_verb_lists_oxford_topic.csv")
```

## Datasets

The `datas` directory should include:

- A verb list constructed using a metaphor dataset.
- Samples that have been mapped with themes.

## Contributing

We welcome contributions from the community. If you find a bug or have a feature request, please open an issue or submit a pull request.

