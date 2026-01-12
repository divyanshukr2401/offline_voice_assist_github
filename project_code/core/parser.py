import json

def parse_text(vosk_result):
    if not vosk_result:
        return None

    return json.loads(vosk_result).get("text", "")
