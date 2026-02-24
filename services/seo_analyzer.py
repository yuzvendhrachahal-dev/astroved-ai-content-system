from textstat import flesch_reading_ease

class SEOAnalyzer:

    def analyze(self, data: dict):

        word_count = data["word_count"]
        title_len = len(data["title"])
        meta_len = len(data["meta"])

        readability = flesch_reading_ease(data["content"])

        score = 0

        if 50 <= title_len <= 60:
            score += 20
        if 150 <= meta_len <= 160:
            score += 20
        if word_count >= 1700:
            score += 30
        if readability >= 60:
            score += 20

        return {
            "score": score,
            "title_len": title_len,
            "meta_len": meta_len,
            "word_count": word_count,
            "readability": readability
        }
