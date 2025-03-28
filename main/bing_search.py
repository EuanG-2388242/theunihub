import json
import requests

def read_bing_key():

    bing_api_key = None

    try:

        with open('bing.key', 'r') as f:

            bing_api_key = f.readline().strip()

    except:

        try:

            with open('../bing.key', 'r') as f:

                bing_api_key = f.readline().strip()

        except:

            raise IOError('bing.key file not found')
    
    if not bing_api_key:

        raise KeyError('Bing key not found')
    
    return bing_api_key

def run_query(search_terms):

    bing_key = read_bing_key()

    search_url = 'https://api.bing.microsoft.com/v7.0/search'

    headers = {'Ocp-Apim-Subscription-Key': bing_key}

    params = {'q': search_terms, 'textDecorations': True, 'textFormat': 'HTML'}

    response = requests.get(search_url, headers=headers, params=params)

    response.raise_for_status()

    search_results = response.json()

    results = []

    if 'webPages' in search_results:

        for result in search_results['webPages']['value']:

            results.append({
                'title': result['name'],
                'link': result['url'],
                'summary': result['snippet']
            })
    
    return results

def main():
    search_terms = str(input("Please enter search terms: "))

    results = run_query(search_terms)

    print(json.dumps(results, indent=2))

if __name__ == '__main__':

    main()