#!/bin/sh

problem_number=$1
root_dir=$(git rev-parse --show-toplevel)

cd $root_dir

mkdir -p "problem${problem_number}/python/test/"

touch "problem${problem_number}/python/README.md"
touch "problem${problem_number}/python/solution.py"
touch "problem${problem_number}/python/test/test_solution${problem_number}.py"

