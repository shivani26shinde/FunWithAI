import os
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from .forms import JobSearchForm

def job_search(request):
    if request.method == 'POST':
        form = JobSearchForm(request.POST)
        if form.is_valid():
            position = form.cleaned_data['position']
            location = form.cleaned_data['location']
            company = form.cleaned_data['company']

            """ file_path = os.path.join(os.path.dirname(__file__), 'my_api.txt')
            with open(file_path, 'r') as f:
                api_data = f.readlines()
            for line in api_data:
                line_data = line.strip().split('=', 1)
                if len(line_data) == 2:
                    key, value = line_data
                    if key == 'apiKey':
                        api_key = value.replace('\\=', '=') """

            # Really silly/wrong way to get data and parse but there are almost no free public apis which I could use
            # Construct the search query URL for the company's career website
            query = f"{position} {location} site:{company}.com/careers"
            url = f"https://www.google.com/search?q={query}"
            
            # Send a request to Google to retrieve search results
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
            response = requests.get(url, headers=headers)
            
            # Parse the search results using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            search_results = soup.find_all('div', class_='r')

            print(search_results)
            
            # Extract the URLs of job postings from the search results
            job_postings = []
            for result in search_results:
                link = result.find('a')['href']
                if 'careers' in link or 'jobs' in link:
                    job_postings.append(link)

            # Render template with job postings
            return render(request, 'job_search_results.html', {'job_postings': job_postings})
    else:
        form = JobSearchForm()

    return render(request, 'job_search.html', {'form': form})