TOP_DIR=.
ENV=~/.envs
README=$(TOP_DIR)/README.md

VERSION=$(strip $(shell cat version))
PROTOS=abi enum rpc state service tx type trace_type
CONFIGS=forge forge_release forge_test forge_default

build:
	@echo "Building the software..."

init: install dep create_env
	@echo "Initializing the repo..."
	@git submodule update --init --recursive

create_env:
	@pip install virtualenv
	@pip install virtualenvwrapper
	( \
		source /usr/local/bin/virtualenvwrapper.sh; \
		mkvirtualenv forge-python-sdk; \
		pip install -r requirements.txt; \
		pre-commit install; \
	)

add_precommit_hook:
	@pre-commit install

travis-init: add_precommit_hook
	@echo "Initialize software required for travis (normally ubuntu software)"

install:
	@echo "Install software required for this repo..."

dep:
	@echo "Install dependencies required for this repo..."

pre-build: install dep
	@echo "Running scripts before the build..."

post-build:
	@echo "Running scripts after the build is done..."

all: pre-build build post-build

test:
	@echo "Running test suites..."

lint:
	@echo "Linting the software..."
	@python .git/hooks/pre-commit

doc:
	@echo "Building the documenation..."

precommit: dep lint doc build test

travis: precommit

travis-deploy: release
	@echo "Deploy the software by travis"

clean:
	@echo "Cleaning the build..."

watch:
	@make build
	@echo "Watching templates and slides changes..."
	@fswatch -o src/ | xargs -n1 -I{} make build

run:
	@echo "Running the software..."

fetch-configs:
	@mkdir -p ./configs
	@echo "Fetching latest configs from Forge..."
	@$(foreach config, $(CONFIGS), curl --silent https://$(GITHUB_TOKEN)@raw.githubusercontent.com/ArcBlock/forge-elixir-sdk/master/priv/$(config).toml > ./configs/$(config).toml;)
	@curl --silent https://$(GITHUB_TOKEN)@raw.githubusercontent.com/ArcBlock/forge-elixir-sdk/master/priv/forge_default.toml> ./forge/config/forge_default.toml
	@echo "All config files are fetched and updated!"

prepare-all-proto:
	@mkdir -p forge/raw_protos
	@mkdir -p forge/protos
	@echo "Preparing all protobuf..."
	@$(foreach proto, $(PROTOS), curl --silent https://$(GITHUB_TOKEN)@raw.githubusercontent.com/ArcBlock/forge-abi/master/lib/protobuf/$(proto).proto > ./forge/raw_protos/$(proto).proto;)
	@curl --silent https://raw.githubusercontent.com/ArcBlock/ex-abci-proto/master/lib/protos/vendor.proto > ./forge/raw_protos/vendor.proto
	@echo "All protobuf files are fetched!"

rebuild-proto: prepare-all-proto
	@echo "Buiding all protobuf files..."
	@python -m grpc_tools.protoc -I ./forge/raw_protos --python_out=./forge/protos --grpc_python_out=./forge/protos ./forge/raw_protos/*.proto
	@sed -i -E 's/^import.*_pb2/from . \0/' ./forge/protos/*.py
	@echo "All protobuf files are built and ready to use!.."

# Event Chain related commands
event-chain-test:
	@echo "Running flow test for event-chain..."
	@python -m examples.event_chain.test

event-chain-server:
	@echo "Starting server for Event-Chain"
	@python -m examples.event_chain.server

init-event-chain:
	@echo "Initializing db for Event-Chain..."
	@mkdir -p ~/.forge/event_chain
	@python -m examples.event_chain.db_helper
	@echo "DB for Event-Chain has been initialized!"

pack-ec:
	@cd examples
	@python ./setup.py sdist bdist_wheel
	@twine upload -r pypi ./dist/*
	@rm -rf ./build
	@rm -rf ./dist
	@echo "Event chain has been uploaded to pypi."

pack-sdk:
	@python ./setup.py sdist bdist_wheel
	@twine upload -r pypi ./dist/*
	@rm -rf ./build
	@rm -rf ./dist
	@echo "forge sdk has been uploaded to pypi."

include .makefiles/*.mk

.PHONY: build init travis-init install dep pre-build post-build all test doc precommit travis clean watch run bump-version create-pr
