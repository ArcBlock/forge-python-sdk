Event Chain: An Event System Built on Forge

Introduction
---

There are two ways of running event-chain on your local. Pick one that suit you more.
1. Developer Setup: if you want to work directly with the source code
2. Quick Setup: if you just want to get a quick sense of it.

Developer Setup
---

1. clone this repo to your local

1. install dependencies for forge-python-sdk:

        `pip install -r requirements.txt`
 2. install dependencies for forge-event-chain

        `pip install -r examples/event_chain/requirements.txt`

Quick Setup
---
1. Go to your python environment

2. `pip install forge-event-chain`


Run
---

Before running event_chain, make sure your local forge is running properly.

1. Add event_chain config in your forge config.
    ```toml
    [app]
    name = "Event-Chain"
    version = "0.1.0"
    sock_tcp = "tcp://127.0.0.1:27219"
    path = "~/.forge/event_chain"
    host="127.0.0.1" # Your local IP address for wallet to connect
    port=5000
    did_address='http://localhost:4000' # The DID service event_chain will call from

    ```

1. restart forge to activate the updated config.

1. simulate original data to start with:

   `FORGE_CONFIG=/home/User/forge_release.toml python -m event_chain.simulation.simulat`
 2. start event_chain server:

    `FORGE_CONFIG=/home/User/forge_release.toml python -m event_chain.server.init`

3. start event_chain application:

   `FORGE_CONFIG=/home/User/forge_release.toml python3 -m event_chain.ec normal`
