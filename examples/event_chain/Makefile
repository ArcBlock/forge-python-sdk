TOP_DIR=.
README=$(TOP_DIR)/README.md

VERSION=$(strip $(shell cat version))
PROTOS=abi enum rpc state service tx type

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


rebuild-proto:
	@echo "Buiding all protobuf files..."
	@python -m grpc_tools.protoc -I ./protos --python_out=./protos  ./protos/*.proto
	@sed -i -E 's/^import.*_pb2/from . \0/' ./protos/*.py
	@echo "All protobuf files are built and ready to use!.."
