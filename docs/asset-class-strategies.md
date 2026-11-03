# Asset-class strategies (v0.63)

Paper research playbooks. All scores and rules are synthetic-factor research only. No live execution.

## Major (BTC/ETH style)

Adaptive multi-factor: EMA/ATR/Supertrend/Ichimoku/BB/Keltner/VWAP/MACD/Heikin-Ashi/SAR/Donchian + GARCH/EWMA/realized/term-structure/vol-of-vol/HAR/jump-vol forecast + Fib/Elliott + options skew/gamma/vanna + funding/basis/on-chain/OI/order-flow/liquidity/MVRV/SOPR/reserve/NVTS/Puell/CDD/supply/entity proxies. Correlation/beta/factor/covariance/PCA adjusted. Risk cap 8%.

## Large-cap alt

Volume-profile/POC/VAH + VWAP + MACD + multi-TF + relative strength z-score + correlation/beta/factor/covariance/PCA + regime cluster + volume delta + netflow + OI + order-flow + Fib + DEX LP + CCI + residual + hierarchical + OPTICS. Risk cap 4%.

## Stablecoin

Adaptive peg deviation with volume confirmation + netflow + liquidity + SOPR + residual + CDD + dormancy + entity + LTH. Risk cap 0%.

## DeFi

Calm multi-scale + low anomaly + Supertrend + ADX + on-chain/smart-money + isolation + risk-parity + CVaR + LP depth/IL/fee/concentrated + Williams %R + residual + HODL + supply + range efficiency. Risk cap 2%.

## Meme

Qualified burst + StochRSI + consistency + hard horizon + volume-flow decay + anomaly + residual + liq heat + order-flow + social + Fib + CCI + beta + narrative + attention + fear-greed. Risk cap 0.5%.

## L2

Relative strength + MACD vs benchmark + adaptive MTF + correlation + cluster + vol forecast + transition + Elliott + residual + factor + hierarchical + PCA. Risk cap 3%.

## RWA

Slow multi-scale + gap/anomaly halt + volume + isolation + forecast + CVaR + realized-cap + NVTS + residual + age-weighted + dormancy + LTH/STH. Risk cap 2%.

## Perpetual

Negative funding carry + contained drift + low anomaly + funding flip + correlation + residual + OI + order-flow + gamma/vanna/charm/vanna-volga/delta-hedge + reserve + basis + basis momentum + carry + funding momentum. Risk cap 2%.

## AI-token

Hybrid burst + activity + divergence + low isolation + strict horizon + smart-money + OI + transition + options vanna + social + residual + narrative + factor + attention + entity. Risk cap 1%.

All classes apply multi-gate risk: class caps, confidence floors, correlation, anomaly, isolation, drawdown, kill switch, vol scaling + forecast + risk-parity + CVaR + beta + factor + covariance + PCA.
