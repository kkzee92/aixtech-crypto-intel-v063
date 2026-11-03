# Security architecture (v0.63)

Version 0.63 extends the zero-trust control plane. Research design only; not a certified product or legal advice.

## Trust boundaries

Synthetic fixture or injected public ticker → Source attestation → Strategy research rules + regime/vol/forecast/correlation/cluster/isolation/residual/risk-parity/CVaR/fib/elliott/options/on-chain/beta/factor/covariance/PCA overlay → Multi-gate risk (class caps, confidence, correlation, anomaly, isolation, drawdown, kill switch, vol scaling + forecast + risk-parity + CVaR + beta + factor + covariance + PCA) → Paper fill only → Hash-chained audit with multi-hash sealed lineage (SHA-256 + SHA3-256 + BLAKE2b + SHA512 + SHA3-512 + BLAKE3 proxy + SHA3-384 + SHAKE proxies + Keccak + SHA3-224), timestamps, residency, consecutive counter, continuous verification + attestation.

Trade/withdrawal keys refused. No order router. assert_paper_only. refuse_trade_secret.

## Roles

| Role | Allowed | Denied |
|---|---|---|
| Researcher | scan, backtest, read audit | place order, withdraw, enable live |
| Auditor | read audit, verify chain, scan | place order, withdraw, enable live |
| Operator | scan, kill switch, read audit | place order, withdraw, enable live |

No trader role.

## Data classes & redaction

Expanded patterns: BIP39, WIF, PEM, AWS keys, GitHub PATs, high-entropy strings, Solana base58, session cookies/tokens, hardware wallet exports, partial seed fragments, quantum-resistant algorithm mentions, exchange API key patterns (incl. Binance, Bybit, OKX, KuCoin, Gate, MEXC, Bitget, Hyperliquid, dYdX specific formats), JWT, private key hex, Telegram/Discord bot tokens, generic long tokens, BIP39 word sequences, hardware serials, API secret fragments, ChaCha20, SSH keys, Lightning invoices, Nostr keys, passphrases, 2FA secrets, mnemonic word lists, BIP39 checksum validation proxies, exchange deposit addresses. Wallet addresses, personal data tripwired.

## Feed integrity & lineage

feed_status for jumps/staleness. attest_source + integrity_digest. Sealed multi-hash lineage with Merkle proxy and monotonic counter. Entropy scoring, isolation forest-style + LOF + autoencoder residual + SVM + DBSCAN + spectral + hierarchical + OPTICS anomaly detection, continuous verification proxies, ATR-percentile + GARCH/EWMA/term-structure/vol-of-vol/HAR/jump forecast tier, quantum-safe hash mentions, continuous attestation, key rotation simulation, access log simulation, role-based access proxy.

## Threats and controls

| Threat | Control |
|---|---|
| Secret committed | gitleaks + expanded redaction |
| Trade key paste | refuse_trade_secret |
| Fixture injection | SYNTHETIC label + attestation |
| Stale/jumped feed | feed_status |
| Oversized risk | Class caps, confidence, correlation, anomaly, isolation, vol scaling + forecast + risk-parity + CVaR + beta + factor + covariance + PCA |
| Runaway loss | Drawdown halt + kill switch |
| Audit tamper | Hash chain + multi-hash seal + Merkle proxy |
| Live-order mistake | Mode guard + RBAC |
| Personal data | PDPA tripwire |

## Incident handling

1. Engage kill switch.
2. Freeze audit chain and record digests.
3. Rotate any pasted secret outside repo.
4. Human review before clearing kill switch.

## Operating rules

- Read-only market credentials only if ever added; never trade keys.
- Logs pass through redact.
- Default is research. Promotion to broker is separate human-approved system.
