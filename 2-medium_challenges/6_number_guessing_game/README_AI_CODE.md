# 🎯 Number Guessing Game — AI Edition

A professional command-line number guessing game featuring three game modes, an AI opponent powered by binary
search, rich terminal UI with ANSI colors and box-drawing characters, a persistent leaderboard, and player
statistics — all built with **zero external dependencies**.

## 📋 Description

This project evolves the classic "guess a number" game into a polished CLI experience that demonstrates advanced
Python patterns. The game offers three distinct modes:

- **Classic Mode** — You guess a randomly chosen number between 1 and 100, guided by directional arrows and a
  hot/cold temperature gauge.
- **AI Mode** — You think of a number, and the AI uses binary search to find it, complete with "thinking"
  animations and personality.
- **Duel Mode** — You race head-to-head against the AI. Both guess the same hidden number in alternating turns.
  Can you beat O(log n)?

## 📖 Game Modes

### 🎯 Classic Mode

Guess the computer's secret number. Four difficulty tiers control how many attempts you get:

| Difficulty   | Attempts | Base Points | Rating   |
|--------------|----------|-------------|----------|
| Easy         | 15       | 100         | ★☆☆☆     |
| Medium       | 10       | 200         | ★★☆☆     |
| Hard         | 5        | 400         | ★★★☆     |
| Impossible   | 3        | 1000        | ★★★★     |

Each guess shows:
- A **directional arrow** (▲/▼) with magnitude (one, two, or three arrows)
- A **temperature gauge** (🔥 Scorching → ❄️ Freezing) based on proximity
- A **visual progress bar** showing remaining attempts

### 🤖 AI Mode

Think of a number between 1 and 100. The AI will guess it using an optimal binary search strategy,
demonstrating O(log n) efficiency. It guarantees finding any number in at most 7 guesses.

### ⚔️ Duel Mode

Both you and the AI guess the same hidden number. You take turns — can human intuition beat algorithmic
precision? Scores are tracked and saved to the leaderboard.

## 🏆 Scoring System

Your score is calculated based on four factors:

```
score = base_points × efficiency × time_factor × streak_bonus
```

- **Base points** — determined by difficulty (100–1000)
- **Efficiency** — ratio of remaining attempts to total (rewarding fewer guesses)
- **Time factor** — bonus for finishing quickly (decays over 2 minutes)
- **Streak bonus** — +10% per consecutive win (up to 10 streak)

## 💡 Example Usage

```
  ╔════════════════════════════════════════════════════════════╗
  ║                                                            ║
  ║            🎯  CLASSIC MODE                                ║
  ║                                                            ║
  ║   I'm thinking of a number between 1 and 100               ║
  ║   Difficulty: Hard  ·  Attempts: 5                         ║
  ║                                                            ║
  ╚════════════════════════════════════════════════════════════╝

  Attempts: [██████████████████████████████] 5/5
  ▸ Your guess: 50
  ▲▲ Higher  ♨️  Very warm

  Attempts: [████████████████████░░░░░░░░░░] 4/5
  History:  50
  ▸ Your guess: 65
  ▼ Lower  🔥 Burning!

  Attempts: [██████████░░░░░░░░░░░░░░░░░░░░] 3/5
  History:  50, 65
  ▸ Your guess: 58

  ╔════════════════════════════════════════════════════════════╗
  ║                                                            ║
  ║            ★  ★  ★  CORRECT!  ★  ★  ★                      ║
  ║                                                            ║
  ║            The number was 58                               ║
  ║            Guesses: 3  ·  Time: 12.4s                      ║
  ║            Score: 312                                      ║
  ║                                                            ║
  ╚════════════════════════════════════════════════════════════╝
```

## ▶️ How to Run

```bash
cd 2-medium_challenges/6_number_guessing_game
python3 number_guessing_ai.py
```

No external packages required — the game uses only the Python standard library.

## 📊 Persistence

The game automatically saves data in two JSON files alongside the script:

- `leaderboard.json` — Top 20 high scores across all modes
- `player_stats.json` — Lifetime statistics (wins, losses, streaks, best time)

## 📚 Learning Objectives

### Prerequisites

To understand this project, you should know:

- **Variables and Data Types**: Strings, integers, floats, lists, dictionaries
- **Input/Output**: Using `input()` and `print()` functions
- **Conditionals**: `if`, `elif`, `else` statements
- **Loops**: `while` and `for` loops
- **Functions**: Creating and calling functions with parameters and return values

### Skills to Practice

This challenge demonstrates:

- **Dataclasses**: Structured data with `@dataclass` for game state, stats, and leaderboard entries
- **Enums**: Type-safe difficulty levels and game modes with `Enum`
- **Type Hints**: Full type annotations on every function signature
- **ANSI Escape Codes**: Rich terminal output with 256-color support, bold, italic, and more
- **File I/O with JSON**: Persistent storage using `json` and `pathlib.Path`
- **Binary Search Algorithm**: The AI opponent demonstrates O(log n) search efficiency
- **Score Calculation**: Multi-factor formula combining efficiency, time, and streak bonuses
- **Input Validation**: Robust handling of invalid user input throughout
- **Modular Architecture**: Clean separation of UI rendering, game logic, and persistence

### Python Concepts Demonstrated

| Concept              | Where Used                                          |
|----------------------|-----------------------------------------------------|
| `@dataclass`         | `GameState`, `PlayerStats`, `LeaderboardEntry`       |
| `Enum`               | `Difficulty`, `GameMode`                             |
| `pathlib.Path`       | File paths for leaderboard and stats                 |
| f-strings            | All terminal output formatting                       |
| List comprehensions  | Color gradient generation                            |
| `time` module        | Game timer and typing animations                     |
| `json` module        | Serialization of leaderboard and stats               |
| `math.log2`          | Computing theoretical optimal guesses                |
| `sys.stdout.write`   | Character-by-character typing animation              |
| Properties           | Computed fields on dataclasses (`win_rate`, etc.)    |

## 🚀 Optional Extensions

### Beginner Level

- **Custom Range**: Allow the player to choose a range other than 1–100
- **Hint System**: Add a "hint" command that reveals whether the number is odd/even
- **Sound Effects**: Use `\a` (bell character) for correct guesses

### Intermediate Level

- **Multiplayer**: Two humans take turns guessing against each other
- **Difficulty Auto-Adjust**: Increase difficulty after consecutive wins
- **Export Stats**: Generate a text report of all-time statistics

### Advanced Level

- **Network Play**: Use sockets for remote multiplayer duels
- **Machine Learning AI**: Replace binary search with a learning agent that adapts to player patterns
- **ncurses UI**: Full terminal UI with `curses` for real-time updates without reprinting

---

**Good luck and have fun! 🎉**

---

_Challenge Type: Medium_
_Topics: Dataclasses, Enums, ANSI Terminal UI, Binary Search, File I/O, Game Design_
_Estimated Time (with deep research): 90–120 minutes_
