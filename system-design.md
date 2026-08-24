# Fragment System Design

## Development

Development setup to allow running the LLM on Orpheus while developing the web application on local devices.

### Server (Orpheus)

Docker container runs Ollama with models. The model API port is exposed and accessed over the network via an environment variale. The model is stored on the server in a docker volume.

### Local Development Devices (Icarus and Atlas)

The web application is developed in a docker container on the development devices, accessing the LLM API through the network.
