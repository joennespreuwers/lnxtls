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
