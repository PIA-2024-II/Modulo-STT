# Microservicio TTS

Microservicio prototipo el cual convierte un archivo de audio en un texto en formato json
De momento, funciona unicamente en español usando un modelo de wav2vec2 de Jonatas Grosman

Antes de usarse, se debe importar el archivo de audio en formato wav, mpeg o x-wav dentro de la carpeta tests, y debe tener de nombre "sample" para que se lea correctamente

## Instalacion:

Instalar los requerimientos:
```bash
pip install -r requirements.txt
```

## Uso:

Dentro de la raiz del microservicio, se debe ejecutar una sesion de uvicorn:

```bash
uvicorn app.main:app --reload
```

De forma predeterminada, el programa se cargara de forma local en la direccion http://127.0.0.1:8000
Para acceder a la documentacion, se agrega "/docs" al lado del enlace donde se este ejecutando el microservicio

Para cargar un audio dentro del microservicio, se debe crear una terminal nueva distinta a la cual se activo el servidor. En ella, se debe aplicar el siguiente comando, asumiendo que la direccion es la predeterminada:
```bash
curl -X POST "http://127.0.0.1:8000/transcribe/" -F "file=@app/tests/sample.{extension}"
```

{extension} debe ser reemplazada por la extension del archivo "sample" que se encuentre en la carpeta tests, de tener otra direccion, se debe reemplazar de igual manera.
En la misma terminal, se mostrara en formato json el resultado en texto del audio recibido.

De querer observar los datos de la extension del archivo, se ejecuta el siguiente comando:
```bash
curl -X POST "http://127.0.0.1:8000/file-extension/" -F "file=@app/tests/sample.{extension}"
```

En el cual se mostrara en pantalla un json con: Nombre, Extension y MIME Type (Tipo de medio)

## Notas:
El programa posee una proteccion para evitar que se carguen archivos que no sean de estos tres formatos, el objetivo es ir mejorando esta proteccion que ahora esta a un nivel basico.

Al entrar a la direccion sin llamar a algun endpoint, se recibira al usuario con un mensaje basico.

El microservicio funciona unicamente usando curl para la subida de archivos, esto debido a que se trata de pruebas locales.