import logging as log

# docs.python.org/3/howto/logging.html
#llamamos una configuración básica

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s:%(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_dato.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('mensaje a niviel debug')
    log.info('mensaje a nivel info')
    log.warning('Mensaje a nievel warning')
    log.error('Mensaje a nivel error')
    log.critical('Mensaje a nivel critical')
