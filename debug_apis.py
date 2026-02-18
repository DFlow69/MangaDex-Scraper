import requests
import json

def test_anilist(query):
    url = 'https://graphql.anilist.co'
    # Request format to see if it's a novel
    query_graphql = '''
    query ($search: String) {
      Page(page: 1, perPage: 5) {
        media(search: $search, type: MANGA) {
          id
          title {
            english
            romaji
            native
          }
          format
          countryOfOrigin
        }
      }
    }
    '''
    variables = {'search': query}
    try:
        r = requests.post(url, json={'query': query_graphql, 'variables': variables}, timeout=5)
        print(f"--- AniList '{query}' ---")
        if r.status_code == 200:
            data = r.json()
            media_list = data.get('data', {}).get('Page', {}).get('media', [])
            for m in media_list:
                print(f"Title: {m.get('title')}")
                print(f"Format: {m.get('format')}")
                print(f"Country: {m.get('countryOfOrigin')}")
                print("-" * 20)
        else:
            print(f"Error: {r.status_code} {r.text}")
    except Exception as e:
        print(f"Exception: {e}")

def test_mangaupdates(query):
    url = "https://api.mangaupdates.com/v1/series/search"
    payload = {
        "search": query,
        "page": 1,
        "perpage": 5
    }
    try:
        r = requests.post(url, json=payload, timeout=5)
        print(f"--- MangaUpdates '{query}' ---")
        if r.status_code == 200:
            data = r.json()
            results = data.get("results", [])
            for res in results:
                rec = res.get("record", {})
                print(f"Title: {rec.get('title')}")
                print(f"Year: {rec.get('year')}")
                print("-" * 20)
        else:
            print(f"Error: {r.status_code} {r.text}")
    except Exception as e:
        print(f"Exception: {e}")

def test_mangadex(query):
    url = "https://api.mangadex.org/manga"
    params = {
        "title": query,
        "limit": 5,
        "includes[]": "cover_art"
    }
    try:
        r = requests.get(url, params=params, timeout=10)
        print(f"--- MangaDex '{query}' ---")
        if r.status_code == 200:
            data = r.json()
            for m in data.get('data', []):
                attrs = m.get('attributes', {})
                titles = attrs.get('title', {})
                en_title = titles.get('en') or list(titles.values())[0]
                print(f"Title: {en_title}")
                print(f"Alt Titles: {attrs.get('altTitles')}")
                print("-" * 20)
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    test_anilist("全職覺醒")
    test_anilist("全职觉醒")
    test_mangaupdates("全職覺醒")
    test_mangaupdates("全职觉醒")
    test_mangadex("全職覺醒")
    test_mangadex("全职觉醒")
