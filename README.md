# payment-gateway

Card authorisation and capture against the acquirer; every attempt is written to the payments
ledger (`acme-payments-db`, PostgreSQL, port 5432, on the Platform `pay-net` path) before the
acquirer is called. Owned by the Payments team. Dynatrace `SERVICE-acme-paygw`.
Releases on Tuesdays only.
