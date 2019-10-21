TOP_DIR=.
ENV=~/.envs
README=$(TOP_DIR)/README.md

VERSION=$(strip $(shell cat version))

PYTHON_TARGET=forge_sdk/protos

PROTOS=enum rpc state service type trace_type tx
ACCOUNT = account/account_migrate account/delegate account/revoke_delegate account/declare
ASSET = asset/create_asset asset/consume_asset asset/acquire_asset asset/update_asset
GOVERNANCE=governance/deploy_protocol governance/activate_protocol governance/deactivate_protocol governance/upgrade_node
TOKEN=token/deposit_token token/withdraw_token token/approve_withdraw token/revoke_withdraw
TRADE=trade/transfer trade/exchange
MISC=misc/poke
SWAP=swap/setup_swap swap/retrieve_swap swap/revoke_swap
TX_PROTOS = $(ACCOUNT) $(ASSET) $(GOVERNANCE) $(TOKEN) $(TRADE) $(MISC) $(SWAP)

test1:
	@echo $(TX_PROTOS)

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
		mkvirtualenv -p python3 forge-sdk; \
		pip install -r requirements.txt; \
		pre-commit install; \
	)

add_precommit_hook:
	@pre-commit install

travis-init:
	@echo "Initialize software required for travis (normally ubuntu software)"

all: pre-build build post-build

test-forge:
	@echo "Running test suites..."
	@python -m pytest test/rpc

test:
	@echo "Running test suites..."
	@python -m pytest test/mcrypto

test-all: test test-forge

lint:
	@echo "Linting the software..."

doc:
	@echo "Building the documenation..."

precommit: dep lint doc build test

travis: precommit

travis-deploy: release
	@echo "Deploy the software by travis"

prepare-tx-protos:
	@echo "Preparing tx protobuf..."
	@$(foreach proto, $(TX_PROTOS),\
	 mkdir -p $(PYTHON_TARGET)/raw_protos/$(proto)/;\
	 curl --silent https://$(GITHUB_TOKEN)@raw.githubusercontent.com/ArcBlock/forge-core-protocols/master/lib/$(proto)/protocol.proto > ./$(PYTHON_TARGET)/raw_protos/$(proto).proto;\
	 mv $(PYTHON_TARGET)/raw_protos/$(proto).proto $(PYTHON_TARGET)/raw_protos/;\
	 rm -rf $(PYTHON_TARGET)/raw_protos/$(proto).proto;)
	@find $(PYTHON_TARGET) -type d -empty -delete
	@rm $(PYTHON_TARGET)/raw_protos/deploy_protocol.proto
	@echo "All tx protobufs are fetched!"

prepare-vendor-protos:
	@mkdir -p $(PYTHON_TARGET)/protos;mkdir -p $(PYTHON_TARGET)/raw_protos
	@echo "Preparing all protobuf..."
	@$(foreach proto, $(PROTOS), curl --silent https://$(GITHUB_TOKEN)@raw.githubusercontent.com/ArcBlock/forge-abi/master/lib/protobuf/$(proto).proto > ./$(PYTHON_TARGET)/raw_protos/$(proto).proto;)
	@curl --silent https://raw.githubusercontent.com/ArcBlock/ex-abci-proto/master/lib/protos/vendor.proto > ./$(PYTHON_TARGET)/raw_protos/vendor.proto
	@echo "All protobuf files are fetched!"

build-all-protos:
	@rm -r $(PYTHON_TARGET)/protos
	@mkdir -p $(PYTHON_TARGET)/protos;mkdir -p $(PYTHON_TARGET)/raw_protos
	@echo "Buiding all protobuf files..."
	@python -m grpc_tools.protoc -I ./$(PYTHON_TARGET)/raw_protos --python_out=./$(PYTHON_TARGET)/protos --grpc_python_out=./$(PYTHON_TARGET)/protos ./$(PYTHON_TARGET)/raw_protos/*.proto
	@sed -i 's/^import.*_pb2/from . &/' ./$(PYTHON_TARGET)/protos/*.py
	@echo "All protobuf files are built and ready to use!.."
	@for filename in ./$(PYTHON_TARGET)/protos/*.py; do \
	 echo "from forge_sdk.protos.protos.$$(basename $$filename .py) import *" >>$(PYTHON_TARGET)/protos/__init__.py; \
	 done

clean-pypi-build:
	@rm -rf build
	@rm -rf dist
	@echo "All build and dist folders are cleaned!"

package-pypi:
	@python setup.py sdist bdist_wheel
	@echo "file packaged successfully!"

upload-pypi:
	@twine upload -r pypi dist/*
	@echo "file uploaded successfully!"

pypi: package-pypi upload-pypi clean-pypi-build


include .makefiles/*.mk

.PHONY: build init travis-init install dep pre-build post-build all test doc precommit travis clean watch run bump-version create-pr
