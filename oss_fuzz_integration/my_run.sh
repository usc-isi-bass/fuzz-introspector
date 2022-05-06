#!/bin/bash -eu
################################################################################

PROJECT=$1
TARGET=$2
CORPUS=$3
NAME=$4

sudo rm -rf ./build/out/$PROJECT ./build/work/$PROJECT

SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
python3 ${SCRIPT_DIR}/my_get_coverage.py $PROJECT $TARGET $CORPUS
python3 ./infra/helper.py build_fuzzers --sanitizer=introspector $1

STORAGE=./output_corpus/${PROJECT}-${TARGET}/$NAME
mkdir -p $STORAGE

rm -rf $STORAGE/*

cp -rf ./build/out/$1/inspector/ $STORAGE/inspector-report
cp -rf ./build/out/$1/report/ $STORAGE/inspector-report/covreport
cp -rf ./build/out/$1/report_target/* $STORAGE/inspector-report/covreport/

echo "If all worked, then you should be able to start a webserver at port 8008 in ./${STORAGE}/inspector-report/"
echo "Use the following command to initialize a webserver in the directory: cd ./${STORAGE}/inspector-report/ && python3 -m http.server 8008"
