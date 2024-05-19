from llms import GPT, Claude3, Gemini, Llama3
from utils import load_json_as_dict, save_json_to_file
import cv2

if __name__ == "__main__":

    MODELS = {
    "OpenAI": ["gpt-4-turbo", "gpt-4o", "gpt-3.5-turbo"], 
    "Anthropic": ["claude-3-opus-20240229", "claude-3-sonnet-20240229", "claude-3-haiku-20240307"], 
    "Google": ["gemini-1.5-pro-latest", "gemini-pro", "gemini-pro-vision", "gemini-1.5-flash-latest"], 
    "Meta": ["llama3-70b-8192", "llama3-8b-8192"]
    }

    desired_format = load_json_as_dict("output_format.json")
    
    system_message = f"""You are a web-scraping agent that can decide how to scrape information
    from webpages. Please organize the JSON scraping in the following format: \n
    {desired_format}
    """

    webpage_image = cv2.imread("images/full_screenshot.png")
    # print(system_message)
    gpt4o = GPT(model_name=MODELS["OpenAI"][1], system_message=system_message)
    gpt4o.add_user_message(frame=webpage_image, user_msg="Please give me results in the desired JSON form.")
    print(gpt4o.generate_response())
    # save_json_to_file(gpt4o.generate_response(), "scrape_results.json")

