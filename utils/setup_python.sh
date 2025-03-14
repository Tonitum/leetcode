#!/bin/sh

problem_number=$1
root_dir=$(git rev-parse --show-toplevel)

cd $root_dir

mkdir -p "problem${problem_number}/python/test/"

touch "problem${problem_number}/python/README.md"
touch "problem${problem_number}/python/solution.py"
touch "problem${problem_number}/python/test/test_solution${problem_number}.py"

echo "from problem${problem_number}.python.solution import Solution\n\n" >> "problem${problem_number}/python/test/test_solution${problem_number}.py"
echo "class TestSolution${problem_number}:\n    def test_case_one(self):\n" >> "problem${problem_number}/python/test/test_solution${problem_number}.py"
