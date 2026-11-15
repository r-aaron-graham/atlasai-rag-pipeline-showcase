# AtlasAI RAG Pipeline Showcase

A notebook collection with a runnable FastAPI reviewer example. See [USAGE.md](USAGE.md) and the [notebooks](notebooks) for the research and deployment examples.

## Run the reviewer API

```sh
python -m pip install -c requirements.lock -r requirements.txt
python -m uvicorn serve.main:app --host 127.0.0.1 --port 8000
```

In a second terminal, run:

```sh
curl -H 'Content-Type: application/json' -d '{"query":"retention"}' http://127.0.0.1:8000/ask
```

The default path retrieves one synthetic policy by keyword and returns its source ID. Set `ATLASAI_PROVIDER=openai` and `OPENAI_API_KEY` to use the optional direct generation path. That path sends the query to OpenAI and needs separate verification. Keep the local server on loopback.

## Deployment verification

Use Python 3.12 on Linux. CI and Docker apply the checked-in dependency constraints.

```sh
python -m pip install -c requirements.lock -r requirements-dev.txt
python -m pytest -q
docker build -t reviewer-smoke .
docker run --rm -p 127.0.0.1:8000:8000 reviewer-smoke
```

Expected result: `retention` returns a cited synthetic retention policy. Unknown topics return no sources. The optional live OpenAI path generates directly from the supplied prompt. The notebooks are separate research and deployment examples.
