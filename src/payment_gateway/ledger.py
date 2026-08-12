"""Ledger writes precede every acquirer call."""
POOL_SIZE = 50
CONNECT_TIMEOUT_S = 30


def write_attempt(pool, attempt: dict) -> None:
    with pool.connection(timeout=CONNECT_TIMEOUT_S) as conn:
        conn.execute("INSERT INTO attempts ...", attempt)
