from crawler import get_google_news, search_litigation
from summarizer import summarize_text

company = input("Enter company name: ")

print("\nCollecting news...\n")
news = get_google_news(company)

print("\nChecking litigation history...\n")
litigation = search_litigation(company)

print("\n------ NEWS ------\n")

for n in news:
    print("-", n)

print("\n------ LITIGATION ------\n")

for l in litigation:
    print("-", l)


combined_text = " ".join(news + litigation)

print("\n------ AI SUMMARY ------\n")

summary = summarize_text(combined_text)

print(summary)