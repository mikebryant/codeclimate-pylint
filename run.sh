#!/bin/bash
set -x

pylint -f codeclimate_reporter.CodeClimateReporter `ls -1 */__init__.py | cut -d '/' -f 1` *.py
PYLINT_EXIT=$?
if [ $PYLINT_EXIT -ge 32 ] || [ $PYLINT_EXIT -eq 1 ]
then
  exit $PYLINT_EXIT
fi
