TOP_DIR=.
README=$(TOP_DIR)/README.md

VERSION=$(strip $(shell cat version))
PROTOS=abi enum rpc state service tx type trace_type
PROTOS=abi enum rpc state service type trace_type
PYTHON_TARGET=protos
CONFIGS=forge forge_release forge_test forge_default
TX_PROTOS=account/account_migrate asset/consume_asset asset/create_asset account/declare governance/deploy_protocol trade/exchange misc/poke stake/stake trade/transfer asset/update_asset governance/upgrade_node deprecated/declare_file

build:
	@echo "Building the software..."

init: install dep
	@echo "Initializing the repo..."

travis-init:
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

prepare-tx-protos:
	@echo "Preparing tx protobuf..."
	@$(foreach proto, $(TX_PROTOS),\
	 mkdir -p $(PYTHON_TARGET)/raw_protos/$(proto)/;\
	 curl --silent https://$(GITHUB_TOKEN)@raw.githubusercontent.com/ArcBlock/forge-core-protocols/master/lib/$(proto)/protocol.proto > ./$(PYTHON_TARGET)/raw_protos/$(proto).proto;\
	 mv $(PYTHON_TARGET)/raw_protos/$(proto).proto $(PYTHON_TARGET)/raw_protos/;\
	 rm -rf $(PYTHON_TARGET)/raw_protos/$(proto).proto;)
	@find $(PYTHON_TARGET) -type d -empty -delete
	@echo "All tx protobufs are fetched!"

prepare-vendor-protos:prepare-tx-protos
	@mkdir -p $(PYTHON_TARGET)/protos;mkdir -p $(PYTHON_TARGET)/raw_protos
	@echo "Preparing all protobuf..."
	@$(foreach proto, $(PROTOS), curl --silent https://$(GITHUB_TOKEN)@raw.githubusercontent.com/ArcBlock/forge-abi/master/lib/protobuf/$(proto).proto > ./$(PYTHON_TARGET)/raw_protos/$(proto).proto;)
	@curl --silent https://raw.githubusercontent.com/ArcBlock/ex-abci-proto/master/lib/protos/vendor.proto > ./$(PYTHON_TARGET)/raw_protos/vendor.proto
	@echo "All protobuf files are fetched!"

build-all-protos: prepare-vendor-protos prepare-tx-protos
	@mkdir -p $(PYTHON_TARGET)/protos;mkdir -p $(PYTHON_TARGET)/raw_protos
	@echo "Buiding all protobuf files..."
	@python -m grpc_tools.protoc -I ./$(PYTHON_TARGET)/raw_protos --python_out=./$(PYTHON_TARGET)/protos --grpc_python_out=./$(PYTHON_TARGET)/protos ./$(PYTHON_TARGET)/raw_protos/*.proto
	@sed -i -E 's/^import.*_pb2/from . \0/' ./$(PYTHON_TARGET)/protos/*.py
	@echo "All protobuf files are built and ready to use!.."
	@for filename in ./$(PYTHON_TARGET)/protos/*.py; do \
	 echo "from event_chain.protos.protos.$$(basename $$filename .py) import *" >>$(PYTHON_TARGET)/protos/__init__.py; \
	 done
