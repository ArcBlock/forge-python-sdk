TOP_DIR=.
ENV=~/.envs
README=$(TOP_DIR)/README.md

VERSION=$(strip $(shell cat version))
PROTOS=abi event type tx state code rpc

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

prepare-all-proto:
	@mkdir -p protos
	@mkdir -p src/protos
	@echo "Preparing all protobuf..."
	@$(foreach proto, $(PROTOS), curl --silent https://$(GITHUB_TOKEN)@raw.githubusercontent.com/ArcBlock/forge/master/tools/forge_sdk/lib/forge_sdk/protobuf/$(proto).proto > ./protos/$(proto).proto;)
	@curl --silent https://raw.githubusercontent.com/ArcBlock/ex_abci/master/lib/abci_protos/vendor.proto > ./protos/vendor.proto
	@echo "All protobuf files are fetched!"

rebuild-proto: prepare-all-proto
	@echo "Buiding all protobuf files..."
	@python -m grpc_tools.protoc -I ./protos --python_out=./src/protos --grpc_python_out=./src/protos ./protos/*.proto
	@sed -i -E 's/^import.*_pb2/from . \0/' ./src/protos/*.py
	@echo "All protobuf files are built and ready to use!.."

include .makefiles/*.mk

.PHONY: build init travis-init install dep pre-build post-build all test doc precommit travis clean watch run bump-version create-pr
