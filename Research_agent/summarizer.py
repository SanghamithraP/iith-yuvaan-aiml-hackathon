from sumy.summarizers.lsa import LsaSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer


def summarize_text(text):

    if len(text) < 100:
        return text

    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()

    summary = summarizer(parser.document, 3)

    result = ""

    for sentence in summary:
        result += str(sentence) + " "

    return result