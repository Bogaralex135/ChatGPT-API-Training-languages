import openai
import typer
from rich import print
from rich.table import Table

api_key = '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'

def main():

    openai.api_key = api_key

    print("[green]ChatGPT API en Python[/green]")
    print("\n[green]¡Ten conversaciones en otros idiomas mientras ChatGPT te enseña![/green]\n")

    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir de la aplicación")
    table.add_row("new", "Crear una nueva conversación")

    print(table)

    # Contexto del asistente
    context = {"role": "system",
               "content": "Eres un asistente conversacional para practicar un idioma. Si te pido una simulacion de entrevista, muestrame una pregunta y cuando te responda muestrame otra, nunca muestres una lista de preguntas. Si cometo un error gramatico o sintactico muestrame la forma correcta de escribir el idioma. Dame consejos sobre como responder cada pregunta. Siempre dame una pregunta cada que me respondas."}

    messages = [context]

    while True:

        content = __prompt()

        if content == "new":
            print("Nueva conversación creada")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)

        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content})

        print(f"[bold green]> [/bold green] [green]{response_content}[/green]")


def __prompt() -> str:
    prompt = typer.prompt("\n¿Sobre qué quieres hablar? ")

    if prompt == "exit":
        exit = typer.confirm("¿Estás seguro?")
        if exit:
            print("¡Hasta luego!")
            raise typer.Abort()

        return __prompt()

    return prompt


if __name__ == "__main__":
    typer.run(main)
