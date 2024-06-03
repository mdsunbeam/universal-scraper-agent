<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/mdsunbeam/universal-scraper-agent">
    <img src="misc/scraper-agent-logo.png" alt="Logo" width="160" height="160">
  </a>

<h3 align="center">Universal Scraper Agent</h3>

  <p align="center">
    Easily extract data from the web through large language models (LLMs) by specifying the format through JSON files.
    <br />
    <!-- <a href="https://github.com/mdsunbeam/llm-hub"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/mdsunbeam/llm-hub">View Demo</a> -->
    <!-- · -->
    <a href="https://github.com/mdsunbeam/universal-scraper-agent/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/mdsunbeam/universal-scraper-agent/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Universal Scraping Agent is a versatile and powerful tool for scraping websites and processing images of webpages to extract specific data using Selenium and multimodal large language models (LLMs). This project allows users to define their scraping requirements through a JSON configuration, making it easy to customize and automate data extraction tasks.

### Supported Models

In the initial release, we support the use of:

- **GPT models from OpenAI**
- **Claude 3 models from Anthropic**
- **Gemini models from Google**

### Key Features

- **Automated Web Scraping**: Uses Selenium to navigate and scrape data from websites.
- **Image Processing**: Captures screenshots of webpages and processes them using LLMs.
- **Customizable Data Extraction**: Users can specify the data to be scraped using a JSON configuration.
- **Dynamic Content Handling**: Capable of handling dynamic web content and AJAX-loaded elements.
- **Multi-Platform Support**: Compatible with Windows, macOS, and Linux.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

The first thing to set up is your OpenAI, Anthropic, Google, and Groq API keys. You need OpenAI for the GPT models, Anthropic for the Claude 3 models, Google for the Gemini models, and finally Groq for Llama 3 models. You only need one of the LLMs to begin automated scraping.

### Prerequisites

1. Get an API key for OpenAI at: [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Get directions for how to generate an API key for Anthropic at: [https://docs.anthropic.com/claude/reference/getting-started-with-the-api](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)
3. Get an API key for Google at: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
4. Create a free account and get an API key for Groq at: [https://console.groq.com/keys](https://console.groq.com/keys)

Next, create four text files called `OPENAI_API_KEY.txt`, `ANTHROPIC_API_KEY.txt`, `GOOGLE_API_KEY.txt`, and `GROQ_API_KEY.txt`. Paste your respective API keys into the text files.

### Installation

1. Make Python virtual environment
   ```sh
   python3.10 -m venv scraper-agent-env
   source scraper-agent-env/bin/activate
   ```
2. Clone the repo
   ```sh
   git clone https://github.com/mdsunbeam/universal-scraper-agent.git
   cd universal-scraper-agent
   ```
3. Install Python packages
   ```sh
   pip install -r requirements.txt 
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1. Define your scraping configuration by creating a JSON file to specify what data you want to extract.

```json
{
    "Description" : "detailed description of the contents of the webpage",
    "Interesting Feature" : ["list of any peculiar, interesting, or unique features about the page"]
}
```

2. Run the scraper agent.

```python
from llms import GPT
from utils import load_json_as_dict, save_json_to_file, explore_links
import cv2
import os


if __name__ == "__main__":

    # Shallow exploration of links on website
    website_url = 'https://mdsunbeam.com/'  # Replace with your target website
    explore_links(website_url)

    MODELS = {
    "OpenAI": ["gpt-4-turbo", "gpt-4o", "gpt-3.5-turbo"]
    }

    desired_format = load_json_as_dict("specific_output.json")
    
    system_message = f"""You are a web-scraping agent that can decide how to scrape information
    from webpages. Please organize the JSON scraping in the following format: \n
    {desired_format}
    """

    # save_json_to_file(gpt4o.generate_response(), "scrape_results.json")
    directory_path = "images"
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            webpage_image = cv2.imread(file_path)
            gpt4o = GPT(model_name=MODELS["OpenAI"][1], system_message=system_message)
            gpt4o.add_user_message(frame=webpage_image, user_msg="Please give me results in the desired JSON form.")
            save_json_to_file(gpt4o.generate_response(), f"scraped_results/result_{filename}.json")

```
or
```sh
python main.py
```

3. View scraping results in the `scraped_results/` folder.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] add a key in the results that saved exact URL
- [ ] error handling during shallow exploration

See the [open issues](https://github.com/mdsunbeam/llm-hub/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/new-feature`)
3. Commit your Changes (`git commit -m 'added new feature'`)
4. Push to the Branch (`git push origin feature/new-feature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

[@MdSunbeam](https://twitter.com/MdSunbeam) - mdsunbeam3.14@gmail.com

Project Link: [https://github.com/mdsunbeam/universal-scraper-agent](https://github.com/mdsunbeam/universal-scraper-agent)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/mdsunbeam/universal-scraper-agent.svg?style=for-the-badge
[contributors-url]: https://github.com/mdsunbeam/universal-scraper-agent/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/mdsunbeam/universal-scraper-agent.svg?style=for-the-badge
[forks-url]: https://github.com/mdsunbeam/universal-scraper-agent/network/members
[stars-shield]: https://img.shields.io/github/stars/mdsunbeam/universal-scraper-agent.svg?style=for-the-badge
[stars-url]: https://github.com/mdsunbeam/universal-scraper-agent/stargazers
[issues-shield]: https://img.shields.io/github/issues/mdsunbeam/universal-scraper-agent.svg?style=for-the-badge
[issues-url]: https://github.com/mdsunbeam/universal-scraper-agent/issues
[license-shield]: https://img.shields.io/github/license/mdsunbeam/universal-scraper-agent.svg?style=for-the-badge
[license-url]: https://github.com/mdsunbeam/universal-scraper-agent/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/mdsunbeam
