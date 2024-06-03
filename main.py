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
