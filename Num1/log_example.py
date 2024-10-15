import logging


# Фильтр для уровня DEBUG и INFO, пришлось добавить отдельно через класс, т.к. иначе залетало всё, что выше
class InfoDebugFilter(logging.Filter):
    def filter(self, record):
        return record.levelno <= logging.INFO


# Создаем логгер
logger = logging.getLogger('multi_logger')
logger.setLevel(logging.DEBUG)  # Логгер будет обрабатывать все сообщения
# Создаем обработчик для debug и info сообщений
debug_info_handler = logging.FileHandler('debug_info.log')
debug_info_handler.setLevel(logging.DEBUG)
# Вызываем фильтр для отсеивания сообщений уровней выше INFO
debug_info_handler.addFilter(InfoDebugFilter())
# Создаем обработчик для warning+
warnings_errors_handler = logging.FileHandler('warnings_errors.log')
warnings_errors_handler.setLevel(logging.WARNING)  # Ловим от WARNING и выше
# Формат сообщений
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# Применяем формат
debug_info_handler.setFormatter(formatter)
warnings_errors_handler.setFormatter(formatter)
# Добавляем обработчики к логгеру
logger.addHandler(debug_info_handler)
logger.addHandler(warnings_errors_handler)
# Пример логирования сообщений
logger.debug('Это сообщение уровня DEBUG')
logger.info('Это сообщение уровня INFO')
logger.warning('Это сообщение уровня WARNING')
logger.error('Это сообщение уровня ERROR')
logger.critical('Это сообщение уровня CRITICAL')
