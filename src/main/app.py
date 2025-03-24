from src import create_app

app = create_app()

if __name__ == "__main__":
    debug_mode = app.config.get("DEBUG", False)
    app.run(host='0.0.0.0', port=5000, debug=debug_mode)