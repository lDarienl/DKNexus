"""
Persistencia ultra-liviana para DKNexus.

Estrategia: clave-valor en memoria RAM mediante **Redis** (cliente nativo de
Python). Es extremadamente rapido y permite guardar el estado de un modelo de
ML con comandos simples, p.ej.:

    redis_set("modelo_pesos", [0.5, -0.2]);
    pesos = redis_get("modelo_pesos");

Si la libreria ``redis`` no esta instalada o no hay un servidor escuchando, se
usa automaticamente un *fallback* a disco (un unico archivo JSON) para no
bloquear al usuario. Los valores se serializan con JSON, de modo que listas,
diccionarios, numeros, strings y booleanos se recuperan con su tipo original.
"""

import json
import os

_DISK_PATH = os.path.join(os.getcwd(), ".dknexus_store.json")

_redis_client = None
_backend = None  # "redis" | "disk"


def _try_connect_redis():
    """Intenta conectar a Redis (localhost:6379). Devuelve el cliente o None."""
    try:
        import redis  # type: ignore
    except ImportError:
        return None
    try:
        client = redis.Redis(
            host=os.environ.get("DKN_REDIS_HOST", "127.0.0.1"),
            port=int(os.environ.get("DKN_REDIS_PORT", "6379")),
            db=0,
            socket_connect_timeout=0.5,
            socket_timeout=0.5,
            decode_responses=True,
        )
        client.ping()
        return client
    except Exception:
        return None


def _ensure_backend():
    """Selecciona el backend una sola vez (Redis si esta disponible, si no disco)."""
    global _redis_client, _backend
    if _backend is not None:
        return
    _redis_client = _try_connect_redis()
    _backend = "redis" if _redis_client is not None else "disk"


def backend_name():
    _ensure_backend()
    return _backend


# --------------------------- Fallback a disco ----------------------------

def _disk_load():
    if not os.path.exists(_DISK_PATH):
        return {}
    try:
        with open(_DISK_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def _disk_save(store):
    with open(_DISK_PATH, "w", encoding="utf-8", newline="") as f:
        json.dump(store, f, ensure_ascii=False)


# ------------------------------- API ------------------------------------

def store_set(key: str, value) -> None:
    """Guarda value bajo key (serializado en JSON)."""
    _ensure_backend()
    payload = json.dumps(value)
    if _backend == "redis":
        _redis_client.set(key, payload)
    else:
        store = _disk_load()
        store[key] = payload
        _disk_save(store)


def store_get(key: str):
    """Recupera el valor de key con su tipo original; None si no existe."""
    _ensure_backend()
    if _backend == "redis":
        raw = _redis_client.get(key)
    else:
        raw = _disk_load().get(key)
    if raw is None:
        return None
    try:
        return json.loads(raw)
    except (ValueError, TypeError):
        return raw


def store_exists(key: str) -> bool:
    _ensure_backend()
    if _backend == "redis":
        return bool(_redis_client.exists(key))
    return key in _disk_load()


def store_del(key: str) -> bool:
    """Elimina key. Devuelve True si existia."""
    _ensure_backend()
    if _backend == "redis":
        return bool(_redis_client.delete(key))
    store = _disk_load()
    existed = key in store
    if existed:
        store.pop(key, None)
        _disk_save(store)
    return existed


def store_keys() -> list:
    """Lista de claves almacenadas."""
    _ensure_backend()
    if _backend == "redis":
        return sorted(_redis_client.keys("*"))
    return sorted(_disk_load().keys())
