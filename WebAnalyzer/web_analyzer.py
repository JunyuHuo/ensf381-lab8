import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/University_of_Calgary"
try:
    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
    #print(soup.prettify())

    #Q3
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
    page_text = soup.get_text().lower()
    words = page_text.split()
    words = [word.strip('.,!?()[]{}":;') for word in words if word.strip('.,!?()[]{}":;')]
    word_counts = Counter(words)
    print("\nMost Common Words:")
    for word, count in word_counts.most_common(5):
        print(f"'{word}': {count} times")
        
    #Q6
    longest_paragraph = ""
    longest_word_count = 0
    for p in paragraphs:
        p_text = p.get_text().strip()
        p_words = [word for word in p_text.lower().split() if word.strip('.,!?()[]{}":;')]
        word_count = len(p_words)
        if word_count >= 5 and word_count > longest_word_count:
            longest_paragraph = p_text
            longest_word_count = word_count
    
    print("\nLongest Paragraph Analysis:")
    print(f"The longest paragraph contains {longest_word_count} words.")
    print("Paragraph content:")
    print(longest_paragraph[:200] + "..." if len(longest_paragraph) > 200 else longest_paragraph)
    
    #Q7
    labels = ['Headings', 'Links', 'Paragraphs']
    values = [heading_count, link_count, paragraph_count]
    plt.bar(labels, values)
    plt.title('Group#30')
    plt.ylabel('Count')
    plt.show()
    
except Exception as e:
    print(f"Error fetching content: {e}")
