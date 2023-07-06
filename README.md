# TransGPT

This is a TransGPT, Help your translate markdown files for OpenAI.

## Requirements

- Python 3.8+
- nodejs 16.x

## build

```shell
# install dependencies
npm install

# python dependencies
cd python/
pip install -r requirements.txt
```

## env

copy `.env.sample` to `.env`, then add your config in `.env`:

```shell
OPENAI_API_KEY="sk-<your key here>"
OPENAI_MODEL="gpt-3.5-turbo-16k"
OPENAI_HOST="https://api.openai.com"
```

## running

### backend

```shell
# start backend
cd python/
uvicorn main:app --reload
```

### frontend

```shell
# start frontend
npm run dev
```
