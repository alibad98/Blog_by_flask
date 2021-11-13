from website import crearte_app
#running a personal server with debugging.
if __name__ == '__main__':
    app = crearte_app()
    app.run(debug=True)