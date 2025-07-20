import os, requests

SERP_KEY = os.getenv("SERP_KEY")
PDL_KEY  = os.getenv("PDL_KEY")

def run(principals: list[dict]) -> list[dict]:
    results = []
    for p in principals:
        q = f'{p["name"]} {p["title"]} site:linkedin.com/in'
        serp = requests.get("https://serpapi.com/search.json",
                            params={"engine":"google", "q":q, "api_key":SERP_KEY}).json()
        link = serp["organic_results"][0]["link"]
        pdl = requests.get("https://api.peopledatalabs.com/v5/person/enrich",
                           headers={"X-API-Key":PDL_KEY},
                           params={"profile": link}).json()
        results.append({**p,
                        "linkedin": link,
                        "email": pdl.get("work_email"),
                        "phone": pdl.get("phone_number")})
    return results
