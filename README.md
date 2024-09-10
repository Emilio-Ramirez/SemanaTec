# SemanaTec

This repository contains projects and exercises for SemanaTec.

## Getting Started

### 1. Create your Python virtual environment

For fish shell:

```bash
python3 -m venv .venv
source .venv/bin/activate.fish
```

For bash/zsh:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install required packages

After activating your virtual environment, install the necessary packages:

```bash
pip install freegames
```

### 3. Run the games

To run a game from the freegames package, use:

```bash
python3 -m freegames.<game_name>
```

Replace `<game_name>` with the name of the game you want to play, for example:

```bash
python3 -m freegames.snake
python3 -m freegames.paint
```

## Troubleshooting

If you encounter a "_tkinter" module error, you may need to install Tkinter support:

```bash
brew install python-tk@3.12
```

Then recreate your virtual environment and reinstall packages.

## Contributing

[Add instructions for how others can contribute to your project]

## License

[Add your license information here]
