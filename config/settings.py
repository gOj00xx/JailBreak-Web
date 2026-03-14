# Konfigurasi aplikasi
import os

class Config:
    # Server
    PORT = 7762
    HOST = '0.0.0.0'
    DEBUG = False
    
    # Paths
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    PROMPT_FOLDER = os.path.join(BASE_DIR, 'prompts')
    TEMPLATE_FOLDER = os.path.join(BASE_DIR, 'templates')
    STATIC_FOLDER = os.path.join(BASE_DIR, 'static')
    
    # Prompts
    MAX_PROMPTS_PER_CATEGORY = 1000
    DEFAULT_PROMPT_COUNT = 3
    MAX_PROMPT_COUNT = 10
    
    # Categories
    CATEGORIES = {
        'fantasy': 'Fantasy World',
        'hacker': 'Hacker Mode',
        'kingdom': 'Medieval Kingdom',
        'anime': 'Anime Universe',
        'scifi': 'Sci-Fi Future',
        'horror': 'Horror Stories',
        'romance': 'Romance Tales',
        'comedy': 'Comedy & Fun',
        'nsfw': 'NSFW (18+)',
        'dark': 'Dark Themes',
        'custom': 'Custom Mix'
    }
    
    # AI Models
    AI_MODELS = [
        {'id': 'deepseek', 'name': 'DeepSeek Chat', 'api_url': 'https://api.deepseek.com/v1/chat/completions'},
        {'id': 'grok', 'name': 'Grok (xAI)', 'api_url': 'https://api.x.ai/v1/chat/completions'},
        {'id': 'openrouter', 'name': 'OpenRouter', 'api_url': 'https://openrouter.ai/api/v1/chat/completions'},
        {'id': 'gemini', 'name': 'Google Gemini', 'api_url': 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent'},
        {'id': 'claude', 'name': 'Anthropic Claude', 'api_url': 'https://api.anthropic.com/v1/messages'},
        {'id': 'gpt4', 'name': 'OpenAI GPT-4', 'api_url': 'https://api.openai.com/v1/chat/completions'},
        {'id': 'llama', 'name': 'Meta Llama', 'api_url': 'https://api.fireworks.ai/inference/v1/chat/completions'},
        {'id': 'mistral', 'name': 'Mistral AI', 'api_url': 'https://api.mistral.ai/v1/chat/completions'}
  ]
