TOP_DIR=.
README=$(TOP_DIR)/README.md

VERSION=$(strip $(shell cat version))
PROTOS=abi enum rpc state service tx type trace_type

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

prepare-all-proto:
	@mkdir -p ./raw_protos
	@mkdir -p ./protos
	@echo "Preparing all protobuf..."
	@$(foreach proto, $(PROTOS), curl --silent https://$(GITHUB_TOKEN)@raw.githubusercontent.com/ArcBlock/forge-abi/master/lib/protobuf/$(proto).proto > ./raw_protos/$(proto).proto;)
	@curl --silent https://raw.githubusercontent.com/ArcBlock/ex-abci-proto/master/lib/protos/vendor.proto > ./raw_protos/vendor.proto
	@echo "All protobuf files are fetched!"

rebuild-proto: prepare-all-proto
	@echo "Buiding all protobuf files..."
	@python -m grpc_tools.protoc -I ./raw_protos --python_out=./protos --grpc_python_out=./protos ./raw_protos/*.proto
	@sed -i -E 's/^import.*_pb2/from . \0/' ./protos/*.py
	@echo "All protobuf files are built and ready to use!.."

rebuild-ec-proto:
	@echo "Buiding all protobuf files..."
	@python -m grpc_tools.protoc -I ./raw_protos --python_out=./protos  ./raw_protos/event-chain.proto
	@sed -i -E 's/^import.*_pb2/from . \0/' ./protos/*.py
	@echo "All protobuf files are built and ready to use!.."

pack-ec:
	@rm -rf ./build
	@rm -rf ./dist
	@python ./setup.py sdist bdist_wheel
	@twine upload -r pypi ./dist/*
	@rm -rf ./build
	@rm -rf ./dist
	@echo "Event chain has been uploaded to pypi."
