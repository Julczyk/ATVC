import requests
from bs4 import BeautifulSoup
import html2text

def get_div_content(url, class_selector):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find the specific <div> element you want to extract
            specific_div = soup.find_all("div", {"class": "body markup"})

            # Check if the specific <div> was found
            if specific_div:
                return str(specific_div)
            else:
                return 'Specific <div> not found on the page.'
        else:
            return 'Failed to retrieve the web page. Status code: ' + str(response.status_code)
    except Exception as e:
        return 'An error occurred: ' + str(e)


def html_to_markdown(html_text):
    # Initialize the HTML to Markdown converter
    converter = html2text.HTML2Text()
    
    # Optionally, set the conversion options (e.g., remove_links=True to remove links)
    # converter.ignore_links = True

    # Convert the HTML to Markdown
    markdown_text = converter.handle(html_text)
    
    return markdown_text

def save_to_file(filename, text):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f'Text saved to {filename}')
    except Exception as e:
        print(f'Error saving text to {filename}: {str(e)}')

url = 'https://ukrainawojna.substack.com/p/dzien-563'
class_selector = "body markup"

div_content = get_div_content(url, class_selector)
converted_text = html_to_markdown(div_content)
save_to_file("markdowned.md", converted_text)
print(converted_text)
