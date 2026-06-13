from services.pdf_service import (
    PDFService
)

from core.pattern_detector import (
    PatternDetector
)

from core.sequence_detector import (
    SequenceDetector
)

from core.entity_extractor import (
    EntityExtractor
)


class IntelligenceService:

    @staticmethod
    def analyze_pdf(filename):

        pdf = (
            PDFService.load_pdf(
                filename
            )
        )

        text = pdf["text"]

        patterns = (
            PatternDetector.detect(
                text
            )
        )

        missing = (
            SequenceDetector
            .find_missing_numbers(
                text
            )
        )

        entities = (
            EntityExtractor.extract(
                text
            )
        )

        return {

            "patterns": patterns,

            "missing_numbers": missing,

            "entities": entities
        }