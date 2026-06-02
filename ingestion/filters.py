class ChunkFilter:

    NOISE_PATTERNS = [

        "TABLE OF CONTENTS",

        "Page No.",

        "PAGE NO",

        "Sr No.",

        "SR NO",

        "LIST OF FIGURES",

        "LIST OF TABLES"
    ]

    MIN_CHARS = 50

    @classmethod
    def is_noise_chunk(
        cls,
        text: str
    ) -> bool:

        text_upper = text.upper()

        for pattern in cls.NOISE_PATTERNS:

            if pattern.upper() in text_upper:
                return True

        if len(text.strip()) < cls.MIN_CHARS:
            return True

        return False
