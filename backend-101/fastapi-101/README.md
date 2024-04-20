# FASTAPI - 101

## Prerequisite
```
pip install "fastapi[all]"
```
You will also need an ASGI server, for production such as Uvicorn or Hypercorn.
```
pip install "uvicorn[standard]"
```

## Running program
```
uvicorn main:app --reload
or
python3 -m uvicorn main:app --reload
```