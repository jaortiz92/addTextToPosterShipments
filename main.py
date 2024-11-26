from app import App
from time import sleep


def run() -> None:
    try:
        App()
    except Exception as e:
        print('Validar app con soporte\n', e)
        sleep(120)


if __name__ == '__main__':
    run()
