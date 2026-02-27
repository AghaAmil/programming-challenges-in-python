"""
Professional AI Number Guessing Game
=====================================
A showcase CLI game with three modes: Classic, AI, and Duel.
Features rich terminal UI, persistent leaderboard, and statistics.
Uses only the Python standard library.
"""

from __future__ import annotations

import json
import math
import os
import random
import re
import sys
import time
import unicodedata
from dataclasses import asdict, dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Optional

# ─────────────────────────────────────────────────────────────────────────────
# ANSI Color & Style System
# ─────────────────────────────────────────────────────────────────────────────

_COLOR_SUPPORT = sys.stdout.isatty()


def _esc(code: str) -> str:
    return f"\033[{code}" if _COLOR_SUPPORT else ""


class C:
    """ANSI escape sequences for terminal styling."""

    RESET = _esc("0m")
    BOLD = _esc("1m")
    DIM = _esc("2m")
    ITALIC = _esc("3m")
    UNDERLINE = _esc("4m")
    BLINK = _esc("5m")
    REVERSE = _esc("7m")
    STRIKETHROUGH = _esc("9m")

    BLACK = _esc("38;5;0m")
    WHITE = _esc("38;5;15m")
    RED = _esc("38;5;196m")
    GREEN = _esc("38;5;82m")
    BLUE = _esc("38;5;33m")
    CYAN = _esc("38;5;51m")
    YELLOW = _esc("38;5;220m")
    ORANGE = _esc("38;5;208m")
    MAGENTA = _esc("38;5;201m")
    PURPLE = _esc("38;5;141m")
    PINK = _esc("38;5;213m")
    GOLD = _esc("38;5;220m")
    LIME = _esc("38;5;118m")
    TEAL = _esc("38;5;30m")
    GRAY = _esc("38;5;245m")
    DARK_GRAY = _esc("38;5;238m")

    FIRE = _esc("38;5;196m")
    WARM = _esc("38;5;208m")
    COOL = _esc("38;5;75m")
    ICE = _esc("38;5;51m")

    BG_BLACK = _esc("48;5;0m")
    BG_DARK = _esc("48;5;233m")
    BG_GOLD = _esc("48;5;220m")
    BG_RED = _esc("48;5;196m")
    BG_GREEN = _esc("48;5;22m")
    BG_BLUE = _esc("48;5;17m")


GRADIENT_WARM = [196, 202, 208, 214, 220, 226]
GRADIENT_COOL = [21, 27, 33, 39, 45, 51]
GRADIENT_RAINBOW = [196, 208, 220, 82, 33, 51, 141, 201]

# ─────────────────────────────────────────────────────────────────────────────
# Terminal UI Primitives
# ─────────────────────────────────────────────────────────────────────────────

WIDTH = 62


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def gradient_text(text: str, palette: list[int]) -> str:
    if not _COLOR_SUPPORT:
        return text
    result: list[str] = []
    for i, ch in enumerate(text):
        color_idx = palette[i % len(palette)]
        result.append(f"\033[38;5;{color_idx}m{ch}")
    result.append(C.RESET)
    return "".join(result)


def styled(text: str, *styles: str) -> str:
    return "".join(styles) + text + C.RESET


def type_text(text: str, delay: float = 0.02) -> None:
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")


def box(lines: list[str], color: str = C.CYAN, width: int = WIDTH) -> str:
    inner = width - 2
    parts = [f"{color}╔{'═' * inner}╗{C.RESET}"]
    for line in lines:
        visible_len = _display_width(line)
        pad = max(0, inner - visible_len)
        parts.append(f"{color}║{C.RESET} {line}{' ' * (pad - 1)}{color}║{C.RESET}")
    parts.append(f"{color}╚{'═' * inner}╝{C.RESET}")
    return "\n".join(parts)


def divider(char: str = "─", color: str = C.DARK_GRAY, width: int = WIDTH) -> str:
    return f"{color}{char * width}{C.RESET}"


def center(text: str, width: int = WIDTH) -> str:
    visible_len = _display_width(text)
    pad = max(0, (width - visible_len) // 2)
    return " " * pad + text


def _strip_ansi(text: str) -> str:
    return re.sub(r"\033\[[0-9;]*m", "", text)


def _display_width(text: str) -> int:
    """Calculate the actual terminal column width of a string,
    accounting for ANSI escapes, wide characters, zero-width codepoints,
    and variation selectors that force emoji (wide) presentation."""
    clean = _strip_ansi(text)
    chars = list(clean)
    width = 0
    i = 0
    while i < len(chars):
        ch = chars[i]
        cat = unicodedata.category(ch)
        if cat in ("Mn", "Me", "Cf"):
            i += 1
            continue
        has_emoji_vs = i + 1 < len(chars) and chars[i + 1] == "\ufe0f"
        eaw = unicodedata.east_asian_width(ch)
        if eaw in ("W", "F") or has_emoji_vs:
            width += 2
        else:
            width += 1
        i += 1
    return width


def progress_bar(
    current: int, total: int, width: int = 30, fill_color: str = C.GREEN, empty_color: str = C.DARK_GRAY
) -> str:
    ratio = current / total if total > 0 else 0
    filled = round(width * ratio)
    empty = width - filled
    bar = f"{fill_color}{'█' * filled}{empty_color}{'░' * empty}{C.RESET}"
    return f"[{bar}] {styled(str(current), C.BOLD)}/{total}"


def temperature_gauge(guess: int, answer: int, low: int, high: int) -> str:
    distance = abs(guess - answer)
    range_size = high - low
    ratio = distance / range_size if range_size > 0 else 1

    if ratio < 0.03:
        return styled("🔥 SCORCHING HOT!", C.BOLD, C.FIRE)
    elif ratio < 0.08:
        return styled("🔥 Burning!", C.FIRE)
    elif ratio < 0.15:
        return styled("♨️  Very warm", C.WARM)
    elif ratio < 0.25:
        return styled("🌤  Warm", C.ORANGE)
    elif ratio < 0.40:
        return styled("🌊 Cool", C.COOL)
    elif ratio < 0.60:
        return styled("🧊 Cold", C.ICE)
    else:
        return styled("❄️  Freezing!", C.BOLD, C.ICE)


def direction_arrow(guess: int, answer: int) -> str:
    diff = answer - guess
    magnitude = abs(diff)
    if magnitude > 30:
        arrows = "▲▲▲" if diff > 0 else "▼▼▼"
    elif magnitude > 15:
        arrows = "▲▲" if diff > 0 else "▼▼"
    else:
        arrows = "▲" if diff > 0 else "▼"
    color = C.GREEN if diff > 0 else C.RED
    label = "Higher" if diff > 0 else "Lower"
    return f"{styled(arrows, C.BOLD, color)} {styled(label, color)}"


def format_time(seconds: float) -> str:
    if seconds < 60:
        return f"{seconds:.1f}s"
    minutes = int(seconds // 60)
    secs = seconds % 60
    return f"{minutes}m {secs:.1f}s"


# ─────────────────────────────────────────────────────────────────────────────
# Data Models
# ─────────────────────────────────────────────────────────────────────────────


class Difficulty(Enum):
    EASY = ("Easy", 15, 100)
    MEDIUM = ("Medium", 10, 200)
    HARD = ("Hard", 5, 400)
    IMPOSSIBLE = ("Impossible", 3, 1000)

    def __init__(self, label: str, max_attempts: int, base_points: int) -> None:
        self.label = label
        self.max_attempts = max_attempts
        self.base_points = base_points


class GameMode(Enum):
    CLASSIC = "Classic"
    AI = "AI"
    DUEL = "Duel"


@dataclass
class GameState:
    mode: GameMode
    difficulty: Difficulty
    answer: int
    low: int = 1
    high: int = 100
    attempts_used: int = 0
    guess_history: list[int] = field(default_factory=list)
    start_time: float = field(default_factory=time.time)
    won: bool = False

    @property
    def attempts_remaining(self) -> int:
        return self.difficulty.max_attempts - self.attempts_used

    @property
    def elapsed(self) -> float:
        return time.time() - self.start_time

    def record_guess(self, guess: int) -> None:
        self.guess_history.append(guess)
        self.attempts_used += 1


@dataclass
class LeaderboardEntry:
    player_name: str
    score: int
    difficulty: str
    mode: str
    guesses: int
    time_seconds: float
    date: str


@dataclass
class PlayerStats:
    games_played: int = 0
    wins: int = 0
    losses: int = 0
    total_guesses: int = 0
    best_time: Optional[float] = None
    current_streak: int = 0
    best_streak: int = 0

    @property
    def win_rate(self) -> float:
        return (self.wins / self.games_played * 100) if self.games_played else 0.0

    @property
    def avg_guesses(self) -> float:
        return (self.total_guesses / self.games_played) if self.games_played else 0.0


# ─────────────────────────────────────────────────────────────────────────────
# Persistence Layer
# ─────────────────────────────────────────────────────────────────────────────

DATA_DIR = Path(__file__).parent
LEADERBOARD_FILE = DATA_DIR / "leaderboard.json"
STATS_FILE = DATA_DIR / "player_stats.json"


def load_leaderboard() -> list[LeaderboardEntry]:
    if not LEADERBOARD_FILE.exists():
        return []
    try:
        data = json.loads(LEADERBOARD_FILE.read_text())
        return [LeaderboardEntry(**entry) for entry in data]
    except json.JSONDecodeError, TypeError, KeyError:
        return []


def save_leaderboard(entries: list[LeaderboardEntry]) -> None:
    entries.sort(key=lambda e: e.score, reverse=True)
    top_entries = entries[:20]
    LEADERBOARD_FILE.write_text(json.dumps([asdict(e) for e in top_entries], indent=2))


def load_stats() -> PlayerStats:
    if not STATS_FILE.exists():
        return PlayerStats()
    try:
        return PlayerStats(**json.loads(STATS_FILE.read_text()))
    except json.JSONDecodeError, TypeError, KeyError:
        return PlayerStats()


def save_stats(stats: PlayerStats) -> None:
    STATS_FILE.write_text(json.dumps(asdict(stats), indent=2))


# ─────────────────────────────────────────────────────────────────────────────
# Score Calculation
# ─────────────────────────────────────────────────────────────────────────────


def calculate_score(state: GameState, streak: int) -> int:
    base = state.difficulty.base_points
    efficiency = state.attempts_remaining / state.difficulty.max_attempts
    time_factor = max(0.3, 1.0 - (state.elapsed / 120))
    streak_bonus = 1.0 + (min(streak, 10) * 0.1)
    return int(base * (0.3 + 0.7 * efficiency) * time_factor * streak_bonus)


# ─────────────────────────────────────────────────────────────────────────────
# Banner & Menus
# ─────────────────────────────────────────────────────────────────────────────

TITLE_ART = r"""
   _  __              __              ______                      _
  / |/ /_ ____ _  ___/ /  ___ ____  / ___/ /_ _____ ___ ___    _(_)
 /    / // /  ' \/ _  /  / -_) __/ / (_ / // / -_|_-<(_-<   / _` |
/_/|_/\_,_/_/_/_/\_,_/   \__/_/    \___/\_,_/\__/___/___/   \__,_|
"""

BRAIN_ART = r"""
      _.---._
    .'       '.    AI ENGINE
   /    ^   ^  \   ──────────
  |    (o) (o)  |  Binary Search
  |      _      |  O(log n)
   \   '___'   /   Adaptive
    '.       .'
      '-----'
"""


def show_banner() -> None:
    print()
    print(gradient_text(TITLE_ART, GRADIENT_RAINBOW))
    print(center(styled("━" * 46, C.DARK_GRAY)))
    subtitle = "  A Professional CLI Game  ·  Powered by Python  "
    print(center(styled(subtitle, C.BOLD, C.PURPLE)))
    print(center(styled("━" * 46, C.DARK_GRAY)))
    print()


def show_main_menu() -> str:
    menu_lines = [
        "",
        styled("  SELECT GAME MODE", C.BOLD, C.GOLD),
        "",
        f"  {styled('[1]', C.BOLD, C.CYAN)}  🎯  Classic Mode    {styled('— You guess the number', C.GRAY)}",
        f"  {styled('[2]', C.BOLD, C.CYAN)}  🤖  AI Mode         {styled('— AI guesses your number', C.GRAY)}",
        f"  {styled('[3]', C.BOLD, C.CYAN)}  ⚔️   Duel Mode       {styled('— Race against the AI', C.GRAY)}",
        "",
        f"  {styled('[4]', C.BOLD, C.YELLOW)}  🏆  Leaderboard",
        f"  {styled('[5]', C.BOLD, C.YELLOW)}  📊  Statistics",
        f"  {styled('[Q]', C.BOLD, C.RED)}  🚪  Quit",
        "",
    ]
    print(box(menu_lines, color=C.PURPLE))
    return input(f"\n  {styled('▸', C.CYAN)} Your choice: ").strip().lower()


def choose_difficulty() -> Difficulty:
    print()
    print(f"  {styled('SELECT DIFFICULTY', C.BOLD, C.GOLD)}")
    print(f"  {styled('─' * 40, C.DARK_GRAY)}")
    for i, diff in enumerate(Difficulty, 1):
        stars = "★" * i + "☆" * (4 - i)
        color = [C.GREEN, C.YELLOW, C.ORANGE, C.RED][i - 1]
        print(
            f"  {styled(f'[{i}]', C.BOLD, C.CYAN)}  {styled(stars, color)}  {styled(diff.label, C.BOLD, color)}"
            f"  {styled(f'({diff.max_attempts} attempts, {diff.base_points} base pts)', C.GRAY)}"
        )
    print()

    while True:
        choice = input(f"  {styled('▸', C.CYAN)} Choice [1-4]: ").strip()
        if choice in ("1", "2", "3", "4"):
            return list(Difficulty)[int(choice) - 1]
        print(styled("  Invalid choice. Enter 1-4.", C.RED))


def get_player_name() -> str:
    name = input(f"\n  {styled('▸', C.CYAN)} Enter your name: ").strip()
    return name if name else "Anonymous"


# ─────────────────────────────────────────────────────────────────────────────
# Classic Mode — Human Guesses
# ─────────────────────────────────────────────────────────────────────────────


def play_classic(player_name: str) -> Optional[int]:
    difficulty = choose_difficulty()
    answer = random.randint(1, 100)
    state = GameState(mode=GameMode.CLASSIC, difficulty=difficulty, answer=answer)

    print()
    print(
        box(
            [
                "",
                center(styled("🎯  CLASSIC MODE", C.BOLD, C.GOLD)),
                "",
                center(
                    f"I'm thinking of a number between {styled('1', C.BOLD, C.CYAN)} and {styled('100', C.BOLD, C.CYAN)}"
                ),
                center(
                    f"Difficulty: {styled(difficulty.label, C.BOLD)}  ·  Attempts: {styled(str(difficulty.max_attempts), C.BOLD)}"
                ),
                "",
            ],
            color=C.BLUE,
        )
    )
    print()

    while state.attempts_remaining > 0:
        remaining_color = (
            C.GREEN if state.attempts_remaining > 3 else (C.YELLOW if state.attempts_remaining > 1 else C.RED)
        )
        bar = progress_bar(state.attempts_remaining, difficulty.max_attempts, fill_color=remaining_color)
        print(f"  {styled('Attempts:', C.BOLD)} {bar}")

        if state.guess_history:
            hist = ", ".join(str(g) for g in state.guess_history[-5:])
            print(f"  {styled('History:', C.DIM)}  {styled(hist, C.GRAY)}")

        try:
            raw = input(f"\n  {styled('▸', C.CYAN)} Your guess: ").strip()
            guess = int(raw)
        except ValueError, EOFError:
            print(styled("  Please enter a valid integer.", C.RED))
            continue

        if guess < 1 or guess > 100:
            print(styled("  Out of range! Pick a number between 1 and 100.", C.RED))
            continue

        state.record_guess(guess)

        if guess == answer:
            state.won = True
            score = _show_classic_win(state, player_name)
            return score

        print(f"  {direction_arrow(guess, answer)}  {temperature_gauge(guess, answer, 1, 100)}")
        print()

    _show_classic_loss(state)
    return None


def _show_classic_win(state: GameState, player_name: str) -> int:
    stats = load_stats()
    stats.current_streak += 1
    score = calculate_score(state, stats.current_streak)

    print()
    win_lines = [
        "",
        center(gradient_text("★  ★  ★  CORRECT!  ★  ★  ★", GRADIENT_WARM)),
        "",
        center(f"The number was {styled(str(state.answer), C.BOLD, C.GOLD)}"),
        center(
            f"Guesses: {styled(str(state.attempts_used), C.BOLD)}  ·  Time: {styled(format_time(state.elapsed), C.BOLD)}"
        ),
        center(f"Score: {styled(str(score), C.BOLD, C.GOLD)}"),
        "",
    ]
    print(box(win_lines, color=C.GREEN))
    type_text(f"\n  {styled('Congratulations, ' + player_name + '!', C.BOLD, C.GREEN)}", delay=0.03)

    _update_stats_win(stats, state)
    _save_score(player_name, score, state)
    return score


def _show_classic_loss(state: GameState) -> None:
    stats = load_stats()
    stats.current_streak = 0

    print()
    loss_lines = [
        "",
        center(styled("GAME OVER", C.BOLD, C.RED)),
        "",
        center(f"The number was {styled(str(state.answer), C.BOLD, C.GOLD)}"),
        center(f"You used all {styled(str(state.difficulty.max_attempts), C.BOLD)} attempts"),
        "",
    ]
    print(box(loss_lines, color=C.RED))

    _update_stats_loss(stats, state)


# ─────────────────────────────────────────────────────────────────────────────
# AI Mode — AI Guesses Your Number
# ─────────────────────────────────────────────────────────────────────────────

AI_THOUGHTS = [
    "Recalibrating neural pathways...",
    "Consulting the probability matrix...",
    "Running Bayesian inference...",
    "Analyzing the search space...",
    "Narrowing down possibilities...",
    "Cross-referencing data patterns...",
    "Eliminating improbable candidates...",
    "Applying binary search heuristic...",
    "Optimizing guess trajectory...",
    "Computing optimal midpoint...",
]


def ai_think(message: Optional[str] = None) -> None:
    thought = message or random.choice(AI_THOUGHTS)
    sys.stdout.write(f"  {styled('🤖', C.BOLD)} {styled(thought, C.ITALIC, C.GRAY)}")
    for _ in range(3):
        time.sleep(0.3)
        sys.stdout.write(styled(".", C.GRAY))
        sys.stdout.flush()
    sys.stdout.write("\n")


def play_ai_mode() -> None:
    print()
    print(
        box(
            [
                "",
                center(styled("🤖  AI MODE", C.BOLD, C.GOLD)),
                "",
                center("Think of a number between 1 and 100."),
                center("The AI will try to guess it!"),
                "",
                center(styled("Respond: [H]igher  [L]ower  [C]orrect", C.BOLD, C.CYAN)),
                "",
            ],
            color=C.MAGENTA,
        )
    )
    input(f"\n  {styled('▸', C.CYAN)} Press Enter when you have your number... ")

    print()
    print(gradient_text(BRAIN_ART, GRADIENT_COOL))

    low, high = 1, 100
    attempts = 0

    while low <= high:
        attempts += 1
        guess = (low + high) // 2

        ai_think()
        print(f"\n  {styled(f'Attempt #{attempts}', C.BOLD, C.PURPLE)}  {styled(f'[Range: {low}–{high}]', C.GRAY)}")
        print(f"  {styled('🤖 AI guesses:', C.BOLD)} {styled(str(guess), C.BOLD, C.GOLD)}")

        while True:
            response = input(f"  {styled('▸', C.CYAN)} [H]igher / [L]ower / [C]orrect: ").strip().lower()
            if response in ("h", "higher"):
                low = guess + 1
                print(f"  {styled('▲ Going higher...', C.GREEN)}")
                break
            elif response in ("l", "lower"):
                high = guess - 1
                print(f"  {styled('▼ Going lower...', C.RED)}")
                break
            elif response in ("c", "correct"):
                _show_ai_win(guess, attempts)
                return
            else:
                print(styled("  Enter H, L, or C.", C.RED))

        if low > high:
            print()
            print(
                box(
                    [
                        "",
                        center(styled("🤔 Something doesn't add up!", C.BOLD, C.RED)),
                        "",
                        center("The range has been exhausted. Are you sure"),
                        center("you followed the rules? Let's try again!"),
                        "",
                    ],
                    color=C.RED,
                )
            )
            return

    print(styled("  No valid number remains — check your responses!", C.RED))


def _show_ai_win(guess: int, attempts: int) -> None:
    print()
    optimal = math.ceil(math.log2(100))
    efficiency = "Optimal!" if attempts <= optimal else f"{attempts - optimal} extra guess(es)"
    lines = [
        "",
        center(gradient_text("★  AI WINS!  ★", GRADIENT_COOL)),
        "",
        center(f"Your number was {styled(str(guess), C.BOLD, C.GOLD)}"),
        center(f"Found in {styled(str(attempts), C.BOLD)} guess(es)"),
        center(f"Theoretical optimum: {styled(str(optimal), C.BOLD)} guesses (binary search)"),
        center(styled(efficiency, C.ITALIC, C.GREEN)),
        "",
    ]
    print(box(lines, color=C.CYAN))


# ─────────────────────────────────────────────────────────────────────────────
# Duel Mode — Human vs AI Race
# ─────────────────────────────────────────────────────────────────────────────


def play_duel(player_name: str) -> Optional[int]:
    difficulty = choose_difficulty()
    answer = random.randint(1, 100)
    state = GameState(mode=GameMode.DUEL, difficulty=difficulty, answer=answer)

    ai_low, ai_high = 1, 100
    ai_guesses: list[int] = []

    print()
    print(
        box(
            [
                "",
                center(styled("⚔️  DUEL MODE", C.BOLD, C.GOLD)),
                "",
                center("Both you and the AI are guessing the same number!"),
                center("You alternate turns. First to guess correctly wins."),
                center(f"Attempts: {styled(str(difficulty.max_attempts), C.BOLD)} each"),
                "",
            ],
            color=C.ORANGE,
        )
    )
    print()

    turn = 0
    while state.attempts_remaining > 0:
        turn += 1
        print(divider("─", C.DARK_GRAY))
        print(center(styled(f"— Round {turn} —", C.BOLD, C.PURPLE)))

        # Human turn
        print(f"\n  {styled(f"👤 {player_name}'s turn", C.BOLD, C.CYAN)}")
        bar = progress_bar(state.attempts_remaining, difficulty.max_attempts)
        print(f"  {styled('Attempts left:', C.DIM)} {bar}")

        while True:
            try:
                raw = input(f"  {styled('▸', C.CYAN)} Your guess: ").strip()
                human_guess = int(raw)
                if 1 <= human_guess <= 100:
                    break
                print(styled("  Pick 1–100.", C.RED))
            except ValueError, EOFError:
                print(styled("  Enter a valid number.", C.RED))

        state.record_guess(human_guess)

        if human_guess == answer:
            state.won = True
            print()
            lines = [
                "",
                center(gradient_text("★ YOU WIN THE DUEL! ★", GRADIENT_WARM)),
                "",
                center(f"The number was {styled(str(answer), C.BOLD, C.GOLD)}"),
                center(f"You beat the AI in {styled(str(state.attempts_used), C.BOLD)} round(s)!"),
                "",
            ]
            print(box(lines, color=C.GREEN))
            score = calculate_score(state, load_stats().current_streak)
            stats = load_stats()
            _update_stats_win(stats, state)
            _save_score(player_name, score, state)
            return score

        print(f"  {direction_arrow(human_guess, answer)}  {temperature_gauge(human_guess, answer, 1, 100)}")

        # AI turn
        print(f"\n  {styled("🤖 AI's turn", C.BOLD, C.MAGENTA)}")
        ai_guess = (ai_low + ai_high) // 2
        ai_guesses.append(ai_guess)
        ai_think()
        print(f"  {styled('🤖 AI guesses:', C.BOLD)} {styled(str(ai_guess), C.BOLD, C.GOLD)}")

        if ai_guess == answer:
            print()
            lines = [
                "",
                center(styled("🤖 AI WINS THE DUEL!", C.BOLD, C.MAGENTA)),
                "",
                center(f"The number was {styled(str(answer), C.BOLD, C.GOLD)}"),
                center(f"AI found it in {styled(str(len(ai_guesses)), C.BOLD)} guess(es)"),
                center(styled("Binary search is powerful!", C.ITALIC, C.GRAY)),
                "",
            ]
            print(box(lines, color=C.MAGENTA))
            stats = load_stats()
            _update_stats_loss(stats, state)
            return None

        if ai_guess < answer:
            ai_low = ai_guess + 1
            print(f"  {styled('▲ AI: Too low, going higher', C.GREEN)}")
        else:
            ai_high = ai_guess - 1
            print(f"  {styled('▼ AI: Too high, going lower', C.RED)}")
        print()

    print()
    lines = [
        "",
        center(styled("DRAW — TIME'S UP!", C.BOLD, C.YELLOW)),
        "",
        center(f"Neither found the number: {styled(str(answer), C.BOLD, C.GOLD)}"),
        "",
    ]
    print(box(lines, color=C.YELLOW))
    stats = load_stats()
    _update_stats_loss(stats, state)
    return None


# ─────────────────────────────────────────────────────────────────────────────
# Statistics & Leaderboard Display
# ─────────────────────────────────────────────────────────────────────────────


def show_leaderboard() -> None:
    entries = load_leaderboard()
    print()
    if not entries:
        print(
            box(
                [
                    "",
                    center(styled("🏆  LEADERBOARD", C.BOLD, C.GOLD)),
                    "",
                    center(styled("No entries yet. Play a game!", C.ITALIC, C.GRAY)),
                    "",
                ],
                color=C.GOLD,
            )
        )
        return

    header = (
        f"  {'#':>3}  {'Player':<14} {'Score':>7}  {'Diff':<12} {'Mode':<8} {'Guesses':>7}  {'Time':>8}  {'Date':<10}"
    )
    lines = [
        "",
        center(styled("🏆  LEADERBOARD  —  TOP 20", C.BOLD, C.GOLD)),
        "",
        styled(header, C.BOLD, C.UNDERLINE),
    ]

    medals = {1: "🥇", 2: "🥈", 3: "🥉"}
    for i, e in enumerate(entries[:20], 1):
        medal = medals.get(i, f"{i:>3}")
        color = [C.GOLD, C.WHITE, C.ORANGE][min(i - 1, 2)] if i <= 3 else C.RESET
        name_col = styled(e.player_name[:14].ljust(14), color)
        score_col = styled(str(e.score).rjust(7), C.BOLD, C.GOLD)
        time_col = format_time(e.time_seconds).rjust(8)
        row = (
            f"  {medal}  {name_col} {score_col}  {e.difficulty:<12} {e.mode:<8} "
            f"{e.guesses:>7}  {time_col}  {e.date:<10}"
        )
        lines.append(row)

    lines.append("")
    print(box(lines, color=C.GOLD, width=max(WIDTH, 90)))


def show_statistics() -> None:
    stats = load_stats()
    print()
    if stats.games_played == 0:
        print(
            box(
                [
                    "",
                    center(styled("📊  STATISTICS", C.BOLD, C.PURPLE)),
                    "",
                    center(styled("No games played yet!", C.ITALIC, C.GRAY)),
                    "",
                ],
                color=C.PURPLE,
            )
        )
        return

    win_bar = progress_bar(stats.wins, stats.games_played, width=20, fill_color=C.GREEN, empty_color=C.RED)
    best = format_time(stats.best_time) if stats.best_time else "N/A"

    lines = [
        "",
        center(styled("📊  YOUR STATISTICS", C.BOLD, C.PURPLE)),
        "",
        f"  {styled('Games Played:', C.BOLD)}   {stats.games_played}",
        f"  {styled('Wins / Losses:', C.BOLD)}  {styled(str(stats.wins), C.GREEN)} / {styled(str(stats.losses), C.RED)}",
        f"  {styled('Win Rate:', C.BOLD)}       {win_bar}  {styled(f'{stats.win_rate:.1f}%', C.BOLD)}",
        f"  {styled('Avg Guesses:', C.BOLD)}    {stats.avg_guesses:.1f}",
        f"  {styled('Best Time:', C.BOLD)}      {best}",
        f"  {styled('Current Streak:', C.BOLD)} {styled(str(stats.current_streak), C.BOLD, C.GREEN)}",
        f"  {styled('Best Streak:', C.BOLD)}    {styled(str(stats.best_streak), C.BOLD, C.GOLD)}",
        "",
    ]
    print(box(lines, color=C.PURPLE))


# ─────────────────────────────────────────────────────────────────────────────
# Stats / Score Helpers
# ─────────────────────────────────────────────────────────────────────────────


def _update_stats_win(stats: PlayerStats, state: GameState) -> None:
    stats.games_played += 1
    stats.wins += 1
    stats.total_guesses += state.attempts_used
    stats.current_streak += 1
    stats.best_streak = max(stats.best_streak, stats.current_streak)
    if stats.best_time is None or state.elapsed < stats.best_time:
        stats.best_time = round(state.elapsed, 2)
    save_stats(stats)


def _update_stats_loss(stats: PlayerStats, state: GameState) -> None:
    stats.games_played += 1
    stats.losses += 1
    stats.total_guesses += state.attempts_used
    stats.current_streak = 0
    save_stats(stats)


def _save_score(player_name: str, score: int, state: GameState) -> None:
    entries = load_leaderboard()
    entries.append(
        LeaderboardEntry(
            player_name=player_name,
            score=score,
            difficulty=state.difficulty.label,
            mode=state.mode.value,
            guesses=state.attempts_used,
            time_seconds=round(state.elapsed, 2),
            date=datetime.now().strftime("%Y-%m-%d"),
        )
    )
    save_leaderboard(entries)


# ─────────────────────────────────────────────────────────────────────────────
# Main Loop
# ─────────────────────────────────────────────────────────────────────────────


def main() -> None:
    clear_screen()
    show_banner()
    player_name = get_player_name()

    while True:
        print()
        choice = show_main_menu()

        if choice in ("1", "classic"):
            clear_screen()
            show_banner()
            play_classic(player_name)
        elif choice in ("2", "ai"):
            clear_screen()
            show_banner()
            play_ai_mode()
        elif choice in ("3", "duel"):
            clear_screen()
            show_banner()
            play_duel(player_name)
        elif choice in ("4", "leaderboard"):
            show_leaderboard()
        elif choice in ("5", "stats", "statistics"):
            show_statistics()
        elif choice in ("q", "quit", "exit"):
            print()
            type_text(styled("  Thanks for playing! See you next time. 👋", C.BOLD, C.PURPLE), delay=0.03)
            print()
            break
        else:
            print(styled("  Invalid choice. Try again.", C.RED))

        if choice in ("1", "2", "3", "classic", "ai", "duel"):
            input(f"\n  {styled('▸', C.CYAN)} Press Enter to return to menu... ")
            clear_screen()
            show_banner()


if __name__ == "__main__":
    main()
