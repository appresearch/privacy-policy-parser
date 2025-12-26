"""Privacy policy parser implementation."""
import re
from pathlib import Path
from typing import Dict, List, Optional
from bs4 import BeautifulSoup
import requests


class Parser:
    """Parse and analyze privacy policies."""
    
    def __init__(self):
        self.key_terms = {
            "data_collection": ["collect", "gather", "obtain", "receive"],
            "data_sharing": ["share", "disclose", "transfer", "sell"],
            "user_rights": ["right", "access", "delete", "opt-out"],
            "cookies": ["cookie", "tracking", "pixel"],
        }
    
    def parse(self, source: str) -> Dict:
        """Parse privacy policy from URL or file."""
        if source.startswith("http"):
            content = self._fetch_url(source)
        else:
            content = Path(source).read_text()
        
        soup = BeautifulSoup(content, "html.parser")
        text = soup.get_text()
        
        return {
            "data_collection": self._extract_section(text, "data_collection"),
            "data_sharing": self._extract_section(text, "data_sharing"),
            "user_rights": self._extract_section(text, "user_rights"),
            "readability_score": self._calculate_readability(text),
        }
    
    def _fetch_url(self, url: str) -> str:
        """Fetch content from URL."""
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.text
    
    def _extract_section(self, text: str, section: str) -> List[str]:
        """Extract relevant sentences for a section."""
        sentences = re.split(r'[.!?]+', text)
        relevant = []
        for sentence in sentences:
            if any(term in sentence.lower() for term in self.key_terms[section]):
                relevant.append(sentence.strip())
        return relevant[:10]  # Limit to 10 sentences
    
    def _calculate_readability(self, text: str) -> float:
        """Calculate simple readability score."""
        words = text.split()
        sentences = re.split(r'[.!?]+', text)
        avg_sentence_length = len(words) / max(len(sentences), 1)
        return min(100, max(0, 100 - avg_sentence_length * 2))



