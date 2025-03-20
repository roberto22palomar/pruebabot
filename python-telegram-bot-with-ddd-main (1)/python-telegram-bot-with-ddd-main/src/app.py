from common.domain.log.loggerService import LoggerService
from flask import Flask
from common.domain.secretsEngine.secretsEngineService import SecretsEngineService
from common.infrastructure.log.basicLoggerService import BasicLoggerService
from common.infrastructure.secretsEngine.fileSecretsEngineService import FileSecretsEngineService
from star.domain.starServiceListenerHost import StarServiceListenerHost
from star.domain.userRepository import UserRepository
from star.infrastructure.inMemoryUserRepository import InMemoryUserRepository
from common.infrastructure.telegramBotStarServiceListenerHost.telegramBotStarServiceListenerHost import TelegramBotStarServiceListenerHost


def main() -> None:
    logger: LoggerService = BasicLoggerService()
    secrets_engine: SecretsEngineService = FileSecretsEngineService(logger)
    user_repository: UserRepository = InMemoryUserRepository(secrets_engine.get_secret("USER_FILE_NAME"))
    star_service_listener: StarServiceListenerHost = TelegramBotStarServiceListenerHost(logger,
                                                                          secrets_engine,
                                                                          user_repository)
    star_service_listener.run()

    from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Estoy vivo!"

def run_server():
    app.run(host="0.0.0.0", port=8080)

if __name__ == '__main__':
    threading.Thread(target=run_server, daemon=True).start()  # 🔹 Iniciar Flask en segundo plano
    main()


if __name__ == '__main__':
    main()