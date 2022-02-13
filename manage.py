import uvicorn
import asyncio
from sys import argv


if __name__ == "__main__":
    if argv[1] == "run":
        from back import app
        uvicorn.run(app)
    elif argv[1] == "initdb":
        from back.utils import create_all_tables
        loop = asyncio.get_event_loop()
        # Blocking call which returns when the hello_world() coroutine is done
        loop.run_until_complete(create_all_tables())