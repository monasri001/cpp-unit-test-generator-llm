#!/bin/bash

echo "🔨 Building project..."
mkdir -p build
cd build
cmake ..
make

echo "✅ Running tests..."
./unit_tests
