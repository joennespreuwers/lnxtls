template = """
[Unit]
Description={description}

[Service]
User={user}
WorkingDirectory={path}
ExecStart={script}
Restart={restart_state}

[Install]
WantedBy=multi-user.target
"""


def create_service():
    name = input("Service name: ")
    with open(f"/etc/systemd/system/{name}.service", "w") as f:
        f.write(
            template.format(
                description=input("Service description: "),
                user=input("User: "),
                path=input("Path: "),
                script=input("Script: "),
                restart_state=input("Restart state: "),
            )
        )


if __name__ == "__main__":
    create_service()
