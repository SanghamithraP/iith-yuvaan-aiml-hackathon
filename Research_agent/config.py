# config.py

# User Agent for web requests (helps avoid blocking)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}

# Number of results to collect
MAX_NEWS = 10
MAX_LITIGATION = 5

# HuggingFace model for summarization
SUMMARIZATION_MODEL = "facebook/bart-large-cnn"

# Timeout for requests
REQUEST_TIMEOUT = 10

# RBI regulation search keyword
RBI_KEYWORD = "RBI regulation India banking rules"

# Enable or disable qualitative notes
ENABLE_SITE_VISIT = True