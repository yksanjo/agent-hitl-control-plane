from datetime import datetime, timezone


def main() -> None:
    print("agent-hitl-control-plane initialized at", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
