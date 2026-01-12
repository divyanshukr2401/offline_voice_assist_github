from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

VOSK_MODEL_PATH = BASE_DIR / "models" / "vosk-model-small-en-in-0.4"

SAMPLE_RATE = 16000
