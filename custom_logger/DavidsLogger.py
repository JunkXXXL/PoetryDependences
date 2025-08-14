import os
import logging
from datetime import datetime


def get_logger(log_file_name: str):
    """
    Настраивает и возвращает логгер с двумя обработчиками: для всех логов (DEBUG и выше)
    и для ошибок (ERROR и выше).

    Args:
        log_file_name: Базовое имя файла для логов (без расширения)

    Returns:
        logging.Logger: Настроенный логгер
    """
    # Настройка логирования
    logger = logging.getLogger(log_file_name)
    logger.setLevel(logging.DEBUG)

    # Создание директории для логов в корне проекта
    log_dir = os.path.join("logs", datetime.now().strftime("%d_%m_%Y"))
    os.makedirs(log_dir, exist_ok=True)

    # Обработчик для info логов (DEBUG и выше)
    info_handler = logging.FileHandler(os.path.join(log_dir, f"{log_file_name}.logs"))
    info_handler.setLevel(logging.DEBUG)
    info_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    info_handler.setFormatter(info_formatter)
    logger.addHandler(info_handler)

    # Обработчик для errors логов (ERROR и выше)
    errors_handler = logging.FileHandler(os.path.join(log_dir, f"{log_file_name}_errors.logs"))
    errors_handler.setLevel(logging.ERROR)
    errors_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    errors_handler.setFormatter(errors_formatter)
    logger.addHandler(errors_handler)

    return logger
