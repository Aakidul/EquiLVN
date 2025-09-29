# EquiLVN
Python-based LVN trading algorithm using swing highs/lows, support/resistance, and volume equilibrium. Ideal for intraday and scalping setups with customizable window sizes. Generates signals from historical data. For reference only — not financial advice


"""
📘 ALPHA DATA TRADING VARIABLES & STRATEGY OVERVIEW
===================================================

This trading script is designed to analyze historical market data and generate trade signals using price action equilibrium concepts and volume node analysis. Please read the following information carefully before using or modifying the code.

🔹 VARIABLES DEFINITIONS:
-------------------------
- OE : Swing High Equilibrium
- E  : Swing Low Equilibrium
- S  : Support
- R  : Resistance
- W  : Window Length (number of candles considered for signal generation)
- M  : Midpoint of the window, calculated as (S + R) / 2
- T  : Target for profit, calculated as: (percentage / 100) * value

📊 FUNCTIONALITY:
-----------------
- The algorithm fetches historical candle data using `pandas`.
- It identifies Swing Highs (OE), Swing Lows (E), and calculates Support (S) and Resistance (R).
- A sliding window (`W`) is used to scan and analyze price behavior. Larger windows tend to yield broader signals and may be more suitable for longer timeframes.
- Midpoints and target projections are used to guide potential entry and exit decisions.

📉 LVNs AND HVNs:
-----------------
- **LVNs (Low Volume Nodes):** Price areas where trading volume is low, often used as potential reversal or breakout zones. This script focuses on **LVNs** to identify low liquidity zones that may prompt sharp price movements.
- **HVNs (High Volume Nodes):** Areas with high trading volume, often acting as support/resistance. These are **not** the focus in this algorithm.

⚠️ DISCLAIMER:
--------------
This tool generates trade signals **based on historical data only**. Market conditions can change rapidly, and this script does **not guarantee** future performance.

- Use it **only as a reference** — do not follow signals blindly.
- The author **Aakidul** is **not responsible for any financial losses** incurred from using this tool.
- Trading is inherently risky. Use proper risk management.

📅 RECOMMENDED TIMEFRAME SETTINGS (for scalping/high-frequency strategies):
-------------------------------------------------------------------------
- 1 Min  ➜ 375 candles
- 3 Min  ➜ 125 candles
- 5 Min  ➜ 75 candles
- 15 Min ➜ 35 candles

💡 Note: These values are **suggested only**. LVNs and signals can change at any time based on market volatility.

🎥 DEMO VIDEO:
--------------
Watch how this algorithm works: [https://youtu.be/-d4ulV3RnCQ?si=tblubZzY4e1JHMX2](https://youtu.be/-d4ulV3RnCQ?si=tblubZzY4e1JHMX2)

"""
