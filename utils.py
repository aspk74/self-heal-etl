def log_error(error_msg):
    with open("log.txt", "w") as f:
        f.write(error_msg)
