#!/bin/sh

problem_number=$1
root_dir=$(git rev-parse --show-toplevel)

cd $root_dir/java

mvn archetype:generate -DgroupId=com.tonitum -DartifactId=problem${problem_number} -DarchetypeArtifactId=maven-archetype-quickstart -DarchetypeVersion=1.5 -DinteractiveMode=false
