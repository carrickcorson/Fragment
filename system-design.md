# Fragment System Design

## Development

Development setup to allow running the LLM on Orpheus while developing the web application on local devices.

### Server (Orpheus)

Docker container runs Ollama with models. The model API port is exposed and accessed over the network via an environment variale. The model is stored on the server in a docker volume.

Docker volume has port 11434 exposed

### Local Development Devices (Icarus and Atlas)

The web application is developed in a docker container on the development devices, accessing the LLM API through the network. Eventually web app build will live on server as well, maybe in it's own docker container connected to the LLM container usig a docker network?

### Pipeline

Text box send button pressed in the chat window. Web app script sends the content to LLM formatter script.

Message is formatted in the LLM formatter. This includes chat memory, etc. Formatted message is forwarded to the pipeline.

Pipeline sends formatted message to the model and waits for a response.

Response is streamed to the pipeline. Pipeline uses a generator to stream the response to the web app script.

Web app script recieves the chunks of text and displays it in the LLM text region.
