import logging

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
try:
    report = generator.generate(Data)
except Exception as e:
    logger.exception("Report generation failed")