#!/bin/bash

echo "🛠️ Building test executable with coverage flags..."

g++ -fprofile-arcs -ftest-coverage -std=c++17 \
  main.cpp \
  tests/test_main_refined.cpp \
  -lgtest -lgtest_main -pthread \
  -o build/test_exec


if [ $? -ne 0 ]; then
  echo "❌ Compilation failed."
  exit 1
fi

echo "✅ Build successful."

echo "🚀 Running tests..."
./build/test_exec

echo "📊 Capturing coverage..."
lcov --directory . --capture --output-file coverage.info

echo "📂 Generating HTML report..."
genhtml coverage.info --output-directory out

echo "🌐 Opening coverage report in browser..."
xdg-open out/index.html
