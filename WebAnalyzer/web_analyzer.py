import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/University_of_Calgary"
try:
    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
    #print(soup.prettify())

    #Q#
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    heading_count = len(headings)
    links = soup.find_all('a')
    link_count = len(links)
    paragraphs = soup.find_all('p')
    paragraph_count = len(paragraphs)
    print("\nWeb Page Analysis:")
    print(f"Number of headings (h1-h6): {heading_count}")
    print(f"Number of links (a tags): {link_count}")
    print(f"Number of paragraphs (p tags): {paragraph_count}")
    
    #Q4
    page_text = soup.get_text().lower()
    keyword = input("\nEnter a keyword to search for: ").lower()
    keyword_count = page_text.count(keyword)
    print(f"\nKeyword Analysis:")
    print(f"The keyword '{keyword}' appears {keyword_count} times in the webpage content.")

    #Q5
    from collections import Counter
    import re
    words = re.findall(r'\b\w+\b', page_text)
    word_counts = Counter(words)
    print("\nMost Common Words:")
    for word, count in word_counts.most_common(5):
        print(f"'{word}': {count} times")
    
except Exception as e:
    print(f"Error fetching content: {e}")