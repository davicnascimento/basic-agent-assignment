from src.config import load_settings
from src.llm import classify_message
from src.validation import validate_result


def main() -> None:
    message = input("Mensagem do cliente: ").strip()
    if not message:
        print("Escreva uma mensagem para continuar.")
        return

    settings = load_settings()
    result = classify_message(settings, message)
    validated = validate_result(result)
    print(validated.model_dump_json(indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
