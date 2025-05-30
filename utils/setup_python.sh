#!/bin/sh

problem_number=$1
root_dir=$(git rev-parse --show-toplevel)

cd $root_dir

mkdir -p "/python/problem${problem_number}/test/"

touch "python/problem${problem_number}/README.md"
touch "python/problem${problem_number}/solution.py"
touch "python/problem${problem_number}/test/test_solution${problem_number}.py"

echo "from problem${problem_number}.python.solution import Solution\n\n" >> "python/problem${problem_number}/test/test_solution${problem_number}.py"
echo "class TestSolution${problem_number}:\n    def test_case_one(self):\n" >> "python/problem${problem_number}/test/test_solution${problem_number}.py"
