import os
from typing import Optional

import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()


class GeminiClient:
    """
    Wrapper around Google's Gemini API.

    Responsibilities:
    - Load API key
    - Configure Gemini SDK
    - Generate responses
    - Support future multimodal extensions
    """

    def __init__(
        self,
        model_name: str = "gemini-2.5-flash"
    ):

        api_key = os.getenv(
            "GEMINI_API_KEY"
        )

        if not api_key:

            raise ValueError(
                "GEMINI_API_KEY not found in environment variables."
            )

        genai.configure(
            api_key=api_key
        )

        self.model_name = (
            model_name
        )

        self.model = (
            genai.GenerativeModel(
                model_name
            )
        )

    def generate(
        self,
        prompt: str,
        temperature: float = 0.2
    ) -> str:
        """
        Generate a response from Gemini.

        Args:
            prompt (str):
                User prompt

            temperature (float):
                Controls randomness

        Returns:
            str:
                Generated response
        """

        try:

            response = (
                self.model.generate_content(
                    prompt,

                    generation_config={
                        "temperature":
                        temperature
                    }
                )
            )

            return (
                response.text
            )

        except Exception as e:

            return (
                f"Gemini Error: {str(e)}"
            )

    def generate_with_system_prompt(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.2
    ) -> str:
        """
        Simulates system instructions.

        Useful for RAG.
        """

        combined_prompt = f"""
SYSTEM INSTRUCTIONS

{system_prompt}

USER QUESTION

{user_prompt}
"""

        return self.generate(
            prompt=combined_prompt,
            temperature=temperature
        )

    def test_connection(
        self
    ) -> bool:
        """
        Verify Gemini connectivity.
        """

        try:

            response = (
                self.model.generate_content(
                    "Reply with OK"
                )
            )

            return (
                len(response.text) > 0
            )

        except Exception:

            return False

    def get_model_name(
        self
    ) -> str:

        return (
            self.model_name
        )