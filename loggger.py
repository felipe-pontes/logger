import random
import time

def generate_logger(level, name):
  """Gera um log aleatório.

  Args:
    level: O nível do log.
    name: O nome do log.

  Returns:
    Um log aleatório.
  """

  level = random.choice(["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])
  name = random.choice(["log1", "log2", "log3", "log4", "log5"])
  message = random.choice([
      "Este é um log de depuração.",
      "Este é um log de informação.",
      "Este é um log de aviso.",
      "Este é um log de erro.",
      "Este é um log crítico.",
  ])
  return f"[{level}] {name}: {message}"


if __name__ == "__main__":
  # Gera um log aleatório.
  log = generate_logger("DEBUG", "log1")
  print(log)

  # Gera 100 logs aleatórios com um intervalo de 1 segundo entre cada log.
  for _ in range(100):
    log = generate_logger(random.choice(["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]),
                           random.choice(["log1", "log2", "log3", "log4", "log5"]))
    time.sleep(1)
    print(log)
