import requests

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
            results = data.get('data', [])
            if not results:
                print("No results found.")
            for m in results:
                attrs = m.get('attributes', {})
                titles = attrs.get('title', {})
                en_title = titles.get('en') or list(titles.values())[0]
                print(f"Title: {en_title}")
                print(f"Alt Titles: {attrs.get('altTitles')}")
                print("-" * 20)
        else:
            print(f"Status: {r.status_code}")
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    test_mangadex("全職覺醒")
