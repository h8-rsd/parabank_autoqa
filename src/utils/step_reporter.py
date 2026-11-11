import allure

from typing import Iterator
from logging import getLogger
from contextlib import contextmanager


logger = getLogger(__name__)


class StepReporter:
    @contextmanager
    def add_step(self, description: str) -> Iterator[None]:
        logger.info("TEST STEP: %s", description)

        with allure.step(description):
            try:
                yield
            except Exception:
                logger.exception("TEST FAILED: %s", description)
                raise
